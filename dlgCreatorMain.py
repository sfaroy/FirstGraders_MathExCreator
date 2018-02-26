# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 19:00:07 2018

dlgCreatorMain.py

@author: Roee
"""

from dlgCreatorMainUi import Ui_MainWindow as uiCreator
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets
from xls_writer import exercise_xls_writer

class DialogCreatorMain(QMainWindow):

    def __init__(self,writer):
        QMainWindow.__init__(self)
        self.ui=uiCreator()
        self.ui.setupUi(self)
        self.ui.cmdAddSheet.clicked.connect(self.AddSheet)
        self.ui.cmdCreate.clicked.connect(self.CreateExcel)
        self.ex_idx=0
        self.writer=writer

    def CreateExcel(self):
        if self.ui.lstExercises.count()>0:
            self.writer.write("exercises.xls")
            from win32com.client import Dispatch

            xl = Dispatch("Excel.Application")
            xl.Visible = True # otherwise excel is hidden

            from os import path as osp

            ex_file=osp.join(osp.abspath("."),'exercises.xls')

            # newest excel does not accept forward slash in path
            wb = xl.Workbooks.Open(ex_file)
            self.close()
        
    def AddSheet(self):
        idx=self.ui.lstTypes.currentRow()
        ex_name="{0}_{1}".format(self.ex_list[idx]['sheet'],self.ex_idx)
        self.ui.lstExercises.addItem(ex_name)
        self.ex_list[idx]['method'](ex_name)
        self.ex_idx=self.ex_idx+1

    def SetExerciseList(self,ex_list):
        self.ex_list=ex_list
        self.ui.lstTypes.clear()
        for item in self.ex_list:
            self.ui.lstTypes.addItem(item['name'])
        

if __name__ == "__main__":
    import sys
    if not QtWidgets.QApplication.instance():
        app = QtWidgets.QApplication(sys.argv)
    else:
        app = QtWidgets.QApplication.instance() 
    writer=exercise_xls_writer()
    MainWindow = DialogCreatorMain(writer)
    ex_list=[{'name':'exercise1'},{'name':'exercise2'}]
    MainWindow.show()
    MainWindow.SetExerciseList(ex_list)
    sys.exit(app.exec_())

