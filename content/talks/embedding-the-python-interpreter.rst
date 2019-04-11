:slug: embedding-the-python-interpreter
:speaker: mark-boer
:year: 2019
:title: Embedding the Python interpreter

More and more applications are adding Python support to offer the user
a scripting language to interact with. Even Microsoft is considering
to officially add Python to Excel. In this talk we will explore how
one would go about doing this.

We dive into the CPtyhon internals and build our own simple REPL using
Python's C-API. I'll show you some of the quirks and pitfalls I ran
into, how you can wrestle the GIL and how to manage global state.
