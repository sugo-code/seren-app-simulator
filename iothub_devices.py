from azure.iot.hub import IoTHubRegistryManager
from azure.iot.hub.models import QuerySpecification

def getDevices(devices: list(), cs: str):
    rm = IoTHubRegistryManager.from_connection_string(cs)
    query = QuerySpecification(query="SELECT * FROM devices")
    res = rm.query_iot_hub(query)
    for d in res.items:
        devices.append(d.device_id)
    return devices