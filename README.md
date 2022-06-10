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
After the JSON is generated, the script automatically publish it into a Azure ioT Hub MQTT queue
## Certificates
The script uses the *paho mqtt* library to push the data into the queue. To do so, we have generated some CA Certificates. 
In order to generate the certificates we used a bash script provided by Microsoft.
These certificates needs to be re-generated every 30 days and need to be changed into the script
