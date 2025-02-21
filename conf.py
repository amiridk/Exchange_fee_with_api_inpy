BASE_URL_API='http://data.fixer.io/api/latest?access_key='
API_KEY='***********' 


FINAL_URL=BASE_URL_API+API_KEY

CONFIG_SETTINGS = {
    'archive' : True,
    'send_mail' : False,
    'prefs' : ['BTC' , 'IRR' , 'IQD' , 'USD' , 'CAD' ,'AED'],
    'notif_sms': {
        'is_enable':True ,
        'phone_number':'******',
        'prefs': {
            'BTC':{'min': '1.05', 'max':'1.07'},
            'IRR':{'min': '42000', 'max':'50000'}
        }
    }
    
}
EMAIL_RECEIVER="********************"
EMAIL_ADDRESS = '****************'
MAILGUN_APIKEY="*****************"
KAVEHNEGAR_APIKEY="*********"