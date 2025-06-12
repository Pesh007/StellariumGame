from krygche import CircleOverlay #moi file
import sys 
from PyQt5 import QtWidgets
from namirane import centrirane #moi file
from pandas import read_excel
from random import randint
from mainPage import mainPage #moi
from secondPage import secondPage #moi
from thirdPage import thirdPage #moi file

def main():
    mainPage()
    rounds, fov = secondPage()
    
    app = QtWidgets.QApplication(sys.argv)
    overlay = CircleOverlay()

    thirdPage(rounds)


    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

