import os
import sys
from PyQt5 import QtCore, QtMultimedia
from PyQt5.QtWidgets import QApplication, QStyleFactory, QPushButton, QWidget, QGridLayout


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.layout = QGridLayout(self)
        self.player = []
        self.setWindowTitle('Фортепиано')
        i = j = 0
        for k, el in enumerate(os.listdir('guitar')):
            self.load_mp3(f'guitar/{el}')
            self.btn = QPushButton(self)
            self.btn.clicked.connect(self.player[k].play)
            self.layout.addWidget(self.btn, i, j)
            j += 1
            if j > 7:
                i += 1
                j = 0

    def load_mp3(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player.append(QtMultimedia.QMediaPlayer())
        self.player[-1].setMedia(content)

    def keyPressEvent(self, event):
        self.player[event.key()].play()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('Fusion'))
    win = Window()
    win.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
