# How to create and update markdown quick-notes

In this tutorial we are going to create a markdown quick-note programmatically 
and then generate the markdown document.

## Creating a markdown quick-note

We are going to create the class `BlogPostSketch`, a derived class of 
`QuickNoteBase`. This quick-note will hold ideas for blog posts.

```python
>>> # Import quick-notes base classes and parsers
>>> from danoan.quick_notes.api.model import QuickNoteBase, QuickNoteList
>>> from danoan.quick_notes.api import to_markdown

>>> # Import the dataclass decorator as every quick-note class should be decorated with
>>> from dataclasses import dataclass
 
>>> @dataclass
... class BlogPostSketch(QuickNoteBase):
...     author: str
...     category: str 
...     date: str

>>> # Use keyword arguments to avoid assigning values to the wrong attributes.
>>> # Every quick-note must have a `title` and a `text` attribute.
>>> quick_note = BlogPostSketch(title="Using generative AI to sharpe creativity", 
...                             author="Jack Kerouac", 
...                             category="writing", 
...                             date="2023-09-21", 
...                             text="""
... Man, you know, the world's changing faster than a jazz riff on a summer night.
... We got these machines now, man, machines that can create like the gods
... themselves. I'm talkin' 'bout generative AI, my friends. It's the poetry of the
... future, and it's here today. So, sit back, cats and kittens, and let me tell
... you how to ride the waves of generative AI to enhance your creative soul.
... """)

>>> # The markdown parser expects a QuickNoteList.
>>> quick_note_list = QuickNoteList.create([quick_note])
>>> markdown_str = to_markdown.parse(quick_note_list)

>>> print(markdown_str)
<!--BEGIN author="Jack Kerouac" category="writing" date="2023-09-21" -->
# Using generative AI to sharpe creativity
<BLANKLINE>
Man, you know, the world's changing faster than a jazz riff on a summer night.
We got these machines now, man, machines that can create like the gods
themselves. I'm talkin' 'bout generative AI, my friends. It's the poetry of the
future, and it's here today. So, sit back, cats and kittens, and let me tell
you how to ride the waves of generative AI to enhance your creative soul.
<BLANKLINE>
<!--END-->
<BLANKLINE>
<BLANKLINE>

```

## Updating a markdown quick-note

We have a markdown quick-note document full of blog post ideas. We would
like to make a change in one of them and re-render the document. 

This is our markdown quick-note document:

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

We would like to make some changes in Jack Kerouac's item and render the updated 
document:

- Add the category "language models".
- Add the text: "In this post we are going to use the InspiredAuthor model from GGG corp."

```python
>>> # Import the markdown to toml parser
>>> from danoan.quick_notes.api import to_toml

>>> # The parser return a `NonRenderedQuickNote`. You should render it using the 
>>> # `BlogPostSketch` class
>>> non_rendered_quick_note = to_toml.parse(markdown_quick_note_document)
>>> post_sketches = non_rendered_quick_note.render(BlogPostSketch)

>>> for post in post_sketches.list_of_quick_note:
...     if post.author == "Jack Kerouac":
...         post.category = "technology,language models"
...         post.text += "\n\nIn this post we are going to use the InspiredAuthor model from GGG corp."
>>> updated_markdown_string = to_markdown.parse(post_sketches)
>>> print(updated_markdown_string)
<!--BEGIN author="Steve Jobs" category="technology" date="2023-08-17" -->
# MiniWatch Review: A Revolution in Wearable Technology
Ladies and gentlemen, tech aficionados, and innovators of the digital age,
gather 'round as we delve into the future of wearable technology. I'm Steve
Jobs, and today, I have the distinct pleasure of introducing you to a
game-changer in the world of wearables: the MiniWatch.
<!--END-->
<BLANKLINE>
<!--BEGIN author="Jack Kerouac" category="technology,language models" date="2023-09-21" -->
# Using generative AI to sharpe creativity
Man, you know, the world's changing faster than a jazz riff on a summer night.
We got these machines now, man, machines that can create like the gods
themselves. I'm talkin' 'bout generative AI, my friends. It's the poetry of the
future, and it's here today. So, sit back, cats and kittens, and let me tell
you how to ride the waves of generative AI to enhance your creative soul.
<BLANKLINE>
In this post we are going to use the InspiredAuthor model from GGG corp.
<!--END-->
<BLANKLINE>
<!--BEGIN author="Elvis Presley" category="performance" date="2023-09-01" -->
# Rockin' the Stage: Elvis's Guide to Performance Techniques
Hey there, cats and kittens, gather 'round 'cause the King is in the building!
Today, I wanna talk to y'all about somethin' that's near and dear to my heart –
the art of rockin' the stage. You see, darlin', it ain't just about singin' a
song; it's about puttin' on a show that'll knock their socks off. So, let's
dive into the world of performance techniques, Elvis style!
<!--END-->
<BLANKLINE>
<BLANKLINE>

```


