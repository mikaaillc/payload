
import csv
import os
import sys  # we'll need this later to run our Qt application
import OpenGL.GL as gl  # python wrapping of OpenGL
import cv2
import numpy as np
import pyqtgraph as pg
import datetime
from OpenGL import GLU
from OpenGL.arrays import vbo
from PyQt5 import QtCore
from PyQt5 import QtOpenGL
from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMessageBox, QLabel, QFileDialog, QWidget
from PyQt5.uic import loadUi
import random
from PyQt5 import QtGui
import pyqtgraph
import pyqtgraph.exporters
import numpy
import socket
import serial


pg.setConfigOption('background', QColor(240, 240, 240))
pg.setConfigOption('foreground', 'k')

basincmat=[]
yukseklikmat=[]
hizmat=[]
sicaklikmat=[]
pilgermat=[]
basincmat1=[]
yukseklikmat1=[]
hizmat1=[]
sicaklikmat1=[]
pilgermat1=[]
havamat1=[]
ax2=0
ay2=0
az2=0

class ana1(QMainWindow):

    def __init__(self):
        super(ana1, self).__init__()
        uic.loadUi("faydaliyük.ui", self)
        self.counter= 0
        self.counter1 = 0
        self.counter2 = 0
        self.counter3 = 0
        self.counter4 = 0
        self.counter5 = 0
        self.paketnum1=0
        label = QLabel(self)
        label.setFixedSize(80, 80)
        pixmap = QPixmap(r'gorseller\\bayrak.png')
        pixmap = pixmap.scaledToWidth(80)
        pixmap = pixmap.scaledToHeight(80)
        label.setPixmap(pixmap)
        label.move(0, -13)

        label2 = QLabel(self)
        label2.setFixedSize(180, 60)
        pixmap2 = QPixmap('gorseller\simge.png')
        pixmap2 = pixmap2.scaledToWidth(180)
        pixmap2 = pixmap2.scaledToHeight(60)
        label2.setPixmap(pixmap2)
        label2.move(475, 650)

        label3 = QLabel(self)
        label3.setFixedSize(230, 80)
        pixmap3 = QPixmap(r'gorseller\teknokent.png')
        pixmap3 = pixmap3.scaledToWidth(230)
        pixmap3 = pixmap3.scaledToHeight(80)
        label3.setPixmap(pixmap3)
        label3.move(590, 620)

        self.glWidget = GLWidget
        self.glWidget = GLWidget(self)
        self.setWindowIcon(QtGui.QIcon("logo"))
        self.dataplot = self.graphicsView.addPlot()
        #self.dataplot.setLabel('left', text='hiz', unitPrefix='m/s')
        self.dataplot.showGrid(x=True, y=True, alpha=1)

        self.dataplot1 = self.graphicsView_2.addPlot()
        self.dataplot1.showGrid(x=True, y=True, alpha=1)

        self.dataplot2 = self.graphicsView_3.addPlot()
        self.dataplot2.showGrid(x=True, y=True, alpha=1)

        self.dataplot3 = self.graphicsView_4.addPlot()
        self.dataplot3.showGrid(x=True, y=True, alpha=1)

        self.dataplot4 = self.graphicsView_5.addPlot()
        self.dataplot4.showGrid(x=True, y=True, alpha=1)

        self.dataplot5 = self.graphicsView_6.addPlot()
        self.dataplot5.showGrid(x=True, y=True, alpha=1)

        self.grafikgr.clicked.connect(self.grafikg)
        self.veribaslat.clicked.connect(self.dongu)  # bu döngü fonksiyonuna gidecek
        self.verigor.clicked.connect(self.veri)
        self.timer5 = QTimer()
        self.timer5.setInterval(1000)
        self.timer5.timeout.connect(self.time)
        self.timer5.start()
        self.lineEdit_29.setText('PORT SEÇİNİZ:')
        self.gonder.clicked.connect(self.gonder1)
    def gonder1(self):
        yazilan=self.lineEdit_29.text().upper()
        com1 = yazilan.split(":")
        self.com_1=str(com1[1])
        self.lineEdit_29.setText('PORT SEÇİLDİ')
    def time(self):
        self.tarih.setText(str(datetime.datetime.strftime(datetime.datetime.now(), '%d %B %Y')))
        self.saat.setText(str(datetime.datetime.strftime(datetime.datetime.now(), '%X')))

    def veri(self):
       os.startfile(r'faydaliyükveri\faydalıveri.csv')
    def grafikg(self):
        os.startfile(r'faydalıyükgrafik')
    def dongu(self):
        global xbee
        try:
            xbee = serial.Serial('{}'.format(self.com_1), 9600)
            self.lineEdit_29.setText('XBEE BAĞLI')
            self.timer = QTimer()
            self.timer.setInterval(1000)
            self.timer.timeout.connect(self.btn_clk)
            self.timer.start()
        except:
            self.lineEdit_29.setText('XBEE BEKLENİYOR')




    def btn_clk(self):
        global datetime, basincmat1,yukseklikmat1,hizmat1,sicaklikmat1,pilgermat1,havamat1,ax2,ay2,az2
        global takimno ,yukseklik, basinc,hiz,sicaklik,pilger, paketno, paketnum, saat, saniye, dakika,lat,long,alt, pitch, roll, yaw, donus,pitc,rol,ya
        try:
            if xbee.inWaiting() > 0:

                an1 = datetime.datetime.now()
                paket = xbee.readline().decode().strip()
                f = paket.split(",")
                basinc1 = str(f[0])
                yukseklik1 = str(f[1])
                hiz1 =str(f[2])
                sicaklik1 = str(f[3])
                pilger1 = str(f[4])
                la1 = str(f[5])
                lo1 = str(f[6])
                al1 = str(f[7])
                ax_1 = str(f[8])
                ay_1 =str(f[9])
                az_1 = str(f[10])
                hava=str(f[11])

                saat1 = an1.hour
                dakika1 = an1.minute
                saniye1 = an1.second


                basincmat1.append(float(basinc1))
                yukseklikmat1.append(float(yukseklik1))
                hizmat1.append(float(hiz1))
                sicaklikmat1.append(float(sicaklik1))
                pilgermat1.append(float(pilger1))
                havamat1.append(float(hava))
                self.dataplot.plot(basincmat1, pen=pg.mkPen('r', width=2), clear=True)
                self.lineEdit_2.setText(str(basinc1) + ' ' + 'Pa')  # Son değer bastırma

                self.dataplot1.plot(yukseklikmat1, pen=pg.mkPen('b', width=2), clear=True)
                self.lineEdit_8.setText(str(yukseklik1) + ' ' + 'm')

                self.dataplot2.plot(hizmat1, pen=pg.mkPen('k', width=2), clear=True)
                self.lineEdit_4.setText(str(hiz1) + ' ' + 'm/s')

                self.dataplot3.plot(sicaklikmat1, pen=pg.mkPen('b', width=2), clear=True)
                self.lineEdit_5.setText(str(sicaklik1) + ' ' + '°c')

                self.dataplot4.plot(pilgermat1, pen=pg.mkPen('r', width=2), clear=True)
                self.lineEdit_6.setText(str(pilger1) + ' ' + 'V')

                self.dataplot5.plot(havamat1, pen=pg.mkPen('r', width=3))
                hava1=int(hava)
                if hava1 < 150:
                    self.lineEdit_12.setText(str(hava) + ' ' + '(ÇOK KALİTELİ)')
                elif hava1 > 150 and hava1<250:
                    self.lineEdit_12.setText(str(hava) + ' ' + '(KALİTELİ)')
                elif hava1 > 250 and hava1<350:
                    self.lineEdit_12.setText(str(hava) + ' ' + '(KALİTESİZ)')
                elif hava1 > 350:
                    self.lineEdit_12.setText(str(hava) + ' ' + '(ÇOK KALİTESİZ)')

                lat1 = float(la1)
                long1 = float(lo1)
                alt1 = float(al1)
                ax2 = float(ax_1)
                ay2 = float(ay_1)
                az2 = float(az_1)
                self.lineEdit_10.setText(str(lat1))
                self.lineEdit_11.setText(str(long1))
                self.lineEdit_9.setText(str(alt1) + ' m')

                self.lineEdit_16.setText(str(ax2) + ' ' + '°')
                self.lineEdit_7.setText(str(ay2) + ' ' + '°')
                self.lineEdit_17.setText(str(az2) + ' ' + '°')

                self.timer_1 = QTimer()
                self.timer_1.setInterval(10)
                self.timer_1.timeout.connect(self.glWidget.updateGL)  # 3d simülasyon timer
                self.timer_1.start()
                self.glWidget.setRotX(ax2)
                self.glWidget.setRotY(ay2)
                self.glWidget.setRotZ(az2)

                if len(basincmat1) > 60:  # GRafik kayıt için
                    self.counter += 1
                    exporter = pg.exporters.ImageExporter(self.dataplot)
                    exporter.params.param('width').setValue(965, blockSignal=exporter.widthChanged)
                    exporter.params.param('height').setValue(608, blockSignal=exporter.heightChanged)
                    exporter.export('faydalıyükgrafik\g_basinc\g_basinc' + str(self.counter) + '.png')
                    basincmat1 = [float(basinc1)]
                if len(yukseklikmat1) > 60:  # GRafik kayıt için
                    self.counter1 += 1
                    exporter = pg.exporters.ImageExporter(self.dataplot1)
                    exporter.params.param('width').setValue(965, blockSignal=exporter.widthChanged)
                    exporter.params.param('height').setValue(608, blockSignal=exporter.heightChanged)
                    exporter.export('faydalıyükgrafik\g_yukseklik\g_yukseklik' + str(self.counter1) + '.png')
                    yukseklikmat1 = [float(yukseklik1)]
                if len(hizmat1) > 60:  # GRafik kayıt için
                    self.counter2 += 1
                    exporter = pg.exporters.ImageExporter(self.dataplot3)
                    exporter.params.param('width').setValue(965, blockSignal=exporter.widthChanged)
                    exporter.params.param('height').setValue(608, blockSignal=exporter.heightChanged)
                    exporter.export('faydalıyükgrafik\g_hiz\g_hiz' + str(self.counter2) + '.png')
                    hizmat1 = [float(hiz1)]
                if len(sicaklikmat1) > 60:  # GRafik kayıt için
                    self.counter3 += 1
                    exporter = pg.exporters.ImageExporter(self.dataplot4)
                    exporter.params.param('width').setValue(965, blockSignal=exporter.widthChanged)
                    exporter.params.param('height').setValue(608, blockSignal=exporter.heightChanged)
                    exporter.export('faydalıyükgrafik\g_sicaklik\g_sicaklik' + str(self.counter3) + '.png')
                    sicaklikmat1 = [float(sicaklik1)]
                if len(pilgermat1) > 60:  # GRafik kayıt için
                    self.counter4 += 1
                    exporter = pg.exporters.ImageExporter(self.dataplot5)
                    exporter.params.param('width').setValue(965, blockSignal=exporter.widthChanged)
                    exporter.params.param('height').setValue(608, blockSignal=exporter.heightChanged)
                    exporter.export('faydalıyükgrafik\g_pilger\g_pilger' + str(self.counter4) + '.png')
                    pilgermat1 = [float(pilger1)]
                if len(havamat1) > 60:  # GRafik kayıt için
                    self.counter5 += 1
                    exporter = pg.exporters.ImageExporter(self.dataplot5)
                    exporter.params.param('width').setValue(965, blockSignal=exporter.widthChanged)
                    exporter.params.param('height').setValue(608, blockSignal=exporter.heightChanged)
                    exporter.export('faydalıyükgrafik\g_hava\g_havakalite' + str(self.counter5) + '.png')
                    havamat1 = [float(hava1)]
                self.paketnum1 += 1

                with open(r'faydaliyükveri\faydalıveri.csv', 'a') as outfile:
                    writer1 = csv.writer(outfile, delimiter='|')
                    writer1.writerow(
                        ['paketnumarası={pak:5}'.format(pak=self.paketnum1),
                         'saat={:3}'.format(saat1), 'dakika={:3}'.format(dakika1),
                         'saniye={:3}'.format(saniye1), 'basinc={bas:6}'.format(bas=basinc1),
                         'yukseklik={yuk:6}'.format(yuk=yukseklik1), 'hiz={hi:8}'.format(hi=hiz1),
                         'sicaklik={sic:8}'.format(sic=sicaklik1),
                         'pilgerilimi={pil:8}'.format(pil=pilger1), 'lat={l1:8}'.format(l1=lat1),
                         'long={l2:8}'.format(l2=long1),
                         'alt={l3:8}'.format(l3=alt1), 'statü={st:8}'.format(st=statu1), 'roll={xx:6}'.format(xx=ax_1),
                         'yaw={yy:6}'.format(yy=ay_1), 'z={zz:6}'.format(zz=az_1),'havakalitesi={hav:6}'.format(hav=hava)
                         ])

        except:
            self.lineEdit_29.setText('XBEE BEKLENİYOR')

class GLWidget(QtOpenGL.QGLWidget):
    def __init__(self, parent=None):
        self.rotX = 0
        self.rotY = 0
        self.rotZ = 0
        self.parent = parent
        QtOpenGL.QGLWidget.__init__(self, parent)
        self.setMinimumSize(391,221)
        self.setGeometry(800, 630, 150, 150)

    def setRotX(self, ax2):
        self.rotX = ax2

    def setRotY(self, ay2):
        self.rotY = ay2

    def setRotZ(self, az2):
        self.rotZ = az2

    def initializeGL(self):
        self.qglClearColor(QtGui.QColor(0, 0, 0))
        gl.glEnable(gl.GL_DEPTH_TEST)
        self.initGeometry()

    def resizeGL(self, width, height):
        gl.glViewport(0, 0, width, height)
        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glLoadIdentity()
        aspect = width / float(height)
        GLU.gluPerspective(70, aspect, 2, 100.0)
        gl.glMatrixMode(gl.GL_MODELVIEW)

    def paintGL(self):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

        gl.glPushMatrix()

        gl.glTranslate(0.0, 0.0, -50.0)
        gl.glScale(30.0, 20.0, 30.0)
        #gl.glRotated(30, 0.5, 0.0, 0.0)
        gl.glRotated(self.rotX, 1.0, 0.0, 0.0)
        gl.glRotated(self.rotY, 0.0, 1.0, 0.0)
        gl.glRotated(self.rotZ, 0.0, 0.0, 1.0)
        gl.glTranslate(-0.5, -0.5, -0.5)  # first, translate cube center to origin


        gl.glEnableClientState(gl.GL_VERTEX_ARRAY)
        gl.glEnableClientState(gl.GL_COLOR_ARRAY)

        gl.glVertexPointer(3, gl.GL_FLOAT, 0, self.vertVBO)
        gl.glColorPointer(3, gl.GL_FLOAT, 0, self.colorVBO)

        gl.glDrawElements(gl.GL_QUADS, len(self.cubeIdxArray), gl.GL_UNSIGNED_INT, self.cubeIdxArray)

        gl.glDisableClientState(gl.GL_VERTEX_ARRAY)
        gl.glDisableClientState(gl.GL_COLOR_ARRAY)

        gl.glPopMatrix()  # restore the previous modelview matrix

    def initGeometry(self):
        self.cubeVtxArray = np.array(
            [[0.0, 0.0, 0.0],
             [0.5, 0.0, 0.0],
             [0.5, 1.5, 0.0],
             [0.0, 1.5, 0.0],
             [0.0, 0.0, 0.5],
             [0.5, 0.0, 0.5],
             [0.5, 1.5, 0.5],
             [0.0, 1.5, 0.5]])
        self.vertVBO = vbo.VBO(np.reshape(self.cubeVtxArray,
                                          (1, -1)).astype(np.float32))
        self.vertVBO.bind()

        self.cubeClrArray = np.array(
            [[0.0, 0.0, 0.0],
             [0.5, 0.0, 0.0],
             [0.5, 1.5, 0.0],
             [0.0, 1.5, 0.0],
             [0.0, 0.0, 0.5],
             [0.5, 0.0, 0.5],
             [0.5, 1.5, 0.5],
             [0.0, 1.5, 0.5]])
        self.colorVBO = vbo.VBO(np.reshape(self.cubeClrArray,
                                           (1, -1)).astype(np.float32))
        self.colorVBO.bind()

        self.cubeIdxArray = np.array(
            [0, 1, 2, 3,
             3, 2, 6, 7,
             1, 0, 4, 5,
             2, 1, 5, 6,
             0, 3, 7, 4,
            7, 6, 5, 4])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ana1()
    window.show()
    sys.exit(app.exec_())

