from operator import index
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Font
import time
from index import palabras1 as pl1

book = Workbook()
sheet = book.active
#plA = pl1.mensaje3

def makesheet():
    sheet["B1"] = "Hello world"
    sheet["A2"] = "Cuak"
    #sheet["E3"] = plA

makesheet()
book.save() #-> Here you add file adress.
