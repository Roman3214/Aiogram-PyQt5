

from cmath import log
import time
import front
import sys, os, zipfile, traceback, subprocess
from PyQt5 import QtWidgets, QtCore 
from PyQt5.QtWidgets import QLineEdit, QInputDialog, QMessageBox
from threading import Thread
from PyQt5.QtCore import QThread
import sqlite3

class ExampleApp(QtWidgets.QMainWindow, front.Ui_MainWindow):
    directory = ''

    def __init__(self):#, queue_in, queue_out):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()

        #self.queue_in = queue_in
        #self.queue_out = queue_out

        self.setupUi(self)  # Это нужно для инициализации дизайна
        #self.btnBrowse.clicked.connect(self.browse_folder)
        #self.btnArch.clicked.connect(self.arch_folder)
        self.extractButton.clicked.connect(self.extract)
        self.CheckBoxALL.stateChanged.connect(self.changeTitle)
        self.btnsend.clicked.connect(self.sendButton)
        self.btnstartTG.clicked.connect(self.btnstartTelegraam)
        self.deleteButton.clicked.connect(self.deletewidget)
        self.testButton.clicked.connect(self.testbuttton)
        self.btnckear.clicked.connect(self.buttonckear)
        self.btnstartClose.clicked.connect(self.buttonClose)

        self.CheckBoxP.stateChanged.connect(self.onClicked_CheckBoxP)
        self.CheckBoxD.stateChanged.connect(self.onClicked_CheckBoxD)
        self.CheckBoxN.stateChanged.connect(self.onClicked_CheckBoxN)
        self.CheckBoxALL.stateChanged.connect(self.onClicked_CheckBoxALL)

        

    def buttonClose(self):
        time.sleep(5)

        self.btnstartTelegraam().kill()
    def buttonckear(self):
        self.TextEdit.clear()

    def onClicked_CheckBoxP(self, state):
        if state == QtCore.Qt.Checked:
            self.CheckBoxP.setStyleSheet(
                "QCheckBox"
                "{background-color: #2B5278;}")
        else:
            self.CheckBoxP.setStyleSheet( 
                
                "QCheckBox"
                "{background-color: #25303E; }")

    def onClicked_CheckBoxD(self, state):
        if state == QtCore.Qt.Checked:
            self.CheckBoxD.setStyleSheet(
                "QCheckBox"
                "{background-color: #2B5278;}")
        else:
            self.CheckBoxD.setStyleSheet( 
                "QCheckBox"
                "{background-color: #25303E; }")

    def onClicked_CheckBoxN(self, state):
        if state == QtCore.Qt.Checked:
            self.CheckBoxN.setStyleSheet(
                "QCheckBox"
                "{background-color: #2B5278;}")
        else:
            self.CheckBoxN.setStyleSheet(
                "QCheckBox"
                "{background-color: #25303E; }")

    def onClicked_CheckBoxALL(self, state):
        try:
            conn = sqlite3.connect('users.db')
            cursor = conn.cursor()
            if state == QtCore.Qt.Checked:
                self.CheckBoxALL.setStyleSheet(
                    "QCheckBox"
                    "{background-color: #2B5278;}")
                cursor.execute('INSERT OR IGNORE INTO "who_to_send_a_message_to" ("branch_name") VALUES (?)', ('send_all'),)
                conn.commit()
            else:
                self.CheckBoxALL.setStyleSheet( 
                    "QCheckBox"
                    "{background-color: #25303E; }")
                sql_update_query = """DELETE FROM who_to_send_a_message_to WHERE branch_name = 'send_all'"""
                cursor.execute(sql_update_query)#, ('send_all', ))
                conn.commit()
        except sqlite3.Error as error:
            print('Error', error)
        finally:
            if(conn):
                conn.close()
        
        
    def testbuttton(self):    
        '''s = self.listWidget.selectedItems()#.text()
        #b = self.listWidget.currentItem().text()
        a = self.listWidget.count()
        items = []
        #self.directorys = QtWidgets.QFileDialog.getOpenFileName(self, "select file")
        for i in range(self.listWidget.count()):
            item = self.listWidget.item(i)
            items.append(item.text())
        print(a)'''
        self.btnstartTelegraam().kill()
        self.close()
        #subprocess.Popen(["main.py"], shell=True, stdout=subprocess.PIPE).kill()
        #re = self.listWidget.findItems(self.directorys[0], items)
        #print(re)
        
        #findItems()    
        #return items
        # разобраться с повторным добовлением

    def btnstartTelegraam(self):
        #if state == QtCore.Qt.Checked:
        #QThread(os.system('main.py'))
        #with subprocess.Popen(args=["start", "python", "main.py"], shell=True, stdout=subprocess.PIPE) as proc:
        #    log(proc.stdout.read())

        proc1 = subprocess.Popen(["main.py"], shell=True, stdout=subprocess.PIPE)#, creationflags = subprocess.CREATE_NO_WINDOW)
        proc1.stdout.close()
        #else:
        #    proc.kill()
        #    subprocess.Popen(args=["start", "python", "main.py"], shell=True, stdout=subprocess.PIPE)
        return proc1

    def format_file(self, photo):
        list_format_photo = ['.raw', '.jpeg', '.jpg', '.tiff', '.psd', '.bmp', '.png', '.gif']
        list_path_photo = []
        for i in list_format_photo:
            if str(photo).lower().find(i) != -1:
                list_path_photo.append(photo)
                print(f'asdsdsq  "{list_path_photo}"')  
        return list_path_photo  

    def extract(self):
        #self.listWidget.clear()  # На случай, если в списке уже есть элементы
        self.directorys = QtWidgets.QFileDialog.getOpenFileName(self, "select file")
        print(self.directorys[0])
        
        list_format_photo = ['.raw', '.jpeg', '.jpg', '.tiff', '.psd', '.bmp', '.png', '.gif']
        list_format_video = ['.avi','.mp4', '.mkv', '.mov', '.mkv', '.vob','.wmv']
        list_format_doc = ['.doc', '.dot', '.pdf', '.docx', '.xml', '.rtf', '.dotx', '.txt']
        list_path_photo = []
        list_path_video = []
        list_path_doc = []
        
        
        items = []
        for i in range(self.listWidget.count()):
            item = self.listWidget.item(i)
            items.append(item.text())
        
        #print(f"asfafdc {list_path_photo}")
        
        if str(items).find(self.directorys[0]) == -1:
            
            self.listWidget.addItem(self.directorys[0])
            for i in list_format_photo:
                if str(self.directorys[0]).lower().find(i) != -1:
                    list_path_photo.insert(0, self.directorys[0])
                    try:
                        conn = sqlite3.connect('users.db')
                        cursor = conn.cursor()
                        cursor.execute('INSERT OR IGNORE INTO "datainfo" ("photo_message") VALUES (?)', (str(list_path_photo[0]),))
                        conn.commit()
                        
                    except sqlite3.Error as error:
                        print('Error', error)
                    finally:
                        if(conn):
                            conn.close()
                    #list_path_photo.append(self.directorys[0])
                    #print(list_path_photo)
            for i in list_format_video:
                if str(self.directorys[0]).lower().find(i) != -1:
                    list_path_video.insert(0, self.directorys[0])
                    try:
                        conn = sqlite3.connect('users.db')
                        cursor = conn.cursor()
                        cursor.execute('INSERT OR IGNORE INTO "datainfo" ("video_message") VALUES (?)', (str(list_path_video[0]),))
                        conn.commit()
                        
                    except sqlite3.Error as error:
                        print('Error', error)
                    finally:
                        if(conn):
                            conn.close()
            
            for i in list_format_doc:
                if str(self.directorys[0]).lower().find(i) != -1:
                    list_path_doc.insert(0, self.directorys[0])
                    try:
                        conn = sqlite3.connect('users.db')
                        cursor = conn.cursor()
                        cursor.execute('INSERT OR IGNORE INTO "datainfo" ("documentation_message") VALUES (?)', (str(list_path_doc[0]),))
                        conn.commit()
                        
                    except sqlite3.Error as error:
                        print('Error', error)
                    finally:
                        if(conn):
                            conn.close()

        elif str(items).find(self.directorys[0]) != -1:
            
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Ошибка")
            msg.setText("Этот файл уже выбран")
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.exec_()
        
        #shutil.copy(self.directorys[0],  os.getcwd())
        
        
        #self.CheckBoxALL.stateChanged.connect(self.changeTitle)
        #print(f'sdfsdf = :  {qwew}')
            #print(self.CheckBoxP.clicked.connect(1))
        '''if self.directory:  # не продолжать выполнение, если пользователь не выбрал директорию
            for file_name in os.listdir(self.directory):  # для каждого файла в директории
                self.listWidget.addItem(file_name)  # добавить файл в listWidget
        self.listWidget.clear()  # На случай, если в списке уже есть элементы
        self.directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")


        if self.directory:  # не продолжать выполнение, если пользователь не выбрал директорию
            for file_name in os.listdir(self.directory):  # для каждого файла в директории
                self.listWidget.addItem(file_name)  # добавить файл в listWidget'''
        return self.directory
        '''
        self.archive = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите архив")
        print(self.archive)
        zip_arch = zipfile.ZipFile(self.archive[0], 'r')
        for files in zip_arch.namelist():
            zip_arch.extract(files)
        zip_arch.close()'''

    def changeTitle(self, state):
    
        if self.CheckBoxALL.isChecked() == True:
            self.CheckBoxP.setChecked(True)# 
            self.CheckBoxD.setChecked(True)# 
            self.CheckBoxN.setChecked(True)#
            
        else:
            self.CheckBoxP.setChecked(False)# какаято х чтото придумать
            self.CheckBoxD.setChecked(False)# какаято х чтото придумать
            self.CheckBoxN.setChecked(False)# какаято х чтото придумать
           
            
    def sendButton(self):
        try:
            conn = sqlite3.connect('users.db')
            cursor = conn.cursor()
            #sql_update_query = """DELETE FROM who_to_send_a_message_to WHERE branch_name = 'send_all'"""
            cursor.execute("DELETE FROM who_to_send_a_message_to ")#, ('send_all', ))
            conn.commit()
        except sqlite3.Error as error:
            print('Error', error)
        finally:
            if(conn):
                conn.close()
        # наладить clear
        parse_text = self.TextEdit.toPlainText()
        ALL = self.CheckBoxALL.isChecked()
        P = self.CheckBoxP.isChecked()
        D = self.CheckBoxD.isChecked()
        N = self.CheckBoxN.isChecked()
        
        if len(parse_text) == 0:

            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Ошибка")
            msg.setText("Пожалуйста убедитесь что вы ввели текст своего сообщения!")
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.exec_()
            #msg.setStyleSheet(self, button_style)

        
            #if self.CheckBoxP.isChecked() and self.CheckBoxD.isChecked() and self.CheckBoxN.isChecked() and self.CheckBoxALL.isChecked() == None:
                #невереное условие 
                
            #    with open('textALL.txt', 'w', encoding= 'utf-8') as write_file:
            #        write_file.write(parse_text)
        if  ALL == True:
            try:
                conn = sqlite3.connect('users.db')
                cursor = conn.cursor() 
                cursor.execute('INSERT OR IGNORE INTO "who_to_send_a_message_to" ("branch_name") VALUES ("Send_All")')
                conn.commit()  
                cursor.close()
            except sqlite3.Error as error:
                print('Error', error)
            finally:
                if(conn):
                    conn.close()              
            #with open('textALL.txt', 'w', encoding= 'utf-8') as write_file:
            #    write_file.write(parse_text)
            

        elif  P and D and N == True:
            try:
                conn = sqlite3.connect('users.db')
                cursor = conn.cursor() 
                cursor.execute('INSERT OR IGNORE INTO "who_to_send_a_message_to" ("branch_name") VALUES ("Send_All")')
                conn.commit()  
                cursor.close()
            except sqlite3.Error as error:
                print('Error', error)
            finally:
                if(conn):
                    conn.close() 
            #with open('textPDN.txt', 'w', encoding= 'utf-8') as write_file:
            #    write_file.write(parse_text)

        elif  P and D == True:
            try:
                conn = sqlite3.connect('users.db')
                cursor = conn.cursor() 
                cursor.execute('INSERT OR IGNORE INTO "who_to_send_a_message_to" ("branch_name") VALUES ("Send_Pogr_Children")')
                conn.commit()  
                cursor.close()
            except sqlite3.Error as error:
                print('Error', error)
            finally:
                if(conn):
                    conn.close() 
            #with open('textPD.txt', 'w', encoding= 'utf-8') as write_file:
            #    write_file.write(parse_text)
        elif  P and N == True:
            try:
                conn = sqlite3.connect('users.db')
                cursor = conn.cursor() 
                cursor.execute('INSERT OR IGNORE INTO "who_to_send_a_message_to" ("branch_name") VALUES ("Send_Pogr_Narko")')
                conn.commit()  
                cursor.close()
            except sqlite3.Error as error:
                print('Error', error)
            finally:
                if(conn):
                    conn.close() 
            #with open('textPN.txt', 'w', encoding= 'utf-8') as write_file:
            #    write_file.write(parse_text)
        elif  D and N == True:
            try:
                conn = sqlite3.connect('users.db')
                cursor = conn.cursor() 
                cursor.execute('INSERT OR IGNORE INTO "who_to_send_a_message_to" ("branch_name") VALUES ("Send_Children_Narko")')
                conn.commit()  
                cursor.close()
            except sqlite3.Error as error:
                print('Error', error)
            finally:
                if(conn):
                    conn.close() 
            #with open('textDN.txt', 'w') as write_file:
            #    write_file.write(parse_text)
                

        elif  P == True:
            try:
                conn = sqlite3.connect('users.db')
                cursor = conn.cursor() 
                cursor.execute('INSERT OR IGNORE INTO "who_to_send_a_message_to" ("branch_name") VALUES ("Send_Pogr")')
                conn.commit()  
                cursor.close()
            except sqlite3.Error as error:
                print('Error', error)
            finally:
                if(conn):
                    conn.close() 
            #with open('textP.txt', 'w', encoding= 'utf-8') as write_file:
            #    write_file.write(parse_text)
        elif D == True:
            try:
                conn = sqlite3.connect('users.db')
                cursor = conn.cursor() 
                cursor.execute('INSERT OR IGNORE INTO "who_to_send_a_message_to" ("branch_name") VALUES ("Send_Children")')
                conn.commit()  
                cursor.close()
            except sqlite3.Error as error:
                print('Error', error)
            finally:
                if(conn):
                    conn.close() 
            #with open('textD.txt', 'w', encoding= 'utf-8') as write_file:
            #    write_file.write(parse_text)
        elif N == True:
            try:
                conn = sqlite3.connect('users.db')
                cursor = conn.cursor() 
                cursor.execute('INSERT OR IGNORE INTO "who_to_send_a_message_to" ("branch_name") VALUES ("Send_Narko")')
                conn.commit()  
                cursor.close()
            except sqlite3.Error as error:
                print('Error', error)
            finally:
                if(conn):
                    conn.close() 
            #with open('textN.txt', 'w', encoding= 'utf-8') as write_file:
            #    write_file.write(parse_text)
        
        try:
            conn = sqlite3.connect('users.db')
            cursor = conn.cursor()  

            cursor.execute('INSERT OR IGNORE INTO "datainfo" ("text_message") VALUES (?)', (str(parse_text),))
            conn.commit()
            
        except sqlite3.Error as error:
            print('Error', error)
        finally:
            if(conn):
                conn.close()

        #users_Pogr = cursor.execute("INSERT INTO datainfo VALUES (?,?,?,?,) ", parse_text)
        #users_id_Pogr = [i[0] for i in users_Pogr]

        
        button = QtWidgets.QApplication.instance().sender()
        if button.text() == 'Отправить':
            self.TextEdit.clear()
        self.listWidget.clear()  
        #print(parse_text)

    def deletewidget(self):
        self.listWidget.currentItem()
        self.listWidget.takeItem(self.listWidget.currentRow())     

#def main():
  # и запускаем приложение
if __name__ == '__main__':
    


    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    password, ok = QInputDialog.getText(None, 'Авторизация', 'Введите пороль:', QLineEdit.Password)
    if not ok:
        QMessageBox.warning(None, 'Внимние', 'Необходимо ввести пороль!')
        quit()

    if password != '123':
        QMessageBox.warning(None, 'Внимние', 'Пороль введен не верно!')
        quit()
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()