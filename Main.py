import FoldersList
from openpyxl import Workbook


excel_document = openpyxl.load_workbook('example.xlsx')
excel_document.get_sheet_by_name('Hoja 1')  #Accedemos a la hoja para obtener datos del excel.
excelList= []
list = collections.defaultdict(list)
for row in ws.iter_rows():
    excelList[row[0].value].append(row[1].value)


creditList = folderList()

for valor in excelList:              #recorro la lista de los creditos de excel.
	for file in creditList:		#recorro la lista de los archivos del disco compartido.
		if (value==file):       #comparo si el valor dentro de la lista de los creditos coincide con alguno de los archivos del disco compartido.
			print(value," se encuentra en el disco K")  #si es igual, imprimo que el numero esta. 
		else: 
			credits.append(value)

print credits

	