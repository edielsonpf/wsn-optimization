from wsntk.network import FreeSpaceSensorNetwork

def NetSim(*args, **kwargs):
    return iter(FreeSpaceSensorNetwork(*args, **kwargs))
