from wsntk.network import SensorNetwork

def NetSim(*args, **kwargs):
    return iter(SensorNetwork(*args, **kwargs))
