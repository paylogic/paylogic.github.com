:slug: vaex-1-billion-rows-1-laptop-serious-data-science
:speaker: jovan-veljanoski
:year: 2019
:title: Vaex: 1 Billion rows, 1 laptop, serious data science

Working with datasets comprising millions or billions or samples is
becoming an increasingly common task, one that is typically tackled
with distributed computing. We will demonstrate how one can attack
such a problem using just a laptop while bringing extra value by
saving time, costs and manpower.  In this talk, we will analyse the
entire public database of the New York City Yellow Cab taxi service,
containing the data for well over a billion trips. Our live
demonstration will showcase how to find which locations are most
lucrative for taxi drivers given a certain time of day, how to
identify interesting objects or events in the data, as well as build a
machine learning model to predict the expected tip amount for a given
trip. We will do the entire exploration and analysis in Python using a
single laptop, live!  All this is possible with Vaex, a DataFrame
library with an expected API. It leverages simple but efficient
out-of-core algorithms for data visualisation, filtering, cleaning,
preprocessing and transformation which are lazily evaluated, together
with efficient storage (memory mapped arrow or hdf5). This makes Vaex
an ideal tool for working with datasets that would otherwise be too
large to fit into the memory of a single computer.
