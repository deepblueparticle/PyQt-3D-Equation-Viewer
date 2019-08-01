# -*- coding: utf-8 -*-
"""
@author: AndrewHN
"""

import sys
import numpy as np
from PyQt5 import QtCore, QtWidgets, uic
import matplotlib.pylab as plt
from matplotlib.backends.backend_qt5agg import FigureCanvas 
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox, QLineEdit, QAction
from PyQt5.QtCore import pyqtSlot
from mpl_toolkits import mplot3d

class MyWindow(QtWidgets.QMainWindow):
    
    def __init__(self, **kwargs):
        super(MyWindow, self).__init__()
        uic.loadUi('equation_visualizer_layout.ui', self) 
        def func(x, y):
            return np.cos(np.sqrt(x ** 2 + y ** 2))
        x = np.linspace(-5, 6, 40)
        y = np.linspace(-5, 6, 40)
        # Returns number spaces evenly w.r.t interval. Similar to arange but instead of step it uses sample number.
        X, Y = np.meshgrid(x, y)
        Z = func(X, Y)
        
        self.fig = plt.figure()
        self.ax = plt.axes(projection='3d')
        self.ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='magma', edgecolor='none')
        
        self.ax.set_title('Surface Map Magma');
        self.ax.view_init(50, 35)
        
        self.plotWidget = FigureCanvas(self.fig)
        self.lay = QtWidgets.QVBoxLayout(self.content_plot) 
        print(self.content_plot)
        self.lay.setContentsMargins(0, 0, 0, 0)      
        self.lay.addWidget(self.plotWidget) 
        self.addToolBar(QtCore.Qt.BottomToolBarArea, NavigationToolbar(self.plotWidget, self))
        
        '''
        self.addToolBar(QtCore.Qt.BottomToolBarArea, NavigationToolbar(self.plotWidget, self))
        self.button = QPushButton('pushButtonNEW', self)
        self.button.move(70,540)
        self.button.clicked.connect(self.onClick)
        
        self.button2 = QPushButton('pushButtonNEW2', self)
        self.button2.move(350,540)
        self.button2.clicked.connect(self.onClick)
        
        self.button3 = QPushButton('pushButtonNEW3', self)
        self.button3.move(550,540)
        self.button3.clicked.connect(self.onClick)
        '''

    def create_wire_frame(self):
        def func(x, y):
            return np.cos(np.sqrt(x ** 2 + y ** 2))
        x = np.linspace(-5, 6, 40)
        y = np.linspace(-5, 6, 40)
        # Returns number spaces evenly w.r.t interval. Similar to arange but instead of step it uses sample number.
        X, Y = np.meshgrid(x, y)
        Z = func(X, Y)
        
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        ax.plot_wireframe(X, Y, Z, color='black')
        ax.set_title('wireframe');
        
        return fig
      
    
    @pyqtSlot()
    def onClick(self):
        self.plotWidget.deleteLater()
        self.__init__()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())