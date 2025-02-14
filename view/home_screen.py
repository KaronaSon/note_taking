from typing import List
import asyncio
from local_storage.model.note_model import NoteModel
from local_storage.view.add_edit_screen import AddEditScreen
from controller.notr_controller import NoteController
from widget.crat_item import CartItem

class HomeScreen:
    def __init__(self):
        self.list = None
        self.noteController = None

    async def onRefresh(self):
        self.noteController = NoteController()
        self.list = await self.noteController.getData()

    def initState(self):
        asyncio.run(self.onRefresh())

    def build(self, context):
        return Scaffold(
            appBar=AppBar(
                backgroundColor=Colors.pink,
                title=Text(
                    "Dating Note",
                    style=TextStyle(
                        color=Colors.white,
                        fontWeight=FontWeight.w500,
                    ),
                ),
                actions=[
                    IconButton(
                        onPressed=lambda: Navigator.push(
                            context,
                            MaterialPageRoute(
                                builder=lambda: AddEditScreen(),
                            ),
                        ),
                        icon=Icon(
                            Icons.add,
                            size=30,
                            color=Colors.white,
                        ),
                    ),
                ],
            ),
            body=FutureBuilder[List[NoteModel]](
                future=self.list,
                builder=lambda context, snapshot: Center(
                    child=CircularProgressIndicator() if snapshot.connectionState == ConnectionState.waiting else Icon(Icons.error) if snapshot.hasError else ListView.builder(
                        itemCount=len(snapshot.data),
                        itemBuilder=lambda context, index: CartItem(
                            model=snapshot.data[index],
                        ),
                    ),
                ),
            ),
        )

