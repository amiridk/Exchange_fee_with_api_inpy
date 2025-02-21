from kavenegar import *
from conf import KAVEHNEGAR_APIKEY,CONFIG_SETTINGS

def send_sms(text):
    
    try:
        api = KavenegarAPI(f'{KAVEHNEGAR_APIKEY}')
        params = {
            'sender': '',#optional
            'receptor': CONFIG_SETTINGS['notif_sms']['phone_number'],#multiple mobile number, split by comma
            'message': text,
        } 
        response = api.sms_send(params)
        print(str(response))
    except APIException as e: 
        print(str(e))
    except HTTPException as e: 
        print(str(e))