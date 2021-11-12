import csv
import sys
from PyQt5.QtWidgets import QApplication, QLineEdit, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout, QComboBox
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor
from data import trackList

widgets = {
    "logo": [],
    "button": [],
    "leaderboard": [],
    "trackSelectPrompt": [],
    "timeEntryPrompt": [],
    "trackCombobox": [],
    "submittedTime": [],
    "backButton": [],
    "leaderboard_button": [],
    "timeEntryButton": []
}

input = ""

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("DiRT RallyCross Lap Times")
window.setFixedWidth(800)
window.setStyleSheet("background: #999999;")

grid = QGridLayout()
window.setLayout(grid)

def clear_widgets():
    for widget in widgets:
        if widgets[widget] != []:
            widgets[widget][-1].hide()
        for i in range(0, len(widgets[widget])):
            widgets[widget].pop()


def saveTime():
    with open("times.csv", "w", newline="") as csvfile:
        timeWriter = csv.writer(csvfile, delimiter=" ", quotechar="|", quoting=csv.QUOTE_MINIMAL)
        timeWriter.writerow(["placeholder"])
        timeWriter.writerow(["_________________"])
        show_scoreboardFrame()

def show_timeEntryFrame():
    clear_widgets()
    timeEntryFrame()

def show_scoreboardFrame():
    clear_widgets()
    scoreboardFrame()

def timeEntryFrame():
    # Display logo
    image = QPixmap("logo.png")
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignLeft)
    logo.setStyleSheet("margin-bottom: 10px;")
    widgets["logo"].append(logo)

    # Button widget
    button = QPushButton("Add time")
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.clicked.connect(saveTime)
    button.setStyleSheet(
    "*{border: 4px solid '#ff0505';"+
    "border-radius:15px;"+
    "font-size: 27px;"+
    "margin: 20px 200px;"+
    "background-color: 'grey';"+
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

    # The combobox will go here
    trackCombobox = QComboBox()
    trackCombobox.addItems(trackList)
    trackCombobox.setStyleSheet(
    "QComboBox {combobox-popup: 0; "+
    "border: 2px solid '#ff0505';"+
    "border-radius: 10px;"+
    "padding: 2px 5px;"+
    "margin: 2px 10px;"+
    "selection-color: 'white';"+
    "background-color: 'white';}"
    )
    trackCombobox.setMaxVisibleItems(11)
    widgets["trackCombobox"].append(trackCombobox)


    # The user prompt for the track selection will go here
    timeEntryPrompt = QLabel("Enter your lap time below")
    timeEntryPrompt.setAlignment(QtCore.Qt.AlignCenter)
    timeEntryPrompt.setStyleSheet(
    "font-size: 27px;"+
    "color: 'white';"+
    "margin: 5px 100px;"
    )
    widgets["timeEntryPrompt"].append(timeEntryPrompt)

    # The time entry widget will go here
    submittedTime = QLineEdit()
    submittedTime.setAlignment(QtCore.Qt.AlignCenter)
    submittedTime.resize(600, 30)
    submittedTime.setStyleSheet(
    "border: 2px solid '#ff0505';"+
    "border-radius: 10px;"+
    "padding: 2px 4px;"+
    "margin: 1px 260px;"+
    "background-color: 'white';"
    )
    widgets["submittedTime"].append(submittedTime)

    # QLabelvar, row pos, column pos
    grid.addWidget(widgets["logo"][-1], 0, 0)
    grid.addWidget(widgets["trackSelectPrompt"][-1], 1, 0)
    grid.addWidget(widgets["trackCombobox"][-1], 2, 0)
    grid.addWidget(widgets["timeEntryPrompt"][-1], 3, 0)
    grid.addWidget(widgets["submittedTime"][-1], 4, 0)
    grid.addWidget(widgets["button"][-1], 5, 0)

# When starting up the software you will have the choice to submit time or access leaderboard
def startFrame():
    timeEntryButton = QPushButton("Add time")
    timeEntryButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    timeEntryButton.clicked.connect(show_timeEntryFrame)
    timeEntryButton.setStyleSheet(
    "*{border: 4px solid '#ff0505';"+
    "border-radius:15px;"+
    "font-size: 27px;"+
    "margin: 20px 20px;"+
    "color: 'white'}"+
    "*:hover{background: '#ff0505';"+
    "font-size: 30px;}"
    )
    widgets["timeEntryButton"].append(timeEntryButton)

    leaderboard_button = QPushButton("Leaderboard")
    leaderboard_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    leaderboard_button.clicked.connect(show_scoreboardFrame)
    leaderboard_button.setStyleSheet(
    "*{border: 4px solid '#ff0505';"+
    "border-radius:15px;"+
    "font-size: 27px;"+
    "margin: 20px 20px;"+
    "color: 'white'}"+
    "*:hover{background: '#ff0505';"+
    "font-size: 30px;}"
    )
    widgets["leaderboard_button"].append(leaderboard_button)

    grid.addWidget(widgets["timeEntryButton"][-1], 1, 1)
    grid.addWidget(widgets["leaderboard_button"][-1], 1, 2)

startFrame()

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
# Button widget to go back to entry frame. Not working atm...
    backButton = QPushButton("Back")
    backButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    backButton.clicked.connect(show_timeEntryFrame)
    backButton.setStyleSheet(
    "*{border: 4px solid '#ff0505';"+
    "border-radius:15px;"+
    "font-size: 27px;"+
    "margin: 20px 100px;"+
    "color: 'white'}"+
    "*:hover{background: '#ff0505';"+
    "font-size: 30px;}"
    )
    widgets["backButton"].append(backButton)

    grid.addWidget(widgets["backButton"][-1], 4, 0)
    grid.addWidget(widgets["leaderboard"][-1], 1, 0, 2, 2)


window.show()
sys.exit(app.exec())
