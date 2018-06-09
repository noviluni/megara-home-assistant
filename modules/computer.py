import webbrowser

from actions import ModuleMixin


class ComputerMixin(ModuleMixin):

    orders = [
              {'words': ['Youtube', 'youtube', 'YouTube'],
               'action': "self.open_browser('http://youtube.com')",
               'speak': 'Abriendo Youtube',
               'orders': None,
               },
              {'words': ['Google', 'google'],
               'action': "self.open_browser('http://google.com')",
               'speak': 'Abriendo Google',
               'orders': None,
               },
              {'words': ['Facebook', 'facebook'],
               'action': "self.open_browser('https://www.facebook.com/')",
               'speak': 'Abriendo Facebook',
               'orders': [{'words': ['Pilar', ],
                           'action': "self.open_browser('https://www.facebook.com/Tameroffman')",
                           'speak': 'Abriendo el Facebook de Pilar',
                           'orders': None,
                           },
                          {'words': ['Marc', 'Mark'],
                           'action': "self.open_browser('https://www.facebook.com/marc.hernandez.12')",
                           'speak': 'Abriendo el Facebook de Marc',
                           'orders': None,
                           }
                          ],
               },
    ]

    def open_browser(self, url):
        webbrowser.open(url)
