from actions import ModuleMixin
import random

class GamesMixin(ModuleMixin):

    orders = [{'words': ['jugar', 'juego', 'palabras encadenadas'],
               'action': 'self.manage_game()',
               'speak': '',
               'orders': None},
              ]

    def manage_game(self):
        self.speak('Ok. Vamos a jugar a palabras encadenadas. Tu dices una palabra, luego yo digo una palabra que '
                   'empiece por la última letra de la palabra que has dicho y asi sucesivamente.')
        used_words = []

        with open('./models/es.dict', 'r') as f:
            all_words = [line.split(None, 1)[0] for line in f]

        known_words = [word.upper() for word in all_words if len(word) > 4 and not word.endswith('s')]

        self.speak('Di una palabra')

        last_letter = ''
        while True:
            self.listen()
            word = self.last_recognised.upper()
            num_words = len(word.split(' '))
            if num_words > 1:
                self.speak('¡No vale! Has dicho más de una palabra! Vuelve a intentarlo.')
                continue
            if word in used_words:
                self.speak('¡Vaya! Has perdido. Esa palabra ya la hemos dicho.')
                break
            if last_letter and not word.startswith(last_letter):
                self.speak('¡Vaya! Has perdido. La palabra {} no empieza por la letra {}.'.format(word, last_letter))
                break
            try:
                letter = word[-1]
                used_words.append(word)
                try:
                    known_words.remove(word)
                except ValueError:
                    pass

                know_words_letter = [w for w in known_words if w.upper().startswith(letter.upper())]
                own_word = random.choice(know_words_letter)

                if not own_word:
                    self.speak('No sé ninguna palabra. Has ganado')
                else:
                    used_words.append(own_word)
                    try:
                        known_words.remove(own_word)
                    except ValueError:
                        pass
                    self.speak('Ok, mi palabra es: {}. Te toca.'.format(own_word), remember=False)
                    print(own_word)
                    last_letter = own_word[-1]
            except IndexError:
                self.speak('Lo siento, tengo problemas tratando de entenderte, ¿puedes repetir la palabra o decir otra?')
