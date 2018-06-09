from conf import BULB_IP

from yeelight import Bulb, RGBTransition, Flow, BulbException

from actions import ModuleMixin


class YeelightMixin(ModuleMixin):
    bulb = None

    orders = [
              {'words': ['bombilla', 'luz'],
               'action': '',
               'speak': 'No sé qué quieres que haga con la luz',
               'orders': [{'words': ['enciende', 'encender', ],
                           'action': 'self.turn_on_bulb()',
                           'speak': '',
                           'orders': None,
                           },
                          {'words': ['apaga', 'apagar'],
                           'action': 'self.turn_off_bulb()',
                           'speak': '',
                           'orders': None,
                           },
                          {'words': ['color', 'colores'],
                           'action': 'self.flow_bulb()',
                           'speak': '',
                           'orders': None,
                           }
                          ],
               },
    ]

    @classmethod
    def set_up(cls):
        cls.bulb = Bulb(BULB_IP)

    def turn_on_bulb(self):
        try:
            if self.bulb.get_properties()['power'] == 'on':
                self.speak('La bombilla ya está encendida.')
            elif self.bulb.get_properties()['power'] == 'off':
                self.bulb.turn_on()
                self.speak('He encendido la luz.')
        except BulbException:
            self.speak('No he podido contactar con la bombilla.')

    def turn_off_bulb(self):
        try:
            if self.bulb.get_properties()['power'] == 'on':
                self.bulb.turn_off()
                self.speak('He apagado la luz.')
            elif self.bulb.get_properties()['power'] == 'off':
                self.speak('La bombilla ya está apagada.')
        except BulbException:
            self.speak('No he podido contactar con la bombilla.')

    def flow_bulb(self):
        transitions = [
            RGBTransition(255, 0, 255, duration=1000)
        ]

        flow = Flow(count=0, transitions=transitions)
        self.bulb.start_flow(flow)