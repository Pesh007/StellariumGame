from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QPushButton
from sys import exit

class CircleOverlay(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Настройки на прозореца
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint |
                            QtCore.Qt.WindowStaysOnTopHint |
                            QtCore.Qt.Tool)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setAttribute(QtCore.Qt.WA_NoSystemBackground, True)

        # Цял екран
        screen = QtWidgets.QApplication.primaryScreen().geometry()
        self.setGeometry(screen)

        # Позиция и радиус на кръга
        self.circle_radius = 30
        self.circle_pos = QtCore.QPoint(screen.width() // 2, screen.height() // 2)

        # Бутон за изход
        self.exit_button = QPushButton("Изход", self)
        self.exit_button.clicked.connect(self.close_app)
        self.exit_button.move(200, 200)
        self.exit_button.setStyleSheet("background-color: red; color: white; font-weight: bold;")

        self.show()

    def close_app(self):
        QtWidgets.QApplication.quit()
        exit()

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)

        pen = QtGui.QPen(QtGui.QColor(0, 255, 0), 4)
        painter.setPen(pen)
        painter.setBrush(QtCore.Qt.NoBrush)

        painter.drawEllipse(self.circle_pos, self.circle_radius, self.circle_radius)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()







