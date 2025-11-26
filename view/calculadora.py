from PyQt5.QtWidgets import QMainWindow, QShortcut
from PyQt5.uic import loadUi
from PyQt5.QtGui import QKeySequence
from funcoes import somar

class Calculadora(QMainWindow):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        loadUi("view/calculadora.ui", self)
        self.show()

        # QShortcut(QKeySequence("0"), self).activated.connect(lambda: self.addNumber(0))
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
        self.btn_igual.clicked.connect(self.showResult)
        self.btn_vir.clicked.connect(self.addComma)
        
    def addNumber(self, numero):
        label = self.display.text()
        if label == "0":
            res = str(numero)
        else:
            res = label + str(numero)
        self.display.setText(res)

    def cleanDisplay(self):
        self.display.setText("0")

    def showResult(self):
        num1 = self.display.text()
        if "," in num1:
            num1 = num1.replace(",", ".")
            num1 = float(num1)
        else:
            num1 = int(num1)
        num2 = 2
        result = somar(num1, num2)
        print(f"Número: {result}")

    def addComma(self):
        ultimo = self.display.text()
        if "," in ultimo:
            return
        else:
            result = ultimo + ","
            self.display.setText(result)
        