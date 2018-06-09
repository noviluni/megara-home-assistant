from actions import ModuleException
from conf import ACTIVE_MODULES
from voice_assistant import Assistant as _Assistant


class Assistant(_Assistant):
    """
    Allows to build an assitant, which can:
    - Implement new behaivour from active modules
    - Analyze last recognised words
    - Execute actions inside

    """
    default_action = None
    default_speak = 'No se cómo responder a eso.'
    orders = []
    activation_word = 'asistente'

    def __init__(self, training_table='training_table', **kwargs):
        """
        Try to import all modules in ACTIVE_MODULES variable. If can't import the associated Mixin raise an exception.
        Then join all orders coming from mixins and assign them in orders property. And execute set_up() property.
        """
        self.TRAINING_TABLE = training_table

        for mod in ACTIVE_MODULES:
            mixin_name = '{}Mixin'.format(mod.capitalize())
            try:
                exec('from modules.{} import {}'.format(mod, mixin_name))
            except ImportError as e:
                raise ModuleException('Bad programmed module: {}'.format(e))
            mixin = eval(mixin_name)
            self.__class__.__bases__ += (mixin,)
            self.orders.extend(mixin.orders)
            mixin.set_up()
        super().__init__(**kwargs)

    def _create_initial_tables(self):
        super()._create_initial_tables()

        tables = self.database.get_table_names()

        if self.TRAINING_TABLE not in tables:
            self.database.create_table(table_name=self.TRAINING_TABLE, columns={'query': 'TEXT', 'action': 'TEXT',
                                                                                'spoken': 'TEXT', 'correct': 'INT'})

    def main(self, initial_sentence='¿Qué deseas?'):
        self.speak(initial_sentence, remember=False)
        self.listen()
        self.execute(self.orders)
        self.adjust_for_ambient_noise()

    def main_training(self, initial_sentence='¿Qué deseas?'):
        self.speak(initial_sentence, remember=False)
        self.listen()
        query = self.last_recognised
        final_action, final_speak = self.execute(self.orders)

        while True:
            self.speak('¿lo he hecho bien?', remember=False)
            self.listen()
            if self.has_heard(['si', 'sí']):
                correct = '1'
                break
            elif self.has_heard('no'):
                correct = '0'
                break
            else:
                self.speak('Lo siento, not he entendido, di "sí" o "no".')

        self.database.insert_into(table_name=self.TRAINING_TABLE, values={'query': query,'action': final_action,
                                                                          'spoken': final_speak, 'correct': correct})
        self.adjust_for_ambient_noise()

    def analyze(self, orders, action=default_action, speak=default_speak):
        for order in orders:
            if self.has_heard(order['words']):
                action = order['action']
                speak = order['speak']

                if order['orders']:
                    orders = order['orders']
                    return self.analyze(orders, action, speak)
        return [action, speak]

    def execute(self, orders):
        final_action, final_speak = self.analyze(orders)
        self.speak(final_speak)
        if final_action:
            eval(final_action)
        return final_action, final_speak

    def wating_keyword(self):
        """Start listening and return True if is called"""
        import os
        from pocketsphinx import LiveSpeech

        # ESPAÑOL
        model_path = './models/'
        speech = LiveSpeech(
            verbose=False,
            sampling_rate=16000,
            buffer_size=2048,
            no_search=False,
            full_utt=False,
            hmm=os.path.join(model_path, 'cmusphinx-es-5.2/model_parameters/voxforge_es_sphinx.cd_ptm_4000'),
            lm=os.path.join(model_path, 'es-20k.lm.gz'),
            dic=os.path.join(model_path, 'es.dict')
        )

        for phrase in speech:
            listened = str(phrase)
            # print('wating: "{}"'.format(listened))
            if self.activation_word in listened:
                return True

    def close(self):
        try:
            self.connexion.close()  # TODO: Change to work with the new database system.
        except Exception:
            pass
        exit()
