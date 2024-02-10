import random
from mazo import mazo


def tirar_runas():
    # Establecemos una versión intacta del diccionario original
    mazo_original = mazo

    # Bienvenida fuera del loop
    print("""— Bienvenido a la Estrella. Soy Argwynzar. ¿Puedo ofrecerte una tirada?\n""")
    
    while True:
        # Cargamos una copia del mazo original para modificarlo
        mazo_modificado = mazo_original

        # Opcionesadiós dentro del loop
        print("""Dependiendo del tipo de consulta puede ser una tirada LIBRE, donde escoges cuántas runas quieres que revise. Te aconseo lo limites un poco, ya que puede volverse caótico. No pidas más de 3.
            También está la elección SENCILLA, en que lanzo 3 runas que  marcan el pasado, presente y futuro de algo.
            Después está la tirada COMPLEJA donde cinco runas marcan el pasado, los factores a favor, los factores en contra, el futuro y el concepto general de cómo irán las cosas.
            Finalmente, la más complicada es la tirada PROFUNDA, en que se usan 9 runas para explorar la postura de lo que rodea la cuestión.\n
            Cuando estés satisfecho, solo dime adiós.""")
        
        # Constante que se usará para escoger entre opciones
        peticion = input("¿Qué tipo de revelación buscas hoy, aventurero?\n").lower()

        # Barajar el mazo para que sus pares estén en desorden
        random.shuffle(mazo_modificado)
        dict(mazo_modificado)

        # Opción de salida
        if peticion == "adiós":
            print("Que la fortuna brille en tu camino, viajero.")
            break

        # Se deriva a las distintas opciones que ofrece la función con ifs y trys para los errores
        
        # LIBRE
        elif peticion == "libre":
            try:
                libre = int(input("¿Cuántas runas quieres tirar? Dame un número. "))
            except ValueError:
                libre = int(input(
                    "Escríbemelo en números enteros, anda. ¿Cuántas runas quieres tirar? "))

            if libre in range(3, 6):
                print("No seas avaricioso, pero te lo permito esta vez.")
                for n in range(libre):
                    runa, cara = mazo.pop(n)
                    print(f"{runa}{cara}\n")
            elif libre > 6 or libre == 0:
                seg_oportunidad = int(input(
                    "Podría maldecirte por esto. Anda, dame otra cantidad. "))
                if seg_oportunidad > 6 or 0:
                    print("Eres imposible.")
                    exit()
                else:
                    for n in range(libre):
                        runa, cara = mazo.pop(n)
                        print(f"{runa}{cara}\n")
            else:
                for n in range(libre):
                    runa, cara = mazo.pop(n)
                    print(f"{runa}{cara}\n")


        # SENCILLA
        # Lanza 3 en configuración pasado, presente, futuro
        elif peticion == "sencilla":
            try:

                print("""\n Las tirada sencilla es una de las más rápidas y eficientes ya que da una revisión rápida a tu situación y te trae un pronóstico sobre lo que ha de venir. \n
                    ¡Veamos qué tienen que decir las runas! \n""")
                
                for n in range(4):
                    runa, cara = mazo.pop()
                    print(f"""Tu pasado fue la runa {runa}{cara}""")
                    runa, cara = mazo.pop()
                    print(f"""Ahora vives bajo el influjo de {runa}{cara}""")
                    runa, cara = mazo.pop()
                    print(f"""Y tu futuro viene descrito con los designios de {runa}{cara}""")
            except:
                print("Algo no salió bien.")


        # COMPLEJA 
        # Lanza 5 en configuración cardinales y centro
        elif peticion == "compleja":
            try:
                runa, cara = mazo.pop()
                print(f"""\n Uuuh, ¿una tirada compleja? Necesitas entender exactamente qué ocurre con tu situación actual. Entiendo.
                    ¡Bien! Pues la primera carta está al sur y es aquella sobre la que nos apoyamos. En este caso es {runa}{cara}\n""")
                runa, cara = mazo.pop()
                print(f"""La siguiente es al norte y es el poder que vela por nosotros, el que nos cuida y ayuda. En tu caso, {runa}{cara}\n""")
                runa, cara = mazo.pop()
                print(f"""Entiendo... \n 
                    Ahora vienen las dificultades, los enemigos o aquello que está puesto en tu camino para oponerse a tus deseos y necesidades. {runa}{cara}\n""")
                runa, cara = mazo.pop()
                print(f"""Pero no todo está en tu contra, tienes de tu lado a {runa}{cara}\n""")
                runa, cara = mazo.pop()
                print(f"""Esto se acaba ya, la siguiente runa resume la tirada, las energías que actúan en tu presente, y en tu caso es {runa}{cara}""")
                
            except:
                print("Algo no salió bien.")

        # PROFUNDA
        # Lanza la versión en X con 8 (2*arista) + 1 central
        elif peticion == "profunda":
            print("""Una tirada profunda, entiendo. Estas se leen situando las runas en forma de equis dejando una en el centro. Cada arista contiene dos cartas y traen información de partes distintas de tu realidad actual. """)
            try:
                runa, cara = mazo.pop()
                print(f"""{runa}{cara}\n""")

                runa, cara = mazo.pop()
                print(f"""{runa}{cara}\n""")

                runa, cara = mazo.pop()
                print(f"""{runa}{cara}\n""")

                runa, cara = mazo.pop()
                print(f"""{runa}{cara}\n""")

                runa, cara = mazo.pop()
                print(f"""{runa}{cara}\n""")

                runa, cara = mazo.pop()
                print(f"""{runa}{cara}\n""")
                
                runa, cara = mazo.pop()
                print(f"""{runa}{cara}\n""")

                runa, cara = mazo.pop()
                print(f"""{runa}{cara}\n""")

                runa, cara = mazo.pop()
                print(f"""{runa}{cara}\n""")

            except:
                print("Algo no salió bien.")
        

        # Restauramos el mazo al original
        mazo_original = mazo_modificado

tirar_runas()
