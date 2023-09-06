from danoan.quick_notes.control import model

from pathlib import Path
from jinja2 import Environment, PackageLoader


def parse(quick_note_table: model.QuickNoteTable) -> str:
    """
    Convert a list of QuickNote into a markdown string.

    Args:
        quick_note_table: A list of QuickNote.

    Returns:
        Markdown string equivalent of the list of QuickNote.
    """
    env = Environment(
        loader=PackageLoader("danoan.quick_notes", package_path="templates")
    )

    template = env.get_template(
        Path("quick-note-table")
        .joinpath("quick-note-table.tpl.md")
        .expanduser()
        .as_posix()
    )
    return template.render({"data": {"quick_note_table": quick_note_table}})
