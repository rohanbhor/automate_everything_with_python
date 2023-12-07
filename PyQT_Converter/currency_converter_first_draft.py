from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QComboBox
from PyQt6.QtCore import Qt
from bs4 import BeautifulSoup
import requests

def get_currency(in_currency, out_currency):
    url = f"https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1"
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    rate = soup.find("span", class_='ccOutputRslt').getText()
    return float(rate.split()[0])

def show_currency():
    input_text = txt.text()
    in_currency = in_combo.currentText()
    out_currency = target_combo.currentText()
    rate = get_currency(in_currency, out_currency)
    output = float(input_text) * rate
    output_label.setText(str(output))

app = QApplication([])
window = QWidget()
window.setWindowTitle("Currency Converter")

layout = QVBoxLayout()

# Add a dropdown widget to the layout
currencies = ["USD", "INR", "CAD", "CNY", "AUD", "CHF", "MXN"]
in_combo = QComboBox()
in_combo.addItems(currencies)
layout.addWidget(in_combo)

# Add a dropdown widget to the layout
target_combo = QComboBox()
target_combo.addItems(currencies)
layout.addWidget(target_combo)

# Create a text widget and add it to the layout
txt = QLineEdit()
layout.addWidget(txt)

# Create a button widget and add it to the layout
btn = QPushButton('Convert')
layout.addWidget(btn)

# widget -> signal -> slot
btn.clicked.connect(show_currency)

# Add a label widget to show the output
output_label = QLabel('')
layout.addWidget(output_label)



window.setLayout(layout)
window.show()
app.exec()