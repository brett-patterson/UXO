from PyQt4.QtGui import *
from PyQt4.QtCore import *
from util.util import load_image

class Footsteps(QGraphicsItem):
    """
    Footsteps: 0 is left, 1 is right
    """
    def __init__(self, x, y, direction, fd):
        QGraphicsItem.__init__(self)
        self.x = x
        self.y = y
        self.direction = direction
        self.footstep_direction = fd
        self.setPos(x,y)

    def boundingRect(self):
        return QRectF(0, 0, 72, 92)

    def paint(self, painter, option, widget):
        if self.footstep_direction == 0:
            image = load_image("footsteps_left.png")
        elif self.footstep_direction == 1:
            image = load_image("footsteps_right.png")

        transform = QTransform().rotate(self.direction)
        image = image.transformed(transform)
        
        # rotates images relative to the player's turns
        if self.footstep_direction == 1 and self.direction == 90:
            draw_x = 0
            draw_y = 25
        elif self.footstep_direction == 0 and self.direction == 180:
            draw_x = 25
            draw_y = 0
        elif self.footstep_direction == 1 and self.direction == 0:
            draw_x = 25
            draw_y = 25
        elif self.direction == 270:
            draw_x = 25
            if self.footstep_direction == 0:
                draw_y = 25
            else:
                draw_y = 0
        else:
            draw_x = 0
            draw_y = 0

        painter.drawImage(draw_x,draw_y,image)
