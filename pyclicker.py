import pyautogui, time, random, os # Importando librerías.

banner = '''
8888888b.            .d8888b.  888 d8b          888                       
888   Y88b          d88P  Y88b 888 Y8P          888                       
888    888          888    888 888              888                       
888   d88P 888  888 888        888 888  .d8888b 888  888  .d88b.  888d888 
8888888P"  888  888 888        888 888 d88P"    888 .88P d8P  Y8b 888P"   
888        888  888 888    888 888 888 888      888888K  88888888 888     
888        Y88b 888 Y88b  d88P 888 888 Y88b.    888 "88b Y8b.     888     
888         "Y88888  "Y8888P"  888 888  "Y8888P 888  888  "Y8888  888     
                888                                                       
           Y8b d88P                                                       
            "Y88P"                                                        \n'''

INFO = "\n[i] Herramientas que presiona teclas de forma automatica."
INFO2 = "\n[i] Creado por Rodion (github.com/IamRodion)\n"

def cleanScreen(): # Función que limpia la pantalla.
    if os.name == 'posix': 
        os.system("clear")
    else:
        os.system("cls")

def main(key, delay, delay_max): # Función principal del código.
    
    delay_random = random.uniform(delay, delay+delay_max) # Se obtiene un número de tipo float aleatorio entre el rango de retardo y el retardo máximo establecido.
    delay_random = round(delay_random, 2) # Se reduce el número de tipo float obtenido a un número de tipo float de 2 decimas.

    pyautogui.press(key) # Se presiona la tecla establecida. Todos los nombres de las teclas se obtienen con pyautogui.KEY_NAMES.
    fecha, hora = getDateAndTime() # Obteniendo la fecha y hora justo antes de la ejecución.
    registro = f'[{fecha} {hora}] Tecla "{key}" ha sido presionada.' # Generando texto a registrar.
    logWrite(registro) # Escribiendo registro en el archivo de logs.

    time.sleep(delay_random) # Se realiza una espera establecida con el número de tipo flotante generado.

def logWrite(text): # Función que registra texto en el archivo de logs.
    with open('log.txt', 'a') as log: # Abre el archivo de log.
        log.write(text+'\n') # Escribe el tecto en el archivo de log.

def getDateAndTime(): # Función que devuelve la fecha y la hora.
    fecha, hora = time.strftime("%d/%m/%Y"), time.strftime("%H:%M:%S") # Obteniendo fecha y hora.
    return fecha, hora # Devolviendo fecha y hora.

if __name__ == "__main__": # Inicializador.
    try: # Intenta ejecutar la función principal luego de obtener todos los parámetros necesarios.
        cleanScreen() # Limpia la pantalla.
        print(banner, INFO, INFO2) # Muestra el banner y la info del programa.

        key = input("[?] Indique la tecla a ser precionada: ") # Obteniendo la tecla a presionar.
        delay = float(input("[?] Indique la cantidad de retardo en segundos: ")) # Obteniendo el retardo en segundos.
        delay_max = float(input("[?] Indique el rango de aletoriedad máximo en segundos (0 = sin aletoriedad): ")) # Obteniendo el rango aleatorio.

        fecha, hora = getDateAndTime() # Obteniendo la fecha y hora justo antes de la ejecución.
        registro = f'[{fecha} {hora}] Programa iniciado | Presionando la tecla "{key}" cada {delay} segundos con retardo máximo de {delay_max} segundos.' # Generando texto a registrar.
        logWrite("-------------------------------------------------------------------------------------------------------------------------")
        logWrite(registro) # Escribiendo registro en el archivo de logs.

        time.sleep(5) # Retardo de 5 segundos para enfocar la pantalla donde se hará clicks

        while True: # Ciclo principal de la función.
            main(key, delay, delay_max) # Ejecutando la función principal.
            
    except KeyboardInterrupt: # En caso que se detenga la ejecución a travéz del teclado (Ctrl+C) mostrará un mensaje y cerrará el programa.
        fecha, hora = getDateAndTime() # Obteniendo la fecha y hora justo antes de la ejecución.
        registro = f'[{fecha} {hora}] Programa finalizado.' # Generando texto a registrar.
        logWrite(registro) # Escribiendo registro en el archivo de logs.
        logWrite("-------------------------------------------------------------------------------------------------------------------------")

        print("\nCerrando programa...")

