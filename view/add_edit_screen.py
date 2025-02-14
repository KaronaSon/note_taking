import random
from datetime import datetime
from local_storage.controller.notr_controller import NoteController
from local_storage.model.note_model import NoteModel
from local_storage.view.home_screen import HomeScreen
from local_storage.widget.colors.item import whiteColor
from local_storage.widget.input_field import InputField

class AddEditScreen:
    def __init__(self, noteModel=None):
        self.noteModel = noteModel
        self.title = ''
        self.description = ''
        self.time = datetime.now()

    def get_data(self):
        self.title = self.noteModel.title
        self.description = self.noteModel.description

    def build(self, context):
        if self.noteModel is not None:
            self.get_data()

        return Scaffold(
            appBar=AppBar(
                backgroundColor='pink',
                leading=IconButton(
                    onPressed=lambda: Navigator.pop(context),
                    icon=Icon(
                        Icons.arrow_back_ios,
                        color=whiteColor,
                    ),
                ),
                title=Text(
                    'Add note' if self.noteModel is None else 'Edit note',
                    style=TextStyle(
                        color=whiteColor,
                        fontWeight='w500',
                    ),
                ),
                actions=[
                    IconButton(
                        onPressed=lambda: self.save_data(context),
                        icon=Icon(
                            Icons.save,
                            color=whiteColor,
                        ),
                    )
                ],
            ),
            body=SingleChildScrollView(
                child=Padding(
                    padding=EdgeInsets.all(8.0),
                    child=Column(
                        children=[
                            InputField(
                                hintText='Note Title',
                                controller=self.title,
                            ),
                            SizedBox(height=20),
                            InputField(
                                hintText='Note Description',
                                controller=self.description,
                                maxLines=10,
                            ),
                        ],
                    ),
                ),
            ),
        )

    def save_data(self, context):
        if self.noteModel is None:
            NoteController().insert_data(
                NoteModel(
                    id=random.randint(0, 10000),
                    title=self.title,
                    description=self.description,
                    time=f'{self.time.year}-{self.time.month}-{self.time.day}',
                ),
            ).when_complete(lambda: Navigator.push_and_remove_until(
                context,
                MaterialPageRoute(
                    builder=lambda: HomeScreen(),
                ),
                lambda route: False,
            ))
        else:
            NoteController().update_data(
                NoteModel(
                    id=self.noteModel.id,
                    title=self.title,
                    description=self.description,
                    time=f'{self.time.year}-{self.time.month}-{self.time.day}',
                ),
            ).when_complete(lambda: Navigator.push_and_remove_until(
                context,
                MaterialPageRoute(
                    builder=lambda: HomeScreen(),
                ),
                lambda route: False,
            ))

