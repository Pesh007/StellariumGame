from krygche import CircleOverlay #moi file
import sys 
from PyQt5 import QtWidgets
from mainPage import mainPage #moi
from secondPage import secondPage #moi
from thirdPage import thirdPage #moi file
from requests import post

def main():
    mainPage()
    rounds, fov = secondPage()
    url = "http://localhost:8090/api/main/fov"
    params = {"fov": fov}
    post(url, params)
    app = QtWidgets.QApplication(sys.argv)
    overlay = CircleOverlay()

    thirdPage(rounds)


    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

