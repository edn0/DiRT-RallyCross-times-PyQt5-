import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor

widgets = {
    "logo": [],
    "button": [],
    "leaderboard": [],
    "trackSelectPrompt": []
}

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("DiRT RallyCross Lap Times")
window.setFixedWidth(1000)
window.setStyleSheet("background: #999999;")

grid = QGridLayout()
window.setLayout(grid)

def timeEntryFrame():
    # Display logo
    image = QPixmap("logo.png")
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignLeft)
    logo.setStyleSheet("margin-bottom: 100px;")
    widgets["logo"].append(logo)

    # Button widget
    button = QPushButton("Add time")
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setStyleSheet(
    "*{border: 4px solid '#ff0505';"+
    "border-radius:15px;"+
    "font-size: 27px;"+
    "margin: 20px 200px;"+
    "color: 'white'}"+
    "*:hover{background: '#ff0505';"+
    "font-size: 30px;}"
    )
    widgets["button"].append(button)

    # Adding the text above the combobox
    trackSelectPrompt = QLabel("Select your track")
    trackSelectPrompt.setAlignment(QtCore.Qt.AlignCenter)
    trackSelectPrompt.setStyleSheet(
        "font-size: 27px;"+
        "color: 'white';"+
        "margin: 5px 100px;"
    )
    widgets["trackSelectPrompt"].append(trackSelectPrompt)
    # QLabelvar, row pos, column pos
    grid.addWidget(widgets["logo"][-1], 0, 0)
    grid.addWidget(widgets["button"][-1], 5, 0)
    grid.addWidget(widgets["trackSelectPrompt"][-1], 1, 0)

timeEntryFrame()

# This will be the frame your are taken to after you submit your time
def scoreboardFrame():
    leaderboard = QLabel("Placeholder for scores")
    leaderboard.setAlignment(QtCore.Qt.AlignCenter)
    leaderboard.setStyleSheet(
        "font-size: 20px;"+
        "color: 'white';"+
        "margin: 100px 20px;"

    )
    widgets["leaderboard"].append(leaderboard)

    grid.addWidget(widgets["leaderboard"][-1], 1, 0, 2, 2)


window.show()
sys.exit(app.exec())
