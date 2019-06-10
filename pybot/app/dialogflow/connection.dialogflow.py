import requests
import json
import os
import dialogflow_v2
web_hook_url="https://whapi.officemate.co.th/send_message"

hd = {
    "content-type":"application/json"
}
def submit_message(user_id,message) :#sent message to @app.route('/send_message', methods=['post'])
  
    msg= {"recipient":{"id":user_id},"message":{"text":message}}
    r=requests.post(web_hook_url, headers=hd, data=json.dumps(msg))
    # send_message_to_dialogflow(msg)

def detect_intent_texts(project_id, session_id, texts, language_code):

    for text in texts:
        
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/opt/app/python_webhook/OFM-CHATBOT-cf91d38e1a05.json"#GOOGLE_API_Dialogflow
        # os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="OFM-CHATBOT-cf91d38e1a05.json"#GOOGLE_API_Dialogflow
        session_client = dialogflow_v2.SessionsClient()
        session = session_client.session_path(project_id, session_id)
        text_input = dialogflow_v2.types.TextInput(text=texts, language_code=language_code)
        query_input = dialogflow_v2.types.QueryInput(text=text_input)
        response = session_client.detect_intent(session=session, query_input=query_input)
        return response.query_result.fulfillment_text
   

def send_message_to_dialogflow(msg):
 
      
        user_id = msg['recipient']['id']
        data_sent = msg['message']['text']
        data_function={ "message": data_sent }
        data_s=json.dumps(data_function)
        

        project_id = "ofm-chatbot"
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/opt/app/python_webhook/OFM-CHATBOT-cf91d38e1a05.json"
        # os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="OFM-CHATBOT-cf91d38e1a05.json"#test local_file
        
        fulfillment_text = detect_intent_texts(project_id, user_id, data_sent, 'en')#call function send message to dialogflow 
        response_text = { "message": fulfillment_text }
        msg={"recipient":{"id":user_id},"message":{"text":response_text}}
        # requests.post(web_hook_url, headers=hd, data=json.dumps(msg)) 
        #point_1_check_message_from dialogflow

        while fulfillment_text == "what is type of report?":
            msg ={"recipient":{
            "id":user_id
            },
            "message":{
            "attachment":{
            "type":"template",
            "payload":{
                "template_type":"button",
                "text": fulfillment_text ,
                "buttons":[
                {
                "type":"postback",
                "title":"Call center",
                "payload":"<DEVELOPER_DEFINED_PAYLOAD>"#menu postback
                },{
                "type":"postback",
                "title":"Store",
                "payload":"<DEVELOPER_DEFINED_PAYLOAD>"#menu postback
                }  
                ]
                }
                }
                }
            }
            
            
        while fulfillment_text == "please select the time period.":
       
            msg ={"recipient":{
            "id":user_id
            },
            "message":{
            "attachment":{
            "type":"template",
            "payload":{
                "template_type":"button",
                "text": fulfillment_text ,
                "buttons":[
                # {
                # "type":"postback",
                # "title":"daily",
                # "payload":"<DEVELOPER_DEFINED_PAYLOAD>"#menu postback
                # },{
                {
                "type":"postback",
                "title":"daily",
                "payload":"<DEVELOPER_DEFINED_PAYLOAD>"
                },{  
                "type":"postback",
                "title":"monthly",
                "payload":"<DEVELOPER_DEFINED_PAYLOAD>"#menu postback
                },{  
                "type":"postback",
                "title":"yearly",
                "payload":"<DEVELOPER_DEFINED_PAYLOAD>"#menu postback
                }  
                ]
                }
                }
                }
            }
        while fulfillment_text =="what date?":
            msg ={"recipient":{
            "id":user_id
            },
            "message":{
            "attachment":{
            "type":"template",
            "payload":{
                "template_type":"button",
                "text": fulfillment_text ,
                "buttons":[
                # {
                # "type":"postback",
                # "title":"daily",
                # "payload":"<DEVELOPER_DEFINED_PAYLOAD>"#menu postback
                # },{
                {
                "type":"postback",
                "title":"Yesterday",
                "payload":"<DEVELOPER_DEFINED_PAYLOAD>"
                },{  
                "type":"postback",
                "title":"select(dd-mm-yyyy)",
                "payload":"<DEVELOPER_DEFINED_PAYLOAD>"#menu postback
                }
                ]
                }
                }
                }
            }
        else:
            response_text = { "message": "error def send_message():" }
            msg={"recipient":{"id":user_id},"message":{"text":response_text}}
            requests.post(web_hook_url, headers=hd, data=json.dumps(msg)) 
            return "200"

        requests.post(web_hook_url, headers=hd, data=json.dumps(msg))   
       

        return "200"
