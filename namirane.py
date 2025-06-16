import requests
from math import cos, sin, radians
from useConfig import find_port

def centrirane(ra: float, dec: float) -> None:

    ra = ra * 15
    ra = radians(ra)
    dec = radians(dec)
    cosDec = cos(dec)
    x=cos(ra)*cosDec
    y=cosDec*sin(ra)
    z=sin(dec)
    pos = [x,y,z]

    params = {
        "j2000" : str(pos)
    }
    port = find_port()
    url = f"http://localhost:{port}/api/main/view"
    response = requests.post(url, params)
