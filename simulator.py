# Composizione del JSON: deviceId, timeStamp,  walkCount, heartFrq, bloodOxigen, isSleeping
from azure.iot.device.aio import IoTHubDeviceClient
from azure.iot.device import Message
from dotenv import load_dotenv
from datetime import datetime
import asyncio
import os
import random
import time
import json
import warnings
warnings.filterwarnings('ignore')
load_dotenv(dotenv_path=os.path.join(os.getcwd(), '.env'))


idList = ['1', '2']
d = random.choice(idList)

try:
    client = IoTHubDeviceClient.create_from_connection_string(os.getenv("CONNECTION_STRING"))
    client.connect()
except:
    raise ConnectionError("Cannot connect to Azure IoT Hub, please check the Connection String")

async def sendMessage(jsonData: str):
    print('Sending message...')
    try:
        await client.send_message(Message(str(jsonData), content_encoding="UTF-8", content_type="application/json"))
        print(f'Sent\n{jsonData}')
    except:
        print('Your message could not be sent')

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

while True:
    asyncio.run(sendMessage(generateData(d)))
    time.sleep(10)