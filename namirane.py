import requests
from math import cos, sin, radians


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

    url = "http://localhost:8090/api/main/view"
    response = requests.post(url, params)
