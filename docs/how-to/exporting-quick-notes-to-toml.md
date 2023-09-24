# Exporting quick-notes to toml

Quick-notes can be also represented in the more general toml format.
A markdown quick-note can be exported to toml and rendered in a different
markup-language or text render mechanism.

Here is it our markdown document:

```python
>>> markdown_quick_note_document="""
... <!--BEGIN author="Steve Jobs" category="technology" date="2023-08-17" -->
... # MiniWatch Review: A Revolution in Wearable Technology
... 
... Ladies and gentlemen, tech aficionados, and innovators of the digital age,
... gather 'round as we delve into the future of wearable technology. I'm Steve
... Jobs, and today, I have the distinct pleasure of introducing you to a
... game-changer in the world of wearables: the MiniWatch.
... 
... <!--END-->
... 
... <!--BEGIN author="Jack Kerouac" category="writing" date="2023-09-21" -->
... # Using generative AI to sharpe creativity
... 
... Man, you know, the world's changing faster than a jazz riff on a summer night.
... We got these machines now, man, machines that can create like the gods
... themselves. I'm talkin' 'bout generative AI, my friends. It's the poetry of the
... future, and it's here today. So, sit back, cats and kittens, and let me tell
... you how to ride the waves of generative AI to enhance your creative soul.
... 
... <!--END-->
... 
... <!--BEGIN author="Elvis Presley" category="performance" date="2023-09-01" -->
... # Rockin' the Stage: Elvis's Guide to Performance Techniques
... 
... Hey there, cats and kittens, gather 'round 'cause the King is in the building!
... Today, I wanna talk to y'all about somethin' that's near and dear to my heart –
... the art of rockin' the stage. You see, darlin', it ain't just about singin' a
... song; it's about puttin' on a show that'll knock their socks off. So, let's
... dive into the world of performance techniques, Elvis style!
... 
... <!--END-->
... 
... """

```

```python
>>> # Import quick-notes base classes and parsers
>>> from danoan.quick_notes.api.model import QuickNoteBase, QuickNoteList
>>> from danoan.quick_notes.api import to_toml

>>> # Import the dataclass decorator as every quick-note class should be decorated with
>>> from dataclasses import dataclass

>>> from io import StringIO
 
>>> @dataclass
... class BlogPostSketch(QuickNoteBase):
...     author: str
...     category: str 
...     date: str


>>> # The parser return a `NonRenderedQuickNote`. You should render it using the 
>>> # `BlogPostSketch` class
>>> non_rendered_quick_note = to_toml.parse(markdown_quick_note_document)
>>> post_sketches = non_rendered_quick_note.render(BlogPostSketch)

>>> ss = StringIO()
>>> post_sketches.write(ss)
>>> print(ss.getvalue())
[[list_of_quick_note]]
title = "MiniWatch Review: A Revolution in Wearable Technology"
text = "Ladies and gentlemen, tech aficionados, and innovators of the digital age,\ngather 'round as we delve into the future of wearable technology. I'm Steve\nJobs, and today, I have the distinct pleasure of introducing you to a\ngame-changer in the world of wearables: the MiniWatch."
author = "Steve Jobs"
category = "technology"
date = "2023-08-17"
<BLANKLINE>
[[list_of_quick_note]]
title = "Using generative AI to sharpe creativity"
text = "Man, you know, the world's changing faster than a jazz riff on a summer night.\nWe got these machines now, man, machines that can create like the gods\nthemselves. I'm talkin' 'bout generative AI, my friends. It's the poetry of the\nfuture, and it's here today. So, sit back, cats and kittens, and let me tell\nyou how to ride the waves of generative AI to enhance your creative soul."
author = "Jack Kerouac"
category = "writing"
date = "2023-09-21"
<BLANKLINE>
[[list_of_quick_note]]
title = "Rockin' the Stage: Elvis's Guide to Performance Techniques"
text = "Hey there, cats and kittens, gather 'round 'cause the King is in the building!\nToday, I wanna talk to y'all about somethin' that's near and dear to my heart –\nthe art of rockin' the stage. You see, darlin', it ain't just about singin' a\nsong; it's about puttin' on a show that'll knock their socks off. So, let's\ndive into the world of performance techniques, Elvis style!"
author = "Elvis Presley"
category = "performance"
date = "2023-09-01"
<BLANKLINE>
<BLANKLINE>

```
