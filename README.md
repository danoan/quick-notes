# Quick Notes

Quick Notes is a markdown dialect that can be converted from and to toml.

## Features

- Generate markdown quick notes;
- Generate toml quick notes;
- Validate a markdown against a toml quick note;
- Generate a toml quick note from command-line arguments.

## Examples

### ingredients.md

```markdown
<!--BEGIN id=0 date="2022-12-30T09:07:33.934408" -->
# 2022-12-30T09:07
I should remember to buy:

- Apples
- Milk
- Sugar

<!--END-->
```

### ingredients.toml

```toml
[[list_of_quick_note]]
id = 0
date = "2022-12-30T09:07:33.934408"
title = "2022-12-30T09:07"
text = "I should remember to buy\n\n- Apples\n- Milk\n - Sugar\n\n"
```

### Usage

```bash
# Generate toml
quick-notes generate-toml ingredients.md

# Generate markdown
quick-notes generate-markdown ingredients.toml

# Validate both versions againts each other. Overwrite is possible.
quick-notes validate ingredients.toml ingredients.md

# Generate toml quick-note from command-line arguments
quick-notes generate-quick-note --id 1 --date "2022-12-30T10:00:00.000000" --title "Orange Book" "I want to buy the orange book"
```
 
