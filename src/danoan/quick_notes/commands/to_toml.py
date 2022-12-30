from danoan.quick_notes.control import model

from lark import Lark, Transformer
from typing import Dict


class _MarkdownQuickNoteToToml(Transformer):
    def identifier(self, s) -> str:
        (s,) = s
        return str(s)

    def integer(self, i) -> int:
        (i,) = i
        return int(i)

    def value(self, v) -> str:
        (v,) = v
        return v

    def escaped_string(self, s) -> str:
        (s,) = s
        return s[1:-1]

    string = identifier

    def title(self, t) -> Dict[str, str]:
        return {"title": t[0]}

    def text(self, t) -> Dict[str, str]:
        return {"text": "\n".join(t)}

    def attribute(self, items) -> Dict[str, str]:
        k, v = items
        return {k: v}

    def entry(self, items) -> model.QuickNote:
        d_params = {}
        for d in items:
            d_params.update(d)

        return model.QuickNote(**d_params)

    def document(self, items) -> model.QuickNoteTable:
        return model.QuickNoteTable(list(items))


def parse(markdown_str: str) -> model.QuickNoteTable:
    """
    Convert a markdown string containing one or more quick note into a QuickNoteTable.

    Args:
        markdown_str: A markdown string containing one or more markdown quick-note.

    Returns:
        A list of QuickNote.
    """
    quick_notes_grammar = r"""
        document: entry*
    
        entry: _begin title text _end
        title: "#" string
        _begin: "<!--BEGIN" (attribute)* "-->" 
        _end: "<!--END-->"
        attribute: identifier "=" value
        value: escaped_string
              |integer
        text: string*
        identifier: /[A-Za-z_]+/ 

        integer: /\d+/
        string: /.+/
        escaped_string: ESCAPED_STRING 

        %import common.ESCAPED_STRING
        %import common.WS
        %ignore WS
    """

    quick_notes_parser = Lark(
        quick_notes_grammar, start="document", parser="lalr", transformer=_MarkdownQuickNoteToToml()
    )

    return quick_notes_parser.parse(markdown_str)
