:slug: provide-a-scalable-and-secure-rest-based-backend-with-python
:speaker: gerard-lutterop
:year: 2019
:title: Provide a scalable and secure REST based backend with Python

REST based backends are a boon for front end developers, since
connecting the front end to the business logic and data layer is very
straightforward using standard internet technologies.

Providing a REST backend turns out to be very difficult, when you want
to adhere to the 'real' REST standards.

We used Python to develop a framework which is agnostic to the web
framework and to the database. The interface can be specified
declaratively using a standard language, to which our framework is
also agnostic. All non-standard logic is implemented using Python on
pre-defined events.

This framework turns out to be extremely productive, not only for the
programmer, but especially for the designer of the
interface. Implementing a battleproof REST based interface is
literally one click away.
