from danoan.quick_notes.commands import to_toml, to_markdown
from danoan.quick_notes import cli

import conftest as conf
from io import StringIO
import pytest


@pytest.mark.parametrize("num_entries", [1, 2, 5])
def test_generate_markdown(num_entries, tmp_path):
    # Initialization
    toml_filepath = tmp_path.joinpath("quick-notes.toml")

    quick_note_table = conf.generate_mock_quick_note_table(num_entries)
    with open(toml_filepath, "w") as f:
        quick_note_table.write_stream(f)

    # Execution
    markdown_string = cli.generate_markdown_from_filepath(toml_filepath)

    # Ground Truth
    quick_note_table_from_generated_markdown = to_toml.parse(markdown_string)

    expected_toml_stream = StringIO()
    quick_note_table.write_stream(expected_toml_stream)

    produced_toml_stream = StringIO()
    quick_note_table_from_generated_markdown.write_stream(produced_toml_stream)

    # Comparison
    assert produced_toml_stream.read() == expected_toml_stream.read()


@pytest.mark.parametrize("num_entries", [1, 2, 5])
def test_generate_toml(num_entries, tmp_path):
    # Initialization
    markdown_filepath = tmp_path.joinpath("quick-notes.md")

    markdown_string = conf.generate_mock_quick_note_markdown(num_entries)
    with open(markdown_filepath, "w") as f:
        f.write(markdown_string)

    # Execution
    quick_note_table = cli.generate_toml_from_filepath(markdown_filepath)

    # Ground Truth
    markdown_from_generated_quick_note_table = to_markdown.parse(
        quick_note_table
    )

    # Comparison
    assert to_toml.parse(markdown_string) == to_toml.parse(
        markdown_from_generated_quick_note_table
    )
