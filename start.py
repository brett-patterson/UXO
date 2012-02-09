import sys, random
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from main_window import Ui_UXO
from preferences import Ui_dialogPreferences
from uxo_dialog_edited import Ui_uxo_dialog
from movable_object import MovableObject
from util.uxo_objects import UXO_OBJECTS
from util import util

class Start(QMainWindow):
    """
    Main application
    """
    def __init__(self, parent=None):
        """
        Initialize ui from Qt Designer file, and connect file menu items
        """
        QWidget.__init__(self, parent)

        # used_objects keeps track of all uxo objects that have appeared
        # to prevent repeats
        self.used_objects = [] 

        self.ui = Ui_UXO()
        self.ui.setupUi(self)

        self.ui.graphicsView.setGeometry(0,0,self.size().width(),self.size().height())
        scene = self.populateScene()
        self.ui.graphicsView.setScene(scene)

        QObject.connect(self.ui.actionNew_Game, SIGNAL("triggered()"), self, SLOT("newGame()"))
        QObject.connect(self.ui.actionPreferences, SIGNAL("triggered()"), self, SLOT("showPreferencesDialog()"))

        # level of zoom
        self.zoomCounter = 0

    def populateScene(self):
        """
        Generates a new scene with the background and a player object
        """
        s = QGraphicsScene(QRectF(0,0, self.ui.graphicsView.width(), self.ui.graphicsView.height()))
        self.player = MovableObject(self, 270, 750, None)
        s.addItem(self.player)
        s.addPixmap(QPixmap("res/img/bg.png"))
        self.player.grabKeyboard() # set player to receive all keyboard events
        return s

    def createUXOPopup(self):
        """
        Creates a zoomable dialog with buttons for safe and not safe
        """
        self.uxo_popup = QDialog()
        u = Ui_uxo_dialog()
        u.setupUi(self.uxo_popup)
        self.uxo_popup.imageLabel = u.imageLabel
        self.uxo_popup.scrollArea = u.scrollArea
        QObject.connect(u.buttonSafe, SIGNAL("clicked()"), self, SLOT("safeSelected()"))
        QObject.connect(u.buttonNotSafe, SIGNAL("clicked()"), self, SLOT("notSafeSelected()"))
        QObject.connect(u.buttonZoom, SIGNAL("clicked()"), self, SLOT("zoom()"))
        
        # set the object to have no Windows title bar and 
        # delete from memory when closed
        self.uxo_popup.setWindowFlags(Qt.FramelessWindowHint) 
        self.uxo_popup.setAttribute(Qt.WA_DeleteOnClose)

        # convert coordinates of the dialog to be relative to the entire screen,
        # not just the application
        p = self.ui.centralwidget.mapToGlobal(self.uxo_popup.pos())
        self.uxo_popup.setGeometry(p.x()+self.ui.graphicsView.width()/2-self.uxo_popup.width()/2,
             p.y()+self.ui.graphicsView.height()/2-self.uxo_popup.height()/2,
             self.uxo_popup.width(), self.uxo_popup.height())
        
        # pick a random object from the list of objects and ensure that it
        # has not already been displayed
        i = random.randint(0, len(UXO_OBJECTS)-1)
        while i in self.used_objects:
            i = random.randint(0, len(UXO_OBJECTS)-1)

        self.used_objects.append(i)

        # scale the image to a smaller size
        pix = util.load_uxo_pixmap(UXO_OBJECTS[i][0])
        pix = pix.scaled(pix.width()*0.4, pix.height()*0.4)
        self.uxo_popup.imageLabel.setPixmap(pix)
        self.uxo_popup.correctAnswer = UXO_OBJECTS[i][1]

        
        # reset zoom and display
        self.zoomCounter = 0
        self.uxo_popup.exec_()
    
    @pyqtSlot()
    def safeSelected(self):
        """
        Called when the safe button on the dialog popup is selected. If the
        object is safe, congratulate the user. If it is not safe, display no
        message, turn the screen black, and restart the game.
        """
        if self.uxo_popup.correctAnswer == "s":
            msg = QMessageBox()
            msg.setWindowTitle("Correct!")
            msg.setText("Nice job! This object is safe.")
            msg.exec_()
        else:
            self.uxo_popup.close()
            self.startBlackoutTimer()

        self.uxo_popup.close()
        if hasattr(self, 'timer'):
            self.timer.stop()

    @pyqtSlot()
    def notSafeSelected(self):
        """
        Called when the not safe button on the dialog popup is selected. If the
        object isn't safe, congratulate the user. If it is safe, alert them that
        it is a safe object, but allow them to keep playing.
        """
        if self.uxo_popup.correctAnswer == "ns":
            msg = QMessageBox()
            msg.setWindowTitle("Correct!")
            msg.setText("Good work! This object is VERY dangerous. Be sure to report it to your local authorities.")
            msg.exec_()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Sorry!")
            msg.setText("Actually, this object is not dangerous. Better safe than sorry, though!")
            msg.exec_()

        self.uxo_popup.close()
        if hasattr(self, 'timer'):
            self.timer.stop()

    @pyqtSlot()
    def zoom(self):
        """
        Zoom in on the image of the uxo. After 3 zooms, the zoom resets to
        the original scale factor.
        """
        if self.zoomCounter < 2:
            pixmap = self.uxo_popup.imageLabel.pixmap()
            scaled_pixmap = pixmap.scaled(pixmap.width()*1.45, pixmap.height()*1.45)
            self.uxo_popup.imageLabel.setPixmap(scaled_pixmap)
            self.uxo_popup.imageLabel.resize(scaled_pixmap.size())
            
            self.zoomCounter += 1
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Danger!")
            msg.setText("Careful! Do not go any closer! Please make your decision within 10 seconds.")
            msg.exec_()
            self.startTimer()

    def startTimer(self):
        """
        Called when the user zooms 3 times on the uxo dialog.
        """
        self.timerCount = 9
        self.timer = QTimer(self)
        QObject.connect(self.timer, SIGNAL("timeout()"), self, SLOT("updateTimer()"))
        self.timer.start(1000)

    def startBlackoutTimer(self):
        """
        Called when the user selects safe on a not safe uxo.
        """
        s = QGraphicsScene(QRectF(0,0, self.ui.graphicsView.width(), self.ui.graphicsView.height()))
        brush = QBrush(QColor("grey"))
        s.setBackgroundBrush(brush)
        self.ui.graphicsView.setScene(s)
        self.blackout_timer = QTimer(self)
        QObject.connect(self.blackout_timer, SIGNAL("timeout()"), self, SLOT("updateBlackoutTimer()"))
        self.blackout_timer.setSingleShot(True)
        self.blackout_timer.start(2000)

    @pyqtSlot()
    def updateTimer(self):
        if self.timerCount > 0:
            self.timerCount -= 1
        else:
            self.uxo_popup.close()
            self.startBlackoutTimer()
            self.timer.stop()

    @pyqtSlot()
    def updateBlackoutTimer(self):
        self.newGame()

    @pyqtSlot()
    def newGame(self):
        self.player = None
        del self.used_objects[ 0:len(self.used_objects) ]
        self.ui.graphicsView.setGeometry(0,0,self.size().width(),self.size().height())
        self.ui.graphicsView.setScene(self.populateScene())
        
        
    @pyqtSlot()
    def showPreferencesDialog(self):
        """
        Preferences dialog not implemented (blank).
        """
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
