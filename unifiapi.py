from pyunifi.controller import Controller

def userlogin(UnifiEndpoint, mac_address, minutes):

    response = UnifiEndpoint.authorize_guest(mac_address, minutes)
    return response