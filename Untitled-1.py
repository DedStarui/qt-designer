import json
from PyQt5.QtWidgets import*
from ui import Ui_MainWindow
class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #self.load_data()
    def load_data(self):
        try:
            with open("notes_data.json", "r", encoding = "utf-8")as file:
                self.notes = json.load(file)
        except(FileNotFoundError, json.JSONDecodeError):
            self.notes = {}
        self.ui.listWidget.addItems(self.notes.keys())


def add_note(self):
    note_name, ok = QInputDialog.getText(self, "Додати замітку", "Назва замітки:")
    if ok and note_name != "":
        if note_name not in self.notes:
            self.notes[note_name] = {"текст": "", "теги": []}
            self.ui.listWidget.addItem(note_name)
            self.ui.textEdit.clear()
        else:
            self.ui.textEdit.setPlainText(self.notes[note_name]["текст"])
        self.ui.listWidget_2.clear()
        self.ui.listWidget_2.addItems(self.notes[note_name]["теги"])
        print(self.notes)

def show_note(self):
    if self.ui.listWidget.selectedItems():
        key = self.ui.listWidget.selectedItems()[0].text()
        if "текст" in self.notes[key]:
            self.ui.textEdit.setPlainText(self.notes[key]["текст"])
        else:
            self.ui.textEdit.clear()
        self.ui.listWidget_2.clear()
        self.ui.listWidget_2.additems(self.notes[key]["теги"])
def save_note(self):
    if self.ui.listWidget.selectedItems():
        key = self.ui.listWidget.selectedItems()[0].text()
        self.notes[key]["текст"] = self.ui.textEdit.toPlainText()
        self.ui.listWidget_2.clear()
        self.ui.listWidget_2.addItems(self.notes[key]["теги"])
        self.ui.listWidget_2.clear()
        self.ui.listWidget_2.addItems(self.notes.keys())
        with open("notes_data.json", "w", encoding = "utf-8")as file:
            json.dump(self.notes, file, sort_keys=True, ensure_ascii=False)
    else:
        print("Замітка для збереження не вибрана!")
def del_note(self):
    if self.ui.listWidget.selectedItems():
        key = self.ui.listWidget.selectedItems()[0].text()
        #вилучимо замітку замітку зі словника notes
        del self.notes[key]
        self.ui.listWidget_2.clear()
        self.ui.textEdit.clear()
        with open("notes_data.json", "w", encoding = "utf-8")as file:
            json.dump(self.notes, file, sort_keys=True, ensure_ascii=False)
        self.ui,listWidget.clear()
        self.ui.listWidget.addItems(self.notes.keys())
    else:
        print("Замітку для видалення не вибрано!")
def add_tag(self):
    if self.ui.listWidget.selectedItems():
        key = self.ui.listWidget.selectedItems()[0].text()
        tag = self.ui.lineEdit.text()
        if not tag in self.notes[key]["теги"]:
            self.notes[key]["теги"].append(tag)
app = QApplication([])
ex = Widget()
ex.show()
app.exec_()






