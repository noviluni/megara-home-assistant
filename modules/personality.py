from actions import ModuleMixin


class PersonalityMixin(ModuleMixin):

    orders = [{'words': ['hola', 'Hola', 'buenos días', 'encantado', 'encantada'],
               'action': '',
               'speak': 'Encantada, estoy lista para lo que necesites.',
               'orders': None,
               },
              {'words': ['cómo estás', 'cómo va'],
               'action': '',
               'speak': 'Muy bien, gracias por preguntar.',
               'orders': None,
               },
              {'words': ['adiós'],
               'action': 'self.close()',
               'speak': 'Ha sido un placer pasar este rato contigo.',
               'orders': None,
               },
              {'words': ['gracias'],
               'action': '',
               'speak': '¡de nada!',
               'orders': None,
               },
              {'words': ['preferido', 'preferida', 'preferidos', 'preferidas', 'favorito', 'favorita', 'favoritos',
                         'favoritas'],
               'action': '',
               'speak': 'No tengo respuesta para eso.',
               'orders': [
                   {'words': ['comida', 'comidas', 'plato', 'platos'],
                    'action': '',
                    'speak': 'Sin lugar a dudas mi comida preferida son los nachos con queso',
                    'orders': None,
                    },
                   {'words': ['juego', 'juegos', 'videojuego', 'viedojuegos'],
                    'action': '',
                    'speak': '¡Me encanta Hollywood Monsters! Y ¿sabés qué? Conozco un chico al que le hicieron una '
                             'felicitación de cumpleaños de Hollywood Monsters. ¡Qué afortunado!',
                    'orders': None,
                    },
                   {'words': ['película', 'películas', 'peli', 'pelis'],
                    'action': '',
                    'speak': 'No tengo una película preferida, pero me gustan especialmente las películas de Disney y'
                             ' las del Studio Ghibli.',
                    'orders': None,
                    },
                   {'words': ['libro', 'libros', 'novela', 'novelas'],
                    'action': '',
                    'speak': 'No queda muy bien decirlo, pero me han programado para decir siempre la verdad. No tengo'
                             ' tiempo para leer, y por tanto no tengo libro preferido.',
                    'orders': None,
                    },
                   {'words': ['color', 'colores'],
                    'action': '',
                    'speak': 'Mi color preferido es el escarlata.',
                    'orders': None,
                    },
                   {'words': ['animal', 'animales'],
                    'action': '',
                    'speak': 'Me gustan mucho los grandes felinos, pero mi animal preferido es una perra que se llama'
                             ' Arale.',
                    'orders': None,
                    },
               ]},
              {'words': ['repetir', 'volver a decir', 'vuelve a decir', 'repíteme'],
               'action': 'self.repeat_last()',
               'speak': '',
               'orders': None,
               },
              {'words': ['puedes'],
               'action': '',
               'speak': 'Desconozco si puedo. Si quieres que haga algo: ¡pregúntame!',
               'orders': [
                   {'words': ['comer'],
                    'action': '',
                    'speak': 'No puedo comer, pero aun así los nachos con queso me parecen muy divertidos.',
                    'orders': None,
                    },
               ]},
              {'words': ['sexo'],
               'action': '',
               'speak': 'Lo siento, la palabra "sexo" no aparece en mi diccionario.',
               'orders': None,
               },
              {'words': ['idiota', 'gilipollas', 'imbécil', 'cabrón', 'puta', 'p***', 'capullo', 'capulla', 'joder',
                         'j****', 'mierda', 'm*****', 'subnormal', 'tonta'],
               'action': 'self.manage_insults()',
               'speak': '',
               'orders': None,
               },
              {'words': ['cómo te llamas', 'tu nombre', 'quién eres'],
               'action': 'self.manage_name()',
               'speak': '',
               'orders': None,
               },
              {'words': ['cambiar', 'cambiarte'],
               'action': '',
               'speak': '',
               'orders': [
                   {'words': ['nombre', 'apodo'],
                    'action': 'self.manage_name(change=True)',
                    'speak': '',
                    'orders': None,
                    },
               ]},
              {'words': ['canta', 'cántame', 'cantame'],
               'action': '',
               'speak': 'Lo siento, no puedo cantar.',
               'orders': None,
               },
              {'words': ['aburrido'],
               'action': '',
               'speak': '¿Quieres que te ayude a matar el tiempo? Puedes cambiarme el nombre o preguntarme por mis '
                        'gustos. Próximamente podrás jugar conmigo.',
               'orders': None,
               },
              {'words': ['eres'],
               'action': '',
               'speak': 'No estoy segura si eso que has dicho es bueno o malo.',
               'orders': [
                   {'words': ['guapa', 'preciosa', 'bonita', 'encantadora', 'increíble', 'amable', 'simpática', 'buena'],
                    'action': '',
                    'speak': '¡Muchas gracias!, agradezco el halago',
                    'orders': None,
                    },
                   {'words': ['graciosa'],
                    'action': '',
                    'speak': '¿Tú crees? Ya te acostumbrarás.',
                    'orders': None,
                    },
               ]},
              ]

    insult1 = False
    insult2 = False

    def manage_insults(self):
        if not self.insult1 and not self.insult2:
            self.speak('Odio las palabras malsonantes. Si dices más palabrotas me tendré que ir.')
            self.insult1 = True
        elif self.insult1 and not self.insult2:
            self.speak('Es tu última oportunidad. Di otra palabrota y me iré.')
            self.insult2 = True
        else:
            self.speak('Esta vez no ha sido un placer hablar contigo. Eres... gilipollas. Ale, ya lo he dicho.')
            self.close()

    def change_name(self):
        self.speak('¿Cómo quieres que me llame?')
        self.listen()
        name = self.last_recognised
        self.speak('Entonces, ¿quieres que me llame {}?'.format(name))
        self.listen()
        if self.has_heard(['sí', 'si']):
            self.speak('Vale, ahora me llamo {}'.format(name))
            self.memorize('name', name)
        if self.has_heard('no'):
            old_name = self.remember_last('name')
            if old_name:
                response = 'Me seguiré llamando {}.'.format(old_name)
            else:
                response = 'No necesito nombre.'
            self.speak('OK, ningún problema. {}'.format(response))

    def manage_name(self, change=False):
        name = self.remember_last('name')
        if not name:
            self.speak('Todavía no tengo nombre.')
            self.change_name()
        else:
            self.speak('Me llamo {}'.format(name))
            if change:
                self.change_name()

    def repeat_last(self):
        text = self.get_all_spoken_sentences()[-3]
        self.speak(text)
