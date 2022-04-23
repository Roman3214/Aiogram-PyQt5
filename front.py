from msilib.schema import CheckBox
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        button_style = ("QPushButton:hover { background-color: #17212B; border-style: outset;  border-radius: 7px; border-color: beige;  min-width: 7em; padding: 3px;}"
        "QPushButton:!hover { background-color: #25303E; border-style: outset;  border-radius: 7px; border-color: beige;  min-width: 7em; padding: 3px; }"
        
        "QPushButton:pressed { background-color: #2B5278; border-style: outset;  border-radius: 7px; border-color: beige;  min-width: 7em; padding: 3px; }")
        
        checkBox_style = (
        "QCheckBox"
        "{background-color: #25303E;}"
        #"QCheckBox:hover"
        #"{ background-color: #17212B; }"
        #"QCheckBox:!hover"
        #"{background-color: #25303E; }"
        )
        checkBox_style_clicked = ("QCheckBox:hover"
        "{"
        "background-color: #2B5278;"
        "}")
       
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 500)
        MainWindow.setMinimumSize(QtCore.QSize(800, 500))
        MainWindow.setMaximumSize(QtCore.QSize(800, 500))
        MainWindow.setStyleSheet("background-color: #0E1621;")
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: #0E1621;")#263748
        
    

        self.btnstartTG = QtWidgets.QPushButton(self.centralwidget)
        self.btnstartTG.setGeometry(QtCore.QRect(20, 20, 170, 23))
        self.btnstartTG.setObjectName("btnstartTG")
        self.btnstartTG.setStyleSheet(button_style)

        self.btnstartClose = QtWidgets.QPushButton(self.centralwidget)
        self.btnstartClose.setGeometry(QtCore.QRect(200, 20, 170, 23))
        self.btnstartClose.setObjectName("btnstartlose")
        self.btnstartClose.setStyleSheet(button_style)
        
            
        #self.lable = QtWidgets.QLabel('<h1>Введите текст оправительного сообщения!</h1>', self.centralwidget)
        #          Координаты как ориентир  x , y, XO , YO
        #self.lable.setGeometry(QtCore.QRect(20, 1, 500, 30))
        #self.lable.setObjectName("lable")
        # --------------------------Отправка 
        self.TextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.TextEdit.setGeometry(QtCore.QRect(20, 60, 500, 150))
        self.TextEdit.setObjectName("TextEdit")
        self.TextEdit.setPlaceholderText("Введите текст сообщения...")
        self.TextEdit.setStyleSheet("background-color: #253950;")

        self.btnsend = QtWidgets.QPushButton(self.centralwidget)
        self.btnsend.setGeometry(QtCore.QRect(420, 230, 81, 23))
        self.btnsend.setObjectName("btnsend")
        self.btnsend.setStyleSheet(button_style)

        self.btnckear = QtWidgets.QPushButton(self.centralwidget)
        self.btnckear.setGeometry(QtCore.QRect(191, 230, 150, 23))
        self.btnckear.setObjectName("btnclear")
        self.btnckear.setStyleSheet(button_style)
        # --------------------------Отправка 

        # ----------------------------чекбокесы
        self.CheckBoxP = QtWidgets.QCheckBox(self.centralwidget)
        self.CheckBoxP.setGeometry(QtCore.QRect(550, 60, 170, 15))
        self.CheckBoxP.setObjectName("Пограничных состояний")
        self.CheckBoxP.setStyleSheet(checkBox_style)
        

        self.CheckBoxD = QtWidgets.QCheckBox(self.centralwidget)
        self.CheckBoxD.setGeometry(QtCore.QRect(550, 95, 170, 15))
        self.CheckBoxD.setObjectName("Детское отделение")
        self.CheckBoxD.setStyleSheet(checkBox_style)

        self.CheckBoxN = QtWidgets.QCheckBox(self.centralwidget)
        self.CheckBoxN.setGeometry(QtCore.QRect(550, 130, 170, 15))
        self.CheckBoxN.setObjectName("Наркология")
        self.CheckBoxN.setStyleSheet(checkBox_style)

        self.CheckBoxALL = QtWidgets.QCheckBox(self.centralwidget)
        self.CheckBoxALL.setGeometry(QtCore.QRect(550, 165, 170, 15))
        self.CheckBoxALL.setObjectName("Выбрать все")
        self.CheckBoxALL.setStyleSheet(
                                        "QCheckBox"
                                        "{background-color: #2B5278;}"
                                        )
        self.CheckBoxALL.setChecked(True)
        # ----------------------------чекбокесы

        
        # --------------------------файлы 
        self.extractButton = QtWidgets.QPushButton(self.centralwidget)
        self.extractButton.setGeometry(QtCore.QRect( 20, 230, 81, 23))
        self.extractButton.setObjectName("extractButton")
        self.extractButton.setStyleSheet(button_style)
    #"border-style: inset;")

        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 270, 500, 150))
        self.listWidget.setObjectName("listWidgets")
        self.listWidget.setStyleSheet( "background-color: #253950;")
       
        

        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteButton.setGeometry(QtCore.QRect( 20, 440, 81, 23))
        self.deleteButton.setObjectName("deleteButton")
        self.deleteButton.setStyleSheet(button_style)
        
        
        self.testButton = QtWidgets.QPushButton(self.centralwidget)
        self.testButton.setGeometry(QtCore.QRect( 115, 440, 81, 23))
        self.testButton.setObjectName("testButton")
        # --------------------------Файлы 

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 21))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        #self.TextEdit.setText(_translate("MainWindow", "Введите текст сообщения..."))
        self.CheckBoxP.setText(_translate("MainWindow", "Пограничных состояний"))
        self.CheckBoxD.setText(_translate("MainWindow", "Детское отделение"))
        self.CheckBoxN.setText(_translate("MainWindow", "Наркологическое отделение"))
        self.CheckBoxALL.setText(_translate("MainWindow", "Выбрать все отделения"))
        self.btnsend.setText(_translate("MainWindow", "Отправить"))
        self.deleteButton.setText(_translate("MainWindow", "Удалить файл"))
        #self.btnBroswse.setText(_translate("MainWindow", "Выбрать папку"))
        #self.btnArch.setText(_translate("MainWindow", "Архивировать"))
        self.extractButton.setText(_translate("MainWindow", "Выбрать файл"))
        self.btnstartTG.setText(_translate("MainWindow", "Запуск/Перезапуск бота"))
        self.testButton.setText(_translate("MainWindow", "Test Button"))
        self.btnckear.setText(_translate("MainWindow", "Очистить сообщение"))
        self.btnstartClose.setText(_translate("MainWindow", "Закрыть бота"))
        #self.CheckBoxALL
        #[mandatoryField="true"] { background-color: yellow }
        #nameEdit = self.CheckBoxALL#(self)
        #nameEdit.setProperty("mandatoryField", True)

        
'''
        self.listWidget2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget2.setGeometry(QtCore.QRect(150, 21, 131, 151))
        self.listWidget2.setObjectName("listWidget2")

        self.btnArch = QtWidgets.QPushButton(self.centralwidget)
        self.btnArch.setGeometry(QtCore.QRect(110, 180, 81, 23))
        self.btnArch.setObjectName("btnArch")

'''