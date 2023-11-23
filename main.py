import sys
import random
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow

from UI import Ui_MainWindow


def draw(qp):
    for i in range(100):
        qp.setBrush(QColor(random.randint(0, 255), random.randint(0, 255),
                    random.randint(0, 255)))
        x = random.randint(20, 600)
        y = random.randint(20, 600)
        r = random.randint(100, 100)
        qp.drawEllipse(x, y, r, r)


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.do_paint = False

    def initUI(self):
        # uic.loadUi("UI.ui", self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.paint)

    def paint(self):
        self.do_paint = True
        self.update()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            draw(qp)
            qp.end()
        self.do_paint = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
