import re
import sys
from PyQt4 import QtGui, QtWebKit, QtCore

class Window(QtGui.QWidget):
    
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.initUI()

    def initUI(self):
        
        self.latlabel = QtGui.QLabel("Lat", self)
        self.latlabel.setGeometry(810,10,30,20)
        self.latqle = QtGui.QLineEdit(self)
        self.latqle.setGeometry(840,10,80,20)

        self.lonlabel = QtGui.QLabel("Lon", self)
        self.lonlabel.setGeometry(810,40,30,20)
        self.lonqle = QtGui.QLineEdit(self)
        self.lonqle.setGeometry(840,40,80,20)

        self.addmkrbtn = QtGui.QPushButton("Add Marker", self)
        self.addmkrbtn.setGeometry(825,70,100,30)

        self.setposbtn = QtGui.QPushButton("Set Position", self)
        self.setposbtn.setGeometry(825,100,100,30)

        self.browser = QtWebKit.QWebView(self)
        self.browser.load(QtCore.QUrl("./example.html"))
        self.frame = self.browser.page().currentFrame()
        self.addmkrbtn.clicked.connect(self.addMarker)
        self.setposbtn.clicked.connect(self.setPosition)
        
        self.setGeometry(300,300,950,600)
        self.show()

    def addMarker(self):
        lat = str(self.latqle.text())
        lon = str(self.lonqle.text())

        if isfloat(lat) and isfloat(lon):
            self.frame.evaluateJavaScript(QtCore.QString("addMarker(%f,%f)"%(float(lat), float(lon))))

    def setPosition(self):
        lat = str(self.latqle.text())
        lon = str(self.lonqle.text())
        if isfloat(lat) and isfloat(lon):
            self.frame.evaluateJavaScript(QtCore.QString("setPosition(%f,%f)"%(float(lat), float(lon))))


def isfloat(s):
    p = re.compile("\d+(\.\d+)?")
    return not(p.match(s)==None)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)    
    window = Window()

    sys.exit(app.exec_())
