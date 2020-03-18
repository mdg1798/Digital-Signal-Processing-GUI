
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import matplotlib
import matplotlib.figure
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np
import webbrowser
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar

import sys
class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.setGeometry(50,50,600,200)
        self.center()
        self.setWindowTitle("DSP LEARNING TOOL")
        p = QtGui.QPalette()
        brush = QtGui.QBrush(QtCore.Qt.white,QtGui.QPixmap('bg5.jpg'))
        p.setBrush(QtGui.QPalette.Active,QtGui.QPalette.Window,brush)
        p.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.Window,brush)
        p.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.Window,brush)
        self.setPalette(p)

        QApplication.setStyle(QStyleFactory.create("cleanlooks"))


        self.setWindowIcon(QtGui.QIcon('icon1.png'))
        grid=QtGui.QGridLayout()
        self.setLayout(grid)
        extractAction=QtGui.QAction("&Quit",self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip('Quit The App')
        extractAction.triggered.connect(QtCore.QCoreApplication.instance().quit)

        openHome=QtGui.QAction("&Home",self)
        openHome.setShortcut("Ctrl+W")
        openHome.triggered.connect(self.__init__)
        self.statusBar()

        openEditor=QtGui.QAction("&Editor",self)
        openEditor.setShortcut("Ctrl+R")
        openEditor.triggered.connect(self.editor)
        self.statusBar()

        openFile=QtGui.QAction("&Open",self)
        openFile.setShortcut("Ctrl+O")
        openFile.setStatusTip('Open File')
        openFile.triggered.connect(self.file_open)

        saveFile=QtGui.QAction("&Save File",self)
        saveFile.setShortcut("Ctrl+S")
        saveFile.setStatusTip('Save File')
        saveFile.triggered.connect(self.file_save)

        openHelp=QtGui.QAction("&Help",self)
        openHelp.setShortcut("Ctrl+H")
        openHelp.setStatusTip('Open Help')
        openHelp.triggered.connect(self.open_help)
        
        mainMenu=self.menuBar()
        
        fileMenu=mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)
        fileMenu.addAction(openFile)
        fileMenu.addAction(saveFile)
        fileMenu.addAction(openHome)
        
        editorMenu=mainMenu.addMenu('&Editor')
        editorMenu.addAction(openEditor)
        editorMenu.addAction(openHelp)
        
        #self.toolbar=NavigationToolbar(self.canvas,self)
        #grid.addWidget(self.toolbar, 40,40)
        self.home()

    def home(self):
        self.center()
        grid=QtGui.QGridLayout()
        self.setLayout(grid)

        btn = QtGui.QPushButton("Quit",self)
        btn.setStyleSheet("background-color: red");
        btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        btn.resize(btn.sizeHint())
        btn.move(500,150)
        grid.addWidget(btn, 2,0)

        l1=QLabel(self)
        l1.setText("PLOTS")
        l1.setStyleSheet("color:white");
        l1.setAlignment(Qt.AlignCenter)
        l1.setOpenExternalLinks(True)
        l1.move(50,20)
        grid.addWidget(l1, 2,1)

        l1=QLabel(self)
        l1.setText("FUNCTIONS")
        l1.setStyleSheet("color:yellow");
        l1.setAlignment(Qt.AlignCenter)
        l1.setOpenExternalLinks(True)
        l1.move(150,20)
        grid.addWidget(l1, 2,1)
        
        btn1=QtGui.QPushButton('Plot1',self)
        btn1.setStyleSheet("background-color: green");
        btn1.resize(btn1.sizeHint())
        btn1.move(50,50)
        btn1.clicked.connect(self.plot1)
        grid.addWidget(btn1, 2,1)
        
        btn2=QtGui.QPushButton('Plot2',self)
        btn2.setStyleSheet("background-color: green");
        btn2.resize(btn2.sizeHint())
        btn2.move(50,100)
        btn2.clicked.connect(self.plot2)
        grid.addWidget(btn2, 2,2)

        btn3=QtGui.QPushButton('Convulution',self)
        btn3.setStyleSheet("background-color: blue; color:white");
        btn3.resize(btn3.sizeHint())
        btn3.move(150,50)
        btn3.clicked.connect(self.plot3)
        grid.addWidget(btn3, 2,3)

        btn4=QtGui.QPushButton('FFT',self)
        btn4.setStyleSheet("background-color: blue; color:white");
        btn4.resize(btn4.sizeHint())
        btn4.move(150,100)
        btn4.clicked.connect(self.plot4)
        grid.addWidget(btn4, 2,4)

        btn5=QtGui.QPushButton('Correlation',self)
        btn5.resize(btn4.sizeHint())
        btn5.move(250,50)
        btn5.clicked.connect(self.plot5)
        grid.addWidget(btn5, 2,5)

        btn6=QtGui.QPushButton('Inverse FFT',self)
        btn6.resize(btn4.sizeHint())
        btn6.move(250,100)
        btn6.clicked.connect(self.plot6)
        grid.addWidget(btn6, 2,6)


        self.show()

   # def style_choiceE(self, text):
   #    self.styleChoice.setText(text)
   #    QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(text))
   #    self.styleChoice =QtGui.QLabel("Windows",self)

    def center(self):
        qr=self.frameGeometry()
        cp=QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        
    def file_open(self):
        name=QtGui.QFileDialog.getOpenFileName(self,'Open File')
        file=open(name,'r')
        self.home()

        with file:
           text=file.read()
           self.textEdit.setText(text)
    
    def open_help(self):
        webbrowser.open('file:///C:/Python34/frame.html')

    def file_save(self):
        name=QtGui.QFileDialog.getSaveFileName(self,'Save File')
        file = open(name,'w')
        text = self.textEdit.toPlainText()
        file.write(text)
        file.close()

    def editor(self):
        self.textEdit=QtGui.QTextEdit()
        self.setCentralWidget(self.textEdit)
        btn7 = QtGui.QPushButton("Quit",self)
        btn7.setStyleSheet("background-color: red");
        btn7.clicked.connect(QtCore.QCoreApplication.instance().quit)
        btn7.resize(btn7.sizeHint())
        btn7.move(500,150)

    def getint(self):
        num,ok = QInputDialog.getInt(self,"integer input dialog","enter a number")
        return num
        

    def plot1(self):
    
        style.use('fivethirtyeight')

        fig = plt.figure()
        ax1 = fig.add_subplot(111)
        #ax1=self.figure.add_subplot(111)
        def animate(i):
          graph_data=open('example.txt','r').read()
          lines = graph_data.split('\n')
          xs = []
          ys = []
          for line in lines:
             if len(line) > 1:
                x, y = line.split(',')
                xs.append(x)
                ys.append(y)
                xs = list(map(int, xs))
                ys = list(map(int, ys))
          ax1.clear()
          ax1.stem(xs, ys, linefmt='b-', markerfmt='bo', basefmt='r-')
        ani = animation.FuncAnimation(fig, animate, interval=1000)
        plt.show()
        self.home()


    def plot2(self):
        
        style.use('fivethirtyeight')

        fig = plt.figure()
        ax1 = fig.add_subplot(111)
        #ax1=self.figure.add_subplot(111)
        def animate(i):
          graph_data=open('example.txt','r').read()
          lines = graph_data.split('\n')
          xs = []
          ys = []
          for line in lines:
             if len(line) > 1:
                x, y = line.split(',')
                xs.append(x)
                ys.append(y)
                xs = list(map(int, xs))
                ys = list(map(int, ys))
          ax1.clear()
          ax1.stem(xs, ys)
        ani = animation.FuncAnimation(fig, animate, interval=1000)
        plt.show()

    def plot3(self):
     
        style.use('fivethirtyeight')
        fig = plt.figure()
        ax1 = fig.add_subplot(111)
        def animate(i):
          graph_data=open('example.txt','r').read()
          graph_data1=open('example1.txt','r').read()
          lines=graph_data.split('\n')
          lines1=graph_data1.split('\n')
          xa=[]
          ya=[]
          xb=[]
          yb=[]
          for line in lines:
            if len(line)>1:
              x,y=line.split(',')
              xa.append(x)
              ya.append(y)
            xa = list(map(int, xa))
            ya = list(map(int, ya))
          for line1 in lines1:
            if len(line1)>1:
              x,y=line1.split(',')
              xb.append(x)
              yb.append(y)
            xb = list(map(int, xb))
            yb = list(map(int, yb))    
          ax1.stem(np.convolve(ya,yb))
        ani = animation.FuncAnimation(fig, animate, interval=1000)
        plt.show()


    def plot4(self):
     
        style.use('fivethirtyeight')
        fig = plt.figure()
        ax1 = fig.add_subplot(111)
        def animate(i):
          graph_data=open('example.txt','r').read()
          #graph_data1=open('example1.txt','r').read()
          lines=graph_data.split('\n')
          #lines1=graph_data1.split('\n')
          xa=[]
          ya=[]
          for line in lines:
            if len(line)>1:
              x,y=line.split(',')
              xa.append(x)
              ya.append(y)
            xa = list(map(int, xa))
            ya = list(map(int, ya))
          #for line1 in lines1:
           # if len(line1)>1:
            #  x,y=line1.split(',')
             # xb.append(x)
              #yb.append(y)
            #xb = list(map(int, xb))
            #yb = list(map(int, yb))    
          #ax1.stem(np.convolve(ya,yb))
          ax1.stem(xa,(np.fft.fft(ya))/10)
        ani = animation.FuncAnimation(fig, animate, interval=1000)
        plt.show()

    def plot5(self):
     
        style.use('fivethirtyeight')
        fig = plt.figure()
        ax1 = fig.add_subplot(111)
        def animate(i):
          graph_data=open('example.txt','r').read()
          graph_data1=open('example1.txt','r').read()
          lines=graph_data.split('\n')
          lines1=graph_data1.split('\n')
          xa=[]
          ya=[]
          xb=[]
          yb=[]
          for line in lines:
            if len(line)>1:
              x,y=line.split(',')
              xa.append(x)
              ya.append(y)
            xa = list(map(int, xa))
            ya = list(map(int, ya))
          for line1 in lines1:
            if len(line1)>1:
              x,y=line1.split(',')
              xb.append(x)
              yb.append(y)
            xb = list(map(int, xb))
            yb = list(map(int, yb))    
          ax1.stem(np.correlate(ya,yb, mode='same'))
        ani = animation.FuncAnimation(fig, animate, interval=1000)
        plt.show()

    def plot6(self):
     
        style.use('fivethirtyeight')
        fig = plt.figure()
        ax1 = fig.add_subplot(111)
        def animate(i):
          graph_data=open('example.txt','r').read()
          #graph_data1=open('example1.txt','r').read()
          lines=graph_data.split('\n')
          #lines1=graph_data1.split('\n')
          xa=[]
          ya=[]
          for line in lines:
            if len(line)>1:
              x,y=line.split(',')
              xa.append(x)
              ya.append(y)
            xa = list(map(int, xa))
            ya = list(map(int, ya))
          #for line1 in lines1:
           # if len(line1)>1:
            #  x,y=line1.split(',')
             # xb.append(x)
              #yb.append(y)
            #xb = list(map(int, xb))
            #yb = list(map(int, yb))    
          #ax1.stem(np.convolve(ya,yb))
          ax1.stem(xa,(np.fft.ifft(ya)))
        ani = animation.FuncAnimation(fig, animate, interval=1000)
        plt.show()

    
def run():
 app=QtGui.QApplication(sys.argv)
 GUI=Window()
 sys.exit(app.exec_())

run()