# Seren-Up - Bracelet Data Simulator
## Summary
The script will generate some data in *JSON* format to simulate a bracelet activity
## Functionality
Every 30 seconds the script will generate some random data like in the example below:
```
{
    'deviceId': 'ad8a9e55-ee64-4912-a016-6e62af009a00',
    'timeStamp': '2022-07-13 14:15:34.477860',
    'walkCount': 5,
    'heartFrq': 56,
    'bloodOxg': 98,
    'bodyTemp': 36.5,
    'bloodPrs': 114,
    'serendipityLvl': 99,
    'batteryLvl': 98,
    'isSleeping': False,
    'isFallen': False
    
}
```
After the JSON is generated, the script automatically publish it into a Azure IoT Hub MQTT queue
## Usage
Before executing the script, please run ```py -m pip install -r requirements.txt ``` in order to install all the dependencies
## Environment Variables
There are used two environment variables:
```CONNECTION_STRING``` that is the connection of a single device (You can retreive it from Azure IoT Hub/Devices/{device_id})
```IOT_HUB_CONNECTION_STRING``` that is the connection string of the IoT Hub (You can retreive it from Azure IoT Hub/Shared Access Policies)
## Execution
Run ```simulator.py```
