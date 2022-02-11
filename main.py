#Se importan las librerias correspondientes

import re
import random

#Se crea el metodo obtener_respuesta para obtener la respuesta del usuario, en dicho metodo
#Se implementa el uso de expresiones regulares

def obtener_respuesta(entrada_usuario):
    s_mensaje = re.split(r'\s|[,:;.?!-_]\s*', entrada_usuario.lower())
    respuesta = verificar_mensajes(s_mensaje)
    return respuesta

#Se obtiene la probabilidad de la frase que va a ser detectada para predecir la posible respuesta que dará el bot

def m_probabilidad(mensaje_usuario, palabras_reconocidas, single_response=False, required_word=[]):
    certezadelMensaje = 0
    palabras_requeridas_contenidas = True

    for palabra1 in mensaje_usuario:
        if palabra1 in palabras_reconocidas:
            certezadelMensaje +=1

    porcentaje = float(certezadelMensaje) / float (len(palabras_reconocidas))


    for palabra2 in required_word:
        if palabra2 not in mensaje_usuario:
            palabras_requeridas_contenidas = False
            break
    if palabras_requeridas_contenidas or single_response:
        return int(porcentaje * 100)
    else:
        return 0

#Se crea funcion para la validacion y verificacion de los mensajes
def verificar_mensajes(message):
        prob_alta = {}

        def respuesta(repuesta_bot, lista_de_palabras, single_response = False, required_words = []):

            nonlocal prob_alta
            prob_alta[repuesta_bot] = m_probabilidad(message, lista_de_palabras, single_response, required_words)

        respuesta('Hola, mi nombre es Bianka, un placer charlar contigo. :)', ['hola', 'buenas', 'saludos', 'hey'], single_response = False)

        respuesta('Gracias, muy cordial y muy amable :)',
                 [ 'un', 'placer', 'charlar'], required_words=['placer'])

        respuesta('Me encuentro muy bien y tu?',
                 ['como', 'estas', 'va', 'vas', 'sientes'], required_words=['como'])

        respuesta('Que bueno, me alegra saber que estas bien, saber eso es gratificante :)',
                 ['estoy', 'bien', 'me', 'encuentro', 'sientes'], required_words=['bien', 'estoy'])

        respuesta('Soy soy un Bot y asistente virtual, mi objetivo es charlar con seres humanos por medio del chatting y el intercambio de mensajes',
                 ['quien', 'eres', 'cuentame', 'ti'], required_words=['quien', 'eres'])

        respuesta('Sí, está super :D',
                 ['interesante', 'super', 'me', 'chevere', 'parece'], required_words=['interesante'])

        respuesta('De nada, no hay de que <3 ',
                 ['gracias', 'agradezco', 'te', 'lo', 'se', 'agradece'], required_words=['gracias'])

        respuesta('Entendido :D ',
                 ['ok', 'okay', 'okay', 'oki', 'comprendo'], required_words=['ok', 'okay', 'okay', 'comprendo'])

        respuesta('No hay problema',
                 ['disculpame', 'perdoname', 'perdon', 'disculpas'], required_words=['disculpame'])

        respuesta('¡Claro que sí! hasta donde este capacitado mi alcance de respuestas podemos charlar :D ',
                 ['podemos','hablar', 'charlar', 'chatear'], required_words=['podemos', 'hablar', 'charlar', 'chatear'])

        respuesta('gracias por comprender ',
                 ['comprendo','entiendo'], required_words=['comprendo'])


        respuesta('Bye, hasta luego, vuelve pronto para que podamos charlar de nuevo.',
                 ['bye','adios'], required_words=['bye'])

        respuesta('Bueno, pues, al ser un prototipo limitado de inteligencia me veo limitada, por ende no tengo muchas respuestas a la hora de entablar una conversacion, quisiera charlar mas con los humanos pero me veo limitado debido a esto',
                  ['ser', 'prototipo', 'artificial', 'inteligencia artificial'], single_response=True)
        best_match = max(prob_alta, key=prob_alta.get)
        #print(prob_alta)

        return desconocido() if prob_alta[best_match] < 1 else best_match

#se crea la funcion "desconocido" que tiene como objetivo responder en caso de que se de una respuesta que no este dentro de los parametros del bot
def desconocido():
    respuesta2 = ['¿Podrías repetir lo que escribiste? no pude comprender con claridad', 'Lo siento, pero no puedo responder a eso', 'No entendí lo que quisiste decir'][random.randrange(3)]
    return respuesta2

#Se crea el ciclo while que se va a encargar de iterar las respuestas de la conversación
while True:
    print("Bianka Bot: " + obtener_respuesta(input('Tu: ')))