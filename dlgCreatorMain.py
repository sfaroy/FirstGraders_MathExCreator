# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 19:00:07 2018

dlgCreatorMain.py

@author: Roee
"""

from dlgCreatorMainUi import Ui_MainWindow as uiCreator
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets

class DialogCreatorMain(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui=uiCreator()
        self.ui.setupUi(self)

    def SetExerciseList(self,ex_list):
        

if __name__ == "__main__":
    import sys
    if not QtWidgets.QApplication.instance():
        app = QtWidgets.QApplication(sys.argv)
    else:
        app = QtWidgets.QApplication.instance() 
    MainWindow = DialogCreatorMain()
    ex_list=[{'name':'exercise1'},{'name':'exercise2'}]
    MainWindow.show()
    MainWindow.SetExecriseList(ex_list)
    sys.exit(app.exec_())

