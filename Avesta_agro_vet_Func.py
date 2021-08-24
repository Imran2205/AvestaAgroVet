from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QCheckBox, QTabWidget
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter, QPrintPreviewDialog
from PyQt5.QtWidgets import *
from functools import partial
import sys
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QDesktopServices
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtCore import QThread, pyqtSignal, QTimer
from PyQt5 import QtWebEngineWidgets
import sys
import pandas as pd
import numpy as np
import pyrebase
import json
import PyQt5.sip
import pdfkit
from string import Template
import datetime
from datetime import datetime as dt
from datetime import date
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
import time
from zeep import Client
import os
import login, message, main_ui, entry_sale, register, library_add_product, add_customer
import add_zone, add_supplier, opening_amount_ui, opening_balance_ui, money_received_ui
import add_expense_type_ui, add_expense_ui, update_entry_sale, update_product_ui, update_product_ui
import update_supplier_ui, update_customer_ui, update_money_received_ui, update_expense_ui, user_access_ui
import message2, product_report_ui, customer_report_ui, sales_detail_ui, money_received_detail_ui
from google.protobuf import timestamp_pb2
import inflect
p = inflect.engine()

path_wkthmltopdf = b'C:\Program Files\wkhtmltopdf\\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)

url = 'https://api2.onnorokomsms.com/sendsms.asmx?WSDL'
client = Client(url)
userName = ''
password = ''
recipientNumber = ''
smsText = ''
smsType = 'TEXT'
maskName = ''
campaignName = ''

file_save_path = os.environ['USERPROFILE']
file_save_path = os.path.join(file_save_path, 'Documents/Machronics')

user_info_file_loc = os.path.join(file_save_path, 'user_info')

if not os.path.exists(user_info_file_loc):
    os.makedirs(user_info_file_loc)

pyrebase_config = {
    "apiKey": "AIzaSyBvljDPKu0_BVYX6xMouGyHOmKWuF2ILzI",
    "authDomain": "machronics-d1ee6.firebaseapp.com",
    "databaseURL": "https://machronics-d1ee6-default-rtdb.firebaseio.com/",
    "projectId": "machronics-d1ee6",
    "storageBucket": "machronics-d1ee6.appspot.com",
    "messagingSenderId": "310427855803",
    "appId": "1:310427855803:web:c2208bad9105dee84df29e",
    "measurementId": "G-MPZBC9W4S1"
}

"""pyrebase_config = {
    "apiKey": "AIzaSyDnsamd4Uw_rnxKUSpkeNrdWnvbba33nP4",
    "authDomain": "avesta-agro-vet.firebaseapp.com",
    "databaseURL": "https://avesta-agro-vet.firebaseio.com",
    "projectId": "avesta-agro-vet6",
    "storageBucket": "avesta-agro-vet.appspot.com",
    "messagingSenderId": "337955644180",
    "appId": "1:337955644180:web:30509098a437d829105801",
    "measurementId": "G-FJM592PW9B"
}"""

firebase = pyrebase.initialize_app(pyrebase_config)
auth = firebase.auth()
db = firebase.database()
storage = firebase.storage()
logo_url = storage.child("images/logo.png").get_url(token = 'e90eab02-dccd-45da-b63d-0481d17cf919')
dimension_url = storage.child("images/dimension.png").get_url(token = '1f2cabef-858b-4aea-b8f2-031bcda93592')
bootstrap_css_url = storage.child("css/bootstrap.min.css").get_url(token = '2f1a976b-3120-4903-bacc-95f6c58bce7b')
bootstrap_js_url = storage.child("js/bootstrap.js").get_url(token = '412e8637-4ea4-4c36-ac3b-abddb086b069')
"""logo_url = storage.child("images/logo.png").get_url(token = '22337852-5675-4e63-80ca-ec99fa70c6f2')
dimension_url = storage.child("images/dimension.png").get_url(token = '6f49902f-e5d8-4a0d-b52d-d8cafc3d9840')
bootstrap_css_url = storage.child("css/bootstrap.min.css").get_url(token = '2f8de675-f2f6-4583-83a1-ed767a58255b')
bootstrap_js_url = storage.child("js/bootstrap.js").get_url(token = '9a3a5e4e-3274-49f8-8bc5-a9ffe0f117df')"""
product_id_starting_number = 10000
customer_id_start = 100300500
supplier_id_start = 10030500
invoice_id_start = 1003005000
money_rcv_id_start = 1003005000
expense_start_value = 1003005000

file_location = ''

class App(QWidget):
    signal = pyqtSignal('PyQt_PyObject')
    def __init__(self):
        super().__init__()
        self.title = 'File Dialog'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        #self.openFileNameDialog()
        #self.openFileNamesDialog()
        self.saveFileDialog()

        #self.show()

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)

    def openFileNamesDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self, "QFileDialog.getOpenFileNames()", "",
                                                "All Files (*);;Python Files (*.py)", options=options)
        if files:
            print(files)

    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, x = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "",
                                                  ".pdf", options=options)
        if fileName:
            self.signal.emit(fileName+x)
            self.close()

class MainUIClass(QTabWidget, main_ui.Ui_TabWidget):
    #switch_window = QtCore.pyqtSignal(str)
    def __init__(self, parent=None):
        super(MainUIClass, self).__init__(parent)
        self.setupUi(self)
        self.saleEntryUi = SaleEntryUIClass()
        self.productLibraryUi = ProductLibraryUIClass()
        self.add_customer_ui = AddCustomerUI()
        self.add_supplier_ui = AddSupplierUI()
        self.add_zone_ui = AddZoneUI()
        self.opening_amount_ui = OpeningAmountUI()
        self.opening_balance_ui = OpeningBalanceUI()
        self.money_received_ui = MoneyReceivedUI()
        self.add_expense_type_ui = AddExpenseTypeUI()
        self.add_expense_ui = AddExpenseUI()
        self.update_sale_entry_ui = UpdateSaleEntryUIClass()
        self.update_product_ui = UpdateProductUI()
        self.update_supplier_ui = UpdateSupplierUI()
        self.update_customer_ui = UpdateCustomerUI()
        self.update_money_received_ui = UpdateMoneyReceivedUI()
        self.update_expense_ui = UpdateExpenseUI()
        self.update_user_ui = UpdateUserUI()
        self.product_report_ui = ProductReportUI()
        self.thread_class = ThreadClass()
        self.customer_report_ui = CustomerReportUI()
        self.sales_detail_ui = SalesDetailUI()
        self.money_receivecd_detail_ui = MoneyReceivedDetailUI()
        self.thread_class.start()
        self.entry_sale_btn.clicked.connect(self.new_sale_entry)
        self.library_add_product_btn.clicked.connect(self.new_product_library)
        self.library_add_customer_btn.clicked.connect(self.add_customer)
        self.library_add_supplier_btn.clicked.connect(self.add_supplier)
        self.library_add_zone_btn.clicked.connect(self.add_zone)
        self.library_add_opening_product_btn.clicked.connect(self.opening_amount)
        self.library_add_opening_amount_btn.clicked.connect(self.opening_balance)
        self.entry_money_btn.clicked.connect(self.money_received)
        self.library_add_expense_btn.clicked.connect(self.add_expense_type)
        self.entry_expense_btn.clicked.connect(self.add_expense)
        self.update_sale_btn.clicked.connect(self.update_sale_entry)
        self.library_update_product_btn.clicked.connect(self.update_product)
        self.library_update_supplier_btn.clicked.connect(self.update_supplier)
        self.library_update_customer_btn.clicked.connect(self.update_customer)
        self.update_money_btn.clicked.connect(self.update_money_receive)
        self.update_expense_btn.clicked.connect(self.update_expense)
        self.library_update_employee_btn.clicked.connect(self.update_user)
        self.pr.clicked.connect(self.product_report)
        user = auth.current_user
        if user:
            admin = db.child('user').child(user['localId']).child('admin').get().val()
            if not admin:
                self.update_sale_btn.setEnabled(False)
                self.library_update_product_btn.setEnabled(False)
                self.library_update_supplier_btn.setEnabled(False)
                self.library_update_customer_btn.setEnabled(False)
                self.update_money_btn.setEnabled(False)
                self.update_expense_btn.setEnabled(False)
                self.library_update_employee_btn.setEnabled(False)
            else:
                self.update_sale_btn.setEnabled(True)
                self.library_update_product_btn.setEnabled(True)
                self.library_update_supplier_btn.setEnabled(True)
                self.library_update_customer_btn.setEnabled(True)
                self.update_money_btn.setEnabled(True)
                self.update_expense_btn.setEnabled(True)
                self.library_update_employee_btn.setEnabled(True)
        else:
            self.update_sale_btn.setEnabled(False)
            self.library_update_product_btn.setEnabled(False)
            self.library_update_supplier_btn.setEnabled(False)
            self.library_update_customer_btn.setEnabled(False)
            self.update_money_btn.setEnabled(False)
            self.update_expense_btn.setEnabled(False)
            self.library_update_employee_btn.setEnabled(False)
        self.cr.clicked.connect(self.customer_report)
        self.sd.clicked.connect(self.sales_detail)
        self.mrd.clicked.connect(self.money_received_detail)
        self.pushButton_logout.clicked.connect(self.logout)

    def logout(self):
        auth.current_user = None
        file_location = os.path.join(user_info_file_loc, 'login_info.info')
        if os.path.exists(file_location):
            os.remove(file_location)
        #controller = Controller
        #controller.show_login()
        self.close()

    def money_received_detail(self):
        self.money_receivecd_detail_ui.show_me()

    def sales_detail(self):
        self.sales_detail_ui.show_me()

    def customer_report(self):
        self.customer_report_ui.show_me()

    def product_report(self):
        self.product_report_ui.show_me()

    def update_user(self):
        self.update_user_ui.show_me()

    def update_expense(self):
        self.update_expense_ui.show_me()

    def update_sale_entry(self):
        self.update_sale_entry_ui.show_me()

    def add_expense_type(self):
        self.add_expense_type_ui.show_me()

    def add_zone(self):
        self.add_zone_ui.show_me()

    def add_customer(self):
        self.add_customer_ui.show_me()

    def add_supplier(self):
        self.add_supplier_ui.show_me()

    def new_sale_entry(self):
        self.saleEntryUi.show_me()

    def new_product_library(self):
        self.productLibraryUi.show_me()

    def opening_amount(self):
        self.opening_amount_ui.show_me()

    def opening_balance(self):
        self.opening_balance_ui.show_me()

    def money_received(self):
        self.money_received_ui.show_me()

    def add_expense(self):
        self.add_expense_ui.show_me()

    def update_product(self):
        self.update_product_ui.show_me()

    def update_supplier(self):
        self.update_supplier_ui.show_me()

    def update_customer(self):
        self.update_customer_ui.show_me()

    def update_money_receive(self):
        self.update_money_received_ui.show_me()

class SalesDetailUI(QMainWindow, sales_detail_ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(SalesDetailUI, self).__init__(parent)
        self.setupUi(self)
        self.row_count = 0
        self.dialog = Dialog()
        self.df = pd.DataFrame()
        self.df2 = pd.DataFrame()

    def show_me(self):
        self.clear_n_new()
        self.show()

    def clear_n_new(self):
        self.create_table()
        try:
            self.dat = db.child('invoice').get().val()
            #print(self.dat)
            self.df = pd.DataFrame(self.dat, columns=self.dat.keys())
            self.df = self.df.transpose()
            #print(self.df)
            """self.dat2 = db.child('customer spend').get().val()
            self.df2 = pd.DataFrame(self.dat2, columns=self.dat2.keys())
            self.df2 = self.df2.transpose()
            self.df = pd.concat([self.df, self.df2], axis=1, sort=False)"""
            ids = list(self.df['invoice id'].values)
            #print(ids)
            for id_ in ids:
                if id_ is not None:
                    self.table.setRowCount(self.row_count)
                    row = self.row_count - 1
                    data = self.df[self.df['invoice id'] == id_]
                    #data = data[0]
                    self.table.setItem(row, 0, QTableWidgetItem(str(id_)))
                    dt = list(data['customer id'])
                    dt = dt[0]
                    self.table.setItem(row, 1, QTableWidgetItem(str(dt)))
                    dt = list(data['sub total'])
                    dt = dt[0]
                    if str(dt) == 'nan':
                        dt = 0.0
                    self.table.setItem(row, 2, QTableWidgetItem("{:.2f}".format(float(dt))))
                    dt = list(data['employee name'])
                    dt = dt[0]
                    self.table.setItem(row, 3, QTableWidgetItem(str(dt)))
                    dt = list(data['booking date'])
                    dt = dt[0]
                    self.table.setItem(row, 4, QTableWidgetItem(str(dt)))
                    dt = list(data['delivery date'])
                    dt = dt[0]
                    self.table.setItem(row, 5, QTableWidgetItem(str(dt)))
                    self.row_count = self.row_count + 1
        except Exception as e:
            print(e)
            self.df2 = pd.DataFrame()
            self.df = pd.DataFrame()
            self.dialog.message_text.setText("Can not load data. Check internet connection")
            self.dialog.displayInfo()


    def add_row(self):
        pass

    def create_table(self):
        self.table.clear()
        self.row_count = 1
        self.table.setRowCount(self.row_count)
        self.row_count = self.row_count + 1
        self.table.setColumnCount(6)
        self.table.setItem(0, 0, QTableWidgetItem("Invoice ID"))
        self.table.setItem(0, 1, QTableWidgetItem("Sold to"))
        self.table.setItem(0, 2, QTableWidgetItem("Total Bill"))
        self.table.setItem(0, 3, QTableWidgetItem("Sold by"))
        self.table.setItem(0, 4, QTableWidgetItem("Order date"))
        self.table.setItem(0, 5, QTableWidgetItem("Delivery date"))
        self.table.move(0, 0)

class MoneyReceivedDetailUI(QMainWindow, money_received_detail_ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MoneyReceivedDetailUI, self).__init__(parent)
        self.setupUi(self)
        self.row_count = 0
        self.dialog = Dialog()
        self.df = pd.DataFrame()
        self.df2 = pd.DataFrame()

    def show_me(self):
        self.clear_n_new()
        self.show()

    def clear_n_new(self):
        self.create_table()
        #try:
        self.dat = db.child('money received').get().val()
        self.df = pd.DataFrame(self.dat, columns=self.dat.keys())
        self.df = self.df.transpose()
        """self.dat2 = db.child('customer spend').get().val()
        self.df2 = pd.DataFrame(self.dat2, columns=self.dat2.keys())
        self.df2 = self.df2.transpose()
        self.df = pd.concat([self.df, self.df2], axis=1, sort=False)"""
        ids = list(self.df['id'].values)
        for id_ in ids:
            self.table.setRowCount(self.row_count)
            row = self.row_count - 1
            data = self.df[self.df['id'] == id_]
            #data = data[0]
            self.table.setItem(row, 0, QTableWidgetItem(str(id_)))
            dt = list(data['customer'])
            dt = dt[0]
            self.table.setItem(row, 1, QTableWidgetItem(str(dt)))
            dt = list(data['amount'])
            dt = dt[0]
            if str(dt) == 'nan':
                dt = 0.0
            self.table.setItem(row, 2, QTableWidgetItem("{:.2f}".format(float(dt))))
            dt = list(data['discount'])
            dt = dt[0]
            if str(dt) == 'nan':
                dt = 0.0
            self.table.setItem(row, 3, QTableWidgetItem("{:.2f}".format(float(dt))))
            dt = list(data['order number'])
            dt = dt[0]
            self.table.setItem(row, 4, QTableWidgetItem(str(dt)))
            dt = list(data['received date'])
            dt = dt[0]
            self.table.setItem(row, 5, QTableWidgetItem(str(dt)))
            dt = list(data['type'])
            dt = dt[0]
            self.table.setItem(row, 6, QTableWidgetItem(str(dt)))

            self.row_count = self.row_count + 1

        """except Exception as e:
            print(e)
            self.df2 = pd.DataFrame()
            self.df = pd.DataFrame()
            self.dialog.message_text.setText("Can not load data. Check internet connection")
            self.dialog.displayInfo()"""


    def add_row(self):
        pass

    def create_table(self):
        self.table.clear()
        self.row_count = 1
        self.table.setRowCount(self.row_count)
        self.row_count = self.row_count + 1
        self.table.setColumnCount(7)
        self.table.setItem(0, 0, QTableWidgetItem("ID"))
        self.table.setItem(0, 1, QTableWidgetItem("Received from"))
        self.table.setItem(0, 2, QTableWidgetItem("Amount"))
        self.table.setItem(0, 3, QTableWidgetItem("Discount"))
        self.table.setItem(0, 4, QTableWidgetItem("Payment of Order no"))
        self.table.setItem(0, 5, QTableWidgetItem("Received date"))
        self.table.setItem(0, 6, QTableWidgetItem("Received via"))
        self.table.move(0, 0)

class CustomerReportUI(QMainWindow, customer_report_ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(CustomerReportUI, self).__init__(parent)
        self.setupUi(self)
        self.row_count = 0
        self.dialog = Dialog()
        self.df = pd.DataFrame()
        self.df2 = pd.DataFrame()

    def show_me(self):
        self.clear_n_new()
        self.show()

    def clear_n_new(self):
        self.create_table()
        try:
            self.dat = db.child('customer').get().val()
            self.df = pd.DataFrame(self.dat, columns=self.dat.keys())
            self.df = self.df.transpose()
            self.dat2 = db.child('customer spend').get().val()
            self.df2 = pd.DataFrame(self.dat2, columns=self.dat2.keys())
            self.df2 = self.df2.transpose()
            self.df = pd.concat([self.df, self.df2], axis=1, sort=False)
            ids = list(self.df['customer id'].values)
            for id_ in ids:
                self.table.setRowCount(self.row_count)
                row = self.row_count - 1
                data = self.df[self.df['customer id'] == id_].values
                data = data[0]
                self.table.setItem(row, 0, QTableWidgetItem(str(id_)))
                self.table.setItem(row, 1, QTableWidgetItem(str(data[1])))
                if str(data[-1]) == 'nan':
                    data[-1] = 0.0
                self.table.setItem(row, 2, QTableWidgetItem("{:.2f}".format(float(data[-1]))))
                if str(data[-2]) == 'nan':
                    data[-2] = 0.0
                self.table.setItem(row, 3, QTableWidgetItem("{:.2f}".format(float(data[-2]))))
                if str(data[-4]) == 'nan':
                    data[-4] = 0.0
                self.table.setItem(row, 4, QTableWidgetItem("{:.2f}".format(float(data[-4]))))

                self.table.setItem(row, 5, QTableWidgetItem(data[2]))
                self.table.setItem(row, 6, QTableWidgetItem(data[5]))
                self.row_count = self.row_count + 1

        except Exception as e:
            print(e)
            self.df2 = pd.DataFrame()
            self.df = pd.DataFrame()
            self.dialog.message_text.setText("Can not load data. Check internet connection")
            self.dialog.displayInfo()


    def add_row(self):
        pass

    def create_table(self):
        self.table.clear()
        self.row_count = 1
        self.table.setRowCount(self.row_count)
        self.row_count = self.row_count + 1
        self.table.setColumnCount(7)
        self.table.setItem(0, 0, QTableWidgetItem("Customer ID"))
        self.table.setItem(0, 1, QTableWidgetItem("Company Name"))
        self.table.setItem(0, 2, QTableWidgetItem("Total Bill"))
        self.table.setItem(0, 3, QTableWidgetItem("Paid"))
        self.table.setItem(0, 4, QTableWidgetItem("Due"))
        self.table.setItem(0, 5, QTableWidgetItem("Contact Person"))
        self.table.setItem(0, 6, QTableWidgetItem("Contact No"))
        self.table.move(0, 0)

class ProductReportUI(QMainWindow, product_report_ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(ProductReportUI, self).__init__(parent)
        self.setupUi(self)
        self.row_count = 0
        self.dialog = Dialog()
        self.df = pd.DataFrame()
        self.df2 = pd.DataFrame()

    def show_me(self):
        self.clear_n_new()
        self.show()

    def clear_n_new(self):
        self.create_table()
        try:
            self.dat = db.child('product').get().val()
            self.df = pd.DataFrame(self.dat, columns=self.dat.keys())
            self.df = self.df.transpose()
            self.dat2 = db.child('product sold').get().val()
            self.df2 = pd.DataFrame(self.dat2, columns=self.dat2.keys())
            self.df2 = self.df2.transpose()
            self.df = pd.concat([self.df, self.df2], axis=1, sort=False)
            ids = list(self.df['id'].values)
            for id_ in ids:
                self.table.setRowCount(self.row_count)
                row = self.row_count - 1
                data = self.df[self.df['id'] == id_].values
                data = data[0]
                self.table.setItem(row, 0, QTableWidgetItem(str(id_)))
                self.table.setItem(row, 1, QTableWidgetItem(str(data[1])))
                self.table.setItem(row, 2, QTableWidgetItem(str(data[2])))
                self.table.setItem(row, 3, QTableWidgetItem(str(data[3])))
                if str(data[5]) == 'nan':
                    data[5] =0
                self.table.setItem(row, 4, QTableWidgetItem(str(int(data[5]))))
                if str(data[4]) == 'nan':
                    data[4] =0.0
                self.table.setItem(row, 5, QTableWidgetItem("{:.2f}".format(float(data[4]))))
                self.row_count = self.row_count + 1

        except Exception as e:
            print(e)
            self.df2 = pd.DataFrame()
            self.df = pd.DataFrame()
            self.dialog.message_text.setText("Can not load data. Check internet connection")
            self.dialog.displayInfo()


    def add_row(self):
        pass

    def create_table(self):
        self.table.clear()
        self.row_count = 1
        self.table.setRowCount(self.row_count)
        self.row_count = self.row_count + 1
        self.table.setColumnCount(6)
        self.table.setItem(0, 0, QTableWidgetItem("Product ID"))
        self.table.setItem(0, 1, QTableWidgetItem("Product Name"))
        self.table.setItem(0, 2, QTableWidgetItem("Unit Price"))
        self.table.setItem(0, 3, QTableWidgetItem("Stock"))
        self.table.setItem(0, 4, QTableWidgetItem("Sell Qty"))
        self.table.setItem(0, 5, QTableWidgetItem("Sell Amount"))
        self.table.move(0, 0)

class UpdateUserUI(QMainWindow, user_access_ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(UpdateUserUI, self).__init__(parent)
        self.setupUi(self)
        self.df = pd.DataFrame()
        self.dialog = Dialog()
        self.save_n_new_btn.clicked.connect(self.save_n_new)
        self.save_n_exit_btn.clicked.connect(self.save_n_exit)
        self.user.currentTextChanged.connect(self.set_value)
        self.saved = False

    def save_n_new(self):
        self.save_n_new_btn.setEnabled(False)
        self.save_n_exit_btn.setEnabled(False)
        QTimer.singleShot(500, lambda: self.call_after_dis())

    def call_after_dis(self):
        self.save()
        self.save_n_new_btn.setEnabled(True)
        self.save_n_exit_btn.setEnabled(True)
        if self.saved:
            self.clear_n_new()

    def save_n_exit(self):
        self.save_n_new_btn.setEnabled(False)
        self.save_n_exit_btn.setEnabled(False)
        QTimer.singleShot(500, lambda: self.call_after_dis2())

    def call_after_dis2(self):
        self.save()
        self.save_n_new_btn.setEnabled(True)
        self.save_n_exit_btn.setEnabled(True)
        if self.saved:
            self.close()

    def save(self):
        if self.admin_access.currentText() == 'yes':
            data = 1
        else:
            data = 0

        user_id = self.df[self.df['first name'] == self.user.currentText()]['id']
        user_id = list(user_id)
        user_id = user_id[0]
        try:
            db.child('user').child(user_id).child('admin').set(data)
        except Exception as e:
            self.dialog.message_text.setText("Error saving data")
            self.dialog.displayInfo()

    def show_me(self):
        self.clear_n_new()
        self.show()

    def clear_n_new(self):
        try:
            self.dat = db.child('user').get().val()
            self.df = pd.DataFrame(self.dat, columns=self.dat.keys())
            self.df = self.df.transpose()
            name1 = list(self.df['first name'])
            self.user.clear()
            for x in range(len(name1)):
                self.user.addItem(name1[x])
            arr = ['yes', 'no']
            self.admin_access.clear()
            for c in range(len(arr)):
                self.admin_access.addItem(arr[c])
            cond = self.df[self.df['first name'] == self.user.currentText()]['admin']
            cond = list(cond)
            cond = cond[0]
            if cond == 1:
                self.admin_access.setCurrentText('yes')
            else:
                self.admin_access.setCurrentText('no')
        except Exception as e:
            self.df = pd.DataFrame()
            self.dialog.message_text.setText("Can not load data. Check internet connection")
            self.dialog.displayInfo()

    def set_value(self):
        cond = self.df[self.df['first name'] == self.user.currentText()]['admin']
        cond = list(cond)
        cond = cond[0]
        if cond == 1:
            self.admin_access.setCurrentText('yes')
        else:
            self.admin_access.setCurrentText('no')

class AddExpenseUI(QMainWindow, add_expense_ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(AddExpenseUI, self).__init__(parent)
        self.setupUi(self)
        self.df = pd.DataFrame()
        self.dialog = Dialog()
        self.save_btn.clicked.connect(self.save)
        self.save_btn.setEnabled(False)
        self.save_btn.hide()
        self.save_n_new_btn.clicked.connect(self.save_n_new)
        self.save_n_exit_btn.clicked.connect(self.save_n_exit)
        self.saved = False

    def save_n_new(self):
        self.save_n_new_btn.setEnabled(False)
        self.save_n_exit_btn.setEnabled(False)
        QTimer.singleShot(500, lambda: self.call_after_dis())

    def call_after_dis(self):
        self.save()
        self.save_n_new_btn.setEnabled(True)
        self.save_n_exit_btn.setEnabled(True)
        if self.saved:
            self.clear_n_new()

    def save_n_exit(self):
        self.save_n_new_btn.setEnabled(False)
        self.save_n_exit_btn.setEnabled(False)
        QTimer.singleShot(500, lambda: self.call_after_dis2())

    def call_after_dis2(self):
        self.save()
        self.save_n_new_btn.setEnabled(True)
        self.save_n_exit_btn.setEnabled(True)
        if self.saved:
            self.close()

    def save(self):
        id = self.id.text()
        data = {
            'id': id,
            'date': str(self.date.date().toPyDate()),
            'type': self.type.currentText(),
            'expense in': self.in__.currentText(),
            'description': self.description.toPlainText(),
            'amount': self.amount.value(),
            'remarks': self.remarks.toPlainText()
        }
        if data['id'] != '' and data['date'] != '' and data['type'] != '' and data['expense in'] != '' and data['description'] != '' and data['amount'] != 0 and data['remarks'] != '':
            try:
                db.child('expense').child(id).set(data)
                self.saved = True
            except Exception as e:
                self.dialog.message_text.setText("Error saving data")
                self.dialog.displayInfo()
                self.saved = False
        else:
            self.dialog.message_text.setText("Please fill up all the required fields")
            self.dialog.displayInfo()
            self.saved = False

    def show_me(self):
        self.clear_n_new()
        self.show()

    def clear_n_new(self):
        try:
            _data__ = db.child('expense type').shallow().get()
            _data__ = list(_data__.val())
            self.type.clear()
            for x in range(len(_data__)):
                self.type.addItem(_data__[x])
        except Exception as e:
            self.df = pd.DataFrame()
            self.dialog.message_text.setText("Can not load data. Check internet connection")
            self.dialog.displayInfo()
        try:
            data_0_ = db.child('expense').shallow().get()
            data_0_ = list(data_0_.val())
            for x in range(len(data_0_)):
                data_0_[x] = int(data_0_[x])
            new_id0 = max(data_0_) + 1
            out_data0 = str(new_id0)
            self.id.setText(out_data0)
        except Exception as e:
            self.id.setText(f'{expense_start_value}')
            self.dialog.message_text.setText("failed to fetch data or no records found")
            self.dialog.displayInfo()
        self.date.setDateTime(QtCore.QDateTime.currentDateTime())
        types = ['Bkash', 'Cash', 'Bank Transfer']
        self.in__.clear()
        for x in range(len(types)):
            self.in__.addItem(types[x])
        self.remarks.setText("")
        self.description.setText("")
        self.amount.setValue(0)

class UpdateExpenseUI(QMainWindow, update_expense_ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(UpdateExpenseUI, self).__init__(parent)
        self.setupUi(self)
        self.df = pd.DataFrame()
        self.dialog = Dialog()
        self.save_btn.clicked.connect(self.save)
        self.save_btn.setEnabled(False)
        self.save_btn.hide()
        self.save_n_new_btn.clicked.connect(self.save_n_new)
        self.save_n_exit_btn.clicked.connect(self.save_n_exit)
        self.saved = False
        self.search_btn.clicked.connect(self.search_func)
        self.edit_btn.clicked.connect(self.edit)

    def save_n_new(self):
        self.save_n_new_btn.setEnabled(False)
        self.save_n_exit_btn.setEnabled(False)
        QTimer.singleShot(500, lambda: self.call_after_dis())

    def call_after_dis(self):
        self.save()
        self.save_n_new_btn.setEnabled(True)
        self.save_n_exit_btn.setEnabled(True)
        if self.saved:
            self.clear_n_new()

    def save_n_exit(self):
        self.save_n_new_btn.setEnabled(False)
        self.save_n_exit_btn.setEnabled(False)
        QTimer.singleShot(500, lambda: self.call_after_dis2())

    def call_after_dis2(self):
        self.save()
        self.save_n_new_btn.setEnabled(True)
        self.save_n_exit_btn.setEnabled(True)
        if self.saved:
            self.close()

    def save(self):
        id = self.id.currentText()
        data = {
            'id': id,
            'date': str(self.date.date().toPyDate()),
            'type': self.type.currentText(),
            'expense in': self.in__.currentText(),
            'description': self.description.toPlainText(),
            'amount': self.amount.value(),
            'remarks': self.remarks.toPlainText()
        }
        if data['id'] != '' and data['date'] != '' and data['type'] != '' and data['expense in'] != '' and data['description'] != '' and data['amount'] != 0 and data['remarks'] != '':
            try:
                db.child('expense').child(id).set(data)
                self.saved = True
            except Exception as e:
                self.dialog.message_text.setText("Error saving data")
                self.dialog.displayInfo()
                self.saved = False
        else:
            self.dialog.message_text.setText("Please fill up all the required fields")
            self.dialog.displayInfo()
            self.saved = False

    def show_me(self):
        self.clear_n_new()
        self.show()

    def clear_n_new(self):
        try:
            _data__ = db.child('expense type').shallow().get()
            _data__ = list(_data__.val())
            self.type.clear()
            for x in range(len(_data__)):
                self.type.addItem(_data__[x])
        except Exception as e:
            self.df = pd.DataFrame()
            self.dialog.message_text.setText("Can not load data. Check internet connection")
            self.dialog.displayInfo()
        try:
            data_0_ = db.child('expense').shallow().get()
            data_0_ = list(data_0_.val())
            self.id.clear()
            for x in range(len(data_0_)):
                self.id.addItem(data_0_[x])
        except Exception as e:
            self.dialog.message_text.setText("failed to fetch data or no records found")
            self.dialog.displayInfo()
        self.date.setDateTime(QtCore.QDateTime.currentDateTime())
        types = ['Bkash', 'Cash', 'Bank Transfer']
        self.in__.clear()
        for x in range(len(types)):
            self.in__.addItem(types[x])
        self.remarks.setText("")
        self.description.setText("")
        self.amount.setValue(0)
        self.set_value()

    def search_func(self):
        data_0 = db.child('expense').shallow().get()
        data_0 = list(data_0.val())
        if self.search.text() != '' and self.search.text() in data_0:
            self.id.setCurrentText(self.search.text())
            self.edit()
        else:
            self.dialog.message_text.setText("No matching query found")
            self.dialog.displayInfo()

    def edit(self):
        self.set_value()

    def set_value(self):
        try:
            expense = db.child('expense').child(self.id.currentText()).get().val()
            self.remarks.setText(expense['remarks'])
            self.amount.setValue(expense['amount'])
            self.type.setCurrentText(expense['type'])
            format_str = '%Y-%m-%d'
            received_date = datetime.datetime.strptime(expense['date'], format_str)
            self.date.setDateTime(received_date)
            self.in__.setCurrentText(expense['expense in'])
            self.description.setText(expense['description'])
        except Exception as e:
            print(e)
            self.dialog.message_text.setText("failed to fetch data or some field value is missing")
            self.dialog.displayInfo()

class MoneyReceivedUI(QMainWindow, money_received_ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MoneyReceivedUI, self).__init__(parent)
        self.setupUi(self)
        self.df = pd.DataFrame()
        self.dialog = Dialog()
        self.save_btn.clicked.connect(self.save)
        self.save_btn.setEnabled(False)
        self.save_btn.hide()
        self.save_n_new_btn.clicked.connect(self.save_n_new)
        self.save_n_exit_btn.clicked.connect(self.save_n_exit)
        self.refresh = True
        self.saved = False
        self.prevSpend = 0.0
        self.saved_data3 = 0.0
        self.new_created = False
        self.new_created3 = False
        self.customer.currentTextChanged.connect(self.customer_changed)

    def customer_changed(self):
        self.new_created = False

    def save_n_new(self):
        self.save_n_new_btn.setEnabled(False)
        self.save_n_exit_btn.setEnabled(False)
        QTimer.singleShot(500, lambda: self.call_after_dis())

    def call_after_dis(self):
        self.save()
        self.save_n_new_btn.setEnabled(True)
        self.save_n_exit_btn.setEnabled(True)
        if self.saved:
            self.clear_n_new()

    def save_n_exit(self):
        self.save_n_new_btn.setEnabled(False)
        self.save_n_exit_btn.setEnabled(False)
        QTimer.singleShot(500, lambda: self.call_after_dis2())

    def call_after_dis2(self):
        self.save()
        self.save_n_new_btn.setEnabled(True)
        self.save_n_exit_btn.setEnabled(True)
        if self.saved:
            self.close()

    def save(self):
        id = self.id.text()
        data = {
            'id': id,
            'customer': self.customer.currentText(),
            'order number': self.order_number.text(),
            'received date': str(self.received_date.date().toPyDate()),
            'type': self.type.currentText(),
            'amount': self.amount.value(),
            'discount': self.discount.value(),
            'remarks': self.remarks.toPlainText()
        }
        if data['id'] != '' and data['order number'] != '' and data['customer'] != '' and data['received date'] != '' and data['type'] != '' and data['amount'] != 0:
            try:
                db.child('money received').child(id).set(data)
                customerId = self.df[self.df["company name"] == self.customer.currentText()]["customer id"]
                customerId = list(customerId)
                customerId = customerId[0]
                balance = self.df[self.df["company name"] == self.customer.currentText()]["opening balance"]
                balance = list(balance)
                balance = float(balance[0])
                balance = balance - self.amount.value() - float(data['discount'])
                db.child('customer').child(customerId).child('opening balance').set(balance)

                if "customer spend" in list(db.shallow().get().val()) and customerId in list(
                        db.child("customer spend").shallow().get().val()) and "paid" in list(db.child("customer spend").child(customerId).shallow().get().val()):
                    if self.refresh:
                        prev_spend = float(db.child("customer spend").child(customerId).child("paid").get().val())
                        self.prevSpend = prev_spend
                    else:
                        prev_spend = self.prevSpend
                    if not self.new_created:
                        new_spend = prev_spend + self.amount.value()
                    else:
                        new_spend = self.amount.value()
                    db.child("customer spend").child(customerId).child("paid").set(new_spend)
                    #self.new_created = False
                else:
                    new_spend = self.amount.value()
                    self.prevSpend = new_spend
                    db.child("customer spend").child(customerId).child("paid").set(new_spend)
                    self.new_created = True

                if "customer spend" in list(db.shallow().get().val()) and customerId in list(
                        db.child("customer spend").shallow().get().val()) and "spent amount" in list(
                    db.child("customer spend").child(customerId).shallow().get().val()):
                    if self.refresh:
                        prev_spend = float(db.child("customer spend").child(customerId).child("spent amount").get().val())
                        self.saved_data3 = prev_spend
                    else:
                        prev_spend = self.saved_data3
                    if not self.new_created3:
                        new_spend = prev_spend - float(data['discount'])
                    else:
                        new_spend =  -1 * self.discount
                    db.child("customer spend").child(customerId).child("spent amount").set(new_spend)
                    # self.new_created3 = False
                else:
                    new_spend = -1 * float(data['discount'])
                    self.saved_data3 = new_spend
                    db.child("customer spend").child(customerId).child("spent amount").set(new_spend)
                    self.new_created3 = True

                try:
                    recipientNumber = self.df[self.df["company name"] == self.customer.currentText()]["number"]
                    recipientNumber = list(recipientNumber)
                    recipientNumber = recipientNumber[0]

                    bill = '{:.2f}'.format(self.amount.value())
                    smsText = f'Dear Customer, Your payment of taka {bill} is successfull.'
                    client.service.OneToOne(userName, password, recipientNumber, smsText, smsType, maskName,
                                            campaignName)
                except Exception as e:
                    print(e)
                self.refresh = False
                self.saved = True
            except Exception as e:
                print(e)
                self.dialog.message_text.setText("Error saving data")
                self.dialog.displayInfo()
                self.saved = False
        else:
            self.dialog.message_text.setText("Please fill up all the required fields")
            self.dialog.displayInfo()
            self.saved = False

    def show_me(self):
        self.clear_n_new()
        self.show()

    def clear_n_new(self):
        try:
            dat = db.child('customer').get().val()
            self.df = pd.DataFrame(dat, columns=dat.keys())
            self.df = self.df.transpose()
            _data__ = list(self.df["company name"])
            self.customer.clear()
            for x in range(len(_data__)):
                self.customer.addItem(_data__[x])
        except Exception as e:
            self.df = pd.DataFrame()
            self.dialog.message_text.setText("Can not load data. Check internet connection")
            self.dialog.displayInfo()
        try:
            data_0 = db.child('money received').shallow().get()
            data_0 = list(data_0.val())
            for x in range(len(data_0)):
                data_0[x] = int(data_0[x])
            new_id0 = max(data_0) + 1
            out_data0 = str(new_id0)
            self.id.setText(out_data0)
        except Exception as e:
            self.id.setText(f'{invoice_id_start}')
            self.dialog.message_text.setText("failed to fetch data or no records found")
            self.dialog.displayInfo()
        self.received_date.setDateTime(QtCore.QDateTime.currentDateTime())
        type = ['Bkash', 'Cash', 'Bank Transfer']
        self.type.clear()
        for x in range(len(type)):
            self.type.addItem(type[x])
        self.remarks.setText("")
        self.order_number.setText("")
        self.amount.setValue(0)
        self.discount.setValue(0)
        self.refresh = True
        self.prevSpend = 0.0
        self.new_created = False

class OpeningBalanceUI(QMainWindow, opening_balance_ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(OpeningBalanceUI, self).__init__(parent)
        self.setupUi(self)
        self.dialog = Dialog()
        self.save_btn.clicked.connect(self.save)
        self.save_btn.setEnabled(False)
        self.save_btn.hide()
        self.save_n_new_btn.clicked.connect(self.save_n_new)
        self.save_n_exit_btn.clicked.connect(self.save_n_exit)
        self.df = pd.DataFrame()
        self.select_product_combo.currentTextChanged.connect(self.set_value)

    def save_n_new(self):
        self.save_n_new_btn.setEnabled(False)
        self.save_n_exit_btn.setEnabled(False)
        QTimer.singleShot(500, lambda: self.call_after_dis())

    def call_after_dis(self):
        self.save()
        self.save_n_new_btn.setEnabled(True)
        self.save_n_exit_btn.setEnabled(True)
        self.set_value()

    def save_n_exit(self):
        self.save_n_new_btn.setEnabled(False)
        self.save_n_exit_btn.setEnabled(False)
        QTimer.singleShot(500, lambda: self.call_after_dis2())

    def call_after_dis2(self):
        self.save()
        self.save_n_new_btn.setEnabled(True)
        self.save_n_exit_btn.setEnabled(True)
        self.close()

    def save(self):
        stock = self.lot_amount_spin.value()
        try:
            id_ = self.df[self.df["company name"] == self.select_product_combo.currentText()]["customer id"]
            id_ = list(id_)
            id_ = id_[0]
            db.child('customer').child(id_).child('opening balance').set(stock)
        except Exception as e:
            self.dialog.message_text.setText("No internet")
            self.dialog.displayInfo()
            print(e)
        self.clear_n_new()

    def show_me(self):
        self.clear_n_new()
        self.show()

    def set_value(self):
        try:
            if len(list(self.df[self.df["company name"] == self.select_product_combo.currentText()]["opening balance"])):
                stock = self.df[self.df["company name"] == self.select_product_combo.currentText()]["opening balance"]
                stock = list(stock)
                stock = stock[0]
                self.lot_amount_spin.setValue(stock)
        except Exception as e:
            self.dialog.message_text.setText("No internet")
            self.dialog.displayInfo()
            print(e)

    def clear_n_new(self):
        self.clear()
        try:
            self.dat = db.child('customer').get().val()
            self.df = pd.DataFrame(self.dat, columns=self.dat.keys())
            self.df = self.df.transpose()
        except Exception as e:
            self.df = pd.DataFrame()
            self.dialog.message_text.setText("Can not load data. Check internet connection")
            self.dialog.displayInfo()
        cols = list(self.df['company name'].values)
        for x in range(len(cols)):
            self.select_product_combo.addItem(cols[x])
        self.set_value()

    def clear(self):
        self.select_product_combo.setCurrentIndex(0)
        self.lot_amount_spin.setValue(0)

class OpeningAmountUI(QMainWindow, opening_amount_ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(OpeningAmountUI, self).__init__(parent)
        self.setupUi(self)
        self.dialog = Dialog()
        self.save_btn.clicked.connect(self.save)
        self.save_btn.setEnabled(False)
        self.save_btn.hide()
        self.save_n_new_btn.clicked.connect(self.save_n_new)
        self.save_n_exit_btn.clicked.connect(self.save_n_exit)
        self.df = pd.DataFrame()
        self.select_product_combo.currentTextChanged.connect(self.set_value)

    def save_n_new(self):
        self.save_n_new_btn.setEnabled(False)
        self.save_n_exit_btn.setEnabled(False)
        QTimer.singleShot(500, lambda: self.call_after_dis())

    def call_after_dis(self):
        self.save()
        self.save_n_new_btn.setEnabled(True)
        self.save_n_exit_btn.setEnabled(True)
        self.set_value()

    def save_n_exit(self):
        self.save_n_new_btn.setEnabled(False)
        self.save_n_exit_btn.setEnabled(False)
        QTimer.singleShot(500, lambda: self.call_after_dis2())

    def call_after_dis2(self):
        self.save()
        self.save_n_new_btn.setEnabled(True)
        self.save_n_exit_btn.setEnabled(True)
        self.close()

    def save(self):
        stock = self.lot_amount_spin.value()
        try:
            id_ = self.df[self.df["name"] == self.select_product_combo.currentText()]["id"]
            id_ = list(id_)
            id_ = id_[0]
            db.child('product').child(id_).child('stock').set(stock)
        except Exception as e:
            self.dialog.message_text.setText("No internet")
            self.dialog.displayInfo()
            print(e)
        self.clear_n_new()

    def show_me(self):
        self.clear_n_new()
        self.show()

    def set_value(self):
        try:
            if len(list(self.df[self.df["name"] == self.select_product_combo.currentText()]["stock"])):
                stock = self.df[self.df["name"] == self.select_product_combo.currentText()]["stock"]
                stock = list(stock)
                stock = stock[0]
                self.lot_amount_spin.setValue(stock)
        except Exception as e:
            self.dialog.message_text.setText("No internet")
            self.dialog.displayInfo()
            print(e)

    def clear_n_new(self):
        self.clear()
        try:
            self.dat = db.child('product').get().val()
            self.df = pd.DataFrame(self.dat, columns=self.dat.keys())
            self.df = self.df.transpose()
        except Exception as e:
            self.df = pd.DataFrame()
            self.dialog.message_text.setText("Can not load data. Check internet connection")
            self.dialog.displayInfo()
        cols = list(self.df['name'].values)
        self.select_product_combo.clear()
        for x in range(len(cols)):
            self.select_product_combo.addItem(cols[x])
        self.set_value()

    def clear(self):
        self.select_product_combo.setCurrentIndex(0)
        self.lot_amount_spin.setValue(0)

class AddCustomerUI(QMainWindow, add_customer.Ui_MainWindow):
    def __init__(self, parent=None):
        super(AddCustomerUI, self).__init__(parent)
        self.setupUi(self)
        self.dialog = Dialog()
        self.save_n_exit_btn.clicked.connect(self.save_n_exit)
        self.save_n_new_btn.clicked.connect(self.save_n_new)
        self.save_btn.clicked.connect(self.save)
        self.save_btn.setEnabled(False)
        self.save_btn.hide()

    def save(self):
        customer_id = self.customer_id_line_edit.text()
        company_name = self.company_name_line_edit.text()
        contact_person = self.contact_person_line_edit.text()
        address = self.address_text_edit.toPlainText()
        zone = self.zone_combo.currentText()
        email = self.email_line_edit.text()
        number = self.number_line_edit.text()
        opening_balance = self.opening_balance_spin.value()
        if customer_id != '' and company_name != '' and contact_person != '' and address != '' and zone != '' and email != '' and number != '':
            try:
                data = {
                    'customer id': customer_id,
                    'company name': company_name,
                    'contact person': contact_person,
                    'address': address,
                    'zone': zone,
                    'email': email,
                    'number': number,
                    'opening balance': opening_balance
                }
                db.child('customer').child(customer_id).set(data)
                self.dialog.message_text.setText("Data saved successfully")
                self.dialog.displayInfo()
            except:
                self.dialog.message_text.setText("Error saving data")
                self.dialog.displayInfo()
        else:
            self.dialog.message_text.setText("Please fill up the empty fields")
            self.dialog.displayInfo()

    def save_n_exit(self):
        customer_id = self.customer_id_line_edit.text()
        company_name = self.company_name_line_edit.text()
        contact_person = self.contact_person_line_edit.text()
        address = self.address_text_edit.toPlainText()
        zone = self.zone_combo.currentText()
        email = self.email_line_edit.text()
        number = self.number_line_edit.text()
        opening_balance = self.opening_balance_spin.value()
        if customer_id != '' and company_name != '' and contact_person != '' and address != '' and zone != '' and email != '' and number != '':
            try:
                data = {
                    'customer id': customer_id,
                    'company name': company_name,
                    'contact person': contact_person,
                    'address': address,
                    'zone': zone,
                    'email': email,
                    'number': number,
                    'opening balance': opening_balance
                }
                db.child('customer').child(customer_id).set(data)
                self.close()
            except:
                self.dialog.message_text.setText("Error saving data")
                self.dialog.displayInfo()
        else:
            self.dialog.message_text.setText("Please fill up the empty fields")
            self.dialog.displayInfo()

    def save_n_new(self):
        customer_id = self.customer_id_line_edit.text()
        company_name = self.company_name_line_edit.text()
        contact_person = self.contact_person_line_edit.text()
        address = self.address_text_edit.toPlainText()
        zone = self.zone_combo.currentText()
        email = self.email_line_edit.text()
        number = self.number_line_edit.text()
        opening_balance = self.opening_balance_spin.value()
        if customer_id != '' and company_name != '' and contact_person != '' and address != '' and zone != '' and email != '' and number != '':
            try:
                data = {
                    'customer id': customer_id,
                    'company name': company_name,
                    'contact person': contact_person,
                    'address': address,
                    'zone': zone,
                    'email': email,
                    'number': number,
                    'opening balance': opening_balance
                }
                db.child('customer').child(customer_id).set(data)
                self.clear_n_new()
            except:
                self.dialog.message_text.setText("Error saving data")
                self.dialog.displayInfo()
        else:
            self.dialog.message_text.setText("Please fill up the empty fields")
            self.dialog.displayInfo()

    def show_me(self):
        self.clear_n_new()
        self.show()

    def clear_n_new(self):
        self.customer_id_line_edit.setText("")
        self.company_name_line_edit.setText("")
        self.contact_person_line_edit.setText("")
        self.address_text_edit.setText("")
        self.zone_combo.clear()
        self.zone_combo.setCurrentIndex(0)
        self.email_line_edit.setText("")
        self.number_line_edit.setText("")
        self.opening_balance_spin.setValue(0)
        try:
            data_ = db.child('zone').shallow().get()
            data_ = list(data_.val())
            for x in range(len(data_)):
                self.zone_combo.addItem(data_[x])
            data_ = db.child('customer').shallow().get()
            data_ = list(data_.val())
            for x in range(len(data_)):
                data_[x] = int(data_[x])
            new_id = max(data_)+1
            out_data = str(new_id)
            self.customer_id_line_edit.setText(out_data)
        except:
            self.customer_id_line_edit.setText(f'{customer_id_start}')
            self.dialog.message_text.setText("failed to fetch data from database or no records in database")
            self.dialog.displayInfo()

class UpdateCustomerUI(QMainWindow, update_customer_ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(UpdateCustomerUI, self).__init__(parent)
        self.setupUi(self)
        self.dialog = Dialog()
        self.save_n_exit_btn.clicked.connect(self.save_n_exit)
        self.save_n_new_btn.clicked.connect(self.save_n_new)
        self.save_btn.clicked.connect(self.save)
        self.save_btn.setEnabled(False)
        self.save_btn.hide()
        self.search_btn.clicked.connect(self.search_func)
        self.edit_btn.clicked.connect(self.edit)

    def save(self):
        customer_id = self.id.currentText()
        company_name = self.company_name_line_edit.text()
        contact_person = self.contact_person_line_edit.text()
        address = self.address_text_edit.toPlainText()
        zone = self.zone_combo.currentText()
        email = self.email_line_edit.text()
        number = self.number_line_edit.text()
        opening_balance = self.opening_balance_spin.value()
        if customer_id != '' and company_name != '' and contact_person != '' and address != '' and zone != '' and email != '' and number != '':
            try:
                data = {
                    'customer id': customer_id,
                    'company name': company_name,
                    'contact person': contact_person,
                    'address': address,
                    'zone': zone,
                    'email': email,
                    'number': number,
                    'opening balance': opening_balance
                }
                db.child('customer').child(customer_id).set(data)
                self.dialog.message_text.setText("Data saved successfully")
                self.dialog.displayInfo()
            except:
                self.dialog.message_text.setText("Error saving data")
                self.dialog.displayInfo()
        else:
            self.dialog.message_text.setText("Please fill up the empty fields")
            self.dialog.displayInfo()

    def save_n_exit(self):
        customer_id = self.id.currentText()
        company_name = self.company_name_line_edit.text()
        contact_person = self.contact_person_line_edit.text()
        address = self.address_text_edit.toPlainText()
        zone = self.zone_combo.currentText()
        email = self.email_line_edit.text()
        number = self.number_line_edit.text()
        opening_balance = self.opening_balance_spin.value()
        if customer_id != '' and company_name != '' and contact_person != '' and address != '' and zone != '' and email != '' and number != '':
            try:
                data = {
                    'customer id': customer_id,
                    'company name': company_name,
                    'contact person': contact_person,
                    'address': address,
                    'zone': zone,
                    'email': email,
                    'number': number,
                    'opening balance': opening_balance
                }
                db.child('customer').child(customer_id).set(data)
                self.close()
            except:
                self.dialog.message_text.setText("Error saving data")
                self.dialog.displayInfo()
        else:
            self.dialog.message_text.setText("Please fill up the empty fields")
            self.dialog.displayInfo()

    def save_n_new(self):
        customer_id = self.id.currentText()
        company_name = self.company_name_line_edit.text()
        contact_person = self.contact_person_line_edit.text()
        address = self.address_text_edit.toPlainText()
        zone = self.zone_combo.currentText()
        email = self.email_line_edit.text()
        number = self.number_line_edit.text()
        opening_balance = self.opening_balance_spin.value()
        if customer_id != '' and company_name != '' and contact_person != '' and address != '' and zone != '' and email != '' and number != '':
            try:
                data = {
                    'customer id': customer_id,
                    'company name': company_name,
                    'contact person': contact_person,
                    'address': address,
                    'zone': zone,
                    'email': email,
                    'number': number,
                    'opening balance': opening_balance
                }
                db.child('customer').child(customer_id).set(data)
                self.clear_n_new()
            except:
                self.dialog.message_text.setText("Error saving data")
                self.dialog.displayInfo()
        else:
            self.dialog.message_text.setText("Please fill up the empty fields")
            self.dialog.displayInfo()

    def show_me(self):
        self.clear_n_new()
        self.show()

    def clear_n_new(self):
        self.search.setText("")
        self.company_name_line_edit.setText("")
        self.contact_person_line_edit.setText("")
        self.address_text_edit.setText("")
        self.zone_combo.clear()
        self.zone_combo.setCurrentIndex(0)
        self.email_line_edit.setText("")
        self.number_line_edit.setText("")
        self.opening_balance_spin.setValue(0)
        try:
            data_ = db.child('zone').shallow().get()
            data_ = list(data_.val())
            for x in range(len(data_)):
                self.zone_combo.addItem(data_[x])
            data_ = db.child('customer').shallow().get()
            data_ = list(data_.val())
            self.id.clear()
            for x in range(len(data_)):
                self.id.addItem(data_[x])
            self.set_value()
        except:
            self.customer_id_line_edit.setText(f'{customer_id_start}')
            self.dialog.message_text.setText("failed to fetch data from database or no records in database")
            self.dialog.displayInfo()

    def search_func(self):
        data_0 = db.child('customer').shallow().get()
        data_0 = list(data_0.val())
        if self.search.text() != '' and self.search.text() in data_0:
            self.id.setCurrentText(self.search.text())
            self.edit()
        else:
            self.dialog.message_text.setText("No matching query found")
            self.dialog.displayInfo()

    def edit(self):
        self.set_value()

    def set_value(self):
        try:
            customer = db.child('customer').child(self.id.currentText()).get().val()
            self.company_name_line_edit.setText(customer['company name'])
            self.contact_person_line_edit.setText(customer['contact person'])
            self.address_text_edit.setText(customer['address'])
            self.zone_combo.setCurrentText(customer['zone'])
            self.email_line_edit.setText(customer['email'])
            self.number_line_edit.setText(customer['number'])
            self.opening_balance_spin.setValue(float(customer['opening balance']))
        except Exception as e:
            self.dialog.message_text.setText("failed to fetch data or some field value is missing")
            self.dialog.displayInfo()

class UpdateMoneyReceivedUI(QMainWindow, update_money_received_ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(UpdateMoneyReceivedUI, self).__init__(parent)
        self.setupUi(self)
        self.df = pd.DataFrame()
        self.dialog = Dialog()
        self.save_btn.clicked.connect(self.save)
        self.save_btn.setEnabled(False)
        self.save_btn.hide()
        self.save_n_new_btn.clicked.connect(self.save_n_new)
        self.save_n_exit_btn.clicked.connect(self.save_n_exit)
        self.saved = False
        self.search_btn.clicked.connect(self.search_func)
        self.edit_btn.clicked.connect(self.edit)
        self.customer.currentTextChanged.connect(self.customer_changed)
        self.prev_am = 0.0
        self.prevSpend = 0.0
        self.refresh = True
        self.new_created = False
        self.prev_discount = 0.0

    def customer_changed(self):
        self.new_created = False

    def save_n_new(self):
        self.save_n_new_btn.setEnabled(False)
        self.save_n_exit_btn.setEnabled(False)
        QTimer.singleShot(500, lambda: self.call_after_dis())

    def call_after_dis(self):
        self.save()
        self.save_n_new_btn.setEnabled(True)
        self.save_n_exit_btn.setEnabled(True)
        if self.saved:
            self.clear_n_new()

    def save_n_exit(self):
        self.save_n_new_btn.setEnabled(False)
        self.save_n_exit_btn.setEnabled(False)
        QTimer.singleShot(500, lambda: self.call_after_dis2())

    def call_after_dis2(self):
        self.save_n_new_btn.setEnabled(False)
        self.save_n_exit_btn.setEnabled(False)
        self.save()
        self.save_n_new_btn.setEnabled(True)
        self.save_n_exit_btn.setEnabled(True)
        if self.saved:
            self.close()

    def save(self):
        id = self.id.currentText()
        data = {
            'id': id,
            'customer': self.customer.currentText(),
            'order number': self.order_number.text(),
            'received date': str(self.received_date.date().toPyDate()),
            'type': self.type.currentText(),
            'amount': self.amount.value(),
            'discount': self.discount.value(),
            'remarks': self.remarks.toPlainText()
        }
        if data['id'] != '' and data['order number'] != '' and data['customer'] != '' and data['received date'] != '' and data['type'] != '' and data['amount'] >= 0:
            try:
                db.child('money received').child(id).set(data)
                customerId = self.df[self.df["company name"] == self.customer.currentText()]["customer id"]
                customerId = list(customerId)
                customerId = customerId[0]
                balance = self.df[self.df["company name"] == self.customer.currentText()]["opening balance"]
                balance = list(balance)
                balance = float(balance[0])
                balance = balance - self.amount.value() + self.prev_am + self.prev_discount - float(data['discount'])
                db.child('customer').child(customerId).child('opening balance').set(balance)

                prev_spend = float(db.child("customer spend").child(customerId).child("paid").get().val())

                new_spend = prev_spend + self.amount.value() - self.prev_am

                db.child("customer spend").child(customerId).child("paid").set(new_spend)

                prev_spend = float(db.child("customer spend").child(customerId).child("spent amount").get().val())

                new_spend = prev_spend + self.prev_discount - float(data['discount'])

                db.child("customer spend").child(customerId).child("spent amount").set(new_spend)

                self.refresh = False
                self.saved = True
            except Exception as e:
                self.dialog.message_text.setText("Error saving data")
                self.dialog.displayInfo()
                self.saved = False
        else:
            self.dialog.message_text.setText("Please fill up all the required fields")
            self.dialog.displayInfo()
            self.saved = False

    def show_me(self):
        self.clear_n_new()
        self.show()

    def clear_n_new(self):
        try:
            dat = db.child('customer').get().val()
            self.df = pd.DataFrame(dat, columns=dat.keys())
            self.df = self.df.transpose()
            _data__ = list(self.df["company name"])
            self.customer.clear()
            for x in range(len(_data__)):
                self.customer.addItem(_data__[x])
        except Exception as e:
            self.df = pd.DataFrame()
            self.dialog.message_text.setText("Can not load data. Check internet connection")
            self.dialog.displayInfo()
        try:
            data_0 = db.child('money received').shallow().get()
            data_0 = list(data_0.val())
            self.id.clear()
            for x in range(len(data_0)):
                self.id.addItem(data_0[x])
        except Exception as e:
            self.dialog.message_text.setText("failed to fetch data or no records found")
            self.dialog.displayInfo()
        self.received_date.setDateTime(QtCore.QDateTime.currentDateTime())
        type = ['Bkash', 'Cash', 'Bank Transfer']
        self.type.clear()
        for x in range(len(type)):
            self.type.addItem(type[x])
        self.remarks.setText("")
        self.order_number.setText("")
        self.amount.setValue(0)
        self.discount.setValue(0)
        self.prevSpend = 0.0
        self.refresh = True
        self.new_created = False
        self.set_value()

    def search_func(self):
        data_0 = db.child('money received').shallow().get()
        data_0 = list(data_0.val())
        if self.search.text() != '' and self.search.text() in data_0:
            self.id.setCurrentText(self.search.text())
            self.edit()
        else:
            self.dialog.message_text.setText("No matching query found")
            self.dialog.displayInfo()

    def edit(self):
        self.set_value()

    def set_value(self):
        try:
            money_rcv = db.child('money received').child(self.id.currentText()).get().val()
            self.remarks.setText(money_rcv['remarks'])
            self.order_number.setText("")
            self.amount.setValue(money_rcv['amount'])
            self.discount.setValue(float(money_rcv['discount']))
            self.type.setCurrentText(money_rcv['type'])
            self.order_number.setText(money_rcv['order number'])
            format_str = '%Y-%m-%d'
            received_date = datetime.datetime.strptime(money_rcv['received date'], format_str)
            self.received_date.setDateTime(received_date)
            self.customer.setCurrentText(money_rcv['customer'])
            self.prev_am = float(money_rcv['amount'])
            self.prev_discount = float(money_rcv['discount'])
        except Exception as e:
            self.dialog.message_text.setText("failed to fetch data or some field value is missing")
            self.dialog.displayInfo()

class AddSupplierUI(QMainWindow, add_supplier.Ui_MainWindow):
    def __init__(self, parent=None):
        super(AddSupplierUI, self).__init__(parent)
        self.setupUi(self)
        self.dialog = Dialog()
        self.save_n_exit_btn.clicked.connect(self.save_n_exit)
        self.save_n_new_btn.clicked.connect(self.save_n_new)
        self.save_btn.clicked.connect(self.save)
        self.save_btn.setEnabled(False)
        self.save_btn.hide()

    def save(self):
        supplier_id = self.supplier_id_line_edit.text()
        supplier_name = self.supplier_name_line_edit.text()
        contact_person = self.contact_person_line_edit.text()
        address = self.address_text_edit.toPlainText()
        email = self.email_line_edit.text()
        number = self.number_line_edit.text()
        if supplier_id != '' and supplier_name != '' and contact_person != '' and address != '' and email != '' and number != '':
            try:
                data = {
                    'supplier id': supplier_id,
                    'supplier name': supplier_name,
                    'contact person': contact_person,
                    'address': address,
                    'email': email,
                    'number': number,
                }
                db.child('supplier').child(supplier_id).set(data)
                self.dialog.message_text.setText("Data saved successfully")
                self.dialog.displayInfo()
            except:
                self.dialog.message_text.setText("Error saving data")
                self.dialog.displayInfo()
        else:
            self.dialog.message_text.setText("Please fill up the empty fields")
            self.dialog.displayInfo()

    def save_n_exit(self):
        supplier_id = self.supplier_id_line_edit.text()
        supplier_name = self.supplier_name_line_edit.text()
        contact_person = self.contact_person_line_edit.text()
        address = self.address_text_edit.toPlainText()
        email = self.email_line_edit.text()
        number = self.number_line_edit.text()
        if supplier_id != '' and supplier_name != '' and contact_person != '' and address != '' and email != '' and number != '':
            try:
                data = {
                    'supplier id': supplier_id,
                    'supplier name': supplier_name,
                    'contact person': contact_person,
                    'address': address,
                    'email': email,
                    'number': number,
                }
                db.child('supplier').child(supplier_id).set(data)
                self.close()
            except:
                self.dialog.message_text.setText("Error saving data")
                self.dialog.displayInfo()
        else:
            self.dialog.message_text.setText("Please fill up the empty fields")
            self.dialog.displayInfo()

    def save_n_new(self):
        supplier_id = self.supplier_id_line_edit.text()
        supplier_name = self.supplier_name_line_edit.text()
        contact_person = self.contact_person_line_edit.text()
        address = self.address_text_edit.toPlainText()
        email = self.email_line_edit.text()
        number = self.number_line_edit.text()
        if supplier_id != '' and supplier_name != '' and contact_person != '' and address != '' and email != '' and number != '':
            try:
                data = {
                    'supplier id': supplier_id,
                    'supplier name': supplier_name,
                    'contact person': contact_person,
                    'address': address,
                    'email': email,
                    'number': number,
                }
                db.child('supplier').child(supplier_id).set(data)
                self.clear_n_new()
            except:
                self.dialog.message_text.setText("Error saving data")
                self.dialog.displayInfo()
        else:
            self.dialog.message_text.setText("Please fill up the empty fields")
            self.dialog.displayInfo()

    def show_me(self):
        self.clear_n_new()
        self.show()

    def clear_n_new(self):
        self.supplier_id_line_edit.setText("")
        self.supplier_name_line_edit.setText("")
        self.contact_person_line_edit.setText("")
        self.address_text_edit.setText("")
        self.email_line_edit.setText("")
        self.number_line_edit.setText("")
        try:
            data_ = db.child('supplier').shallow().get()
            data_ = list(data_.val())
            for x in range(len(data_)):
                data_[x] = int(data_[x])
            new_id = max(data_)+1
            out_data = str(new_id)
            self.supplier_id_line_edit.setText(out_data)
        except:
            self.supplier_id_line_edit.setText(f'{supplier_id_start}')
            self.dialog.message_text.setText("failed to fetch data from database or no records in database")
            self.dialog.displayInfo()

class UpdateSupplierUI(QMainWindow, update_supplier_ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(UpdateSupplierUI, self).__init__(parent)
        self.setupUi(self)
        self.dialog = Dialog()
        self.save_n_exit_btn.clicked.connect(self.save_n_exit)
        self.save_n_new_btn.clicked.connect(self.save_n_new)
        self.save_btn.clicked.connect(self.save)
        self.save_btn.setEnabled(False)
        self.save_btn.hide()
        self.search_btn.clicked.connect(self.search_func)
        self.edit_btn.clicked.connect(self.edit)

    def save(self):
        supplier_id = self.id.currentText()
        supplier_name = self.supplier_name_line_edit.text()
        contact_person = self.contact_person_line_edit.text()
        address = self.address_text_edit.toPlainText()
        email = self.email_line_edit.text()
        number = self.number_line_edit.text()
        if supplier_id != '' and supplier_name != '' and contact_person != '' and address != '' and email != '' and number != '':
            try:
                data = {
                    'supplier id': supplier_id,
                    'supplier name': supplier_name,
                    'contact person': contact_person,
                    'address': address,
                    'email': email,
                    'number': number,
                }
                db.child('supplier').child(supplier_id).set(data)
                self.dialog.message_text.setText("Data saved successfully")
                self.dialog.displayInfo()
            except:
                self.dialog.message_text.setText("Error saving data")
                self.dialog.displayInfo()
        else:
            self.dialog.message_text.setText("Please fill up the empty fields")
            self.dialog.displayInfo()

    def save_n_exit(self):
        supplier_id = self.id.currentText()
        supplier_name = self.supplier_name_line_edit.text()
        contact_person = self.contact_person_line_edit.text()
        address = self.address_text_edit.toPlainText()
        email = self.email_line_edit.text()
        number = self.number_line_edit.text()
        if supplier_id != '' and supplier_name != '' and contact_person != '' and address != '' and email != '' and number != '':
            try:
                data = {
                    'supplier id': supplier_id,
                    'supplier name': supplier_name,
                    'contact person': contact_person,
                    'address': address,
                    'email': email,
                    'number': number,
                }
                db.child('supplier').child(supplier_id).set(data)
                self.close()
            except:
                self.dialog.message_text.setText("Error saving data")
                self.dialog.displayInfo()
        else:
            self.dialog.message_text.setText("Please fill up the empty fields")
            self.dialog.displayInfo()

    def save_n_new(self):
        supplier_id = self.id.currentText()
        supplier_name = self.supplier_name_line_edit.text()
        contact_person = self.contact_person_line_edit.text()
        address = self.address_text_edit.toPlainText()
        email = self.email_line_edit.text()
        number = self.number_line_edit.text()
        if supplier_id != '' and supplier_name != '' and contact_person != '' and address != '' and email != '' and number != '':
            try:
                data = {
                    'supplier id': supplier_id,
                    'supplier name': supplier_name,
                    'contact person': contact_person,
                    'address': address,
                    'email': email,
                    'number': number,
                }
                db.child('supplier').child(supplier_id).set(data)
                self.clear_n_new()
            except:
                self.dialog.message_text.setText("Error saving data")
                self.dialog.displayInfo()
        else:
            self.dialog.message_text.setText("Please fill up the empty fields")
            self.dialog.displayInfo()

    def show_me(self):
        self.clear_n_new()
        self.show()

    def clear_n_new(self):
        self.search.setText("")
        self.supplier_name_line_edit.setText("")
        self.contact_person_line_edit.setText("")
        self.address_text_edit.setText("")
        self.email_line_edit.setText("")
        self.number_line_edit.setText("")
        try:
            data_ = db.child('supplier').shallow().get()
            data_ = list(data_.val())
            self.id.clear()
            for x in range(len(data_)):
                self.id.addItem(data_[x])
            self.set_value()
        except:
            self.dialog.message_text.setText("failed to fetch data from database or no records in database")
            self.dialog.displayInfo()

    def search_func(self):
        data_0 = db.child('supplier').shallow().get()
        data_0 = list(data_0.val())
        if self.search.text() != '' and self.search.text() in data_0:
            self.id.setCurrentText(self.search.text())
            self.edit()
        else:
            self.dialog.message_text.setText("No matching query found")
            self.dialog.displayInfo()

    def edit(self):
        self.set_value()

    def set_value(self):
        try:
            supplier = db.child('supplier').child(self.id.currentText()).get().val()
            self.supplier_name_line_edit.setText(supplier['supplier name'])
            self.contact_person_line_edit.setText(supplier['contact person'])
            self.address_text_edit.setText(supplier['address'])
            self.email_line_edit.setText(supplier['email'])
            self.number_line_edit.setText(supplier['number'])
        except Exception as e:
            self.dialog.message_text.setText("failed to fetch data or some field value is missing")
            self.dialog.displayInfo()

class AddZoneUI(QMainWindow, add_zone.Ui_MainWindow):
    def __init__(self, parent=None):
        super(AddZoneUI, self).__init__(parent)
        self.setupUi(self)
        self.dialog = Dialog()
        self.save_n_exit_btn.clicked.connect(self.save_n_exit)
        self.save_n_new_btn.clicked.connect(self.save_n_new)

    def save_n_exit(self):
        zone = self.zone_line_edit.text()
        if zone != '':
            try:
                data = {'zone': zone}
                db.child('zone').child(zone).set(data)
                self.close()
            except:
                self.dialog.message_text.setText("Error saving data")
                self.dialog.displayInfo()
        else:
            self.dialog.message_text.setText("Please fill up the empty field")
            self.dialog.displayInfo()

    def save_n_new(self):
        zone = self.zone_line_edit.text()
        if zone != '':
            try:
                data = {'zone': zone}
                db.child('zone').child(zone).set(data)
                self.zone_line_edit.setText("")
            except:
                self.dialog.message_text.setText("Error saving data")
                self.dialog.displayInfo()
        else:
            self.dialog.message_text.setText("Please fill up the empty field")
            self.dialog.displayInfo()

    def show_me(self):
        self.clear_n_new()
        self.show()

    def clear_n_new(self):
        self.zone_line_edit.setText("")

class AddExpenseTypeUI(QMainWindow, add_expense_type_ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(AddExpenseTypeUI, self).__init__(parent)
        self.setupUi(self)
        self.dialog = Dialog()
        self.save_n_exit_btn.clicked.connect(self.save_n_exit)
        self.save_n_new_btn.clicked.connect(self.save_n_new)

    def save_n_exit(self):
        e_type = self.expense_type.text()
        if e_type != '':
            try:
                data = {'expense type': e_type}
                db.child('expense type').child(e_type).set(data)
                self.close()
            except:
                self.dialog.message_text.setText("Error saving data")
                self.dialog.displayInfo()
        else:
            self.dialog.message_text.setText("Please fill up the empty field")
            self.dialog.displayInfo()

    def save_n_new(self):
        e_type = self.expense_type.text()
        if e_type != '':
            try:
                data = {'expense type': e_type}
                db.child('expense type').child(e_type).set(data)
                self.expense_type.setText("")
            except:
                self.dialog.message_text.setText("Error saving data")
                self.dialog.displayInfo()
        else:
            self.dialog.message_text.setText("Please fill up the empty field")
            self.dialog.displayInfo()

    def show_me(self):
        self.clear_n_new()
        self.show()

    def clear_n_new(self):
        self.expense_type.setText("")

class ProductLibraryUIClass(QMainWindow, library_add_product.Ui_MainWindow):
    def __init__(self, parent=None):
        super(ProductLibraryUIClass, self).__init__(parent)
        self.setupUi(self)
        self.dialog = Dialog()
        self.save_btn.clicked.connect(self.save_product)
        self.save_btn.setEnabled(False)
        self.save_btn.hide()
        self.save_n_new_btn.clicked.connect(self.save_n_new)
        self.save_n_exit_btn.clicked.connect(self.save_n_exit)

    def save_product(self):
        product_id = self.product_id.text()
        product_name = self.product_name.text()
        unit_price = self.unit_price.value()
        if product_name != '' and unit_price != 0:
            data = {'id': product_id, 'name': product_name, 'price': unit_price, 'stock': 0}
            try:
                db.child('product').child(product_id).set(data)
                self.dialog.message_text.setText("successfully saved data")
                self.dialog.displayInfo()
            except Exception as e:
                self.dialog.message_text.setText("error saving data")
                self.dialog.displayInfo()
        else:
            self.dialog.message_text.setText("please fill up the empty fields")
            self.dialog.displayInfo()

    def save_n_new(self):
        product_id = self.product_id.text()
        product_name = self.product_name.text()
        unit_price = self.unit_price.value()
        if product_name != '' and unit_price != 0:
            data = {'id': product_id, 'name': product_name, 'price': unit_price, 'stock': 0}
            try:
                db.child('product').child(product_id).set(data)
                self.clear_n_new()
            except Exception as e:
                self.dialog.message_text.setText("error saving data")
                self.dialog.displayInfo()
        else:
            self.dialog.message_text.setText("please fill up the empty fields")
            self.dialog.displayInfo()

    def save_n_exit(self):
        product_id = self.product_id.text()
        product_name = self.product_name.text()
        unit_price = self.unit_price.value()
        if product_name != '' and unit_price != 0:
            data = {'id': product_id, 'name': product_name, 'price': unit_price, 'stock': 0}
            try:
                db.child('product').child(product_id).set(data)
                self.close()
            except Exception as e:
                self.dialog.message_text.setText("error saving data")
                self.dialog.displayInfo()
        else:
            self.dialog.message_text.setText("please fill up the empty fields")
            self.dialog.displayInfo()

    def show_me(self):
        self.clear_n_new()
        self.show()

    def clear_n_new(self):
        self.product_id.setText("")
        self.product_name.setText("")
        self.unit_price.setValue(0)
        try:
            data_ = db.child('product').shallow().get()
            data_ = list(data_.val())
            for x in range(len(data_)):
                data_[x] = int(data_[x])
            new_id = max(data_)+1
            out_data = str(new_id)
            self.product_id.setText(out_data)
        except:
            self.product_id.setText(f'{product_id_starting_number}')
            self.dialog.message_text.setText("failed to fetch data or no records found")
            self.dialog.displayInfo()

class UpdateProductUI(QMainWindow, update_product_ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(UpdateProductUI, self).__init__(parent)
        self.setupUi(self)
        self.dialog = Dialog()
        self.save_btn.clicked.connect(self.save_product)
        self.save_btn.setEnabled(False)
        self.save_btn.hide()
        self.save_n_new_btn.clicked.connect(self.save_n_new)
        self.save_n_exit_btn.clicked.connect(self.save_n_exit)
        self.search_btn.clicked.connect(self.search_func)
        self.edit_btn.clicked.connect(self.edit)

    def save_product(self):
        product_id = self.id.currentText()
        product_name = self.product_name.text()
        unit_price = self.unit_price.value()
        stock = self.stock.value()
        if product_name != '' and unit_price != 0:
            data = {'id': product_id, 'name': product_name, 'price': unit_price, 'stock': stock}
            try:
                db.child('product').child(product_id).set(data)
                self.dialog.message_text.setText("successfully saved data")
                self.dialog.displayInfo()
            except Exception as e:
                self.dialog.message_text.setText("error saving data")
                self.dialog.displayInfo()
        else:
            self.dialog.message_text.setText("please fill up the empty fields")
            self.dialog.displayInfo()

    def save_n_new(self):
        product_id = self.id.currentText()
        product_name = self.product_name.text()
        unit_price = self.unit_price.value()
        stock = self.stock.value()
        if product_name != '' and unit_price != 0:
            data = {'id': product_id, 'name': product_name, 'price': unit_price, 'stock': stock}
            try:
                db.child('product').child(product_id).set(data)
                self.clear_n_new()
            except Exception as e:
                self.dialog.message_text.setText("error saving data")
                self.dialog.displayInfo()
        else:
            self.dialog.message_text.setText("please fill up the empty fields")
            self.dialog.displayInfo()

    def save_n_exit(self):
        product_id = self.id.currentText()
        product_name = self.product_name.text()
        unit_price = self.unit_price.value()
        stock = self.stock.value()
        if product_name != '' and unit_price != 0:
            data = {'id': product_id, 'name': product_name, 'price': unit_price, 'stock': stock}
            try:
                db.child('product').child(product_id).set(data)
                self.close()
            except Exception as e:
                self.dialog.message_text.setText("error saving data")
                self.dialog.displayInfo()
        else:
            self.dialog.message_text.setText("please fill up the empty fields")
            self.dialog.displayInfo()

    def show_me(self):
        self.clear_n_new()
        self.show()

    def clear_n_new(self):
        self.product_name.setText("")
        self.search.setText("")
        self.unit_price.setValue(0)
        try:
            data_ = db.child('product').shallow().get()
            data_ = list(data_.val())
            self.id.clear()
            for x in range(len(data_)):
                self.id.addItem(data_[x])
            self.set_value()
        except:
            self.dialog.message_text.setText("failed to fetch data or no records found")
            self.dialog.displayInfo()

    def search_func(self):
        data_0 = db.child('product').shallow().get()
        data_0 = list(data_0.val())
        if self.search.text() != '' and self.search.text() in data_0:
            self.id.setCurrentText(self.search.text())
            self.edit()
        else:
            self.dialog.message_text.setText("No matching query found")
            self.dialog.displayInfo()

    def edit(self):
        self.set_value()

    def set_value(self):
        try:
            product = db.child('product').child(self.id.currentText()).get().val()
            self.product_name.setText(product['name'])
            self.unit_price.setValue(float(product['price']))
            self.stock.setValue(int(product['stock']))
        except Exception as e:
            self.stock.setValue(0)
            self.dialog.message_text.setText("failed to fetch data or some field value is missing")
            self.dialog.displayInfo()

class SaleEntryUIClass(QMainWindow, entry_sale.Ui_MainWindow):
    def __init__(self, parent=None):
        super(SaleEntryUIClass, self).__init__(parent)
        self.setupUi(self)
        self.dialog = Dialog()
        self.dialog2 = Dialog2()
        self.app = App()
        self.app.signal.connect(self.change_file)
        self.row_count = 1
        self.pre_selected = ''
        self.pre_selected_row = -1
        self.pre_selected_col = -1
        self.df = pd.DataFrame()
        self.df2 = pd.DataFrame()
        #self.save_data = pd.DataFrame(columns = ['Serial No', 'Product ID', 'Product Name', 'Unit Price', 'Quantity', 'Total'])
        #print(self.save_data)
        self.save_data = {}
        self.products_dict = {}
        self.products_dict_final = {}
        self.sub_total_amount = 0.00
        self.paid = 0.00
        self.discount = 0.00
        self.save_location = ''
        self.entry_product_id_combo.currentTextChanged.connect(self.id_changed)
        self.entry_product_name_combo.currentTextChanged.connect(self.name_changed)
        self.entry_customer_id_combo.currentTextChanged.connect(self.customer_changed)
        self.entry_add_btn.clicked.connect(self.add_product)
        self.save_btn.clicked.connect(self.save)
        self.save_btn.setEnabled(False)
        self.save_btn.hide()
        self.tb_row = """"""
        self.save_n_new_btn.clicked.connect(self.save_n_new)
        self.save_n_exit_btn.clicked.connect(self.save_n_exit)
        self.select_location_btn.clicked.connect(self.set_file_location)
        self.print_btn.clicked.connect(self.printDialog)
        self.table_top = """
                <div style="margin-top: 150px;">
                    <table class="table">
                      <thead class="thead-light">
                        <tr>
                          <th scope="col">Serial No</th>
                          <th scope="col">Product Name</th>
                          <th scope="col">Unit Price</th>
                          <th scope="col">Quantity</th>
                          <th scope="col">Total</th>
                        </tr>
                      </thead>
                      <tbody>"""
        self.table_mid = """
                <tr>
                      <th scope="row">$serial</th>
                      <td>$product_name</td>
                      <td>$unit_price</td>
                      <td>$quantity</td>
                      <td>$item_total</td>
                </tr>"""
        self.table_bottom = """      
                      <tr>
                          <th scope="row"></th>
                          <td></td>
                          <td> </td>
                          <td>Total Amount</td>
                          <td>$sub_total</td>
                        </tr>
                      </tbody>
                    </table>
                </div>
                <div>
                    <div style="float: left; width: 400px;">
                        <div style="margin-left: 180px; text-align: left;">
                            <a style="font-size: 15px; font-weight: 500; color: black;">
                                Discount $discount_percent %
                            </a>
                            <br>
                            <a style="font-size: 15px; font-weight: 500; color: black;">
        
                            </a>
                            <br>
                            <a style="font-size: 15px; font-weight: 500; color: black;">
                                Sale Tax rate $tax_percent %
                            </a>
                            <br>
                            <a style="font-size: 15px; font-weight: 500; color: black;">
        
                            </a>
                        </div>
                    </div>
                    <div style="float: right; width: 350px;">
                        <div style="float: left;">
                            <a style="font-size: 15px; font-weight: 500; color: black;">
                                Discount Amount
                            </a>
                            <br>
                            <a style="font-size: 15px; font-weight: 500; color: black;">
                                After Discount
                            </a>
                            <br>
                            <a style="font-size: 15px; font-weight: 500; color: black;">
                                Tax Amount
                            </a>
                            <br>
                            <a style="font-size: 15px; font-weight: 500; color: black;">
                                Net Amount
                            </a>
                            <br>
                        </div>
                        <div style="float: right; margin-right: 20px;">
                            <a style="font-size: 15px; font-weight: 500; color: black;">
                                $discount
                            </a>
                            <br>
                            <a style="font-size: 15px; font-weight: 500; color: black;">
                                $after_discount
                            </a>
                            <br>
                            <a style="font-size: 15px; font-weight: 500; color: black;">
                                $tax_amount
                            </a>
                            <br>
                            <a style="font-size: 15px; font-weight: 500; color: black;">
                                $total
                            </a>
                            <br>
                        </div>
                    </div>
                </div>
                <div style="margin-top: 140px;">
                
                </div>
                <div style="margin-left: 20px;">
                    <a style="font-size: 15px; font-weight: 500; color: black;">
                        In Word: $in_word  taka only
                    </a>
                </div>
                <hr>
                
                <div style="margin-top: 20px;">
                    <div style="float: left; width: 400px;">
                        
                    </div>
                    <div style="float: right; width: 350px;">
                        <div style="float: left;">
                            <a style="font-size: 15px; font-weight: 500; color: black;">
                                Paid
                            </a>
                            <br>
                        </div>
                        <div style="float: right; margin-right: 20px;">
                            <a style="font-size: 15px; font-weight: 500; color: black;">
                                $paid
                            </a>
                            <br>
                        </div>
                    </div>
                </div>
                <br>
                <hr>
                <div style="margin-top: 20px;">
                    <div style="float: left; width: 400px;">
                        
                    </div>
                    <div style="float: right; width: 350px;">
                        <div style="float: left;">
                            <a style="font-size: 15px; font-weight: 500; color: black;">
                                Due
                            </a>
                            <br>
                        </div>
                        <div style="float: right; margin-right: 20px;">
                            <a style="font-size: 15px; font-weight: 500; color: black;">
                                $due
                            </a>
                            <br>
                        </div>
                    </div>
                </div>
                <br>
                <hr>
                <div style="margin-left: 20px;">
                    <a style="font-size: 15px; font-weight: 500; color: black;">
                        Due In Word: $in_word_due  taka only
                    </a>
                </div>
                <br>
                <hr>
                <br>
                """
        self.top = """
        <!doctype html>
        <html>
        <head>
        <meta charset="utf-8">
        <title>Untitled Document</title>
        <link rel="stylesheet" href="$css_link">
        <style>
            .clearfix:after {
              content: "";
              display: table;
              clear: both;
            }
        
            a {
              color: #5D6975;
              #text-decoration: underline;
            }
        
            body {
              position: relative;
              width: 21cm;
              height: 29.7cm;
              margin: 0 auto;
              color: #001028;
              background: #FFFFFF;
              font-family: Arial, sans-serif;
              font-size: 12px;
              font-family: Arial;
            }
        
            header {
              padding: 10px 0;
              margin-bottom: 30px;
            }
        
            #logo {
              text-align: center;
              margin-bottom: 10px;
            }
        
            #logo img {
              width: 200px;
            }
        
            h1 {
              border-top: 1px solid  #5D6975;
              border-bottom: 1px solid  #5D6975;
              color: #5D6975;
              font-size: 2.4em;
              line-height: 1.4em;
              font-weight: normal;
              text-align: center;
              margin: 0 0 20px 0;
              background: url($dimension_png);
            }
        
            #project {
              float: left;
            }
        
            #project span {
              color: #5D6975;
              text-align: right;
              width: 52px;
              margin-right: 10px;
              display: inline-block;
              font-size: 0.8em;
            }
        
            #company {
              float: right;
              text-align: right;
            }
        
            #project div,
            #company div {
              white-space: nowrap;
            }
        
        
        
            #notices .notice {
              color: #5D6975;
              font-size: 1.2em;
            }
        
            footer {
              color: #5D6975;
              width: 100%;
              height: 30px;
              bottom: 0;
              border-top: 1px solid #C1CED9;
              padding: 8px 0;
              text-align: center;
              margin-top: 50px;
            }
        </style>
        </head>
        
        <body>
            <div>
                <div style="margin-top: 50px; margin-bottom: 10px;">
                    <div style="text-align: center;">
        
                        <div style="width: 300px; margin: 0 auto;">
                            <div style="float: left; margin-top: 0px;">
                                <img style="height: 40px; width: 40px;" src="$logo_png">
                            </div>
                            <div>
                                <a style="color: black; font-size: 30px; font-weight: 500;">
                                    Machronics
                                </a>
                            </div>
        
                        </div>
                        <br>
                        <a style="font-size: 15px; font-weight: 500; color: black;">
                            Mirpur Dohs, Mirpur-12,
                        </a>
                        <br>
                        <a style="font-size: 15px; font-weight: 500; color: black;">
                            Dhaka
                        </a>
                        <br>
                        <br>
                        <a style="color: black; font-size: 20px; font-weight: 500;">
                            INVOICE
                        </a>
                    </div>
        
                    <div style="margin-left: 15px; margin-right: 15px;">
                        <div style="text-align: left; float: left;">
                            <a style="font-size: 15px; font-weight: 500; color: black;">
                                Invoice No: $invoice_id
                            </a>
                            <br>
                            <a style="font-size: 15px; font-weight: 500; color: black;">
                                Name: $client
                            </a>
                            <br>
                            <a style="font-size: 15px; font-weight: 500; color: black;">
                                Address: $address
                            </a>
                            <br>
                            <a style="font-size: 15px; font-weight: 500; color: black;">
                                Zone: $zone
                            </a>
                        </div>
                        <div style="text-align: left; float: right;">
                            <a style="font-size: 15px; font-weight: 500; color: black;">
                                Sold By: $sales_by
                            </a>
                            <br>
                            <a style="font-size: 15px; font-weight: 500; color: black;">
                                Order Date: $order_date
                            </a>
                            <br>
                            <a style="font-size: 15px; font-weight: 500; color: black;">
                                Delivery Date: $delivery_date
                            </a>
                            <br>
                            <br>
                            <a style="font-size: 15px; font-weight: 500; color: black;">
                                $due
                            </a>
                        </div>
                    </div>
                </div>"""

        self.bottom = """
              <div style="margin-top: 70px;">
                    <div style="float: left; width: 350px; text-align: center;">
                        <a style="font-size: 15px; font-weight: 500; color: black; text-decoration-line: overline;">
                            Customer's Signature
                        </a>
                    </div>
                    <div style="float: right; width: 350px;">
                        <div style="text-align: center;">
                            <a style="font-size: 15px; font-weight: 500; color: black;  text-decoration-line: overline;">
                                Authorized Signature
                            </a>
                        </div>
                    </div>
                </div>
                <div style="margin-top: 140px;">
                </div>
                <hr>
                <div style="text-align: left;">
                    <a style="font-size: 15px; font-weight: 500; color: black;">
                        N.B: This is a computer generated document and is valid if not signed.
                    </a>
                </div>
            </div>
        
        
            <script src="$js_url"></script>
        </body>
        </html>
        """
        self.refresh = True
        self.saved_data1 = []
        self.saved_data2 = []
        self.saved_data3 = 0.00
        self.saved_data4 = []
        self.new_created1 = []
        self.new_created2 = []
        self.new_created3 = False
        self.prevSpend = 0.0
        self.new_created = False
        self.page = QtWebEngineWidgets.QWebEnginePage()

    def save_n_new(self):
        self.save_n_new_btn.setEnabled(False)
        self.save_n_exit_btn.setEnabled(False)
        self.print_btn.setEnabled(False)
        QTimer.singleShot(500, lambda: self.call_after_dis())

    def call_after_dis(self):
        cond = self.save()
        self.save_n_new_btn.setEnabled(True)
        self.save_n_exit_btn.setEnabled(True)
        self.print_btn.setEnabled(True)
        if cond:
            self.clear_n_new()

    def save_n_exit(self):
        self.save_n_new_btn.setEnabled(False)
        self.save_n_exit_btn.setEnabled(False)
        self.print_btn.setEnabled(False)
        QTimer.singleShot(500, lambda: self.run_after_dis_2())

    def run_after_dis_2(self):
        cond = self.save()
        self.save_n_new_btn.setEnabled(True)
        self.save_n_exit_btn.setEnabled(True)
        self.print_btn.setEnabled(True)
        if cond:
            self.close()


    def set_file_location(self):
        self.app.initUI()

    def change_file(self, value):
        self.file_location_line_edit.setText(str(value))

    def printDialog(self):
        self.save_n_new_btn.setEnabled(False)
        self.save_n_exit_btn.setEnabled(False)
        self.print_btn.setEnabled(False)
        QTimer.singleShot(500, lambda: self.run_after_dis_3())

    def run_after_dis_3(self):
        keys = []
        for x in self.products_dict.keys():
            if int(self.products_dict[x]['Quantity']) != 0:
                keys.append(x)

        if len(self.new_created1) == len(self.products_dict.keys()) == len(self.new_created2):
            for z in range(len(self.new_created1)):
                if str(z + 1) not in keys:
                    del self.new_created1[z]
                    del self.new_created2[z]

        yy = 1
        self.products_dict_final = {}
        for key in keys:
            self.products_dict_final[f'{yy}'] = self.products_dict[key]
            yy = yy + 1
        self.paid = self.paidSpinBox.value()
        self.discount = self.discountSpinBox.value()
        self.save_data["invoice id"] = self.entry_invoice_id_line_edit.text()
        self.save_data["customer id"] = self.entry_customer_id_combo.currentText()
        self.save_data["address"] = self.entry_address_line_edit.text()
        self.save_data["location"] = self.entry_location_line_edit.text()
        self.save_data["employee name"] = self.entry_employee_name_combo.currentText()
        self.save_data["booking date"] = str(self.booking_date.date().toPyDate())
        self.save_data["delivery date"] = str(self.delivery_date.date().toPyDate())
        self.save_data["products"] = self.products_dict_final
        self.save_data["sub total"] = self.sub_total_amount
        self.save_data["paid"] = self.paid
        self.save_data["discount"] = self.discount
        company_name = self.entry_customer_id_combo.currentText()
        email = self.df2[self.df2["company name"] == self.entry_customer_id_combo.currentText()]["email"]
        email = list(email)
        email = email[0]
        customerId = self.df2[self.df2["company name"] == self.entry_customer_id_combo.currentText()]["customer id"]
        customerId = list(customerId)
        customerId = customerId[0]
        self.save_location = self.file_location_line_edit.text()
        for count, x in enumerate(self.products_dict_final.keys()):
            tb_row = Template(self.table_mid).safe_substitute(
                serial = "{}".format(count+1),
                product_name=self.products_dict_final[x]['Product Name'],
                unit_price=self.products_dict_final[x]['Unit Price'],
                quantity=self.products_dict_final[x]['Quantity'],
                item_total="{:.2f}".format(float(self.products_dict_final[x]['Total']))
            )
            self.tb_row = self.tb_row + tb_row

        bal_b = self.df2[self.df2["company name"] == self.entry_customer_id_combo.currentText()]["opening balance"]
        bal_b = list(bal_b)
        bal_b = float(bal_b[0])
        total_due = bal_b + self.sub_total_amount - self.discount - self.paid
        words = p.number_to_words(int(self.sub_total_amount - self.discount))
        words_due = p.number_to_words(int(self.sub_total_amount - self.discount - self.paid))
        discount_perc = (self.discount/self.sub_total_amount) * 100
        table_bottom = Template(self.table_bottom).safe_substitute(sub_total="{:.2f}".format(self.sub_total_amount),
                                                                   discount_percent = "{:.2f}".format(discount_perc), discount = "{:.2f}".format(self.discount),
                                                                   after_discount="{:.2f}".format(self.sub_total_amount - self.discount),
                                                                   tax_percent="0.0", tax_amount="0.00",
                                                                   total="{:.2f}".format(self.sub_total_amount - self.discount),
                                                                   in_word = words,
                                                                   paid = str(self.paid),
                                                                   due = str(self.sub_total_amount - self.discount - self.paid),
                                                                   in_word_due = words_due)
        top = Template(self.top).safe_substitute(css_link=bootstrap_css_url, logo_png=logo_url, dimension_png=dimension_url,
                                                 invoice_id=self.save_data["invoice id"],
                                                 client=company_name, address=self.save_data["address"],
                                                 zone = self.save_data["location"],
                                                 sales_by = self.save_data["employee name"],
                                                 due="",
                                                 order_date=self.save_data["booking date"],
                                                 delivery_date=self.save_data["delivery date"])
        #due = "{:.2f}".format(total_due),
        bottom = Template(self.bottom).safe_substitute(js_link = bootstrap_js_url)
        html = top + self.table_top + self.tb_row + table_bottom + bottom
        self.save_file(html)
        path = r"{}".format(self.save_location)
        url = bytearray(QUrl.fromLocalFile(path).toEncoded()).decode()
        QDesktopServices.openUrl(QUrl(url))
        QTimer.singleShot(500, lambda: self.save_after_print())


    def save_after_print(self):
        try:
            keys = []
            for x in self.products_dict.keys():
                if int(self.products_dict[x]['Quantity']) != 0:
                    keys.append(x)

            if len(self.new_created1) == len(self.products_dict.keys()) == len(self.new_created2):
                for z in range(len(self.new_created1)):
                    if str(z+1) not in keys:
                        del self.new_created1[z]
                        del self.new_created2[z]

            yy = 1
            self.products_dict_final = {}
            for key in keys:
                self.products_dict_final[f'{yy}'] = self.products_dict[key]
                yy = yy + 1
            self.paid = self.paidSpinBox.value()
            self.discount = self.discountSpinBox.value()
            self.save_data["invoice id"] = self.entry_invoice_id_line_edit.text()
            self.save_data["customer id"] = self.entry_customer_id_combo.currentText()
            self.save_data["address"] = self.entry_address_line_edit.text()
            self.save_data["location"] = self.entry_location_line_edit.text()
            self.save_data["employee name"] = self.entry_employee_name_combo.currentText()
            self.save_data["booking date"] = str(self.booking_date.date().toPyDate())
            self.save_data["delivery date"] = str(self.delivery_date.date().toPyDate())
            self.save_data["products"] = self.products_dict_final
            self.save_data["sub total"] = self.sub_total_amount
            self.save_data["paid"] = self.paid
            self.save_data["discount"] = self.discount
            company_name = self.entry_customer_id_combo.currentText()
            email = self.df2[self.df2["company name"] == self.entry_customer_id_combo.currentText()]["email"]
            email = list(email)
            email = email[0]
            customerId = self.df2[self.df2["company name"] == self.entry_customer_id_combo.currentText()]["customer id"]
            customerId = list(customerId)
            customerId = customerId[0]
            self.save_location = self.file_location_line_edit.text()
            if self.save_location != '' and self.save_data["invoice id"] != '' and self.save_data["customer id"] != '' and self.save_data["address"] != '' and self.save_data["location"] != '' and self.save_data["employee name"] != '' and self.save_data["booking date"] != '' and self.save_data["delivery date"] != '' and self.save_data["products"] != {}:
                try:
                    db.child('invoice').child(self.entry_invoice_id_line_edit.text()).set(self.save_data)
                    today = date.today()
                    day = today.day
                    month = today.month
                    year = str(today.year)
                    year = year[-2:]
                    if month < 10:
                        month = f'0{month}'
                    if day < 10:
                        day = f'0{day}'
                    date_str = f'{day}{month}{year}'
                    zone = self.save_data["location"]
                    if "daily invoice count" in list(db.shallow().get().val()):
                        if date_str in list(db.child('daily invoice count').shallow().get().val()):
                            if zone in list(db.child('daily invoice count').child(date_str).shallow().get().val()):
                                count_from_db = db.child('daily invoice count').child(date_str).child(zone).child(
                                    'count').get().val()
                                count_from_db = int(count_from_db) + 1
                                data = {
                                    'count': count_from_db
                                }
                                db.child('daily invoice count').child(date_str).child(zone).set(data)
                            else:
                                count = 1
                                data = {
                                    'count': count
                                }
                                db.child('daily invoice count').child(date_str).child(zone).set(data)
                        else:
                            count = 1
                            data = {
                                'count': count
                            }
                            db.child('daily invoice count').child(date_str).child(zone).set(data)
                    else:
                        count = 1
                        data = {
                            'count': count
                        }
                        db.child('daily invoice count').child(date_str).child(zone).set(data)
                    i = 0
                    for x in self.products_dict_final.keys():
                        if self.refresh:
                            prev_stock = db.child('product').child(self.products_dict_final[x]['Product ID']).child('stock').get().val()
                            self.saved_data4.append(prev_stock)
                        else:
                            if i < len(self.saved_data4):
                                prev_stock = self.saved_data4[i]
                            else:
                                prev_stock = db.child('product').child(self.products_dict_final[x]['Product ID']).child(
                                    'stock').get().val()
                                self.saved_data4.append(prev_stock)
                        if str(prev_stock) == 'nan':
                            prev_stock = 0
                        else:
                            prev_stock = int(prev_stock)
                        new_stock = prev_stock - int(self.products_dict_final[x]['Quantity'])
                        db.child('product').child(self.products_dict_final[x]['Product ID']).child('stock').set(new_stock)
                        if "product sold" in list(db.shallow().get().val()) and self.products_dict_final[x]['Product ID'] in list(db.child("product sold").shallow().get().val()):
                            if self.refresh:
                                sold_quant = int(db.child("product sold").child(self.products_dict_final[x]['Product ID']).child("sold unit").get().val())
                                sold_amount = float(db.child("product sold").child(self.products_dict_final[x]['Product ID']).child("sold amount").get().val())
                                self.saved_data1.append(sold_quant)
                                self.saved_data2.append(sold_amount)
                                sold_quant = sold_quant + int(self.products_dict_final[x]['Quantity'])
                                sold_amount = sold_amount + float(self.products_dict_final[x]['Total'])
                                self.new_created1.append(False)
                                self.new_created2.append(False)
                            else:
                                if i < len(self.saved_data1):
                                    sold_quant = self.saved_data1[i]
                                    if not self.new_created1[i]:
                                        sold_quant = sold_quant + int(self.products_dict_final[x]['Quantity'])
                                    else:
                                        sold_quant = int(self.products_dict_final[x]['Quantity'])
                                    #self.new_created1[i] = False
                                else:
                                    sold_quant = int(db.child("product sold").child(self.products_dict_final[x]['Product ID']).child("sold unit").get().val())
                                    self.saved_data1.append(sold_quant)
                                    sold_quant = sold_quant + int(self.products_dict_final[x]['Quantity'])
                                    self.new_created1.append(False)

                                if i < len(self.saved_data2):
                                    sold_amount = self.saved_data2[i]
                                    if not self.new_created2[i]:
                                        sold_amount = sold_amount + float(self.products_dict_final[x]['Total'])
                                    else:
                                        sold_amount = float(self.products_dict_final[x]['Total'])
                                    #self.new_created2[i] = False
                                else:
                                    sold_amount = float(db.child("product sold").child(self.products_dict_final[x]['Product ID']).child("sold amount").get().val())
                                    self.saved_data2.append(sold_amount)
                                    sold_amount = sold_amount + float(self.products_dict_final[x]['Total'])
                                    self.new_created2.append(False)

                            db.child("product sold").child(self.products_dict_final[x]['Product ID']).child("sold unit").set(sold_quant)
                            db.child("product sold").child(self.products_dict_final[x]['Product ID']).child("sold amount").set(sold_amount)
                            #db.child("product sold").child(self.products_dict_final[x]['Product ID']).child("stock").set(new_stock)
                        else:
                            product_data = {
                                'sold unit': self.products_dict_final[x]['Quantity'],
                                'sold amount': float(self.products_dict_final[x]['Total'])
                            }
                            self.saved_data1.append(int(self.products_dict_final[x]['Quantity']))
                            self.saved_data2.append(float(self.products_dict_final[x]['Total']))
                            self.new_created1.append(True)
                            self.new_created2.append(True)
                            db.child("product sold").child(self.products_dict_final[x]['Product ID']).set(product_data)
                        i = i + 1
                    c_id = self.df2[self.df2["company name"] == self.entry_customer_id_combo.currentText()][
                        "customer id"]
                    c_id = list(c_id)
                    c_id = c_id[0]

                    if "customer spend" in list(db.shallow().get().val()) and c_id in list(
                            db.child("customer spend").shallow().get().val()) and "paid" in list(
                        db.child("customer spend").child(c_id).shallow().get().val()):
                        if self.refresh:
                            prev_spend = float(db.child("customer spend").child(c_id).child("paid").get().val())
                            self.prevSpend = prev_spend
                        else:
                            prev_spend = self.prevSpend
                        if not self.new_created:
                            new_spend = prev_spend + self.paid
                        else:
                            new_spend = self.paid
                        db.child("customer spend").child(c_id).child("paid").set(new_spend)
                        # self.new_created = False
                    else:
                        new_spend = self.paid
                        self.prevSpend = new_spend
                        db.child("customer spend").child(c_id).child("paid").set(new_spend)
                        self.new_created = True

                    if "customer spend" in list(db.shallow().get().val()) and c_id in list(
                            db.child("customer spend").shallow().get().val()) and "spent amount" in list(db.child("customer spend").child(c_id).shallow().get().val()):
                        if self.refresh:
                            prev_spend = float(db.child("customer spend").child(c_id).child("spent amount").get().val())
                            self.saved_data3 = prev_spend
                        else:
                            prev_spend = self.saved_data3
                        if not self.new_created3:
                            new_spend = prev_spend + self.sub_total_amount - self.discount
                        else:
                            new_spend = self.sub_total_amount - self.discount
                        db.child("customer spend").child(c_id).child("spent amount").set(new_spend)
                        #self.new_created3 = False
                    else:
                        db.child("customer spend").child(c_id).child("spent amount").set(self.sub_total_amount - self.discount)
                        self.saved_data3 = self.sub_total_amount - self.discount
                        self.new_created3 = True

                    bal_b = self.df2[self.df2["company name"] == self.entry_customer_id_combo.currentText()]["opening balance"]
                    bal_b = list(bal_b)
                    bal_b = float(bal_b[0])
                    bal_a = bal_b + float(self.sub_total_amount) - self.discount - self.paid
                    db.child('customer').child(customerId).child('opening balance').set(bal_a)
                    self.refresh = False
                    try:
                        recipientNumber = self.df2[self.df2["company name"] == self.entry_customer_id_combo.currentText()]["number"]
                        recipientNumber = list(recipientNumber)
                        recipientNumber = recipientNumber[0]
                        or_id = self.save_data["invoice id"]
                        d_date = self.save_data["delivery date"]
                        bill = '{:.2f}'.format(self.sub_total_amount - self.discount)
                        now = dt.now()
                        current_time = now.strftime("%H:%M:%S")
                        date_now = dt.today().strftime('%Y-%m-%d')
                        smsText = f'Your Product Invoice no. is {or_id}, dated {date_now} {current_time}, of value Tk {bill}. Thanks for shopping at Machronics'
                        client.service.OneToOne(userName, password, recipientNumber, smsText, smsType, maskName, campaignName)
                        #bill = '{:.2f}'.format(bal_a)
                        #smsText = f'Dear Customer, Your total due is {bill} taka.'
                        #client.service.OneToOne(userName, password, recipientNumber, smsText, smsType, maskName, campaignName)
                    except Exception as e:
                        print(e)
                    self.tb_row = """"""
                    self.dialog.message_text.setText("Data Saved")
                    self.dialog.displayInfo()
                    #self.dialog2.close()
                except Exception as e:
                    print(e)
                    self.dialog.message_text.setText("Error saving data")
                    self.dialog.displayInfo()
                    #self.dialog2.close()
            else:
                self.dialog.message_text.setText("Fill up all the fields")
                self.dialog.displayInfo()
                #self.dialog2.close()
        except Exception as e:
            print(e)
            self.dialog.message_text.setText("No internet")
            self.dialog.displayInfo()

        self.save_n_new_btn.setEnabled(True)
        self.save_n_exit_btn.setEnabled(True)
        self.print_btn.setEnabled(True)
        self.clear_n_new()

    def save_file(self, html):
        try:
            path = os.path.join(file_save_path, 'invoice')
            if not os.path.isdir(path):
                os.mkdir(path)
            path = os.path.join(path, "file.html")
            with open(path, "w") as file:
                file.write(html)
            self.save_location = self.file_location_line_edit.text()
            pdfkit.from_file(path, self.save_location, configuration=config)
        except:
            pass

    def save(self):
        """self.dialog2.message_text.setText("Saving Data")
        self.dialog2.displayInfo()"""
        try:
            keys = []
            for x in self.products_dict.keys():
                if int(self.products_dict[x]['Quantity']) != 0:
                    keys.append(x)

            if len(self.new_created1) == len(self.products_dict.keys()) == len(self.new_created2):
                for z in range(len(self.new_created1)):
                    if str(z+1) not in keys:
                        del self.new_created1[z]
                        del self.new_created2[z]

            yy = 1
            self.products_dict_final = {}
            for key in keys:
                self.products_dict_final[f'{yy}'] = self.products_dict[key]
                yy = yy + 1

            self.discount = self.discountSpinBox.value()
            self.paid = self.paidSpinBox.value()
            self.save_data["invoice id"] = self.entry_invoice_id_line_edit.text()
            self.save_data["customer id"] = self.entry_customer_id_combo.currentText()
            self.save_data["address"] = self.entry_address_line_edit.text()
            self.save_data["location"] = self.entry_location_line_edit.text()
            self.save_data["employee name"] = self.entry_employee_name_combo.currentText()
            self.save_data["booking date"] = str(self.booking_date.date().toPyDate())
            self.save_data["delivery date"] = str(self.delivery_date.date().toPyDate())
            self.save_data["products"] = self.products_dict_final
            self.save_data["sub total"] = self.sub_total_amount
            self.save_data["paid"] = self.paid
            self.save_data["discount"] = self.discount
            company_name = self.entry_customer_id_combo.currentText()
            email = self.df2[self.df2["company name"] == self.entry_customer_id_combo.currentText()]["email"]
            email = list(email)
            email = email[0]
            customerId = self.df2[self.df2["company name"] == self.entry_customer_id_combo.currentText()]["customer id"]
            customerId = list(customerId)
            customerId = customerId[0]
            self.save_location = self.file_location_line_edit.text()
            if self.save_location != '' and self.save_data["invoice id"] != '' and self.save_data["customer id"] != '' and self.save_data["address"] != '' and self.save_data["location"] != '' and self.save_data["employee name"] != '' and self.save_data["booking date"] != '' and self.save_data["delivery date"] != '' and self.save_data["products"] != {}:
                try:
                    db.child('invoice').child(self.entry_invoice_id_line_edit.text()).set(self.save_data)
                    today = date.today()
                    day = today.day
                    month = today.month
                    year = str(today.year)
                    year = year[-2:]
                    if month < 10:
                        month = f'0{month}'
                    if day < 10:
                        day = f'0{day}'
                    date_str = f'{day}{month}{year}'
                    zone = self.save_data["location"]
                    if "daily invoice count" in list(db.shallow().get().val()):
                        if date_str in list(db.child('daily invoice count').shallow().get().val()):
                            if zone in list(db.child('daily invoice count').child(date_str).shallow().get().val()):
                                count_from_db = db.child('daily invoice count').child(date_str).child(zone).child(
                                    'count').get().val()
                                count_from_db = int(count_from_db) + 1
                                data = {
                                    'count': count_from_db
                                }
                                db.child('daily invoice count').child(date_str).child(zone).set(data)
                            else:
                                count = 1
                                data = {
                                    'count': count
                                }
                                db.child('daily invoice count').child(date_str).child(zone).set(data)
                        else:
                            count = 1
                            data = {
                                'count': count
                            }
                            db.child('daily invoice count').child(date_str).child(zone).set(data)
                    else:
                        count = 1
                        data = {
                            'count': count
                        }
                        db.child('daily invoice count').child(date_str).child(zone).set(data)
                    i = 0
                    for count, x in enumerate(self.products_dict_final.keys()):
                        tb_row = Template(self.table_mid).safe_substitute(
                            serial="{}".format(count + 1),
                            product_name=self.products_dict_final[x]['Product Name'],
                            unit_price=self.products_dict_final[x]['Unit Price'],
                            quantity=self.products_dict_final[x]['Quantity'],
                            item_total="{:.2f}".format(float(self.products_dict_final[x]['Total']))
                        )
                        self.tb_row = self.tb_row + tb_row
                        if self.refresh:
                            prev_stock = db.child('product').child(self.products_dict_final[x]['Product ID']).child('stock').get().val()
                            self.saved_data4.append(prev_stock)
                        else:
                            if i < len(self.saved_data4):
                                prev_stock = self.saved_data4[i]
                            else:
                                prev_stock = db.child('product').child(self.products_dict_final[x]['Product ID']).child(
                                    'stock').get().val()
                                self.saved_data4.append(prev_stock)
                        if str(prev_stock) == 'nan':
                            prev_stock = 0
                        else:
                            prev_stock = int(prev_stock)
                        new_stock = prev_stock - int(self.products_dict_final[x]['Quantity'])
                        db.child('product').child(self.products_dict_final[x]['Product ID']).child('stock').set(new_stock)
                        if "product sold" in list(db.shallow().get().val()) and self.products_dict_final[x]['Product ID'] in list(db.child("product sold").shallow().get().val()):
                            if self.refresh:
                                sold_quant = int(db.child("product sold").child(self.products_dict_final[x]['Product ID']).child("sold unit").get().val())
                                sold_amount = float(db.child("product sold").child(self.products_dict_final[x]['Product ID']).child("sold amount").get().val())
                                self.saved_data1.append(sold_quant)
                                self.saved_data2.append(sold_amount)
                                sold_quant = sold_quant + int(self.products_dict_final[x]['Quantity'])
                                sold_amount = sold_amount + float(self.products_dict_final[x]['Total'])
                                self.new_created1.append(False)
                                self.new_created2.append(False)
                            else:
                                if i < len(self.saved_data1):
                                    sold_quant = self.saved_data1[i]
                                    if not self.new_created1[i]:
                                        sold_quant = sold_quant + int(self.products_dict_final[x]['Quantity'])
                                    else:
                                        sold_quant = int(self.products_dict_final[x]['Quantity'])
                                    #self.new_created1[i] = False
                                else:
                                    sold_quant = int(db.child("product sold").child(self.products_dict_final[x]['Product ID']).child("sold unit").get().val())
                                    self.saved_data1.append(sold_quant)
                                    sold_quant = sold_quant + int(self.products_dict_final[x]['Quantity'])
                                    self.new_created1.append(False)

                                if i < len(self.saved_data2):
                                    sold_amount = self.saved_data2[i]
                                    if not self.new_created2[i]:
                                        sold_amount = sold_amount + float(self.products_dict_final[x]['Total'])
                                    else:
                                        sold_amount = float(self.products_dict_final[x]['Total'])
                                    #self.new_created2[i] = False
                                else:
                                    sold_amount = float(db.child("product sold").child(self.products_dict_final[x]['Product ID']).child("sold amount").get().val())
                                    self.saved_data2.append(sold_amount)
                                    sold_amount = sold_amount + float(self.products_dict_final[x]['Total'])
                                    self.new_created2.append(False)

                            db.child("product sold").child(self.products_dict_final[x]['Product ID']).child("sold unit").set(sold_quant)
                            db.child("product sold").child(self.products_dict_final[x]['Product ID']).child("sold amount").set(sold_amount)
                            #db.child("product sold").child(self.products_dict_final[x]['Product ID']).child("stock").set(new_stock)
                        else:
                            product_data = {
                                'sold unit': self.products_dict_final[x]['Quantity'],
                                'sold amount': float(self.products_dict_final[x]['Total'])
                            }
                            self.saved_data1.append(int(self.products_dict_final[x]['Quantity']))
                            self.saved_data2.append(float(self.products_dict_final[x]['Total']))
                            self.new_created1.append(True)
                            self.new_created2.append(True)
                            db.child("product sold").child(self.products_dict_final[x]['Product ID']).set(product_data)
                        i = i + 1
                    c_id = self.df2[self.df2["company name"] == self.entry_customer_id_combo.currentText()][
                        "customer id"]
                    c_id = list(c_id)
                    c_id = c_id[0]

                    if "customer spend" in list(db.shallow().get().val()) and c_id in list(
                            db.child("customer spend").shallow().get().val()) and "paid" in list(
                        db.child("customer spend").child(c_id).shallow().get().val()):
                        if self.refresh:
                            prev_spend = float(db.child("customer spend").child(c_id).child("paid").get().val())
                            self.prevSpend = prev_spend
                        else:
                            prev_spend = self.prevSpend
                        if not self.new_created:
                            new_spend = prev_spend + self.paid
                        else:
                            new_spend = self.paid
                        db.child("customer spend").child(c_id).child("paid").set(new_spend)
                        # self.new_created = False
                    else:
                        new_spend = self.amount.value() + float(data['discount'])
                        self.prevSpend = new_spend
                        db.child("customer spend").child(c_id).child("paid").set(new_spend)
                        self.new_created = True

                    if "customer spend" in list(db.shallow().get().val()) and c_id in list(
                            db.child("customer spend").shallow().get().val()) and "spent amount" in list(db.child("customer spend").child(c_id).shallow().get().val()):
                        if self.refresh:
                            prev_spend = float(db.child("customer spend").child(c_id).child("spent amount").get().val())
                            self.saved_data3 = prev_spend
                        else:
                            prev_spend = self.saved_data3
                        if not self.new_created3:
                            new_spend = prev_spend + self.sub_total_amount - self.discount
                        else:
                            new_spend = self.sub_total_amount - self.discount
                        db.child("customer spend").child(c_id).child("spent amount").set(new_spend)
                        #self.new_created3 = False
                    else:
                        db.child("customer spend").child(c_id).child("spent amount").set(self.sub_total_amount - self.discount)
                        self.saved_data3 = self.sub_total_amount - self.discount
                        self.new_created3 = True

                    bal_b = self.df2[self.df2["company name"] == self.entry_customer_id_combo.currentText()][
                        "opening balance"]
                    bal_b = list(bal_b)
                    bal_b = float(bal_b[0])
                    total_due = bal_b + self.sub_total_amount - self.discount - self.paid
                    words = p.number_to_words(int(self.sub_total_amount - self.discount))
                    words_due = p.number_to_words(int(self.sub_total_amount - self.discount - self.paid))
                    discount_perc = (self.discount / self.sub_total_amount) * 100

                    table_bottom = Template(self.table_bottom).safe_substitute(
                        sub_total="{:.2f}".format(self.sub_total_amount),
                        discount_percent="{:.2f}".format(discount_perc), discount="{:.2f}".format(self.discount),
                        after_discount="{:.2f}".format(self.sub_total_amount - self.discount),
                        tax_percent="0.0", tax_amount="0.00",
                        total="{:.2f}".format(self.sub_total_amount - self.discount),
                        in_word=words,
                        paid=str(self.paid),
                        due=str(self.sub_total_amount - self.discount - self.paid),
                        in_word_due=words_due)
                    top = Template(self.top).safe_substitute(css_link=bootstrap_css_url, logo_png=logo_url, dimension_png=dimension_url,
                                                             invoice_id=self.save_data["invoice id"],
                                                             client=company_name, address=self.save_data["address"],
                                                             zone=self.save_data["location"],
                                                             sales_by=self.save_data["employee name"],
                                                             due="",
                                                             order_date=self.save_data["booking date"],
                                                             delivery_date=self.save_data["delivery date"])
                    #due="{:.2f}".format(total_due),
                    bottom = Template(self.bottom).safe_substitute(js_link=bootstrap_js_url)
                    html = top + self.table_top + self.tb_row + table_bottom + bottom
                    self.save_file(html)
                    bal_a = bal_b + float(self.sub_total_amount) - self.discount - self.paid
                    db.child('customer').child(customerId).child('opening balance').set(bal_a)
                    self.refresh = False
                    try:
                        recipientNumber = self.df2[self.df2["company name"] == self.entry_customer_id_combo.currentText()]["number"]
                        recipientNumber = list(recipientNumber)
                        recipientNumber = recipientNumber[0]
                        or_id = self.save_data["invoice id"]
                        bill = '{:.2f}'.format(self.sub_total_amount - self.discount)
                        now = dt.now()
                        current_time = now.strftime("%H:%M:%S")
                        date_now = dt.today().strftime('%Y-%m-%d')
                        smsText = f'Your Product Invoice no. is {or_id}, dated {date_now} {current_time}, of value Tk {bill}. Thanks for shopping at Machronics'
                        client.service.OneToOne(userName, password, recipientNumber, smsText, smsType, maskName, campaignName)
                        #bill = '{:.2f}'.format(bal_a)
                        #smsText = f'Dear Customer, Your total due is {bill} taka.'
                        #client.service.OneToOne(userName, password, recipientNumber, smsText, smsType, maskName, campaignName)
                    except Exception as e:
                        print(e)
                    self.tb_row = """"""
                    self.dialog.message_text.setText("Data Saved")
                    self.dialog.displayInfo()
                    #self.dialog2.close()
                    return True
                except Exception as e:
                    print(e)
                    self.dialog.message_text.setText("Error saving data")
                    self.dialog.displayInfo()
                    #self.dialog2.close()
                    return False
            else:
                self.dialog.message_text.setText("Fill up all the fields")
                self.dialog.displayInfo()
                #self.dialog2.close()
                return False
        except Exception as e:
            print(e)
            self.dialog.message_text.setText("No internet")
            self.dialog.displayInfo()
            return False

    def customer_changed(self):
        self.new_created3 = False
        try:
            if len(list(self.df2[self.df2["company name"]==self.entry_customer_id_combo.currentText()]["address"]))!=0:
                addr = self.df2[self.df2["company name"]==self.entry_customer_id_combo.currentText()]["address"]
                addr = list(addr)
                addr = addr[0]
                self.entry_address_line_edit.setText(addr)
                zone = self.df2[self.df2["company name"] == self.entry_customer_id_combo.currentText()]["zone"]
                zone = list(zone)
                zone = zone[0]
                self.entry_location_line_edit.setText(zone)
                today = date.today()
                day = today.day
                month = today.month
                year = str(today.year)
                year = year[-2:]
                if month < 10:
                    month = f'0{month}'
                if day < 10:
                    day = f'0{day}'
                date_str = f'{day}{month}{year}'
                invoice_zone = str(zone[:3])
                invoice_zone = invoice_zone.upper()

                count = 1
                if "daily invoice count" in list(db.shallow().get().val()):
                    if date_str in list(db.child('daily invoice count').shallow().get().val()):
                        if zone in list(db.child('daily invoice count').child(date_str).shallow().get().val()):
                            count_from_db = db.child('daily invoice count').child(date_str).child(zone).child('count').get().val()
                            count_from_db = int(count_from_db) + 1
                            count = count_from_db
                        else:
                            count = 1
                    else:
                        count = 1
                else:
                    count = 1
                invoice_id = f'{invoice_zone}{date_str}-{count:04}'
                self.entry_invoice_id_line_edit.setText(invoice_id)
                i_id = self.entry_invoice_id_line_edit.text()
                # dirr = os.getcwd()
                dirr = file_save_path
                dirr = os.path.join(dirr, 'invoice')
                if not os.path.isdir(dirr):
                    os.mkdir(dirr)
                dir = f'{i_id}.pdf'
                dir = os.path.join(dirr, dir)
                self.file_location_line_edit.setText(dir)
                self.save_location = self.file_location_line_edit.text()

        except Exception as e:
            print(e)
            self.dialog.message_text.setText("No internet")
            self.dialog.displayInfo()

    def add_product(self):
        quantity = self.entry_quantity_spin.value()
        if quantity == 0:
            quantity = 1
        if quantity > 0:
            self.entry_table.setRowCount(self.row_count)
            row = self.row_count - 1
            self.entry_table.setItem(row, 0, QTableWidgetItem(str(row)))
            self.entry_table.setItem(row, 1, QTableWidgetItem(self.entry_product_id_combo.currentText()))
            self.entry_table.setItem(row, 2, QTableWidgetItem(self.entry_product_name_combo.currentText()))
            price = list(self.df[self.df["id"]==self.entry_product_id_combo.currentText()]["price"])
            price = price[0]
            self.sub_total_amount = self.sub_total_amount + (float(price) * quantity)
            tot = f'{float(price) * quantity}'
            self.entry_table.setItem(row, 3, QTableWidgetItem(f'{price}'))
            self.entry_table.setItem(row, 4, QTableWidgetItem(f'{quantity}'))
            self.entry_table.setItem(row, 5, QTableWidgetItem(tot))
            self.sub_total.setText(f'{self.sub_total_amount}')
            dict = {
                "Serial No": row,
                "Product ID": self.entry_product_id_combo.currentText(),
                "Product Name": self.entry_product_name_combo.currentText(),
                "Unit Price": price,
                "Quantity": quantity,
                "Total": tot
            }
            self.products_dict[f"{row}"] = dict
            self.row_count = self.row_count+1
            self.entry_quantity_spin.setValue(0)
        else:
            self.dialog.message_text.setText("Please select quantity")
            self.dialog.displayInfo()

    def id_changed(self):
        try:
            dt = self.entry_product_id_combo.currentText()
            name = list(self.df[self.df['id'] == dt]['name'])
            self.entry_product_name_combo.setCurrentText(name[0])
            stock = list(self.df[self.df['name'] == dt]['stock'])
            stock = stock[0]
            if str(stock) == 'nan':
                stock = 0
            else:
                stock = int(stock)
            if stock <= 0:
                self.entry_add_btn.setEnabled(False)
            else:
                self.entry_add_btn.setEnabled(True)
        except:
            pass

    def name_changed(self):
        try:
            dt = self.entry_product_name_combo.currentText()
            ids = list(self.df[self.df['name'] == dt]['id'])
            self.entry_product_id_combo.setCurrentText(ids[0])
            stock = list(self.df[self.df['name'] == dt]['stock'])
            stock = stock[0]
            if str(stock) == 'nan':
                stock = 0
            else:
                stock = int(stock)
            if stock <= 0:
                self.entry_add_btn.setEnabled(False)
            else:
                self.entry_add_btn.setEnabled(True)
        except:
            pass


    def show_me(self):
        self.clear_n_new()
        self.show()

    def clear_n_new(self):
        self.sub_total_amount = 0.00
        self.createTable()
        self.file_location_line_edit.setText("")
        self.save_data = {}
        self.products_dict = {}
        self.products_dict_final = {}
        self.df2 = pd.DataFrame()
        self.df = pd.DataFrame()
        self.tb_row = ""


        #print("Sdsdsd")
        try:
            try:
                self.dat = db.child('product').get().val()
                self.df = pd.DataFrame(self.dat, columns=self.dat.keys())
                self.df = self.df.transpose()
                self.dat2 = db.child('customer').get().val()
                self.df2 = pd.DataFrame(self.dat2, columns=self.dat2.keys())
                self.df2 = self.df2.transpose()
            except Exception as e:
                self.df2 = pd.DataFrame()
                self.df = pd.DataFrame()
                self.dialog.message_text.setText("Can not load data. Check internet connection")
                self.dialog.displayInfo()

            #self.file_location_line_edit.setText('')
            self.save_location = ''
            self.entry_address_line_edit.setText("")
            self.entry_location_line_edit.setText("")
            self.sub_total.setText("0.00")
            self.discountSpinBox.setValue(0.0)
            self.paidSpinBox.setValue(0.0)
            self.booking_date.setDateTime(QtCore.QDateTime.currentDateTime())
            self.delivery_date.setDateTime(QtCore.QDateTime.currentDateTime())
            data_ = self.df['id']
            data_ = list(data_.values)
            self.entry_product_id_combo.clear()
            self.entry_product_name_combo.clear()
            formLayout = QFormLayout()
            groupBox = QGroupBox("Product List")
            labelLis = []
            comboList = []
            for x in range(len(data_)):
                self.entry_product_id_combo.addItem(data_[x])
                name = self.df[self.df["id"] == data_[x]]["name"]
                name = list(name)
                name = name[0]
                stock = self.df[self.df["id"] == data_[x]]["stock"]
                stock = list(stock)
                stock = stock[0]
                if str(stock) == 'nan':
                    stock = 0
                else:
                    stock = int(stock)
                self.entry_product_name_combo.addItem(name)
                labelLis.append(QLabel(name + f' ({stock} in stock)'))
                comboList.append(QPushButton('ADD', self))
                comboList[x].clicked.connect(partial(self.set_item, name=name))
                if stock <= 0:
                    comboList[x].setEnabled(False)
                else:
                    comboList[x].setEnabled(True)
                formLayout.addRow(labelLis[x], comboList[x])
            groupBox.setLayout(formLayout)
            self.product_list.setWidget(groupBox)
            self.product_list.setWidgetResizable(True)
            _data__ = list(self.df2["company name"])
            self.entry_customer_id_combo.clear()
            for x in range(len(_data__)):
                self.entry_customer_id_combo.addItem(_data__[x])
            dat = db.child('user').get().val()
            df = pd.DataFrame(dat, columns=dat.keys())
            df = df.transpose()
            _data__1 = list(df["first name"])
            _data__2 = list(df["last name"])
            self.entry_employee_name_combo.clear()
            for x in range(len(_data__1)):
                self.entry_employee_name_combo.addItem(_data__1[x] + " " +  _data__2[x])
            first_name = db.child('user').child(auth.current_user['localId']).child('first name').get().val()
            last_name = db.child('user').child(auth.current_user['localId']).child('last name').get().val()
            self.entry_employee_name_combo.setCurrentText(first_name + " " +  last_name)
            self.refresh = True
            self.saved_data1 = []
            self.saved_data2 = []
            self.saved_data3 = 0.00
            self.saved_data4 = []
            self.new_created1 = []
            self.new_created2 = []
            self.new_created3 = False
            self.prevSpend = 0.0
            self.new_created = False
            i_id = self.entry_invoice_id_line_edit.text()
            #dirr = os.getcwd()
            dirr = file_save_path
            dirr = os.path.join(dirr, 'invoice')
            if not os.path.isdir(dirr):
                os.mkdir(dirr)
            dir = f'{i_id}.pdf'
            dir = os.path.join(dirr, dir)
            self.file_location_line_edit.setText(dir)
            self.customer_changed()
        except Exception as e:
            self.entry_invoice_id_line_edit.setText(f'{invoice_id_start}')
            self.dialog.message_text.setText("failed to fetch data or no records found")
            self.dialog.displayInfo()

    def set_item(self, name):
        self.entry_product_name_combo.setCurrentText(name)
        self.name_changed()
        self.add_product()

    def createTable(self):
        self.entry_table.clear()
        self.row_count = 1
        self.entry_table.setRowCount(1)
        self.row_count = self.row_count + 1
        self.entry_table.setColumnCount(6)
        self.entry_table.setItem(0, 0, QTableWidgetItem("Serial No"))
        self.entry_table.setItem(0, 1, QTableWidgetItem("Product ID"))
        self.entry_table.setItem(0, 2, QTableWidgetItem("Product Name"))
        self.entry_table.setItem(0, 3, QTableWidgetItem("Unit Price"))
        self.entry_table.setItem(0, 4, QTableWidgetItem("Quantity"))
        self.entry_table.setItem(0, 5, QTableWidgetItem("Total"))
        """self.entry_table.setItem(1, 0, QTableWidgetItem("Cell (2,1)"))
        self.entry_table.setItem(1, 1, QTableWidgetItem("Cell (2,2)"))
        self.entry_table.setItem(2, 0, QTableWidgetItem("Cell (3,1)"))
        self.entry_table.setItem(2, 1, QTableWidgetItem("Cell (3,2)"))
        self.entry_table.setItem(3, 0, QTableWidgetItem("Cell (4,1)"))
        self.entry_table.setItem(3, 1, QTableWidgetItem("Cell (4,2)"))"""
        self.entry_table.move(0, 0)

        # table selection change
        self.entry_table.itemChanged.connect(self.on_change)
        self.entry_table.itemDoubleClicked.connect(self.on_select)

    @pyqtSlot()
    def on_select(self):
        for currentQTableWidgetItem in self.entry_table.selectedItems():
            self.pre_selected_row = currentQTableWidgetItem.row()
            self.pre_selected_col = currentQTableWidgetItem.column()

    @pyqtSlot()
    def on_change(self):
        for currentQTableWidgetItem in self.entry_table.selectedItems():
            if currentQTableWidgetItem.row() == self.pre_selected_row and currentQTableWidgetItem.column() == self.pre_selected_col:
                if currentQTableWidgetItem.text() != self.pre_selected:
                    #print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())
                    column_name = self.entry_table.item(0, currentQTableWidgetItem.column()).text()
                    #print(column_name)
                    unit = self.entry_table.item(currentQTableWidgetItem.row(), 4).text()
                    unit_pr = self.entry_table.item(currentQTableWidgetItem.row(), 3).text()
                    it_tot = float(unit_pr)*float(unit)
                    self.products_dict[f"{currentQTableWidgetItem.row()}"][column_name] = currentQTableWidgetItem.text()
                    self.products_dict[f"{currentQTableWidgetItem.row()}"]['Total'] = float(self.products_dict[f"{currentQTableWidgetItem.row()}"]['Quantity']) * float(self.products_dict[f"{currentQTableWidgetItem.row()}"]['Unit Price'])
                    self.pre_selected = currentQTableWidgetItem.text()
                    self.entry_table.setItem(currentQTableWidgetItem.row(), 5, QTableWidgetItem(f'{it_tot}'))
                else:
                    self.pre_selected = ''
                total = 0
                for x in range(1, self.entry_table.rowCount()):
                    total = total + float(self.entry_table.item(x, 5).text())
                self.sub_total.setText(f'{total}')
                self.sub_total_amount = total

        self.pre_selected_row = -1
        self.pre_selected_col = -1

class UpdateSaleEntryUIClass(QMainWindow, update_entry_sale.Ui_MainWindow):
    def __init__(self, parent=None):
        super(UpdateSaleEntryUIClass, self).__init__(parent)
        self.setupUi(self)
        self.dialog = Dialog()
        self.app = App()
        self.app.signal.connect(self.change_file)
        self.row_count = 1
        self.pre_selected = ''
        self.pre_selected_row = -1
        self.pre_selected_col = -1
        self.df = pd.DataFrame()
        self.df2 = pd.DataFrame()
        #self.save_data = pd.DataFrame(columns = ['Serial No', 'Product ID', 'Product Name', 'Unit Price', 'Quantity', 'Total'])
        #print(self.save_data)
        self.save_data = {}
        self.products_dict = {}
        self.products_dict_final = {}
        self.old_product_dict = {}
        self.bef_new = 0
        self.paid = 0.00
        self.discount = 0.00
        self.sub_total_amount = 0.00
        self.save_location = ''
        self.entry_product_id_combo.currentTextChanged.connect(self.id_changed)
        self.entry_product_name_combo.currentTextChanged.connect(self.name_changed)
        self.entry_customer_id_combo.currentTextChanged.connect(self.customer_changed)
        self.edit_btn.clicked.connect(self.edit)
        self.entry_add_btn.clicked.connect(self.add_product)
        self.save_btn.clicked.connect(self.save)
        self.save_btn.setEnabled(False)
        self.save_btn.hide()
        self.tb_row = """"""
        self.save_n_new_btn.clicked.connect(self.save_n_new)
        self.save_n_exit_btn.clicked.connect(self.save_n_exit)
        self.select_location_btn.clicked.connect(self.set_file_location)
        self.print_btn.clicked.connect(self.printDialog)
        self.search_btn.clicked.connect(self.search_func)
        self.table_top = """
                        <div style="margin-top: 150px;">
                            <table class="table">
                              <thead class="thead-light">
                                <tr>
                                  <th scope="col">Serial No</th>
                                  <th scope="col">Product Name</th>
                                  <th scope="col">Unit Price</th>
                                  <th scope="col">Quantity</th>
                                  <th scope="col">Total</th>
                                </tr>
                              </thead>
                              <tbody>"""
        self.table_mid = """
                        <tr>
                              <th scope="row">$serial</th>
                              <td>$product_name</td>
                              <td>$unit_price</td>
                              <td>$quantity</td>
                              <td>$item_total</td>
                        </tr>"""
        self.table_bottom = """      
                              <tr>
                                  <th scope="row"></th>
                                  <td></td>
                                  <td> </td>
                                  <td>Total Amount</td>
                                  <td>$sub_total</td>
                                </tr>
                              </tbody>
                            </table>
                        </div>
                        <div>
                            <div style="float: left; width: 400px;">
                                <div style="margin-left: 180px; text-align: left;">
                                    <a style="font-size: 15px; font-weight: 500; color: black;">
                                        Discount $discount_percent %
                                    </a>
                                    <br>
                                    <a style="font-size: 15px; font-weight: 500; color: black;">

                                    </a>
                                    <br>
                                    <a style="font-size: 15px; font-weight: 500; color: black;">
                                        Sale Tax rate $tax_percent %
                                    </a>
                                    <br>
                                    <a style="font-size: 15px; font-weight: 500; color: black;">

                                    </a>
                                </div>
                            </div>
                            <div style="float: right; width: 350px;">
                                <div style="float: left;">
                                    <a style="font-size: 15px; font-weight: 500; color: black;">
                                        Discount Amount
                                    </a>
                                    <br>
                                    <a style="font-size: 15px; font-weight: 500; color: black;">
                                        After Discount
                                    </a>
                                    <br>
                                    <a style="font-size: 15px; font-weight: 500; color: black;">
                                        Tax Amount
                                    </a>
                                    <br>
                                    <a style="font-size: 15px; font-weight: 500; color: black;">
                                        Net Amount
                                    </a>
                                    <br>
                                </div>
                                <div style="float: right; margin-right: 20px;">
                                    <a style="font-size: 15px; font-weight: 500; color: black;">
                                        $discount
                                    </a>
                                    <br>
                                    <a style="font-size: 15px; font-weight: 500; color: black;">
                                        $after_discount
                                    </a>
                                    <br>
                                    <a style="font-size: 15px; font-weight: 500; color: black;">
                                        $tax_amount
                                    </a>
                                    <br>
                                    <a style="font-size: 15px; font-weight: 500; color: black;">
                                        $total
                                    </a>
                                    <br>
                                </div>
                            </div>
                        </div>
                        <div style="margin-top: 140px;">

                        </div>
                        <div style="margin-left: 20px;">
                            <a style="font-size: 15px; font-weight: 500; color: black;">
                                In Word: $in_word  taka only
                            </a>
                        </div>
                        <hr>

                        <div style="margin-top: 20px;">
                            <div style="float: left; width: 400px;">

                            </div>
                            <div style="float: right; width: 350px;">
                                <div style="float: left;">
                                    <a style="font-size: 15px; font-weight: 500; color: black;">
                                        Paid
                                    </a>
                                    <br>
                                </div>
                                <div style="float: right; margin-right: 20px;">
                                    <a style="font-size: 15px; font-weight: 500; color: black;">
                                        $paid
                                    </a>
                                    <br>
                                </div>
                            </div>
                        </div>
                        <br>
                        <hr>
                        <div style="margin-top: 20px;">
                            <div style="float: left; width: 400px;">

                            </div>
                            <div style="float: right; width: 350px;">
                                <div style="float: left;">
                                    <a style="font-size: 15px; font-weight: 500; color: black;">
                                        Due
                                    </a>
                                    <br>
                                </div>
                                <div style="float: right; margin-right: 20px;">
                                    <a style="font-size: 15px; font-weight: 500; color: black;">
                                        $due
                                    </a>
                                    <br>
                                </div>
                            </div>
                        </div>
                        <br>
                        <hr>
                        <div style="margin-left: 20px;">
                            <a style="font-size: 15px; font-weight: 500; color: black;">
                                Due In Word: $in_word_due  taka only
                            </a>
                        </div>
                        <br>
                        <hr>
                        <br>
                        """
        self.top = """
                <!doctype html>
                <html>
                <head>
                <meta charset="utf-8">
                <title>Untitled Document</title>
                <link rel="stylesheet" href="$css_link">
                <style>
                    .clearfix:after {
                      content: "";
                      display: table;
                      clear: both;
                    }

                    a {
                      color: #5D6975;
                      #text-decoration: underline;
                    }

                    body {
                      position: relative;
                      width: 21cm;
                      height: 29.7cm;
                      margin: 0 auto;
                      color: #001028;
                      background: #FFFFFF;
                      font-family: Arial, sans-serif;
                      font-size: 12px;
                      font-family: Arial;
                    }

                    header {
                      padding: 10px 0;
                      margin-bottom: 30px;
                    }

                    #logo {
                      text-align: center;
                      margin-bottom: 10px;
                    }

                    #logo img {
                      width: 200px;
                    }

                    h1 {
                      border-top: 1px solid  #5D6975;
                      border-bottom: 1px solid  #5D6975;
                      color: #5D6975;
                      font-size: 2.4em;
                      line-height: 1.4em;
                      font-weight: normal;
                      text-align: center;
                      margin: 0 0 20px 0;
                      background: url($dimension_png);
                    }

                    #project {
                      float: left;
                    }

                    #project span {
                      color: #5D6975;
                      text-align: right;
                      width: 52px;
                      margin-right: 10px;
                      display: inline-block;
                      font-size: 0.8em;
                    }

                    #company {
                      float: right;
                      text-align: right;
                    }

                    #project div,
                    #company div {
                      white-space: nowrap;
                    }



                    #notices .notice {
                      color: #5D6975;
                      font-size: 1.2em;
                    }

                    footer {
                      color: #5D6975;
                      width: 100%;
                      height: 30px;
                      bottom: 0;
                      border-top: 1px solid #C1CED9;
                      padding: 8px 0;
                      text-align: center;
                      margin-top: 50px;
                    }
                </style>
                </head>

                <body>
                    <div>
                        <div style="margin-top: 50px; margin-bottom: 10px;">
                            <div style="text-align: center;">

                                <div style="width: 300px; margin: 0 auto;">
                                    <div style="float: left; margin-top: 0px;">
                                        <img style="height: 40px; width: 40px;" src="$logo_png">
                                    </div>
                                    <div>
                                        <a style="color: black; font-size: 30px; font-weight: 500;">
                                            Machronics
                                        </a>
                                    </div>

                                </div>
                                <br>
                                <a style="font-size: 15px; font-weight: 500; color: black;">
                                    Mirpur Dohs, Mirpur-12,
                                </a>
                                <br>
                                <a style="font-size: 15px; font-weight: 500; color: black;">
                                    Dhaka
                                </a>
                                <br>
                                <br>
                                <a style="color: black; font-size: 20px; font-weight: 500;">
                                    INVOICE
                                </a>
                            </div>

                            <div style="margin-left: 15px; margin-right: 15px;">
                                <div style="text-align: left; float: left;">
                                    <a style="font-size: 15px; font-weight: 500; color: black;">
                                        Invoice No: $invoice_id
                                    </a>
                                    <br>
                                    <a style="font-size: 15px; font-weight: 500; color: black;">
                                        Name: $client
                                    </a>
                                    <br>
                                    <a style="font-size: 15px; font-weight: 500; color: black;">
                                        Address: $address
                                    </a>
                                    <br>
                                    <a style="font-size: 15px; font-weight: 500; color: black;">
                                        Zone: $zone
                                    </a>
                                </div>
                                <div style="text-align: left; float: right;">
                                    <a style="font-size: 15px; font-weight: 500; color: black;">
                                        Sold By: $sales_by
                                    </a>
                                    <br>
                                    <a style="font-size: 15px; font-weight: 500; color: black;">
                                        Order Date: $order_date
                                    </a>
                                    <br>
                                    <a style="font-size: 15px; font-weight: 500; color: black;">
                                        Delivery Date: $delivery_date
                                    </a>
                                    <br>
                                    <br>
                                    <a style="font-size: 15px; font-weight: 500; color: black;">
                                        $due
                                    </a>
                                </div>
                            </div>
                        </div>"""

        self.bottom = """
                      <div style="margin-top: 70px;">
                            <div style="float: left; width: 350px; text-align: center;">
                                <a style="font-size: 15px; font-weight: 500; color: black; text-decoration-line: overline;">
                                    Customer's Signature
                                </a>
                            </div>
                            <div style="float: right; width: 350px;">
                                <div style="text-align: center;">
                                    <a style="font-size: 15px; font-weight: 500; color: black;  text-decoration-line: overline;">
                                        Authorized Signature
                                    </a>
                                </div>
                            </div>
                            </div>
                            <div style="margin-top: 140px;">
                            </div>
                            <hr>
                            <div style="text-align: left;">
                                <a style="font-size: 15px; font-weight: 500; color: black;">
                                    N.B: This is a computer generated document and is valid if not signed.
                                </a>
                            </div>
                      </div>
                      <script src="$js_url"></script>
                </body>
                </html>
        """
        self.refresh = True
        self.saved_data1 = []
        self.saved_data2 = []
        self.saved_data3 = 0.00
        self.saved_data4 = []
        self.new_created1 = []
        self.new_created2 = []
        self.new_created3 = False
        self.prevSpend = 0.0
        self.new_created = False
        self.invoice_id.currentTextChanged.connect(self.inactive)

    def inactive(self):
        self.save_n_new_btn.setEnabled(False)
        self.save_n_exit_btn.setEnabled(False)
        self.print_btn.setEnabled(False)

    def search_func(self):
        data_0 = db.child('invoice').shallow().get()
        data_0 = list(data_0.val())
        if self.search.text() != '' and self.search.text() in data_0:
            self.invoice_id.setCurrentText(self.search.text())
            self.edit()
        else:
            self.dialog.message_text.setText("No matching query found")
            self.dialog.displayInfo()

    def save_n_new(self):
        self.save_n_new_btn.setEnabled(False)
        self.save_n_exit_btn.setEnabled(False)
        self.print_btn.setEnabled(False)
        QTimer.singleShot(500, lambda: self.call_after_dis())

    def call_after_dis(self):
        cond = self.save()
        self.save_n_new_btn.setEnabled(True)
        self.save_n_exit_btn.setEnabled(True)
        self.print_btn.setEnabled(True)
        if cond:
            self.clear_n_new()

    def save_n_exit(self):
        self.save_n_new_btn.setEnabled(False)
        self.save_n_exit_btn.setEnabled(False)
        self.print_btn.setEnabled(False)
        QTimer.singleShot(500, lambda: self.run_after_dis_2())

    def run_after_dis_2(self):
        cond = self.save()
        self.save_n_new_btn.setEnabled(True)
        self.save_n_exit_btn.setEnabled(True)
        self.print_btn.setEnabled(True)
        if cond:
            self.close()

    def set_file_location(self):
        self.app.initUI()

    def change_file(self, value):
        self.file_location_line_edit.setText(str(value))

    def printDialog(self):
        self.save_n_new_btn.setEnabled(False)
        self.save_n_exit_btn.setEnabled(False)
        self.print_btn.setEnabled(False)
        QTimer.singleShot(500, lambda: self.run_after_dis_3())

    def run_after_dis_3(self):
        keys = []
        for x in self.products_dict.keys():
            if int(self.products_dict[x]['Quantity']) != 0:
                keys.append(x)
        yy = 1
        self.products_dict_final = {}
        for key in keys:
            self.products_dict_final[f'{yy}'] = self.products_dict[key]
            yy = yy + 1

        prev_total = float(self.save_data["sub total"])
        prev_discount = float(self.save_data["discount"])
        prev_paid = float(self.save_data["paid"])
        self.paid = self.paidSpinBox.value()
        self.discount = self.discountSpinBox.value()
        self.save_data["invoice id"] = self.invoice_id.currentText()
        self.save_data["customer id"] = self.entry_customer_id_combo.currentText()
        self.save_data["address"] = self.entry_address_line_edit.text()
        self.save_data["location"] = self.entry_location_line_edit.text()
        self.save_data["employee name"] = self.entry_employee_name_combo.currentText()
        self.save_data["booking date"] = str(self.booking_date.date().toPyDate())
        self.save_data["delivery date"] = str(self.delivery_date.date().toPyDate())
        self.save_data["products"] = self.products_dict_final
        self.save_data["sub total"] = self.sub_total_amount
        company_name = self.entry_customer_id_combo.currentText()
        email = self.df2[self.df2["company name"] == self.entry_customer_id_combo.currentText()]["email"]
        email = list(email)
        email = email[0]
        customerId = self.df2[self.df2["company name"] == self.entry_customer_id_combo.currentText()]["customer id"]
        customerId = list(customerId)
        customerId = customerId[0]
        self.save_location = self.file_location_line_edit.text()
        for count, x in enumerate(self.products_dict_final.keys()):
            tb_row = Template(self.table_mid).safe_substitute(
                serial="{}".format(count + 1),
                product_name=self.products_dict_final[x]['Product Name'],
                unit_price=self.products_dict_final[x]['Unit Price'],
                quantity=self.products_dict_final[x]['Quantity'],
                item_total="{:.2f}".format(float(self.products_dict_final[x]['Total']))
            )
            self.tb_row = self.tb_row + tb_row
        bal_b = self.df2[self.df2["company name"] == self.entry_customer_id_combo.currentText()]["opening balance"]
        bal_b = list(bal_b)
        bal_b = float(bal_b[0])
        total_due = bal_b + self.sub_total_amount - prev_total - self.paid - self.discount + prev_paid + prev_discount
        words = p.number_to_words(int(self.sub_total_amount - self.discount))
        words_due = p.number_to_words(int(self.sub_total_amount - self.discount - self.paid))
        discount_perc = (self.discount / self.sub_total_amount) * 100
        table_bottom = Template(self.table_bottom).safe_substitute(
            sub_total="{:.2f}".format(self.sub_total_amount),
            discount_percent="{:.2f}".format(discount_perc), discount="{:.2f}".format(self.discount),
            after_discount="{:.2f}".format(self.sub_total_amount - self.discount),
            tax_percent="0.0", tax_amount="0.00",
            total="{:.2f}".format(self.sub_total_amount - self.discount),
            in_word=words,
            paid=str(self.paid),
            due=str(self.sub_total_amount - self.discount - self.paid),
            in_word_due=words_due)
        top = Template(self.top).safe_substitute(css_link=bootstrap_css_url, logo_png=logo_url, dimension_png=dimension_url,
                                                 invoice_id=self.save_data["invoice id"],
                                                 client=company_name, address=self.save_data["address"],
                                                 zone=self.save_data["location"],
                                                 sales_by=self.save_data["employee name"],
                                                 due="",
                                                 order_date=self.save_data["booking date"],
                                                 delivery_date=self.save_data["delivery date"])
        #due="{:.2f}".format(total_due),
        bottom = Template(self.bottom).safe_substitute(js_link=bootstrap_js_url)
        html = top + self.table_top + self.tb_row + table_bottom + bottom
        self.save_file(html)
        path = r"{}".format(self.save_location)
        url = bytearray(QUrl.fromLocalFile(path).toEncoded()).decode()
        QDesktopServices.openUrl(QUrl(url))
        QTimer.singleShot(500, lambda: self.save_after_print(prev_total, prev_discount, prev_paid))

        #self.clear_n_new()
        #if is_correct:
        """printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer, self)"""
        """self.page = QtWebEngineWidgets.QWebEnginePage()
        self.page.setHtml(html)
        printer = QPrinter()
        dialog = QPrintDialog(printer, self)
        if dialog.exec_() == QPrintDialog.Accepted:
            self.page.print(printer, self.print_completed)"""

    """def print_completed(self):
        pass"""

    """def printDialog(self):
        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer, self)
        if dialog.exec_() == QPrintDialog.Accepted:
            self.textEdit.print_(printer)

    def printpreviewDialog(self):
        printer = QPrinter(QPrinter.HighResolution)
        previewDialog = QPrintPreviewDialog(printer, self)
        previewDialog.paintRequested.connect(self.printPreview)
        previewDialog.exec_()

    def printPreview(self, printer):
        self.textEdit.print_(printer)"""

    def save_after_print(self, prev_total, prev_discount, prev_paid):
        #prev_total = float(self.save_data["sub total"])
        #print(prev_total)
        #print(prev_discount)
        #print(prev_paid)
        #prev_discount = float(self.save_data["discount"])
        #prev_paid = float(self.save_data["paid"])
        prev_discount = float(prev_discount)
        prev_paid = float(prev_paid)
        self.paid = self.paidSpinBox.value()
        self.discount = self.discountSpinBox.value()
        self.save_data["invoice id"] = self.invoice_id.currentText()
        self.save_data["customer id"] = self.entry_customer_id_combo.currentText()
        self.save_data["address"] = self.entry_address_line_edit.text()
        self.save_data["location"] = self.entry_location_line_edit.text()
        self.save_data["employee name"] = self.entry_employee_name_combo.currentText()
        self.save_data["booking date"] = str(self.booking_date.date().toPyDate())
        self.save_data["delivery date"] = str(self.delivery_date.date().toPyDate())
        self.save_data["products"] = self.products_dict_final
        self.save_data["sub total"] = self.sub_total_amount
        self.save_data["paid"] = self.paid
        self.save_data["discount"] = self.discount
        company_name = self.entry_customer_id_combo.currentText()
        email = self.df2[self.df2["company name"] == self.entry_customer_id_combo.currentText()]["email"]
        email = list(email)
        email = email[0]
        customerId = self.df2[self.df2["company name"] == self.entry_customer_id_combo.currentText()]["customer id"]
        customerId = list(customerId)
        customerId = customerId[0]
        self.save_location = self.file_location_line_edit.text()
        try:
            if self.save_location != '' and self.save_data["invoice id"] != '' and self.save_data["customer id"] != '' and self.save_data["address"] != '' and self.save_data["location"] != '' and self.save_data["employee name"] != '' and self.save_data["booking date"] != '' and self.save_data["delivery date"] != '' and self.save_data["products"] != {}:
                i = 0
                for x in self.products_dict.keys():
                    if self.refresh:
                        prev_stock = db.child('product').child(self.products_dict[x]['Product ID']).child(
                            'stock').get().val()
                        self.saved_data4.append(prev_stock)
                    else:
                        if i < len(self.saved_data4):
                            prev_stock = self.saved_data4[i]
                        else:
                            prev_stock = db.child('product').child(self.products_dict[x]['Product ID']).child(
                                'stock').get().val()
                            self.saved_data4.append(prev_stock)
                    if str(prev_stock) == 'nan':
                        prev_stock = 0
                    else:
                        prev_stock = int(prev_stock)
                    new_stock = prev_stock - int(self.products_dict[x]['Quantity']) + int(
                        self.old_product_dict[x]['Quantity'])
                    db.child('product').child(self.products_dict[x]['Product ID']).child('stock').set(new_stock)
                    if "product sold" in list(db.shallow().get().val()) and self.products_dict[x][
                        'Product ID'] in list(db.child("product sold").shallow().get().val()):
                        if self.refresh:
                            sold_quant = int(db.child("product sold").child(self.products_dict[x]['Product ID']).child(
                                "sold unit").get().val())
                            self.saved_data1.append(sold_quant)
                            sold_amount = float(
                                db.child("product sold").child(self.products_dict[x]['Product ID']).child(
                                    "sold amount").get().val())
                            self.saved_data2.append(sold_amount)
                            sold_quant = sold_quant + int(self.products_dict[x]['Quantity']) - int(
                                self.old_product_dict[x]['Quantity'])
                            sold_amount = sold_amount + float(self.products_dict[x]['Total']) - float(
                                self.old_product_dict[x]['Total'])
                            self.new_created1.append(False)
                            self.new_created2.append(False)
                        else:
                            if i < len(self.saved_data1):
                                sold_quant = self.saved_data1[i]
                                if not self.new_created1[i]:
                                    sold_quant = sold_quant + int(self.products_dict[x]['Quantity']) - int(
                                        self.old_product_dict[x]['Quantity'])
                                else:
                                    sold_quant = int(self.products_dict[x]['Quantity']) - int(
                                        self.old_product_dict[x]['Quantity'])
                                # self.new_created1[i] = False
                            else:
                                sold_quant = int(
                                    db.child("product sold").child(self.products_dict[x]['Product ID']).child(
                                        "sold unit").get().val())
                                self.saved_data1.append(sold_quant)
                                sold_quant = sold_quant + int(self.products_dict[x]['Quantity']) - int(
                                    self.old_product_dict[x]['Quantity'])
                                self.new_created1.append(False)

                            if i < len(self.saved_data2):
                                sold_amount = self.saved_data2[i]
                                if not self.new_created2[i]:
                                    sold_amount = sold_amount + float(self.products_dict[x]['Total']) - float(
                                        self.old_product_dict[x]['Total'])
                                else:
                                    sold_amount = float(self.products_dict[x]['Total']) - float(
                                        self.old_product_dict[x]['Total'])
                                # self.new_created2[i] = False
                            else:
                                sold_amount = float(
                                    db.child("product sold").child(self.products_dict[x]['Product ID']).child(
                                        "sold amount").get().val())
                                self.saved_data2.append(sold_amount)
                                sold_amount = sold_amount + float(self.products_dict[x]['Total']) - float(
                                    self.old_product_dict[x]['Total'])
                                self.new_created2.append(False)

                        db.child("product sold").child(self.products_dict[x]['Product ID']).child("sold unit").set(
                            sold_quant)
                        db.child("product sold").child(self.products_dict[x]['Product ID']).child("sold amount").set(
                            sold_amount)

                        # db.child("product sold").child(self.products_dict[x]['Product ID']).child("stock").set(
                        #    new_stock)
                    else:
                        product_data = {
                            'sold unit': self.products_dict[x]['Quantity'],
                            'sold amount': float(self.products_dict[x]['Total'])
                        }
                        self.saved_data1.append(int(self.products_dict[x]['Quantity']))
                        self.saved_data2.append(float(self.products_dict[x]['Total']))
                        db.child("product sold").child(self.products_dict[x]['Product ID']).set(product_data)
                        self.new_created1.append(True)
                        self.new_created2.append(True)
                    i = i + 1
                try:
                    db.child('invoice').child(self.invoice_id.currentText()).set(self.save_data)

                    c_id = self.df2[self.df2["company name"] == self.entry_customer_id_combo.currentText()][
                        "customer id"]
                    c_id = list(c_id)
                    c_id = c_id[0]
                    if "customer spend" in list(db.shallow().get().val()) and c_id in list(
                            db.child("customer spend").shallow().get().val()) and "spent amount" in list(db.child("customer spend").child(c_id).shallow().get().val()):
                        if self.refresh:
                            prev_spend = float(db.child("customer spend").child(c_id).child("spent amount").get().val())
                            self.saved_data3 = prev_spend
                        else:
                            prev_spend = self.saved_data3
                        if not self.new_created3:
                            new_spend = prev_spend + float(self.sub_total_amount) - prev_total - self.discount
                        else:
                            new_spend = float(self.sub_total_amount) - prev_total - self.discount
                        db.child("customer spend").child(c_id).child("spent amount").set(new_spend)
                    else:
                        db.child("customer spend").child(c_id).child("spent amount").set(self.sub_total_amount)
                        self.saved_data3 = self.sub_total_amount - self.discount
                        self.new_created3 = True

                    if "customer spend" in list(db.shallow().get().val()) and c_id in list(
                            db.child("customer spend").shallow().get().val()) and "paid" in list(
                        db.child("customer spend").child(c_id).shallow().get().val()):
                        if self.refresh:
                            prev_spend = float(db.child("customer spend").child(c_id).child("paid").get().val())
                            self.prevSpend = prev_spend
                        else:
                            prev_spend = self.prevSpend
                        if not self.new_created:
                            new_spend = prev_spend + self.paid - prev_paid
                        else:
                            new_spend = self.paid - prev_paid
                        db.child("customer spend").child(c_id).child("paid").set(new_spend)
                        # self.new_created = False
                    else:
                        new_spend = self.paid - prev_paid
                        self.prevSpend = new_spend
                        db.child("customer spend").child(c_id).child("paid").set(new_spend)
                        self.new_created = True

                    bal_b = self.df2[self.df2["company name"] == self.entry_customer_id_combo.currentText()]["opening balance"]
                    bal_b = list(bal_b)
                    bal_b = float(bal_b[0])
                    bal_a = bal_b + self.sub_total_amount - prev_total - self.paid - self.discount + prev_discount + prev_paid
                    db.child('customer').child(customerId).child('opening balance').set(bal_a)
                    self.refresh = False
                    try:
                        recipientNumber = self.df2[self.df2["company name"] == self.entry_customer_id_combo.currentText()]["number"]
                        recipientNumber = list(recipientNumber)
                        recipientNumber = recipientNumber[0]
                        or_id = self.save_data["invoice id"]
                        d_date = self.save_data["delivery date"]
                        bill = '{:.2f}'.format(self.sub_total_amount - self.discount)
                        smsText = f"Your order {or_id} has been updated. Total bill amount is {bill} taka and estimated delivery date is {d_date}."
                        client.service.OneToOne(userName, password, recipientNumber, smsText, smsType, maskName, campaignName)
                        #bill = '{:.2f}'.format(bal_a)
                        #smsText = f'Dear Customer, Your total due is {bill} taka.'
                        #client.service.OneToOne(userName, password, recipientNumber, smsText, smsType, maskName, campaignName)
                    except Exception as e:
                        print(e)
                    self.tb_row = """"""
                    self.set_all_field()
                    self.dialog.message_text.setText("Data Saved")
                    self.dialog.displayInfo()

                except Exception as e:
                    print(e)
                    self.dialog.message_text.setText("Error saving data")
                    self.dialog.displayInfo()
            else:
                self.dialog.message_text.setText("Fill up all the fields")
                self.dialog.displayInfo()

        except Exception as e:
            print(e)
            self.dialog.message_text.setText("No internet")
            self.dialog.displayInfo()
        #self.save_n_new_btn.setEnabled(True)
        #self.save_n_exit_btn.setEnabled(True)
        #self.print_btn.setEnabled(True)

    def save_file(self, html):
        try:
            path = os.path.join(file_save_path, 'invoice')
            if not os.path.isdir(path):
                os.mkdir(path)
            path = os.path.join(path, "file.html")
            with open(path, "w") as file:
                file.write(html)
            pdfkit.from_file(path, self.save_location, configuration=config)
        except:
            pass

    def save(self):
        try:
            keys = []
            for x in self.products_dict.keys():
                if int(self.products_dict[x]['Quantity']) != 0:
                    keys.append(x)
            yy = 1
            self.products_dict_final = {}
            for key in keys:
                self.products_dict_final[f'{yy}'] = self.products_dict[key]
                yy = yy + 1

            prev_total = float(self.save_data["sub total"])
            prev_discount = float(self.save_data["discount"])
            prev_paid = float(self.save_data["paid"])
            self.discount = self.discountSpinBox.value()
            self.paid = self.paidSpinBox.value()
            self.save_data["invoice id"] = self.invoice_id.currentText()
            self.save_data["customer id"] = self.entry_customer_id_combo.currentText()
            self.save_data["address"] = self.entry_address_line_edit.text()
            self.save_data["location"] = self.entry_location_line_edit.text()
            self.save_data["employee name"] = self.entry_employee_name_combo.currentText()
            self.save_data["booking date"] = str(self.booking_date.date().toPyDate())
            self.save_data["delivery date"] = str(self.delivery_date.date().toPyDate())
            self.save_data["products"] = self.products_dict_final
            self.save_data["sub total"] = self.sub_total_amount
            company_name = self.entry_customer_id_combo.currentText()
            email = self.df2[self.df2["company name"] == self.entry_customer_id_combo.currentText()]["email"]
            email = list(email)
            email = email[0]
            customerId = self.df2[self.df2["company name"] == self.entry_customer_id_combo.currentText()]["customer id"]
            customerId = list(customerId)
            customerId = customerId[0]
            self.save_location = self.file_location_line_edit.text()
            if self.save_location != '' and self.save_data["invoice id"] != '' and self.save_data["customer id"] != '' and self.save_data["address"] != '' and self.save_data["location"] != '' and self.save_data["employee name"] != '' and self.save_data["booking date"] != '' and self.save_data["delivery date"] != '' and self.save_data["products"] != {}:
                i = 0
                for x in self.products_dict.keys():
                    if self.refresh:
                        prev_stock = db.child('product').child(self.products_dict[x]['Product ID']).child(
                            'stock').get().val()
                        self.saved_data4.append(prev_stock)
                    else:
                        if i < len(self.saved_data4):
                            prev_stock = self.saved_data4[i]
                        else:
                            prev_stock = db.child('product').child(self.products_dict[x]['Product ID']).child(
                                'stock').get().val()
                            self.saved_data4.append(prev_stock)
                    if str(prev_stock) == 'nan':
                        prev_stock = 0
                    else:
                        prev_stock = int(prev_stock)
                    new_stock = prev_stock - int(self.products_dict[x]['Quantity']) + int(
                        self.old_product_dict[x]['Quantity'])
                    db.child('product').child(self.products_dict[x]['Product ID']).child('stock').set(new_stock)
                    if "product sold" in list(db.shallow().get().val()) and self.products_dict[x][
                        'Product ID'] in list(db.child("product sold").shallow().get().val()):
                        if self.refresh:
                            sold_quant = int(db.child("product sold").child(self.products_dict[x]['Product ID']).child(
                                "sold unit").get().val())
                            self.saved_data1.append(sold_quant)
                            sold_amount = float(
                                db.child("product sold").child(self.products_dict[x]['Product ID']).child(
                                    "sold amount").get().val())
                            self.saved_data2.append(sold_amount)
                            sold_quant = sold_quant + int(self.products_dict[x]['Quantity']) - int(
                                self.old_product_dict[x]['Quantity'])
                            sold_amount = sold_amount + float(self.products_dict[x]['Total']) - float(
                                self.old_product_dict[x]['Total'])
                            self.new_created1.append(False)
                            self.new_created2.append(False)
                        else:
                            if i < len(self.saved_data1):
                                sold_quant = self.saved_data1[i]
                                if not self.new_created1[i]:
                                    sold_quant = sold_quant + int(self.products_dict[x]['Quantity']) - int(
                                        self.old_product_dict[x]['Quantity'])
                                else:
                                    sold_quant = int(self.products_dict[x]['Quantity']) - int(
                                        self.old_product_dict[x]['Quantity'])
                                # self.new_created1[i] = False
                            else:
                                sold_quant = int(
                                    db.child("product sold").child(self.products_dict[x]['Product ID']).child(
                                        "sold unit").get().val())
                                self.saved_data1.append(sold_quant)
                                sold_quant = sold_quant + int(self.products_dict[x]['Quantity']) - int(
                                    self.old_product_dict[x]['Quantity'])
                                self.new_created1.append(False)

                            if i < len(self.saved_data2):
                                sold_amount = self.saved_data2[i]
                                if not self.new_created2[i]:
                                    sold_amount = sold_amount + float(self.products_dict[x]['Total']) - float(
                                        self.old_product_dict[x]['Total'])
                                else:
                                    sold_amount = float(self.products_dict[x]['Total']) - float(
                                        self.old_product_dict[x]['Total'])
                                # self.new_created2[i] = False
                            else:
                                sold_amount = float(
                                    db.child("product sold").child(self.products_dict[x]['Product ID']).child(
                                        "sold amount").get().val())
                                self.saved_data2.append(sold_amount)
                                sold_amount = sold_amount + float(self.products_dict[x]['Total']) - float(
                                    self.old_product_dict[x]['Total'])
                                self.new_created2.append(False)

                        db.child("product sold").child(self.products_dict[x]['Product ID']).child("sold unit").set(
                            sold_quant)
                        db.child("product sold").child(self.products_dict[x]['Product ID']).child("sold amount").set(
                            sold_amount)

                        # db.child("product sold").child(self.products_dict[x]['Product ID']).child("stock").set(
                        #    new_stock)
                    else:
                        product_data = {
                            'sold unit': self.products_dict[x]['Quantity'],
                            'sold amount': float(self.products_dict[x]['Total'])
                        }
                        self.saved_data1.append(int(self.products_dict[x]['Quantity']))
                        self.saved_data2.append(float(self.products_dict[x]['Total']))
                        db.child("product sold").child(self.products_dict[x]['Product ID']).set(product_data)
                        self.new_created1.append(True)
                        self.new_created2.append(True)
                    i = i + 1
                try:
                    db.child('invoice').child(self.invoice_id.currentText()).set(self.save_data)
                    for count, x in enumerate(self.products_dict_final.keys()):
                        tb_row = Template(self.table_mid).safe_substitute(
                            serial="{}".format(count + 1),
                            product_name=self.products_dict_final[x]['Product Name'],
                            unit_price=self.products_dict_final[x]['Unit Price'],
                            quantity=self.products_dict_final[x]['Quantity'],
                            item_total="{:.2f}".format(float(self.products_dict_final[x]['Total']))
                        )
                        self.tb_row = self.tb_row + tb_row
                    c_id = self.df2[self.df2["company name"] == self.entry_customer_id_combo.currentText()][
                        "customer id"]
                    c_id = list(c_id)
                    c_id = c_id[0]
                    if "customer spend" in list(db.shallow().get().val()) and c_id in list(
                            db.child("customer spend").shallow().get().val()) and "spent amount" in list(db.child("customer spend").child(c_id).shallow().get().val()):
                        if self.refresh:
                            prev_spend = float(db.child("customer spend").child(c_id).child("spent amount").get().val())
                            self.saved_data3 = prev_spend
                        else:
                            prev_spend = self.saved_data3
                        if not self.new_created3:
                            new_spend = prev_spend + float(self.sub_total_amount) - prev_total - self.discount
                        else:
                            new_spend = float(self.sub_total_amount) - prev_total - self.discount
                        db.child("customer spend").child(c_id).child("spent amount").set(new_spend)
                    else:
                        db.child("customer spend").child(c_id).child("spent amount").set(self.sub_total_amount)
                        self.saved_data3 = self.sub_total_amount - self.discount
                        self.new_created3 = True

                    if "customer spend" in list(db.shallow().get().val()) and c_id in list(
                            db.child("customer spend").shallow().get().val()) and "paid" in list(
                        db.child("customer spend").child(c_id).shallow().get().val()):
                        if self.refresh:
                            prev_spend = float(db.child("customer spend").child(c_id).child("paid").get().val())
                            self.prevSpend = prev_spend
                        else:
                            prev_spend = self.prevSpend
                        if not self.new_created:
                            new_spend = prev_spend + self.paid - prev_paid
                        else:
                            new_spend = self.paid - prev_paid
                        db.child("customer spend").child(c_id).child("paid").set(new_spend)
                        # self.new_created = False
                    else:
                        new_spend = self.paid - prev_paid
                        self.prevSpend = new_spend
                        db.child("customer spend").child(c_id).child("paid").set(new_spend)
                        self.new_created = True
                    bal_b = self.df2[self.df2["company name"] == self.entry_customer_id_combo.currentText()][
                        "opening balance"]
                    bal_b = list(bal_b)
                    bal_b = float(bal_b[0])
                    total_due = bal_b + self.sub_total_amount - prev_total - self.paid - self.discount + prev_discount + prev_paid
                    words = p.number_to_words(int(self.sub_total_amount - self.discount))
                    words_due = p.number_to_words(int(self.sub_total_amount - self.discount - self.paid))
                    discount_perc = (self.discount / self.sub_total_amount) * 100
                    table_bottom = Template(self.table_bottom).safe_substitute(
                        sub_total="{:.2f}".format(self.sub_total_amount),
                        discount_percent="{:.2f}".format(discount_perc), discount="{:.2f}".format(self.discount),
                        after_discount="{:.2f}".format(self.sub_total_amount  - self.discount),
                        tax_percent="0.0", tax_amount="0.00",
                        total="{:.2f}".format(self.sub_total_amount - self.discount),
                        in_word=words,
                        paid=str(self.paid),
                        due=str(self.sub_total_amount - self.discount - self.paid),
                        in_word_due=words_due)
                    top = Template(self.top).safe_substitute(css_link=bootstrap_css_url, logo_png=logo_url, dimension_png=dimension_url,
                                                             invoice_id=self.save_data["invoice id"],
                                                             client=company_name, address=self.save_data["address"],
                                                             zone=self.save_data["location"],
                                                             sales_by=self.save_data["employee name"],
                                                             due="",
                                                             order_date=self.save_data["booking date"],
                                                             delivery_date=self.save_data["delivery date"])
                    #due="{:.2f}".format(total_due),
                    bottom = Template(self.bottom).safe_substitute(js_link=bootstrap_js_url)
                    html = top + self.table_top + self.tb_row + table_bottom + bottom
                    self.save_file(html)
                    bal_a = bal_b + self.sub_total_amount - prev_total - self.paid - self.discount + prev_discount + prev_paid
                    db.child('customer').child(customerId).child('opening balance').set(bal_a)
                    self.refresh = False
                    try:
                        recipientNumber = self.df2[self.df2["company name"] == self.entry_customer_id_combo.currentText()]["number"]
                        recipientNumber = list(recipientNumber)
                        recipientNumber = recipientNumber[0]
                        or_id = self.save_data["invoice id"]
                        d_date = self.save_data["delivery date"]
                        bill = '{:.2f}'.format(self.sub_total_amount - self.discount)
                        smsText = f"Your order {or_id} has been updated. Total bill amount is {bill} taka and estimated delivery date is {d_date}."
                        client.service.OneToOne(userName, password, recipientNumber, smsText, smsType, maskName, campaignName)
                        #bill = '{:.2f}'.format(bal_a)
                        #smsText = f'Dear Customer, Your total due is {bill} taka.'
                        #client.service.OneToOne(userName, password, recipientNumber, smsText, smsType, maskName, campaignName)
                    except Exception as e:
                        print(e)
                    self.tb_row = """"""
                    self.set_all_field()
                    """self.dialog.message_text.setText("Data Saved")
                    self.dialog.displayInfo()"""
                    return True
                except Exception as e:
                    print(e)
                    self.dialog.message_text.setText("Error saving data")
                    self.dialog.displayInfo()
                    return False
            else:
                self.dialog.message_text.setText("Fill up all the fields")
                self.dialog.displayInfo()
                return False
        except Exception as e:
            print(e)
            self.dialog.message_text.setText("No internet")
            self.dialog.displayInfo()
            return False

    def customer_changed(self):
        self.new_created3 = False
        try:
            if len(list(self.df2[self.df2["company name"]==self.entry_customer_id_combo.currentText()]["address"]))!=0:
                addr = self.df2[self.df2["company name"]==self.entry_customer_id_combo.currentText()]["address"]
                addr = list(addr)
                addr = addr[0]
                self.entry_address_line_edit.setText(addr)
                zone = self.df2[self.df2["company name"] == self.entry_customer_id_combo.currentText()]["zone"]
                zone = list(zone)
                zone = zone[0]
                self.entry_location_line_edit.setText(zone)
        except:
            self.dialog.message_text.setText("No internet")
            self.dialog.displayInfo()

    def add_product(self):
        quantity = self.entry_quantity_spin.value()
        if quantity == 0:
            quantity = 1
        if quantity > 0:
            self.entry_table.setRowCount(self.row_count)
            row = self.row_count - 1
            self.entry_table.setItem(row, 0, QTableWidgetItem(str(row)))
            self.entry_table.setItem(row, 1, QTableWidgetItem(self.entry_product_id_combo.currentText()))
            self.entry_table.setItem(row, 2, QTableWidgetItem(self.entry_product_name_combo.currentText()))
            price = list(self.df[self.df["id"]==self.entry_product_id_combo.currentText()]["price"])
            price = price[0]
            self.sub_total_amount = self.sub_total_amount + (float(price) * quantity)
            tot = f'{float(price) * quantity}'
            self.entry_table.setItem(row, 3, QTableWidgetItem(f'{price}'))
            self.entry_table.setItem(row, 4, QTableWidgetItem(f'{quantity}'))
            self.entry_table.setItem(row, 5, QTableWidgetItem(tot))
            self.sub_total.setText(f'{self.sub_total_amount}')
            dict = {
                "Serial No": row,
                "Product ID": self.entry_product_id_combo.currentText(),
                "Product Name": self.entry_product_name_combo.currentText(),
                "Unit Price": price,
                "Quantity": quantity,
                "Total": tot
            }
            dict2 = {
                "Serial No": row,
                "Product ID": self.entry_product_id_combo.currentText(),
                "Product Name": self.entry_product_name_combo.currentText(),
                "Unit Price": price,
                "Quantity": 0,
                "Total": 0.0
            }
            self.products_dict[f"{row}"] = dict
            self.old_product_dict[f"{row}"] = dict2
            self.row_count = self.row_count+1
            self.entry_quantity_spin.setValue(0)
        else:
            self.dialog.message_text.setText("Please select quantity")
            self.dialog.displayInfo()

    def id_changed(self):
        try:
            dt = self.entry_product_id_combo.currentText()
            name = list(self.df[self.df['id'] == dt]['name'])
            self.entry_product_name_combo.setCurrentText(name[0])
            stock = list(self.df[self.df['name'] == dt]['stock'])
            stock = stock[0]
            if str(stock) == 'nan':
                stock = 0
            else:
                stock = int(stock)
            if stock <= 0:
                self.entry_add_btn.setEnabled(False)
            else:
                self.entry_add_btn.setEnabled(True)
        except:
            pass

    def name_changed(self):
        try:
            dt = self.entry_product_name_combo.currentText()
            ids = list(self.df[self.df['name'] == dt]['id'])
            self.entry_product_id_combo.setCurrentText(ids[0])
            stock = list(self.df[self.df['name'] == dt]['stock'])
            stock = stock[0]
            if str(stock) == 'nan':
                stock = 0
            else:
                stock = int(stock)
            if stock <= 0:
                self.entry_add_btn.setEnabled(False)
            else:
                self.entry_add_btn.setEnabled(True)
        except:
            pass


    def show_me(self):
        self.clear_n_new()
        self.show()

    def clear_n_new(self):
        self.sub_total_amount = 0.00
        self.createTable()
        #print("Sdsdsd")
        self.file_location_line_edit.setText('')
        self.products_dict = {}
        self.save_data = {}
        self.old_product_dict = {}
        self.products_dict_final = {}
        self.prevSpend = 0.0
        self.new_created = False
        self.discount = 0
        self.paid = 0
        try:
            try:
                self.dat = db.child('product').get().val()
                self.df = pd.DataFrame(self.dat, columns=self.dat.keys())
                self.df = self.df.transpose()
                self.dat2 = db.child('customer').get().val()
                self.df2 = pd.DataFrame(self.dat2, columns=self.dat2.keys())
                self.df2 = self.df2.transpose()
            except Exception as e:
                self.df2 = pd.DataFrame()
                self.df = pd.DataFrame()
                self.dialog.message_text.setText("Can not load data. Check internet connection")
                self.dialog.displayInfo()
            data_0 = db.child('invoice').shallow().get()
            #self.file_location_line_edit.setText('')
            self.save_location = ''
            data_0 = list(data_0.val())
            self.invoice_id.clear()
            for x in range(len(data_0)):
                self.invoice_id.addItem(data_0[x])
            self.entry_address_line_edit.setText("")
            self.entry_location_line_edit.setText("")
            self.sub_total.setText("0.00")
            self.booking_date.setDateTime(QtCore.QDateTime.currentDateTime())
            self.delivery_date.setDateTime(QtCore.QDateTime.currentDateTime())
            data_ = self.df['id']
            data_ = list(data_.values)
            self.entry_product_id_combo.clear()
            self.entry_product_name_combo.clear()
            formLayout = QFormLayout()
            groupBox = QGroupBox("Product List")
            labelLis = []
            comboList = []
            for x in range(len(data_)):
                self.entry_product_id_combo.addItem(data_[x])
                name = self.df[self.df["id"] == data_[x]]["name"]
                name = list(name)
                name = name[0]
                stock = self.df[self.df["id"] == data_[x]]["stock"]
                stock = list(stock)
                stock = stock[0]
                if str(stock) == 'nan':
                    stock = 0
                else:
                    stock = int(stock)
                self.entry_product_name_combo.addItem(name)
                labelLis.append(QLabel(name + f' ({stock} in stock)'))
                comboList.append(QPushButton('ADD', self))
                comboList[x].clicked.connect(partial(self.set_item, name = name))
                if stock <= 0:
                    comboList[x].setEnabled(False)
                else:
                    comboList[x].setEnabled(True)
                formLayout.addRow(labelLis[x], comboList[x])
            groupBox.setLayout(formLayout)
            self.product_list.setWidget(groupBox)
            self.product_list.setWidgetResizable(True)
            _data__ = list(self.df2["company name"])
            self.entry_customer_id_combo.clear()
            for x in range(len(_data__)):
                self.entry_customer_id_combo.addItem(_data__[x])
            dat = db.child('user').get().val()
            df = pd.DataFrame(dat, columns=dat.keys())
            df = df.transpose()
            _data__1 = list(df["first name"])
            _data__2 = list(df["last name"])
            self.entry_employee_name_combo.clear()
            for x in range(len(_data__1)):
                self.entry_employee_name_combo.addItem(_data__1[x] + " " +  _data__2[x])
            first_name = db.child('user').child(auth.current_user['localId']).child('first name').get().val()
            last_name = db.child('user').child(auth.current_user['localId']).child('last name').get().val()
            self.entry_employee_name_combo.setCurrentText(first_name + " " + last_name)
            self.refresh = True
            self.saved_data1 = []
            self.saved_data2 = []
            self.saved_data3 = 0.00
            self.saved_data4 = []
            self.new_created1 = []
            self.new_created2 = []
            self.new_created3 = False
            self.set_all_field()
        except Exception as e:
            print(e)
            self.dialog.message_text.setText("failed to fetch data or no records found")
            self.dialog.displayInfo()

    def edit(self):
        #self.clear_n_new()
        self.save_n_new_btn.setEnabled(True)
        self.save_n_exit_btn.setEnabled(True)
        self.print_btn.setEnabled(True)
        self.set_all_field()

    def set_all_field(self):
        self.file_location_line_edit.setText('')
        self.createTable()
        self.products_dict = {}
        self.save_data = {}
        self.old_product_dict = {}
        self.products_dict_final = {}
        self.discount = 0
        self.paid = 0
        self.sub_total_amount = 0
        self.prevSpend = 0
        try:
            self.dat = db.child('product').get().val()
            self.df = pd.DataFrame(self.dat, columns=self.dat.keys())
            self.df = self.df.transpose()
            self.dat2 = db.child('customer').get().val()
            self.df2 = pd.DataFrame(self.dat2, columns=self.dat2.keys())
            self.df2 = self.df2.transpose()
        except Exception as e:
            self.df2 = pd.DataFrame()
            self.df = pd.DataFrame()
            self.dialog.message_text.setText("Can not load data. Check internet connection")
            self.dialog.displayInfo()
        try:
            self.save_data = dict(db.child('invoice').child(self.invoice_id.currentText()).get().val())
            #print(self.save_data)
            i_id = self.invoice_id.currentText()
            #dirr = os.getcwd()
            dirr = file_save_path
            dirr = os.path.join(dirr, 'invoice')
            if not os.path.isdir(dirr):
                os.mkdir(dirr)
            dir = f'{i_id}.pdf'
            dir = os.path.join(dirr, dir)
            self.file_location_line_edit.setText(dir)
            y = 1
            for x in range(len(self.save_data['products'])):
                if self.save_data['products'][x] != None:
                    self.products_dict[f'{y}'] = self.save_data['products'][x]
                    y = y + 1
            self.bef_new = y - 1
            for key in self.products_dict.keys():
                dicto = {
                    "Serial No": self.products_dict[key]['Serial No'],
                    "Product ID": self.products_dict[key]['Product ID'],
                    "Product Name": self.products_dict[key]['Product Name'],
                    "Unit Price": self.products_dict[key]['Unit Price'],
                    "Quantity": self.products_dict[key]['Quantity'],
                    "Total": self.products_dict[key]['Total']
                }
                self.old_product_dict[key] = dicto
            self.entry_customer_id_combo.setCurrentText(self.save_data['customer id'])
            self.entry_address_line_edit.setText(self.save_data['address'])
            self.entry_location_line_edit.setText(self.save_data['location'])
            self.entry_employee_name_combo.setCurrentText(self.save_data['employee name'])
            self.paidSpinBox.setValue(self.save_data['paid'])
            self.discountSpinBox.setValue(self.save_data['discount'])
            format_str = '%Y-%m-%d'
            datetime_book = datetime.datetime.strptime(self.save_data['booking date'], format_str)
            # qtDate_book = QtCore.QDate.fromString(datetime_book, 'yyyy-MM-dd')
            datetime_delivery = datetime.datetime.strptime(self.save_data['delivery date'], format_str)
            # qtDate_delivery = QtCore.QDate.fromString(datetime_delivery, 'yyyy-MM-dd')
            self.booking_date.setDateTime(datetime_book)
            self.delivery_date.setDateTime(datetime_delivery)

            for product in self.products_dict:
                self.entry_table.setRowCount(self.row_count)
                row = self.row_count - 1
                self.entry_table.setItem(row, 0, QTableWidgetItem(str(row)))
                self.entry_table.setItem(row, 1, QTableWidgetItem(str(self.products_dict[f'{product}']['Product ID'])))
                self.entry_table.setItem(row, 2, QTableWidgetItem(self.products_dict[f'{product}']['Product Name']))
                self.entry_table.setItem(row, 3, QTableWidgetItem(str(self.products_dict[f'{product}']['Unit Price'])))
                self.entry_table.setItem(row, 4, QTableWidgetItem(str(self.products_dict[f'{product}']['Quantity'])))
                self.entry_table.setItem(row, 5, QTableWidgetItem(str(self.products_dict[f'{product}']['Total'])))
                self.row_count = self.row_count + 1
            self.sub_total_amount = self.save_data["sub total"]
            self.sub_total.setText(str(self.save_data["sub total"]))
        except Exception as e:
            print(e)
            self.dialog.message_text.setText("failed to fetch data or no records found")
            self.dialog.displayInfo()

    def set_item(self, name):
        self.entry_product_name_combo.setCurrentText(name)
        self.name_changed()
        self.add_product()

    def createTable(self):
        self.entry_table.clear()
        self.row_count = 1
        self.entry_table.setRowCount(1)
        self.row_count = self.row_count + 1
        self.entry_table.setColumnCount(6)
        self.entry_table.setItem(0, 0, QTableWidgetItem("Serial No"))
        self.entry_table.setItem(0, 1, QTableWidgetItem("Product ID"))
        self.entry_table.setItem(0, 2, QTableWidgetItem("Product Name"))
        self.entry_table.setItem(0, 3, QTableWidgetItem("Unit Price"))
        self.entry_table.setItem(0, 4, QTableWidgetItem("Quantity"))
        self.entry_table.setItem(0, 5, QTableWidgetItem("Total"))
        """self.entry_table.setItem(1, 0, QTableWidgetItem("Cell (2,1)"))
        self.entry_table.setItem(1, 1, QTableWidgetItem("Cell (2,2)"))
        self.entry_table.setItem(2, 0, QTableWidgetItem("Cell (3,1)"))
        self.entry_table.setItem(2, 1, QTableWidgetItem("Cell (3,2)"))
        self.entry_table.setItem(3, 0, QTableWidgetItem("Cell (4,1)"))
        self.entry_table.setItem(3, 1, QTableWidgetItem("Cell (4,2)"))"""
        self.entry_table.move(0, 0)

        # table selection change
        self.entry_table.itemChanged.connect(self.on_change)
        self.entry_table.itemDoubleClicked.connect(self.on_select)

    @pyqtSlot()
    def on_select(self):
        for currentQTableWidgetItem in self.entry_table.selectedItems():
            self.pre_selected_row = currentQTableWidgetItem.row()
            self.pre_selected_col = currentQTableWidgetItem.column()

    @pyqtSlot()
    def on_change(self):
        for currentQTableWidgetItem in self.entry_table.selectedItems():
            if currentQTableWidgetItem.row() == self.pre_selected_row and currentQTableWidgetItem.column() == self.pre_selected_col:
                if currentQTableWidgetItem.text() != self.pre_selected:
                    #print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())
                    column_name = self.entry_table.item(0, currentQTableWidgetItem.column()).text()
                    #print(column_name)
                    unit = self.entry_table.item(currentQTableWidgetItem.row(), 4).text()
                    unit_pr = self.entry_table.item(currentQTableWidgetItem.row(), 3).text()
                    it_tot = float(unit_pr)*float(unit)
                    self.products_dict[f"{currentQTableWidgetItem.row()}"][column_name] = currentQTableWidgetItem.text()
                    self.products_dict[f"{currentQTableWidgetItem.row()}"]['Total'] = float(self.products_dict[f"{currentQTableWidgetItem.row()}"]['Quantity']) * float(self.products_dict[f"{currentQTableWidgetItem.row()}"]['Unit Price'])
                    """if currentQTableWidgetItem.row() > self.bef_new:
                        self.old_product_dict[f"{currentQTableWidgetItem.row()}"][
                            column_name] = currentQTableWidgetItem.text()
                        self.old_product_dict[f"{currentQTableWidgetItem.row()}"]['Total'] = float(
                            self.old_product_dict[f"{currentQTableWidgetItem.row()}"]['Quantity']) * float(
                            self.old_product_dict[f"{currentQTableWidgetItem.row()}"]['Unit Price'])"""
                    self.pre_selected = currentQTableWidgetItem.text()
                    self.entry_table.setItem(currentQTableWidgetItem.row(), 5, QTableWidgetItem(f'{it_tot}'))
                else:
                    self.pre_selected = ''
                total = 0
                for x in range(1, self.entry_table.rowCount()):
                    total = total + float(self.entry_table.item(x, 5).text())
                self.sub_total.setText(f'{total}')
                self.sub_total_amount = total

        self.pre_selected_row = -1
        self.pre_selected_col = -1

class RegisterUIClass(QMainWindow, register.Ui_MainWindow):
    def __init__(self, parent=None):
        super(RegisterUIClass, self).__init__(parent)
        self.setupUi(self)
        self.dialog = Dialog()
        self.reg_btn.clicked.connect(self.register_func)

    def register_func(self):
        email = self.email_reg.text()
        pass_ = self.pass_reg.text()
        pass_c = self.pass_confirm_reg.text()
        first_name = self.first_name_reg.text()
        last_name = self.last_name_reg.text()
        if email!='' and pass_!='' and pass_c!='' and first_name!='' and last_name!='':
            if pass_ == pass_c:
                try:
                    user = auth.create_user_with_email_and_password(email, pass_)
                    user_id = user['localId']
                    data = {'id': user_id, 'first name': first_name, 'last name': last_name, 'admin': 0, 'staff': 1}
                    db.child("user").child(user_id).set(data)
                    self.dialog.message_text.setText("Registration successful")
                    self.dialog.displayInfo()
                    self.close()
                except Exception as e:
                    self.email_reg.setText("")
                    self.pass_reg.setText("")
                    self.pass_confirm_reg.setText("")
                    self.first_name_reg.setText("")
                    self.last_name_reg.setText("")
                    self.dialog.message_text.setText("An error occurred")
                    #print(e)
                    self.dialog.displayInfo()
            else:
                self.pass_reg.setText("")
                self.pass_confirm_reg.setText("")
                self.dialog.message_text.setText("Enter password correctly")
                self.dialog.displayInfo()
        else:
            self.pass_reg.setText("")
            self.pass_confirm_reg.setText("")
            self.dialog.message_text.setText("Please fill up empty fields")
            self.dialog.displayInfo()

    def show_me(self):
        self.email_reg.setText("")
        self.pass_reg.setText("")
        self.pass_confirm_reg.setText("")
        self.first_name_reg.setText("")
        self.last_name_reg.setText("")
        self.show()

class LoginUIClass(QMainWindow, login.Ui_MainWindow):
    switch_window = QtCore.pyqtSignal(str)
    def __init__(self, parent=None):
        super(LoginUIClass, self).__init__(parent)
        self.setupUi(self)
        self.RegisterButton.clicked.connect(self.register_func)
        self.LoginButton.clicked.connect(self.login_func)
        self.dialog = Dialog()
        self.register = RegisterUIClass()

    def register_func(self):
        self.register.show_me()

    def login_func(self):
        email = self.EmailLine.text()
        password = self.PassLine.text()
        try:
            user = auth.sign_in_with_email_and_password(email,password)
            access = db.child('user').child(user['localId']).child('staff').get().val()
            if access:
                if self.checkBox_remember_me.isChecked():
                    file_loc = os.path.join(user_info_file_loc, 'login_info.info')
                    with open(file_loc, 'w') as f:
                        f.write(f'{email},{password},end')
                self.switch_window.emit("Logged in")
            else:
                self.dialog.message_text.setText("you do not have permission to login")
                self.dialog.displayInfo()
        except Exception as e:
            self.dialog.message_text.setText("error")
            self.dialog.displayInfo()
            print(e)

class Dialog(QtWidgets.QDialog, message.Ui_Dialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        self.setupUi(self)

    def displayInfo(self):
        self.show()

class Dialog2(QtWidgets.QDialog, message2.Ui_Dialog):
    def __init__(self, parent=None):
        super(Dialog2, self).__init__(parent)
        self.setupUi(self)

    def displayInfo(self):
        self.show()

class ThreadClass(QtCore.QThread):
    #signal = pyqtSignal('PyQt_PyObject')
    #signal_2 = pyqtSignal('PyQt_PyObject')
    def __init__(self, parent = None):
        super(ThreadClass, self).__init__(parent)

    def run(self):
        while 1:
            user = auth.current_user
            if user:
                user = auth.refresh(user['refreshToken'])
            time.sleep(30*60)

class Controller:
    def __init__(self):
        pass
    def show_login(self):
        self.window = LoginUIClass()
        self.window.switch_window.connect(self.show_window_main)
        self.window.show()

    def show_window_main(self):
        self.window_two = MainUIClass()
        self.window.close()
        self.window_two.show()

    def show_window_main_direct(self):
        self.window_two = MainUIClass()
        self.window_two.show()

def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    file_location = os.path.join(user_info_file_loc, 'login_info.info')
    if os.path.exists(file_location):
        with open(file_location, 'r') as f:
            data = f.readlines()[0].split(',')
            email = data[0]
            pass_w = data[1]
            user = auth.sign_in_with_email_and_password(email, pass_w)
            access = db.child('user').child(user['localId']).child('staff').get().val()
            if access:
                controller.show_window_main_direct()
    else:
        controller.show_login()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()