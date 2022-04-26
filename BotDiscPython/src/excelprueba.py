from operator import index
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Font
import time
from index import palabras1 as pl1

book = Workbook()
sheet = book.active
#plA = pl1.mensaje3

def makesheet():
    sheet["B1"] = "Hola mundo"
    sheet["A2"] = "Pato"
    #sheet["E3"] = plA

makesheet()
book.save("C:/Users/franc/Escritorio/BotDiscPython/DataBase/ExcelPrueba.xlsx")
