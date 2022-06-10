# Composizione del JSON: deviceId, timeStamp,  walkCount, heartFrq, bloodOxigen, isSleeping
import paho.mqtt.client as mqtt
from dotenv import load_dotenv
from datetime import datetime
import os
import ssl
import random
import time
import json

env_path = os.path.join(os.getcwd(), '.env')
load_dotenv(dotenv_path=env_path)

idList = ['1', '2']
d = random.choice(idList)

path_to_root_cert = os.getenv("PATH_TO_ROOT_CERT")
cert_file = os.getenv("CERT_FILE")
key_file = os.getenv("KEY_FILE")
device_id = os.getenv("DEVICE_ID")
iot_hub_name = os.getenv("IOT_HUB_NAME")

def on_connect(client, userdata, flags, rc):
    print("Device connected with result code: " + str(rc))


def on_disconnect(client, userdata, rc):
    print("Device disconnected with result code: " + str(rc))


def on_publish(client, userdata, mid):
    print("Device sent message")

def generateData(devId: int):
    isSleeping = False
    isFallen = False
    if  datetime.now().hour >= 22:
        isSleeping = True
    if random.randrange(0,200) == 150:
        isFallen = True
    jsonData = {
        'deviceId': d,
        'timeStamp': str(datetime.now()),
        'walkCount': random.randrange(0, 10),
        'heartFrq': random.randrange(50, 60),
        'bloodOxg': random.randrange(98, 100),
        'isSleeping': isSleeping,
        'isFallen': isFallen
    }
    return json.dumps(jsonData)

client = mqtt.Client(client_id=device_id, protocol=mqtt.MQTTv311)

client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_publish = on_publish

client.username_pw_set(username=iot_hub_name+".azure-devices.net/" + device_id + "/?api-version=2021-04-12", password=None)

client.tls_set(ca_certs=path_to_root_cert, certfile=cert_file, keyfile=key_file, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)
client.tls_insecure_set(False)

client.connect(iot_hub_name+".azure-devices.net", port=8883)
client.publish("devices/" + device_id + "/messages/events/", generateData(d), qos=1)
client.loop_forever()