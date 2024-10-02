import random

def obtener_enlaces_descarga(nombre_juego):
    # Esta es una lista simulada de enlaces. En un caso real, obtendrías enlaces de una API o un scraping web.
    enlaces_simulados = [
        f"https://ejemplo.com/descarga/{nombre_juego}/version1",
        f"https://ejemplo.com/descarga/{nombre_juego}/version2",
        f"https://ejemplo.com/descarga/{nombre_juego}/version3",
        f"https://ejemplo.com/descarga/{nombre_juego}/version4",
        f"https://ejemplo.com/descarga/{nombre_juego}/version5",
        f"https://ejemplo.com/descarga/{nombre_juego}/version6",
        f"https://ejemplo.com/descarga/{nombre_juego}/version7",
        f"https://ejemplo.com/descarga/{nombre_juego}/version8",
        f"https://ejemplo.com/descarga/{nombre_juego}/version9",
        f"https://ejemplo.com/descarga/{nombre_juego}/version10",
    ]

    # Barajar los enlaces y devolver solo los primeros 10 (o menos si hay menos de 10)
    random.shuffle(enlaces_simulados)
    return enlaces_simulados[:10]

def main():
    nombre_juego = input("Introduce el nombre del juego: ")
    enlaces = obtener_enlaces_descarga(nombre_juego)

    print("\nEnlaces de descarga para '{}':".format(nombre_juego))
    for enlace in enlaces:
        print(enlace)

if __name__ == "__main__":
    main()
