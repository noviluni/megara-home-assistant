from actions import ModuleMixin
from conf import GOOGLE_KNOWLEDGE_API_KEY


class MoreMixin(ModuleMixin):

    orders = [{'words': ['traducir', 'traduce', 'tradúceme'],
               'action': 'self.get_translation()',
               'speak': '',
               'orders': None,
               },
              {'words': ['Google', 'google'],
               'action': '',
               'speak': '',
               'orders': [{'words': ['buscar', 'busca'],
                           'action': "self.google_search()",
                           'speak': '',
                           'orders': None,
                           },
                          ]
               },
              ]

    def _google_search_api(self, query, language=None):
        language = language if language else self.speak_language
        processed_query = query.replace(" ", "+")

        import requests
        url = 'https://kgsearch.googleapis.com/v1/entities:search'
        params = {'key': GOOGLE_KNOWLEDGE_API_KEY, 'languages': language, 'limit': '1', 'query': processed_query}
        response = requests.get(url, params=params)
        result = response.json()
        try:
            description = result['itemListElement'][0]['result']['detailedDescription']['articleBody']
        except (KeyError, IndexError):
            description = 'No consigo información sobre {}'.format(query)

        return description

    def google_search(self):
        self.speak('¿Qué deseas buscar en google?')
        self.listen()
        query = self.last_recognised
        result = self._google_search_api(query)
        self.speak(result)

    def translate(self, sentence, to_language='EN', from_language='ES'):
        import pydeepl
        translation = pydeepl.translate(sentence, to_language, from_lang=from_language)
        return translation

    def get_translation(self):
            idiomas = {'alemán': 'DE', 'inglés': 'EN', 'francés': 'FR', 'español': 'ES', 'italiano': 'IT',
                       'holandés': 'NL', 'polaco': 'PL'}
            lang_1 = ''
            lang_2 = ''
            index_1 = None
            index_2 = None
            from_lang = ''
            to_lang = ''
            traduccion = ''

            for idioma in idiomas:
                index = self.last_recognised.find(idioma)
                if index > 0 and lang_1 == '':
                    lang_1 = idioma
                    index_1 = index
                elif index > 0 and lang_1 != '' and lang_2 == '':
                    lang_2 = idioma
                    index_2 = index

            if lang_1 and lang_2 and index_1 and index_2:
                if index_1 < index_2:
                    from_lang, to_lang = lang_1, lang_2
                else:
                    to_lang, from_lang = lang_1, lang_2

                self.speak('OK, voy a traducir del {} al {}. Dime qué frase quieres que traduzca'.format(from_lang,
                                                                                                         to_lang))
                self.listen(language=idiomas[from_lang])
                frase = self.last_recognised
                self.speak('Esta frase se dice así:')
                traduccion = self.translate(frase, idiomas[to_lang], idiomas[from_lang])
                print(traduccion)
                self.speak(traduccion, language=idiomas[to_lang])
            else:
                self.speak('Debes decir de qué idioma a qué idioma quieres traducir. Si lo has hecho, entonces lo que '
                           'ocurre es que no sé hablar alguno de los idiomas que has mencionado.')
            return traduccion
