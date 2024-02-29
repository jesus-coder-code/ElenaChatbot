import requests
import sett
import json
import time

def obtener_Mensaje_whatsapp(message):
    if 'type' not in message :
        text = 'mensaje no reconocido'

    typeMessage = message['type']
    if typeMessage == 'text':
        text = message['text']['body']
    return text

def enviar_Mensaje_whatsapp(data):
    try:
        whatsappToken = sett.whatsapp_token
        whatsappUrl = sett.whatsapp_url
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'Bearer' + whatsappToken}
        #print("se envia ", data)
        response = requests.post(whatsappUrl, 
                                 headers=headers, 
                                 data=data)
        
        if response.status_code == 200:
            return 'mensaje enviado', 200
        else:
            return 'error al enviar mensaje', response.status_code
    except Exception as e:
        return e,403
    
def text_Message(number,text):
    data = json.dumps(
            {
                "messaging_product": "whatsapp",    
                "recipient_type": "individual",
                "to": number,
                "type": "text",
                "text": {
                    "body": text
                }
            }
    )
    return data


def administrar_chatbot(text,number, messageId, name):
    try:
        text = text.lower() #mensaje que envio el usuario
        list = []
        #print("mensaje del usuario: ",text)

        data = text_Message(number, "hola soy Elena Chatbot")
        enviar_Mensaje_whatsapp(data)
    except Exception as e:
        print(e)
        return 'error' + str(e)



