from database.service_db import ServiceDatabase
from model.note_model import NoteModel

class NoteController:
    def __init__(self):
        self.service = ServiceDatabase()

    async def insert_data(self, note_model):
        db = await self.service.initialize_data()
        await db.insert(self.service.table, note_model.to_json())
        await db.close()

    async def get_data(self):
        db = await self.service.initialize_data()
        result = await db.query(self.service.table)
        notes = [NoteModel.from_json(row) for row in result]
        await db.close()
        return notes

    async def update_data(self, note_model):
        db = await self.service.initialize_data()
        await db.update(
            self.service.table, note_model.to_json(), where="id=?", where_args=[note_model.id]
        )
        await db.close()

    async def delete_data(self, id):
        db = await self.service.initialize_data()
        await db.delete(self.service.table, where="id=?", where_args=[id])
        await db.close()
