from flask import Flask, request
import sett 
import services

app = Flask(__name__)

@app.route('/bienvenido', methods=['GET'])
def  bienvenido():
    return 'welcome to Elena Chatbot'

@app.route('/webhook', methods=['GET'])
def verificar_token():
    try:
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')

        if token == sett.token and challenge != None:
            return challenge
        else:
            return 'token incorrecto', 403
    except Exception as e:
        return e,403
    
@app.route('/webhook', methods=['POST'])
def recibir_mensajes():
    try:
        '''body = request.get_json()
        entry = body['entry'][0]
        changes = entry['changes'][0]
        value = changes['value']
        message = value['messages'][0]
        number = message['from']
        messageId = message['id']
        contacts = value['contacts'][0]
        name = contacts['profile']['name']
        text = services.obtener_Mensaje_whatsapp(message)

        services.administrar_chatbot(text, number,messageId,name)'''

        body = request.get_json()
        entry = body['entry'][0]  # Obtener la primera entrada
        message = entry['changes'][0]['value']['messages'][0]  # Obtener el primer mensaje
        message_body = message['text']['body']  # Obtener el cuerpo del mensaje
        number = message['from']  # Obtener el número de teléfono del remitente
        messageId = message['id']  # Obtener el ID del mensaje
        name = entry['changes'][0]['value']['contacts'][0]['profile']['name']  # Obtener el nombre del remitente
        services.administrar_chatbot(message_body, number, messageId, name)  # Llamar a la función para administrar el chatbot
       
        return 'envio correcto'

    except Exception as e:
        return 'no enviado ' + str(e)

if __name__ == '__main__':
    app.run()
