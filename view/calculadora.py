from PyQt5.QtWidgets import QMainWindow, QShortcut
from PyQt5.uic import loadUi
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import pyqtSlot, QTimer
from funcoes import somar, dividir, multiplicar, subtrair, porcentagem

from os import path
import sys

def loadFile(file):
    base_path = getattr(sys, "_MEIPASS", path.dirname(path.abspath(__file__)))
    return path.join(base_path, file)

class Calculadora(QMainWindow):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        loadUi(loadFile("view/calculadora.ui"), self)
        self.show()

        self.num1 = 0
        self.num2 = 0
        self.finish = False
        self.selectedOperation = None
        self.operationList = {
            "+": somar,
            "-": subtrair,
            "x": multiplicar,
            "÷": dividir,
            "%": porcentagem
        }

        self.btn_1.clicked.connect(lambda: self.addNumber(1))
        self.btn_2.clicked.connect(lambda: self.addNumber(2))
        self.btn_3.clicked.connect(lambda: self.addNumber(3))
        self.btn_4.clicked.connect(lambda: self.addNumber(4))
        self.btn_5.clicked.connect(lambda: self.addNumber(5))
        self.btn_6.clicked.connect(lambda: self.addNumber(6))
        self.btn_7.clicked.connect(lambda: self.addNumber(7))
        self.btn_8.clicked.connect(lambda: self.addNumber(8))
        self.btn_9.clicked.connect(lambda: self.addNumber(9))
        self.btn_0.clicked.connect(lambda: self.addNumber(0))
        self.btn_ac.clicked.connect(self.cleanDisplay)
        self.btn_del.clicked.connect(self.deletar)
        self.btn_inv.clicked.connect(self.invert)
        self.btn_igual.clicked.connect(self.showResult)
        self.btn_vir.clicked.connect(self.addComma)
        self.btn_mais.clicked.connect(lambda: self.setOperation("+"))
        self.btn_menos.clicked.connect(lambda: self.setOperation("-"))
        self.btn_vezes.clicked.connect(lambda: self.setOperation("x"))
        self.btn_div.clicked.connect(lambda: self.setOperation("÷"))
        self.btn_por.clicked.connect(self.percent)

    def timerClean(self):
        self.cronometro = QTimer(self)
        self.cronometro.singleShot(2000, self.timeOutClean)

    def timeOutClean(self):
        self.btn_inv.setEnabled(True)
        self.btn_igual.setEnabled(True)
        self.btn_mais.setEnabled(True)
        self.btn_menos.setEnabled(True)
        self.btn_vezes.setEnabled(True)
        self.btn_div.setEnabled(True)
        self.btn_por.setEnabled(True)
        self.display.setText("0")
        self.display2.setText("0")
        self.num1 = 0
        self.num2 = 0
        self.selectedOperation = None

    def addNumber(self, numero):
        label = self.display.text()
        if label == "0" or self.finish:
            self.finish = False
            res = str(numero)
        else:
            res = label + str(numero)
        self.display.setText(res)

    def addComma(self):
        ultimo = self.display.text()
        if "," in ultimo:
            return
        else:
            result = ultimo + ","
            self.display.setText(result)

    def cleanDisplay(self):
        self.display.setText("0")
        self.display2.setText("0")
        self.num1 = 0
        self.num2 = 0

    def deletar(self):
        delet = self.display.text()
        delet = delet[:-1]

        if len(delet) == 0:
            delet = "0"

        self.display.setText(delet)

    def invert(self):
        numero = self.getNumberDisplay(self.display)
        numero = str(numero * -1)
        self.setNumberDisplay(numero)

    def percent(self):
        perc = self.getNumberDisplay(self.display)
        result = porcentagem(self.num1, perc)
        self.setNumberDisplay(result)

    def setOperation(self, operationList):
        self.selectedOperation = operationList
        self.num1 = self.getNumberDisplay(self.display)
        self.num2 = 0
        result = self.display.text()
        self.display2.setText(result)
        self.display.setText("0")
        self.btn_ac.setText("AC")

    def getNumberDisplay(self, display):
        num = display.text()
        if "," in num:
            num = num.replace(",", ".")
            num = float(num)
        else:
            num = int(num)
        return num
    
    def setNumberDisplay(self, num):
        num = str(num)
        num = num.replace(".", ",")
        self.display.setText(num)

    def setCalcDisplay(self, num1, num2, operation):
        num1 = str(num1).replace(".", ",")
        num2 = str(num2).replace(".", ",")
        result = f"{num1} {operation} {num2} = "
        self.display2.setText(result)

    def showResult(self):
        if self.selectedOperation:
            if self.num2 == 0:
                self.num2 = self.getNumberDisplay(self.display)

            num1 = self.num1
            num2 = self.num2

            operation = self.operationList.get(self.selectedOperation)
            result = operation(num1, num2)
            self.num1 = result

            self.setNumberDisplay(result)
            self.setCalcDisplay(num1, num2, self.selectedOperation)
            self.finish = True
            if isinstance(result, str):
                self.timerClean()