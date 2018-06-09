from actions import ModuleMixin


class OrganizationMixin(ModuleMixin):

    orders = [{'words': ['qué hora es'],
               'action': 'self.calculate_hour()',
               'speak': '',
               'orders': None,
               },
              ]

    def calculate_hour(self):
        import datetime
        now = datetime.datetime.now()
        self.speak('Son las {} y {} minutos.'.format(now.hour, now.minute))


# elif home.has_heard('avísame dentro de'):
#     numbers = [int(number) for number in home.last_recognised.split() if s.isdigit()]
#     if home.has_heard('horas'):
#         if len(numbers) > 1:
#
#     elif home.has_heard('minutos'):
#         pass
#     else:
#         home.speak
# elif home.has_heard(['lista', 'listado']):
#     if home.has_heard(['crea', 'crear', 'créame']):
#         # home.speak('Creando una lista. ¿Qué nombre quieres ponerle a la lista?')
#         # name = home.listen()
#         # home.speak('He creado una lista llamada {}.'.format('name'))
#         home.speak('He creado una lista sustituyendo la antigua')
#         home.speak('¿Quieres añadir algo a la lista?')
#         home.listen()
#         if home.has_heard(['si', 'sí']):
#             home.speak('Dime qué elementos quieres añadir separados por una "y"')
#             elements = home.listen()
#             lista += elements.split(' y ')
#             home.speak('De acuerdo, he añadido esos elementos a la lista.')
#         elif home.has_heard('no'):
#             home.speak('De acuerdo')
#     elif home.has_heard(['consultar', 'dime', 'léeme', 'lee']):
#         lista_str = ''
#         for element in lista:
#             lista_str += element+', '
#         home.speak('Los elementos que hay en la lista son: {}'.format(lista_str))
