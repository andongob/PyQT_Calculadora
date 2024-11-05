# Form implementation generated from reading ui file 'calculadora.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt6 import QtCore, QtGui, QtWidgets

from lcd import lcd
from boton import crea_boton

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(408, 491)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # Pantalla lcd
        self.lcdNumber = lcd(self.centralwidget)
        
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 90, 361, 351))
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gridLayoutWidget.sizePolicy().hasHeightForWidth())
        self.gridLayoutWidget.setSizePolicy(sizePolicy)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        
        # Números
        self.btn_0 = crea_boton(self.gridLayoutWidget, "btn_0")
        self.gridLayout.addWidget(self.btn_0, 4, 1, 1, 1)
        self.btn_0.clicked.connect(self.numero0)
        
        
        self.btn_1 = crea_boton(self.gridLayoutWidget, "btn_1")
        self.gridLayout.addWidget(self.btn_1, 1, 0, 1, 1)
        self.btn_2 = crea_boton(self.gridLayoutWidget, "btn_2")
        self.gridLayout.addWidget(self.btn_2, 1, 1, 1, 1)
        self.btn_3 = crea_boton(self.gridLayoutWidget, "btn_3")
        self.gridLayout.addWidget(self.btn_3, 1, 2, 1, 1)
        self.btn_4 = crea_boton(self.gridLayoutWidget, "btn_4")
        self.gridLayout.addWidget(self.btn_4, 2, 0, 1, 1)
        self.btn_5 = crea_boton(self.gridLayoutWidget, "btn_5")
        self.gridLayout.addWidget(self.btn_5, 2, 1, 1, 1)
        self.btn_6 = crea_boton(self.gridLayoutWidget, "btn_6")
        self.gridLayout.addWidget(self.btn_6, 2, 2, 1, 1)
        self.btn_7 = crea_boton(self.gridLayoutWidget, "btn_7")
        self.gridLayout.addWidget(self.btn_7, 3, 0, 1, 1)
        self.btn_8 = crea_boton(self.gridLayoutWidget, "btn_8")
        self.gridLayout.addWidget(self.btn_8, 3, 1, 1, 1)
        self.btn_9 = crea_boton(self.gridLayoutWidget, "btn_9")
        self.gridLayout.addWidget(self.btn_9, 3, 2, 1, 1)
        
        self.btn_porcentaje = crea_boton(self.gridLayoutWidget, "btn_porcentaje")
        self.gridLayout.addWidget(self.btn_porcentaje, 0, 2, 1, 1)
        
        self.btn_sumar = crea_boton(self.gridLayoutWidget, "btn_sumar")
        self.gridLayout.addWidget(self.btn_sumar, 3, 3, 1, 1)
        
        self.btn_restar = crea_boton(self.gridLayoutWidget, "btn_restar")
        self.gridLayout.addWidget(self.btn_restar, 2, 3, 1, 1)
        
        self.btn_multiplicar = crea_boton(self.gridLayoutWidget, "btn_multiplicar")
        self.gridLayout.addWidget(self.btn_multiplicar, 1, 3, 1, 1)
        
        self.btn_dividir = crea_boton(self.gridLayoutWidget, "btn_dividir")
        self.gridLayout.addWidget(self.btn_dividir, 0, 3, 1, 1)
        
        self.btn_decimal = crea_boton(self.gridLayoutWidget, "btn_decimal")
        self.gridLayout.addWidget(self.btn_decimal, 4, 0, 1, 1)
        
        self.btn_borrar = crea_boton(self.gridLayoutWidget, "btn_borrar")
        self.gridLayout.addWidget(self.btn_borrar, 0, 0, 1, 1)
         
        self.btn_resultado = crea_boton(self.gridLayoutWidget, "btn_resultado")
        self.gridLayout.addWidget(self.btn_resultado, 4, 2, 1, 1)
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 408, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def numero0(self, value):
        print("Marcado el 0")
        print(value)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_porcentaje.setText(_translate("MainWindow", "%"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_sumar.setText(_translate("MainWindow", "+"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_borrar.setText(_translate("MainWindow", "AC"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_restar.setText(_translate("MainWindow", "-"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_dividir.setText(_translate("MainWindow", "/"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_multiplicar.setText(_translate("MainWindow", "*"))
        self.btn_decimal.setText(_translate("MainWindow", "."))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.btn_resultado.setText(_translate("MainWindow", "="))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())