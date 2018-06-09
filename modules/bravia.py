from actions import ModuleMixin
from conf import TV_IP, TV_PIN
from braviarc.braviarc import BraviaRC


class BraviaMixin(ModuleMixin):
    tv = None

    orders = [{'words': ['traducir', 'traduce', 'tradúceme'],
               'action': 'self.get_translation()',
               'speak': '',
               'orders': None,
               },
              ]

    def __init__(self):
        super().__init__()

        if TV_IP and TV_PIN:
            self.tv = BraviaRC(TV_IP)
            self.tv.connect(TV_PIN, 'my_device_id', 'my device name')

    def get_power_status_tv(self):
        """returns: off, active or standby"""
        return self.tv.get_power_status()

    def turn_on_tv(self):
        self.tv.turn_on()

    def turn_off_tv(self):
        self.tv.turn_off()

    def volume_up_tv(self):
        self.tv.volume_up()

    def volume_down_tv(self):
        self.tv.volume_down()

    def mute_volume_tv(self):
        self.tv.mute_volume(None)

    def get_playing_info_tv(self):
        return self.tv.get_playing_info()['programTitle']

    def media_play_tv(self):
        self.tv.media_play()

    def media_pause_tv(self):
        self.tv.media_pause()

    def media_next_track_tv(self):
        self.tv.media_next_track()

    def media_previous_track_tv(self):
        self.tv.media_previous_track()


# elif home.has_heard([' tele', 'tv', 'televisión', 'televisor']):
#     if home.has_heard(['enciende', 'encender']):
#         if home.get_power_status_tv() == 'active':
#             home.speak('El televisor ya está encendido')
#         else:
#             home.turn_on_tv()
#             home.speak('He encendido el televisor')
#     elif home.has_heard(['apaga', 'apagar']):
#         if home.get_power_status_tv() == 'off' or home.get_power_status_tv == 'standby':
#             home.speak('El televisor ya está apagado')
#         else:
#             home.turn_off_tv()
#             home.speak('He apagado el televisor')
#     elif home.has_heard('volumen'):
#         if home.has_heard(['quita', 'quitar', 'silenciar', 'silencia', 'silencio']):
#             home.mute_volume_tv()
#             home.speak('He silenciado el televisor')
#     else:
#         home.speak('No sé qué quieres que haga con el televisor.')
#
# # if home.has_heard('canal'):
# #     if home.has_heard(preferidos) and home.has_heard('Pilar'):
# #         home.
