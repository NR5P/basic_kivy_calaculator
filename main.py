import kivy

from kivy.app import App
from kivy.uix.gridlayout import GridLayout


class CalcGridLayout(GridLayout):
    def calculate(self, calculation):
        if calculation:
            try:
                self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = "Error"

    def operator_check(self, operator):
        operator_list = ["/", "*", "-", "+"]
        if self.display.text[-1] in operator_list:
            self.display.text = self.display.text[:-1]
            self.display.text += operator
        else:
            self.display.text += operator

    def period_check(self):
        if self.display.text[-1] != ".":
            self.display.text += "."

    def del_function(self):
        self.display.text = self.display.text[:-1]


class CalculatorApp(App):
    title = "basic kivy calculator"

    def build(self):
        return CalcGridLayout()


CalculatorApp().run()