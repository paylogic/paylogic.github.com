:slug: tensorflow-in-rust-with-a-little-help-from-python
:speaker: daniel-de-kok
:year: 2019
:title: Tensorflow in Rust with a little help from Python

Tensorflow is a widely-used library for defining and running
computation graphs, such as machine learning models. Rust is a safe,
strongly-typed, compiled language with zero-cost abstractions. Rust
and Tensorflow seem like a natural match for performance-critical
machine learning applications. However, the Tensorflow Python module
provides the richest API to construct graphs, whereas Rust has to rely
on the very limited Tensorflow C API. In this talk, I will show how
you can train and run Tensorflow graphs directly from Rust, with a
little help from Python. We will use the rich Python Tensorflow API to
define a computation graph with the necessary ops. We will then use
this graph directly from Rust to train the model parameters and do
predictions after training. The result is a Rust program that only has
a dependency on the Tensorflow shared library. I will conclude the
presentation with a real-world example of a Rust sequence tagger,
sticker, that was used to annotate a 27.3 billion token web corpus.
