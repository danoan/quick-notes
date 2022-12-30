{% for quick_note in data.quick_note_table.list_of_quick_note -%}
<!--BEGIN id={{quick_note.id}} date="{{quick_note.date}}" -->
# {{quick_note.title}}
{{quick_note.text}}
<!--END-->

{% endfor %}
