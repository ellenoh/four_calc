from PyQt4 import QtGui
import fourcalc_ui

OP_ADD = 'add'
OP_SUBTRACT = 'subtract'
OP_DIVIDE = 'divide'
OP_MULTIPLY = 'multiply'
OP_EQUAL = 'equal'

ALL_OPS = [OP_ADD, OP_SUBTRACT, OP_MULTIPLY, OP_DIVIDE]

class Calculator(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.ui = fourcalc_ui.Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Calculator")
        self.last_num = 0
        self.last_op = 'nothing'
        self.hold_val = False
        self.ui.output_le.setText('0')
        
        self.ui.k0_btn.clicked.connect(self.press_zero)
        self.ui.k1_btn.clicked.connect(self.press_one)
        self.ui.k2_btn.clicked.connect(self.press_two)
        self.ui.k3_btn.clicked.connect(self.press_three)
        self.ui.k4_btn.clicked.connect(self.press_four)
        self.ui.k5_btn.clicked.connect(self.press_five)
        self.ui.k6_btn.clicked.connect(self.press_six)
        self.ui.k7_btn.clicked.connect(self.press_seven)   
        self.ui.k8_btn.clicked.connect(self.press_eight)
        self.ui.k9_btn.clicked.connect(self.press_nine)
        
        self.ui.decimal_btn.clicked.connect(self.press_decimal)
        self.ui.back_btn.clicked.connect(self.backSpace)
        
        self.ui.add_btn.clicked.connect(self.doAdd)
        self.ui.minus_btn.clicked.connect(self.doSubtract)
        self.ui.equal_btn.clicked.connect(self.doEqual)
        self.ui.clr_btn.clicked.connect(self.doClear)
        self.ui.multiply_btn.clicked.connect(self.doMultiply)
        self.ui.divide_btn.clicked.connect(self.doDivide)

                      
    def doClear(self):
        """
        Clears the calculator
        """
        self.last_num = 0
        self.last_op = 'nothing'
        self.ui.output_le.setText('0')
        
    def doDivide(self):
        self.doLastOp()        
        self.last_num = float(self.ui.output_le.text())
        self.last_op = OP_DIVIDE
            
    def doMultiply(self):
        self.doLastOp()            
        self.last_num = float(self.ui.output_le.text())
        self.last_op = OP_MULTIPLY
        
    def doSubtract(self):
        self.doLastOp()                
        self.last_num = float(self.ui.output_le.text())
        self.last_op = OP_SUBTRACT
        
    def doEqual(self):
        self.doLastOp()
        self.last_num = 0
        self.last_op = 'equal'
        self.hold_val = True
        
    def doAdd(self):
        self.doLastOp()        
        self.last_num = float(self.ui.output_le.text())
        self.last_op = OP_ADD
    
    def doLastOp(self):
        """
        Sets the last operation and stores the last number
        """
        if self.last_op == OP_ADD:
            new_num = self.last_num + float(self.ui.output_le.text())
            self.updateScreen(new_num)
        elif self.last_op == OP_SUBTRACT:
            new_num = self.last_num - float(self.ui.output_le.text())
            self.updateScreen(new_num)
        elif self.last_op == OP_MULTIPLY:
            new_num = self.last_num * float(self.ui.output_le.text())
            self.updateScreen(new_num)              
        elif self.last_op == OP_DIVIDE:
            new_num = self.last_num / float(self.ui.output_le.text())
            self.updateScreen(new_num)
        self.hold_val = True

    def updateScreen(self, new_num):
        self.last_num = new_num
        if str(new_num)[-2:] =='.0':
            self.ui.output_le.setText(str(int(new_num)))
        else:
            self.ui.output_le.setText(str(new_num))
        
    def press_zero(self):
        self.appendNumber(0)  
    def press_one(self):
        self.appendNumber(1)  
    def press_two(self):
        self.appendNumber(2)  
    def press_three(self):
        self.appendNumber(3)      
    def press_four(self):
        self.appendNumber(4)     
    def press_five(self):
        self.appendNumber(5)    
    def press_six(self):
        self.appendNumber(6)        
    def press_seven(self):
        self.appendNumber(7)     
    def press_eight(self):
        self.appendNumber(8)    
    def press_nine(self):
        self.appendNumber(9)
        
    def press_decimal(self):
        if self.hold_val:
            self.ui.output_le.setText('0.')
            self.hold_val = False
        elif '.' not in self.ui.output_le.text():
            self.ui.output_le.setText(self.ui.output_le.text() + '.')

    def appendNumber(self, num):
        cur_txt = self.ui.output_le.text()
        if cur_txt == '0':
            cur_txt = ''
        elif self.hold_val:
            cur_txt = ''
            self.hold_val = False
        cur_txt += str(num)
        self.ui.output_le.setText(cur_txt)
    
    def backSpace(self):
        cur_txt = self.ui.output_le.text()
        self.ui.output_le.setText(cur_txt[0:-1])

if __name__ == '__main__':
    app = QtGui.QApplication([])
    window = Calculator()
    window.show()
    app.exec_()
