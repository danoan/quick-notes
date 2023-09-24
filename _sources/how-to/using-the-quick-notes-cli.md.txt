# Quick-notes CLI

The quick-notes package comes up with a CLI application to generate and 
validate quick-notes based on the data layout 
`danoan.quick_notes.cli.model.QuickNote`.

## Generate a toml quick-note

```bash
quick-notes generate-quick-note --title "Pumpking soup" "Today we are going to make a delicious pumpkin soup to warm it up autumn days." > quick-notes-recipes.toml 
```

## Generate a markdown quick-note

```bash
quick-notes generate-markdown "quick-notes-recipes.toml" > quick-notes-recipes.md
```

## Validate quick-note files

```bash
quick-notes validate -t "quick-notes-recipes.toml" -m "quick-notes-recipes.md"
```

