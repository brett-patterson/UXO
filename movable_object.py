from PyQt4.QtGui import *
from PyQt4.QtCore import *
from util.util import load_image
from footsteps import Footsteps

class MovableObject(QGraphicsItem):
    def __init__(self, x, y, image_name):
        QGraphicsItem.__init__(self)
        self.x = x
        self.y = y
        self.setPos(x,y)
        self.direction = None
        self.footstep_direction = 0
        self.image_name = image_name
        self.vertorhor = None
        self.setZValue(10)

    def boundingRect(self):
        return QRectF(0, 0, 84, 84)

    def paint(self, painter, option, widget):
        if self.image_name is not None:
            image = load_image(self.image_name)
            if self.vertorhor == None:
                painter.drawImage(0, 0, image)
            elif self.vertorhor == 0:
                painter.drawImage(20, 0, image)
            elif self.vertorhor == 1:
                painter.drawImage(0, 20, image)

    def keyPressEvent(self, event):
        if (event.key() == Qt.Key_Left):
            if self.x > 0:
                self.x -= 35
                self.setX(self.x)
                self.direction = 270
                self.vertorhor = None
        elif (event.key() == Qt.Key_Right):
            if self.x < self.scene().width()-self.boundingRect().width()-2:
                self.x += 35
                self.setX(self.x)
                self.direction = 90
                self.vertorhor = 0
        elif (event.key() == Qt.Key_Up):
            if self.y > 0:
                self.y -= 35
                self.setY(self.y)
                self.direction = 0
                self.vertorhor = None
        elif (event.key() == Qt.Key_Down):
            if self.y < self.scene().height()-self.boundingRect().height()-2:
                self.y += 35
                self.setY(self.y)
                self.direction = 180
                self.vertorhor = 1

        if self.direction != None:
            if self.direction == 90:
                f_x = self.x-42
                f_y = self.y
            elif self.direction == 180:
                f_x = self.x
                f_y = self.y-42
            elif self.direction == 270:
                f_x = self.x+42
                f_y = self.y
            elif self.direction == 0:
                f_x = self.x
                f_y = self.y+42

            f = Footsteps(self.x, self.y, self.direction, self.footstep_direction)
            self.scene().addItem(f)
            if self.footstep_direction == 0:
                self.footstep_direction = 1
            elif self.footstep_direction == 1:
                self.footstep_direction = 0

    def mousePressEvent(self, event):
        button = event.button()
        if button == Qt.LeftButton and self.boundingRect().contains(event.pos()):
            menu = QMenu()
            menu.addAction("HERRO")
            menu.exec_(event.screenPos())

