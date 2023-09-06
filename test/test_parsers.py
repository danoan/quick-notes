from danoan.quick_notes.commands import to_toml, to_markdown
from danoan.quick_notes.control import model

import conftest as conf
import pytest


@pytest.mark.parametrize("n_entries", [1, 2, 5])
def test_valid_markdown(n_entries, tmp_path):
    list_of_mock_quick_note = [
        conf.MockQuickNoteFactory.next() for _ in range(n_entries)
    ]
    expected_quick_note_table = model.QuickNoteTable(
        [x.quick_note for x in list_of_mock_quick_note]
    )

    quick_note_table = to_toml.parse(
        "\n".join([x.markdown_string() for x in list_of_mock_quick_note])
    )
    assert quick_note_table == expected_quick_note_table


@pytest.mark.parametrize("n_entries", [1, 2, 5])
def test_valid_quick_note_table(n_entries, tmp_path):
    list_of_mock_quick_note = [
        conf.MockQuickNoteFactory.next() for _ in range(n_entries)
    ]
    expected_quick_note_markdown = "\n".join(
        [x.markdown_string() for x in list_of_mock_quick_note]
    )
    expected_quick_note_markdown += (
        "\n"  # This accounts for the newline added by the template render
    )

    quick_note_table = model.QuickNoteTable(
        [x.quick_note for x in list_of_mock_quick_note]
    )
    quick_note_markdown = to_markdown.parse(quick_note_table)

    assert quick_note_markdown == expected_quick_note_markdown
