:slug: finalfusion-rustic-word-embeddings-for-python
:speaker: daniel-de-kok
:year: 2019
:title: finalfusion: rustic word embeddings for Python

Word embeddings have drastically changed natural language processing throughout
the last five years. Word embeddings represent words as vectors rather than
as discrete units, allowing machine learning techniques to exploit similarities
between words.

In the first half of this talk, I will introduce the finalfusion Python module.
finalfusion supports word representations with subword units to account for
words that were not seen in the training data. finalfusion's API allows you to
do similarity and anology queries, as well as computing word embeddings for
downstream use in neural networks.

The finalfusion Python module is a thin, type-safe wrapper around the rust2vec
Rust library. In the second half of this talk, I will dive deeper into the
implementation of the module as a real-world example of implementing Python
modules in Rust.
