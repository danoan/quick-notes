from danoan.utils.toml_dataclass import TomlDataClassIO, TomlTableDataClassIO
from dataclasses import dataclass
from typing import List


@dataclass
class QuickNote(TomlDataClassIO):
    id: int
    date: str
    title: str
    text: str


@dataclass
class QuickNoteTable(TomlTableDataClassIO):
    list_of_quick_note: List[QuickNote]
