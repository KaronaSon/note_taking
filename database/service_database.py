import sqlite3
from model.note_model import NoteModel
from database.service_db import ServiceDatabase

class NoteController:
    def __init__(self):
        self.service = ServiceDatabase()

    def insert_data(self, note_model):
        db = self.service.initialize_data()
        cursor = db.cursor()
        cursor.execute("INSERT INTO {} VALUES (?, ?)".format(self.service.table), (note_model.title, note_model.content))
        db.commit()
        db.close()

    def get_data(self):
        db = self.service.initialize_data()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM {}".format(self.service.table))
        result = cursor.fetchall()
        notes = []
        for row in result:
            note = NoteModel(row[0], row[1])
            notes.append(note)
        db.close()
        return notes

    def update_data(self, note_model):
        db = self.service.initialize_data()
        cursor = db.cursor()
        cursor.execute("UPDATE {} SET title=?, content=? WHERE id=?".format(self.service.table), (note_model.title, note_model.content, note_model.id))
        db.commit()
        db.close()

    def delete_data(self, id):
        db = self.service.initialize_data()
        cursor = db.cursor()
        cursor.execute("DELETE FROM {} WHERE id=?".format(self.service.table), (id,))
        db.commit()
        db.close()
