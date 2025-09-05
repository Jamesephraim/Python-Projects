import openpyxl
import os
#pip install openpyxl

filepath=r"data1.xlsx"


if not os.path.exists(filepath):
    workbook=openpyxl.Workbook()
    Sheet1=workbook.active
    headings=['Pin','Name','Age','Branch']
    Sheet1.append(headings)
    workbook.save(filepath)
