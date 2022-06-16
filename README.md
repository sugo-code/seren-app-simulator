# Seren-Up - Bracalet Data Simulator
## Summary
The script will generate some data in *JSON* format to simulate a bracalet activity
## Functionality
Every 30 seconds the script will generate some random data like in the example below:
```
{
    "deviceId": 4,
    "timeStamp": "2022-06-10 20:36:00.707347",
    "walkCount": 7,
    "heartFrq": 50,
    "bloodOxg": 98,
    "isSleeping": false,
    "isFallen": false
}
```
After the JSON is generated, the script automatically publish it into a Azure IoT Hub MQTT queue
## Usage
Before executing the script, please run ```py -m pip install -r requirements.txt ``` in order to install all the dependencies
## Environment Variables
There are used two environment variables:
```CONNECTION_STRING``` that is the connection of a single device (You can retreive it from Azure IoT Hub/Devices/{device_id})
```IOT_HUB_CONNECTION_STRING``` that is the connection string of the IoT Hub (You can retreive it from Azure IoT Hub/Shared Access Policies)
## Connection
In order to connect and add messages you have to create an environment variable with the *device* connection string (you can get it from IoT Hub)

