from actions import ModuleMixin
from conf import WUNDERGROUND_API_KEY


class WeatherMixin(ModuleMixin):

    orders = [{'words': ['tiempo', 'predicción', 'meteorológica', 'meteorológico'],
               'action': '',
               'speak': '¿Quieres saber el tiempo? Pregúntame sobre el tiempo de hoy, mañana o de pasado mañana.',
               'orders': [{'words': ['hoy', ],
                           'action': "self.forecast(0)",
                           'speak': '',
                           'orders': None,
                           },
                          {'words': ['mañana', ],
                           'action': "self.forecast(1)",
                           'speak': '',
                           'orders': None,
                           },
                          {'words': ['pasado mañana', ],
                           'action': "self.forecast(2)",
                           'speak': '',
                           'orders': None,
                           },
                          ]
               },
              ]

    def _weather_api(self, day, key):
        import requests
        features = 'forecast'
        # features = 'conditions'
        # features = 'hourly'
        url = 'http://api.wunderground.com/api/{key}/{features}/{settings}/q/{query}.{format}'\
            .format(key=key, features=features, settings='lang:CA', query='39.632495,2.630316', format='json')
        response = requests.get(url)
        dias = response.json()
        try:
            result = dias['forecast']['txt_forecast']['forecastday'][day]['fcttext_metric']
        except KeyError:
            return ''
        return result

    def forecast(self, day=0):
        forecast = self._weather_api(day, key=WUNDERGROUND_API_KEY)
        equival = {'NO': 'Noroeste', 'SO': 'Suroeste', 'NE': 'Noreste', 'SE': 'Sureste', ' C': ' grados'}
        day_names = {0: 'hoy', 1: 'mañana', 2: 'pasado mañana'}
        for element in equival:
            forecast = forecast.replace(element, equival[element])
        if forecast:
            if 0 < day <= 3:
                self.speak('La previsión para {} es: {}.'.format(day_names[day], forecast))
            else:
                self.speak('La previsión es: {}.'.format(forecast))
        else:
            self.speak('He tenido un problema intentando obtener la previsión del tiempo.')
