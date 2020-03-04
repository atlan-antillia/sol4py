import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QTextEdit,QWidget, QAction, QTabWidget,QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
 
class App(QMainWindow):
 
    def __init__(self, name, x, y, width, height):
        super().__init__()
        self.setWindowTitle(name)
        self.setGeometry(x, y, width, height)
 
        self.table_widget = PanedWindow(self, width-40, height-40)

        self.setCentralWidget(self.table_widget)
 
        self.show()
 
class PanedWindow(QTabWidget):        
 
    def __init__(self, parent, width, height):   
        super(PanedWindow, self).__init__(parent)
        self.layout = QVBoxLayout(self)
 
        # Initialize tab screen

 
        self.tab1 = QWidget()	
        self.tab2 = QWidget()
 
        # Add tabs
        self.addTab(self.tab1, "Tab 1")
        self.addTab(self.tab2, "Tab 2")
 
        # Create first tab
        self.tab1.layout = QVBoxLayout(self.tab1)
        self.text_editor = QTextEdit("Hello \n World\n")
        self.tab1.layout.addWidget(self.text_editor)
 

        self.resize(width, height) 

  #def add(self, child, name):
  #    layout = QVBoxLayout(child)
  #    self.addTab(child, name)
       
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App(sys.argv[0], 10, 20, 600, 400)
    sys.exit(app.exec_())
