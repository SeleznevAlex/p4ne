from matplotlib import pyplot
from openpyxl import load_workbook

wb = load_workbook('data_analysis_lab.xlsx')
sheetData = wb['Data']
columnA = sheetData['A'][1:]
columnB = sheetData['B'][1:]
columnC = sheetData['C'][1:]
columnD = sheetData['D'][1:]


def getvalue(x):
    return x.value


years = list(map(getvalue, columnA))
temps = list(map(getvalue, columnB))
otn_temps = list(map(getvalue, columnC))
k_sun = list(map(getvalue, columnD))

pyplot.plot(years, otn_temps, label="Graph of otn temperature")
pyplot.plot(years, k_sun, label="Graph of sun's activity")
pyplot.show()
