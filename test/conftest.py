from danoan.quick_notes.api import model

from dataclasses import dataclass
import datetime
from textwrap import dedent
from typing import Any, Dict


@dataclass
class MockQuickNote(model.QuickNoteBase):
    id: int
    date: str
    title: str

    def markdown_string(self) -> str:
        temp = dedent(
            f"""\
            <!--BEGIN id={self.id} date="{self.date}" -->
            # {self.title}
            {{}}
            <!--END-->
            """
        )
        # This avoids errors in indentation that dedent is not able to capture when
        # doing the varible substitution direclty in the statement above
        return temp.format(self.text)


class MockQuickNoteFactory:
    id = 0

    @staticmethod
    def next() -> MockQuickNote:
        MockQuickNoteFactory.id += 1
        date = str(datetime.datetime.now().isoformat())
        title = f"Quick Note Title {MockQuickNoteFactory.id}"
        text = dedent(
            """\
        This afternoon I met Michel Fuhler and we talked about
        the cultivation of potatoes in the south of Germany. I
        want to try the dish basterwalthoim that he suggested me."""
        )
        return MockQuickNote(
            id=MockQuickNoteFactory.id, date=date, title=title, text=text
        )


def generate_mock_quick_note_markdown(num_entries: int) -> str:
    list_of_quick_note = [
        MockQuickNoteFactory.next() for _ in range(num_entries)
    ]
    return "\n".join([x.markdown_string() for x in list_of_quick_note])


def generate_mock_quick_note_list(
    num_entries: int,
) -> model.QuickNoteList:
    list_of_quick_note = [
        MockQuickNoteFactory.next() for _ in range(num_entries)
    ]
    return model.QuickNoteList.create(list_of_quick_note)
