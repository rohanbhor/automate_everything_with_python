from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit

def make_sentence():
    input_text = txt.text()
    output_label.setText(input_text.capitalize() + '.')

app = QApplication([])
window = QWidget()
window.setWindowTitle("Sentence Maker")

layout = QVBoxLayout()

# Create a text widget and add it to the layout
txt = QLineEdit()
layout.addWidget(txt)

# Create a button widget and add it to the layout
btn = QPushButton('Make')
layout.addWidget(btn)

# widget -> signal -> slot
btn.clicked.connect(make_sentence)

# Add a label widget to show the output
output_label = QLabel('')
layout.addWidget(output_label)

window.setLayout(layout)
window.show()
app.exec()