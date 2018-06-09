import operator

import nltk
import numpy as np
from nltk.stem.snowball import SpanishStemmer
from voice_assistant import Assistant as _Assistant
from keras.models import model_from_json


class Assistant(_Assistant):
    """
    Allows to build an assitant, which can:
    - Implement new behaivour from active modules
    - Analyze last recognised words
    - Execute actions inside

    """

    def __init__(self, language='en', database_name='memory', memory_table='memory', listen_log_table='listen_log',
                 speak_log_table='speak_log'):
        super().__init__(language, database_name, memory_table, listen_log_table, speak_log_table)

        try:
            json_file = open('modelo_gustos.json', 'r')
            loaded_model_json = json_file.read()
            json_file.close()

            self.model = model_from_json(loaded_model_json)
            self.model.load_weights("modelo_gustos.h5")
            self.model.compile(loss='mean_squared_error', optimizer='adam', metrics=['binary_accuracy'])
        except Exception:
            print('****ERROR: Error cargando modelo...****')

        self.stemmer = SpanishStemmer()
        self.words = ['¿qu', '?', 'peli', 'pelis', 'color', 'favorit', 'leer', 'libr', 'novel', 'ver', 'prefier',
                      'gust', 'pelicul', 'jug', '¿cual', 'prefer', 'jueg', 'com', 'plat', 'animal', 'videojueg']
        self.classes = ['comida', 'color', 'animal', 'juego', 'libro', 'película']

    def main(self, initial_sentence='¿Qué deseas?'):
        self.speak(initial_sentence, remember=False)
        self.listen()
        self.process_orders(self.last_recognised)
        self.adjust_for_ambient_noise()

    def process_orders(self, sentence):
        _class = self.classify_sentence(sentence)

        if not _class:
            self.speak('no estoy segura de lo que me quieres preguntar')
        else:
            if _class == 'comida':
                self.speak('Sin lugar a dudas mi comida preferida son los nachos con queso')
            if _class == 'color':
                self.speak('Mi color preferido es el escarlata.')
            if _class == 'animal':
                self.speak('Me gustan mucho los grandes felinos, pero mi animal preferido es una perra que se llama'
                           ' Arale.')
            if _class == 'juego':
                self.speak('¡Me encanta Hollywood Monsters!')
            if _class == 'libro':
                self.speak('No queda muy bien decirlo, pero me han programado para decir siempre la verdad. No tengo'
                           ' tiempo para leer, y por tanto no tengo libro preferido.')
            if _class == 'película':
                self.speak('No tengo una película preferida, pero me gustan especialmente las películas de Disney y'
                           ' las del Studio Ghibli.')

    def classify_sentence(self, sentence, min_val=0.5):
        results = self.get_classification(sentence)
        if float(results[0][1]) < min_val:
            return None
        else:
            return results[0][0]

    def clean_up_sentence(self, sentence):
        sentence_words = nltk.word_tokenize(sentence)
        sentence_words = [self.stemmer.stem(word.lower()) for word in sentence_words]
        return sentence_words

    def bow(self, sentence, words):
        sentence_words = self.clean_up_sentence(sentence)
        bag = [0] * len(words)
        for s in sentence_words:
            for i, w in enumerate(words):
                if w == s:
                    bag[i] = 1
        return np.array(bag)

    def get_classification(self, sentence):
        array = [self.bow(sentence, self.words)]
        np_array = np.array(array, "float32")
        prediction = self.model.predict(np_array).round(2)[0]
        result = dict(zip(self.classes, prediction))
        return sorted(result.items(), key=operator.itemgetter(1))[::-1]




