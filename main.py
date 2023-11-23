import sys
import random
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.do_paint = None
        self.initUI()

    def initUI(self):
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.paint)

    def paint(self):
        self.do_paint = True
        self.update()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
        self.do_paint = False

    def draw_flag(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        for i in range(100):
            x = random.randint(20, 600)
            y = random.randint(20, 600)
            r = random.randint(10, 100)
            qp.drawEllipse(x, y, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())