from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QComboBox, QHBoxLayout, QFileDialog
from PyQt6.QtCore import Qt
from pathlib import Path
from bs4 import BeautifulSoup
import requests

def open_files():
    global file_names
    file_names, _ = QFileDialog.getOpenFileNames(window, "Select Files")
    file_list.setText('\n'.join(file_names))

def destroy_files():
    for filename in file_names:
        path = Path(filename)
        with open(path, 'wb') as f:
            f.write(b'')
        path.unlink()
    file_list.setText("Files Destroyed Successfully!")


app = QApplication([])
window = QWidget()
window.setWindowTitle("File Destroyer")

layout = QVBoxLayout()

description = QLabel('Select the files you want to destroy. The files will be <font color="red">permanently</font> deleted')
layout.addWidget(description)

open_btn = QPushButton("Open Files")
open_btn.setToolTip("Open Files")
open_btn.setFixedWidth(100)
layout.addWidget(open_btn, alignment=Qt.AlignmentFlag.AlignCenter)

open_btn.clicked.connect(open_files)

destroy_btn = QPushButton("Destroy Files")
destroy_btn.setToolTip("Delete the files")
destroy_btn.setFixedWidth(100)
layout.addWidget(destroy_btn, alignment=Qt.AlignmentFlag.AlignCenter)

destroy_btn.clicked.connect(destroy_files)

file_list = QLabel('')
layout.addWidget(file_list, alignment=Qt.AlignmentFlag.AlignCenter)

window.setLayout(layout)
window.show()
app.exec()
