import pandas as pd
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
import sys

rawSheets = pd.read_excel(
    "C:/dane/Nauka/NiemieckiA1/bazaSlowek.ods",
    sheet_name=None,
    header=None,
    engine="odf",
)

oneBigSheet = [
    tuple(row)
    for df in rawSheets.values()
    for row in df.itertuples(index=False, name=None)
]

noNaNs = [
    tuple(x for x in row if not pd.isna(x) and 'END' not in row)
    for row in oneBigSheet
]

for entry in noNaNs:
    print(entry)

# app = QApplication(sys.argv)
# window = QWidget()
# window = QMainWindow()
# window.show()
# app.exec()