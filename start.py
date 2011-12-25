import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from main_window import Ui_UXO
from preferences import Ui_dialogPreferences
from movable_object import MovableObject

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
        face = MovableObject(50, 50, None)
        s.addItem(face)
        face.grabKeyboard()
        return s
    
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
