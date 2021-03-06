from PyQt4.QtGui import *
from PyQt4.QtCore import *
from util.util import load_image
from footsteps import Footsteps

class MovableObject(QGraphicsItem):
    def __init__(self, parent, x, y, image_name):
        QGraphicsItem.__init__(self)
        self.parent = parent
        self.x = x
        self.y = y
        self.setPos(x,y)
        self.direction = None # rotation of footsteps
        self.footstep_direction = 0 # 0 is left foot, 1 is right foot
        self.image_name = image_name
        self.vertorhor = None # moving horizontally or vertically
        self.setZValue(10)
        self.footsteps = 0

    def boundingRect(self):
        return QRectF(0, 0, 84, 84)

    def paint(self, painter, option, widget):
        # draws image with offset for aesthetics
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
            else:
                # user has reached the top of the screen
                msg = QMessageBox()
                msg.setWindowTitle("Congratulations!")
                msg.setText("Mother-voice in local dialect: Mommy very happy that child come home safe")
                msg.exec_()
                self.parent.newGame()
        elif (event.key() == Qt.Key_Down):
            if self.y < self.scene().height()-self.boundingRect().height()-2:
                self.y += 35
                self.setY(self.y)
                self.direction = 180
                self.vertorhor = 1
        else:
            return

        if self.direction != None:
            # put down footsteps behind the player
            f = Footsteps(self.x, self.y, self.direction, self.footstep_direction)
            self.parent.ui.graphicsView.scene().addItem(f)
            # switch feet
            if self.footstep_direction == 0:
                self.footstep_direction = 1
            elif self.footstep_direction == 1:
                self.footstep_direction = 0

            self.footsteps += 1

            # create a dialog every 5 steps
            if self.footsteps == 5:
                self.parent.createUXOPopup()
                self.footsteps = 0 
