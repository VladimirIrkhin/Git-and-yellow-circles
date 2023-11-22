import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor
from random import randrange
from interface import Ui_MainWindow


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setFixedSize(400, 400)
        self.coolButton.clicked.connect(self.paint)
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.repaint()
    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()
            self.do_paint = False
    def draw_circle(self, qp):
        qp.setBrush(QColor(randrange(1, 255), randrange(1, 255), randrange(1, 255)))
        r = randrange(1, 200)
        qp.drawEllipse(200 - r // 2, 250 - r // 2, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())
