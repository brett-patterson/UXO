import sys, random
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from main_window import Ui_UXO
from preferences import Ui_dialogPreferences
from uxo_dialog import Ui_uxo_dialog
from movable_object import MovableObject
from util.uxo_objects import UXO_OBJECTS, USED_OBJECTS
from util import util

class Start(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
 
        self.ui = Ui_UXO()
        self.ui.setupUi(self)

        self.ui.graphicsView.setGeometry(0,0,800,600)
        scene = self.populateScene()
        self.ui.graphicsView.setScene(scene)

        QObject.connect(self.ui.actionNew_Game, SIGNAL("triggered()"), self, SLOT("newGame()"))
        QObject.connect(self.ui.actionPreferences, SIGNAL("triggered()"), self, SLOT("showPreferencesDialog()"))

    def populateScene(self):
        s = QGraphicsScene(QRectF(0,0, self.ui.graphicsView.width(), self.ui.graphicsView.height()))
        self.player = MovableObject(self, 285, 550, None)
        s.addItem(self.player)
        s.addPixmap(QPixmap("res/img/back_1.png"))
        self.player.grabKeyboard()
        return s

    def createUXOPopup(self):
        self.uxo_popup = QDialog()
        u = Ui_uxo_dialog()
        u.setupUi(self.uxo_popup)
        
        i = random.randint(0, len(UXO_OBJECTS)-1)
        while i in USED_OBJECTS:
            i = random.randint(0, len(UXO_OBJECTS)-1)

        USED_OBJECTS.append(i)
        u.imageLabel.setPixmap(util.load_uxo_pixmap(UXO_OBJECTS[i][0]))
        self.uxo_popup.correctAnswer = UXO_OBJECTS[i][1]

        self.uxo_popup.setWindowFlags(Qt.FramelessWindowHint)
        p = self.ui.centralwidget.mapToGlobal(self.uxo_popup.pos())
        self.uxo_popup.setGeometry(p.x()+self.uxo_popup.width()/2,
             p.y()+self.ui.graphicsView.height()/2-self.uxo_popup.height()/2,
             self.uxo_popup.width(), self.uxo_popup.height())

        QObject.connect(u.buttonSafe, SIGNAL("clicked()"), self, SLOT("safeSelected()"))
        QObject.connect(u.buttonNotSafe, SIGNAL("clicked()"), self, SLOT("notSafeSelected()"))
        QObject.connect(u.buttonZoom, SIGNAL("clicked()"), self, SLOT("zoom()"))

        self.uxo_popup.exec_()
    
    @pyqtSlot()
    def safeSelected(self):
        print "safe"
        self.uxo_popup.close()

    @pyqtSlot()
    def notSafeSelected(self):
        print "not safe"
        self.uxo_popup.close()

    @pyqtSlot()
    def zoom(self):
        print "zoom"

    @pyqtSlot()
    def newGame(self):
        self.ui.graphicsView.setScene(self.populateScene())
        
    @pyqtSlot()
    def showPreferencesDialog(self):
        self.preferences = QDialog()
        p = Ui_dialogPreferences()
        p.setupUi(self.preferences)
        self.preferences.setAttribute(Qt.WA_DeleteOnClose)
        self.preferences.exec_()
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myapp = Start()
    myapp.show()
    sys.exit(app.exec_())
