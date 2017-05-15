:slug: abstraction-between-consumer-and-datastore
:speaker: marco-vellinga
:year: 2017
:title: Creating abstraction between consumer and datastore

When using the full feature set of Django (ORM, Forms, Views), your application business logic is easily fragmented across multiple apps. This was especially true in our case where we had an API that contained duplicate business logic.

At VoIPGRID we started to separate our front-end from the back-end. To make this possible we need to create entry-points for our front-end to talk to the back-end. This could be done by implementing an HTTP API, but we wanted something more generic. We decided to create a 'Data Access Layer' that sits between a HTTP API and a datastore. This layer of abstraction holds all the business logic for accessing data. During my talk I will discuss design choices and questions that needed to be answered. An overview of inner workings and flow is also displayed. There will also be something about versioning in the talk.

We came across several issues that we did not find a ready solution for. Sharing this knowledge could be interesting as well as the open source packages that came out of this.
