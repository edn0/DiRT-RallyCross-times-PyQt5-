import sys
from PyQt5.QtWidgets import QApplication, QLineEdit, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout, QComboBox
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor

widgets = {
    "logo": [],
    "button": [],
    "leaderboard": [],
    "trackSelectPrompt": [],
    "timeEntryPrompt": [],
    "trackCombobox": [],
    "submittedTime": []
}

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("DiRT RallyCross Lap Times")
window.setFixedWidth(1000)
window.setStyleSheet("background: #999999;")

grid = QGridLayout()
window.setLayout(grid)

def clear_widgets():
    for widget in widgets:
        if widgets[widget] != []:
            widgets[widget][-1].hide()
        for i in range(0, len(widgets[widget])):
            widgets[widget].pop()


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
    logo.setStyleSheet("margin-bottom: 100px;")
    widgets["logo"].append(logo)

    # Button widget
    button = QPushButton("Add time")
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.clicked.connect(show_scoreboardFrame)
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

    # The combobox will go here
    trackCombobox = QComboBox()
    trackCombobox.addItem("Mettet, Belgium")
    trackCombobox.addItem("Trois-Rivières, Canada")
    trackCombobox.addItem("Lydden Hill, England")
    trackCombobox.addItem("Silverstone, England")
    trackCombobox.addItem("Lohéac, France")
    trackCombobox.addItem("Hell, Norway")
    trackCombobox.addItem("Montalegre, Portugal")
    trackCombobox.addItem("Killarney International Raceway, South Africa")
    trackCombobox.addItem("Circuit de Barcelona-Catalunya, Spain")
    trackCombobox.addItem("Höljes, Sweden")
    trackCombobox.addItem("Yas Marina Circuit, Abu Dhabi")
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
    widgets["submittedTime"].append(submittedTime)

    # QLabelvar, row pos, column pos
    grid.addWidget(widgets["logo"][-1], 0, 0)
    grid.addWidget(widgets["trackSelectPrompt"][-1], 2, 0)
    grid.addWidget(widgets["trackCombobox"][-1], 3, 0)
    grid.addWidget(widgets["timeEntryPrompt"][-1], 4, 0)
    grid.addWidget(widgets["submittedTime"][-1], 5, 0)
    grid.addWidget(widgets["button"][-1], 6, 0)

show_timeEntryFrame()



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
