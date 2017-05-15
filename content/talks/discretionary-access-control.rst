:slug: discretionary-access-control
:speaker: jaap-bresser
:year: 2017
:title: Beyond Role Based Authorization, implementing Discretionary Access Control using Postgres and SQLAlchemy
:fulltitle: Beyond Role Based Authorization, implementing Discretionary Access Control using Postgres and SQLAlchemy

Many (web) applications start out using Role Based Authorization. And for good reason: it is simple and effective. It lacks, however, the flexibility to support more advanced use cases, such as users granting permissions to other users.

A more flexible way of authorization that does support such use cases, is Discretionary Access Control (DAC). The ways in which DAC can be implemented are manifold.

In this talk you will be introduced to different implementations of DAC in well-known software. Design choices that arise when implementing DAC are further examined by means of a practical case at the independent career platform "Profileermij" (a python web application based on Flask, SQLAlchemy with a Postgres data store). Detailed explanation, including code samples, will show you how Postgres features, like indexes on JSON columns, can be utilized to implement Access Control Lists in a simple and efficient manner. While DAC provides a very flexible way of authentication, there is a caveat: this flexibility comes with complexity. In the last part of this talk you will therefore receive some useful advice on how to manage this complexity and -equally important- considerations on when it might be better not to opt for DAC.

This talk will of interest for people who are completely new to the subject, but also for those who are considering implementing or already have implemented DAC, as I could provide them with practical implementation advice as well as some insight in the implications of different design choices. Finally, people with an general interest in authorization and security might also enjoy this talk.
