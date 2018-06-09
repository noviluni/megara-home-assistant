import requests


def obtenerPeliculas():
    parametros = {"aficine_action": "getJSON"}

    url = "http://www.aficine.com/"

    response = requests.get(url, params=parametros)
    peliculas = response.json()

    listaPeliculas = ''

    peliculitas = peliculas["peliculas"]

    for pelicula in peliculitas:
        fecha = pelicula["fecha_estreno"]
        year = fecha[:4]
        month = fecha[4:6]
        day = fecha[6:8]
        listaPeliculas += "{}, estreno el: {} de {} de {}".format(pelicula["titulo"], day, month, year)

    return listaPeliculas

                # peliculas["pases_ocimaxpalma"]
                # peliculas["pases_rivoli"]
                # peliculas["pases_augusta"]
                # peliculas["pases_portopi"]
    return infoPelicula



if __name__ == "__main__":
    print(obtenerPeliculas())
    # print(obtenerDatosPelicula(32060))
