class NoteModel:
    def __init__(self, id, title, description, time):
        self.id = id
        self.title = title
        self.description = description
        self.time = time

    def from_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'time': self.time
        }

    @classmethod
    def to_json(cls, res):
        return cls(id=res['id'], title=res['title'], description=res['description'], time=res['time'])


