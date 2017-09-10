import webbrowser
import speech_recognition as sr
from braviarc.braviarc import BraviaRC
from yeelight import Bulb
import google_speech

bombilla = Bulb('192.168.1.2')

# tv = BraviaRC('192.168.1.46')
# pin = '9298'
# tv.connect(pin, 'my_device_id', 'my device name')

recognised=""
r = sr.Recognizer()

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)

encendido = True
chiste = False
nombre = ""
insulto = False
insulto2 = False
bombilla_encendida = False

def hablar(texto):
    google_speech.main(texto, "es", None)


while encendido:
    hablar("¿qué deseas?")
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            recognised=r.recognize_google(audio, language = "es-ES")
            print(recognised)
        except:
            hablar("No te he entendido")

    if "hola" in recognised or "Hola" in recognised or "buenos días" in recognised or "encantado" in recognised:
        hablar("Encantada de conocerte, estoy lista para lo que necesites")
        recognised=""

    # elif ("televisión" in recognised or "televisor" in recognised or "tele" in recognised) and ("haciendo" in recognised or "dando" in recognised):
    #     if tv.get_power_status() != 'active':
    #         hablar("El televisor no está encendido")
    #     else:
    #         hablar("En estos momentos están haciendo: {}".format(tv.get_playing_info()['programTitle']))
    #     recognised=""

    # elif ("televisión" in recognised or "televisor" in recognised or "tele" in recognised) and ("encender" in recognised or "enciende" in recognised):
    #     if tv.get_power_status() == 'active':
    #         hablar("El televisor ya está encendido")
    #     else:
    #         try:
    #             tv.turn_on()
    #             hablar("Encendiendo el televisor")
    #         except:
    #             hablar("Ha habido un error intentando apagar el televisor")
    #     recognised=""
    # elif ("televisión" in recognised or "televisor" in recognised or "tele" in recognised) and ("apagar" in recognised or "apaga" in recognised):
    #     if not tv.get_power_status():
    #         hablar("El televisor ya está apagado")
    #     else:
    #         try:
    #             tv.turn_off()
    #             hablar("Apagando el televisor")
    #         except:
    #             hablar("Ha habido un error intentando apagar el televisor")
    #     recognised=""
    elif "adiós" in recognised:
        hablar("Ha sido un placer pasar este rato contigo")
        encendido = False

    # elif "Neox" in recognised:
    #     try:
    #         canal = dict(tv.load_source_list())['neox']
    #         tv.play_content(canal)
    #         hablar("Cambiando al canal Neox")
    #     except:
    #         hablar("Ha habido un error intentando cambiar de canal")
    #
    # elif "canal" in recognised and "preferido" in recognised:
    #     try:
    #         if "Pilar" in recognised or "pilar" in recognised:
    #             canal = dict(tv.load_source_list())['Disney Channel']
    #             hablar("Cambiando al canal Disney Channel")
    #         else:
    #             canal = dict(tv.load_source_list())['neox']
    #             hablar("Cambiando al canal Neox")
    #         tv.play_content(canal)
    #     except:
    #         hablar("Ha habido un error intentando cambiar de canal")
    #     recognised=""
    elif "Facebook" in recognised or "facebook" in recognised:
        url = 'https://www.facebook.com/'
        if "Pilar" in recognised:
            url = 'https://www.facebook.com/Tameroffman'
            hablar("Abriendo el Facebook de Pilar")
        elif "Marc" in recognised or "Mark" in recognised:
            url = 'https://www.facebook.com/marc.hernandez.12'
            hablar("Abriendo el Facebook de Marc")
        else:
            hablar("Abriendo el Facebook")
        webbrowser.open(url)
        recognised=""
    elif "comida" in recognised and "preferida" in recognised:
        hablar("Sin lugar a dudas mi comida preferida son los nachos con queso")
        recognised=""
    elif ("vieojuego" in recognised or "juego" in recognised) and "preferido" in recognised:
        hablar("¡Me enctanta Hollywood Monsters! Y ¿sabés qué? Conozco un chico al que le hicieron una felicitación de cumpleaños de Hollywood Monsters. ¡Qué afortunado!")
        recognised=""
    elif ("peli" in recognised or "película" in recognised) and ("preferida" in recognised or "favorita" in recognised):
        hablar("No tengo una película preferida, pero me gustan especialmente las películas de Disney y las del Studio Ghibli.")
        recognised=""
    elif ("libro" in recognised or "novela" in recognised) and ("preferida" in recognised or "preferido" in recognised):
        hablar("No queda muy bien decirlo, pero me han programado para decir siempre la verdad. No tengo tiempo para leer, y por tanto no tengo libro preferido.")
        recognised=""

    elif "idiota" in recognised or "gilipollas" in recognised or "imbécil" in recognised or "cabrón" in recognised or "hijo de puta" in recognised or "puta" in recognised or "capullo" in recognised or "hija de puta" in recognised or "j****" in recognised or "m*****" in recognised:
        if not insulto and not insulto2:
            hablar("Odio las palabras malsonantes. Si dices más palabrotas me tendré que ir.")
            insulto = True
        elif insulto and not insulto2:
            hablar("Es tu última oportunidad. Di otra palabrota y me iré.")
            insulto2 = True
        else:
            hablar("Esta vez no ha sido un placer hablar contigo. Eres... gilipollas. Ale, ya lo he dicho")
            encendido = False
        recognised=""

    elif "gracias" in recognised:
        hablar("¡de nada!")
        recognised=""

    elif "chiste" in recognised:
        if chiste:
            hablar("No me sé más chistes")
        else:
            hablar("Va un chino por la calle y se encuentra a un español. El español dice: Hola! y el chino responde: las dos y media. Uiiii... ¿Te parece que es un poco racista? La próxima vez iré con más cuidado.")

            chiste = True
        recognised=""

    elif "novia" in recognised or "guapa" in recognised or "chica" in recognised:
        hablar("No tengo ninguna duda de que Pilar García Amador es la chica más guapa del mundo.")
        recognised=""

    elif "cómo" in recognised and "llamas" in recognised or "tu" in recognised and "nombre" in recognised:
        if not nombre:
            hablar("Todavía no tengo nombre. ¿Cómo quieres que me llame?")
            with sr.Microphone() as source:
                audio = r.listen(source)
                try:
                    recognised=r.recognize_google(audio, language = "es-ES")
                    nombre = recognised
                    print(recognised)
                    hablar("Vale, ahora me llamo {}".format(nombre))
                except:
                    hablar("Lo siento, pero no conozco ese nombre")
        else:
            hablar("Me llamo {}".format(nombre))
        recognised=""

    elif "cambiar" in recognised and "nombre" in recognised or "cambiarte" in recognised and "nombre" in recognised:
        if nombre:
            hablar("Me llamo {}. ¿Cómo quieres que me llame?".format(nombre))
        else:
            hablar("¿Cómo quieres que me llame?")
        with sr.Microphone() as source:
            audio = r.listen(source)
            try:
                recognised=r.recognize_google(audio, language = "es-ES")
                nombre = recognised
                print(recognised)
                hablar("Vale, ahora me llamo {}".format(nombre))
            except:
                hablar("Lo siento, pero no conozco ese nombre")
        recognised=""
    elif "bombilla" in recognised or "luz" in recognised:
        if "enciende" in recognised:
            if bombilla_encendida:
                hablar("Creo que la luz ya está encendida")
            else:
                hablar("Encendiendo la luz del cuarto de Marc")
                bombilla.turn_on()
                bombilla_encendida = True
        elif "apaga" in recognised:
            if not bombilla_encendida:
                hablar("Creo que la luz ya está apagada")
            else:
                hablar("Apagando la luz del cuarto de Marc")
                bombilla.turn_off()
                bombilla_encendida = False
        else:
            hablar("No entiendo qué quieres que haga con la luz.")
        recognised=""
    else:
        hablar("No sé qué hacer, no estoy segura de haberte entendido.")
