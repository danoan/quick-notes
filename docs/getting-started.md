# Getting started with quick-notes

Markdown dialect with metadata support and toml serialization.

## Features

- Markdown with metadata.
- Markdown <--> toml.
- CLI to generate and validate .md and .toml quick-notes.

## What is a quick note?

A quick note is a labeled text that can be represented in markdown or toml format.

### Markdown quick note 

A markdown quick note is a markdown text wrapper with special
markdown comments starting with `<!--BEGIN-->` and ending with
`<!--END-->`. 

Here is the `ingredients.md` file.

```
<!--BEGIN id=0 date="2022-12-30T09:07:33.934408" -->
# 2022-12-30T09:07
I should remember to buy:

- Apples
- Milk
- Sugar

<!--END-->
```

The `<!--BEGIN-->` statement accepts any list of key-value attributes that could be represented as a string or as an integer.

### Toml quick note

Quick notes in a markdown file can be converted to its toml representation. The `ingredients.md` above would have the corresponding `ingredients.toml`:

```toml
[[list_of_quick_note]]
id = 0
date = "2022-12-30T09:07:33.934408"
title = "2022-12-30T09:07"
text = "I should remember to buy\n\n- Apples\n- Milk\n - Sugar\n\n"
```

## CLI application

The CLI application supports the following commands:

- generate-toml: converts a markdown quick-note to toml quick-note.
- generate-markdown: converts a toml quick-note to markdown quick-note.
- validate: check if a toml quick-note and a markdown quick-note are equivalent.
- generate-quick-note: generate a toml quick-note according to a data-layout.

To create toml quick-notes you need to specify a data-layout.

### Data Layout 

A data layout is a python dataclass with support to write and read toml files. The `quick-notes` package comes with a single data layout named: `QuickNote`.

```python   
@dataclass
class QuickNote(TomlDataClassIO):
    id: int
    date: str
    title: str
    text: str


@dataclass
class QuickNoteList(TomlTableDataClassIO):
    list_of_quick_note: List[QuickNote]

```

## API module   

The CLI application relies on the quick-notes api. One can import the module `api` to create new applications using quick-notes.

