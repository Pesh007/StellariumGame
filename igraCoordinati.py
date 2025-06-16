from krygche import CircleOverlay #moi file
import sys 
from PyQt5 import QtWidgets
from mainPage import mainPage #moi
from secondPage import secondPage #moi
from thirdPage import thirdPage #moi file
from requests import post
from useConfig import find_port

def main():
    mainPage()
    rounds, fov = secondPage()
    port = find_port()
    url = f"http://localhost:{port}/api/main/fov"
    params = {"fov": fov}
    post(url, params)
    app = QtWidgets.QApplication(sys.argv)
    overlay = CircleOverlay()

    thirdPage(rounds)


    sys.exit(app.exec_())

if __name__ == "__main__":
    main()


