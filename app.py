import csv
import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QLineEdit, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout, QComboBox
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor
from data import trackList, dbTrackList

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

# // # TODO:
# Figure out how to handle time conversion to seconds in order to store it as an int representing how many seconds the lap took, from the string input from the user.
# Figure out how to pull the result and add it to db, then display it in the leaderboard, just like in BlindtestScore

def checkDb():
    con = sqlite3.connect("times.db")
    cur = con.cursor()
    cur.execute("select * from times")
    search_results = cur.fetchall()
    print(search_results)
    con.close()

con = sqlite3.connect("times.db")
cur = con.cursor()
cur.execute("create table if not exists times(circuit text, times text)")
## cur.executemany("insert into times values (?, ?)", dbTrackList)
con.commit()
checkDb()
con.close()


input = ""

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("DiRT RallyCross Lap Times")
window.setFixedWidth(600)
window.setStyleSheet("background: #140202;")

grid = QGridLayout()
window.setLayout(grid)

def clear_widgets():
    for widget in widgets:
        if widgets[widget] != []:
            widgets[widget][-1].hide()
        for i in range(0, len(widgets[widget])):
            widgets[widget].pop()

# Function that will fetch data and write to the db
def SQLSaveTime():
    timeEntered = submittedTime.text()
    print(timeEntered)
    selectedTrack = trackCombobox.currentText()
    print(selectedTrack)
    con = sqlite3.connect("times.db")
    cur = con.cursor()
    cur.execute("update times set times=? where circuit=?", (timeEntered, selectedTrack))
    con.commit()
    con.close()

def show_timeEntryFrame():
    clear_widgets()
    timeEntryFrame()

def show_scoreboardFrame():
    clear_widgets()
    scoreboardFrame()

def timeEntryFrame():
    global submittedTime
    global trackCombobox
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
    button.clicked.connect(SQLSaveTime)
    button.setStyleSheet(
    "*{border: 2px solid '#ff0505';"+
    "border-radius:10px;"+
    "font-size: 16px;"+
    "margin: 10px 200px;"+
    "background-color: '#cec8c8';"+
    "color: 'black'}"+
    "*:hover{background: '#ff0505';"+
    "font-size: 16px;}"
    )
    widgets["button"].append(button)

    # Adding the text above the combobox
    trackSelectPrompt = QLabel("Select your track")
    trackSelectPrompt.setAlignment(QtCore.Qt.AlignCenter)
    trackSelectPrompt.setStyleSheet(
        "font-size: 22px;"+
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
    "background-color: '#cec8c8';}"+
    "*{background: '#cec8c8'}"
    )
    trackCombobox.setMaxVisibleItems(11)
    widgets["trackCombobox"].append(trackCombobox)


    # The user prompt for the track selection will go here
    timeEntryPrompt = QLabel("Enter your lap time below")
    timeEntryPrompt.setAlignment(QtCore.Qt.AlignCenter)
    timeEntryPrompt.setStyleSheet(
    "font-size: 22px;"+
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
    "margin: 1px 60px;"+
    "background-color: '#cec8c8';"
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
    "font-size: 22px;"+
    "margin: 20px 20px;"+
    "color: 'white'}"+
    "*:hover{background: '#ff0505';"+
    "font-size: 22px;}"
    )
    widgets["timeEntryButton"].append(timeEntryButton)

    leaderboard_button = QPushButton("Leaderboard")
    leaderboard_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    leaderboard_button.clicked.connect(show_scoreboardFrame)
    leaderboard_button.setStyleSheet(
    "*{border: 4px solid '#ff0505';"+
    "border-radius:15px;"+
    "font-size: 22px;"+
    "margin: 20px 20px;"+
    "color: 'white'}"+
    "*:hover{background: '#ff0505';"+
    "font-size: 22px;}"
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
    backButton.clicked.connect(show_timeEntryFrame) ##### MAYBE I CAN WRITE A => function so i am able to write it to txt file immediately????? ---- nope, the solution was classes, something i should've learned before going into this
    backButton.setStyleSheet(
    "*{border: 4px solid '#ff0505';"+
    "border-radius:15px;"+
    "font-size: 22px;"+
    "margin: 20px 100px;"+
    "color: 'white'}"+
    "*:hover{background: '#ff0505';"+
    "font-size: 22px;}"
    )
    widgets["backButton"].append(backButton)

    grid.addWidget(widgets["backButton"][-1], 4, 0)
    grid.addWidget(widgets["leaderboard"][-1], 1, 0, 2, 2)


window.show()
sys.exit(app.exec())
