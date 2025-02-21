import requests
from conf import FINAL_URL , CONFIG_SETTINGS
from mailing import send_smtp_email
import json
import os
from sms import send_sms

def get_data_from_api(): 
    res = requests.get(FINAL_URL)
    if res.status_code == 200:
        return json.loads(res.text)
    return None


def final_arch (file_name , data) :
    if not os.path.exists('archive'):
        os.mkdir('archive')
    with open(f'archive/{file_name}.json', 'w') as f:
        json.dump(data, f)

def send_mail(timestamp , data):
    subj = f'{timestamp} rates'
    if CONFIG_SETTINGS['prefs'] is not None:
        tmp = dict()
        for pref in CONFIG_SETTINGS['prefs']:
            tmp[pref] = data[pref]
        data=tmp
    text = json.dumps(data)
    send_smtp_email(subj, text)
    pass



def check_critics(rates):
    msg=''
    prefered = CONFIG_SETTINGS['notif_sms']['prefs']
    for rule in prefered:
        if float(rates[rule]) <= float(prefered[rule]['min']):
            msg += f'{rule} is reached {prefered[rule]["min"]}\n'
        if float(rates[rule]) >= float(prefered[rule]['min']):
            msg += f'{rule} is passed {prefered[rule]["max"]}\n'
    return msg


if __name__ == '__main__':
    print('start')
    res = get_data_from_api()
    if CONFIG_SETTINGS['archive']:
        final_arch(res['timestamp'], res['rates'])
    if CONFIG_SETTINGS['send_mail']:
        send_mail(res['timestamp'], res['rates'])
    if CONFIG_SETTINGS['notif_sms']['is_enable']:
        notif_msg=check_critics(res['rates'])
        if notif_msg is not None:
            send_sms(notif_msg)
    
