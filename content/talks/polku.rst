:slug: polku
:speaker: german-gomez-herrero
:year: 2017
:title: Polku: Serverless Stream Processing with Python
:fulltitle: Polku: Serverless Stream Processing with Python

Polku is a serverless stream processing framework for the AWS cloud, written entirely in Python. Although it is still under heavy development, it has been battle-tested in a production setting at FindHotel for almost a year now, and we think is already stable enough for others to benefit from it. Polku follows Python's "batteries included" philosophy and lets you focus on high-level data transformations. Deploying, operating and extending Polku is very easy. If you have some basic Python skills and access to the AWS cloud, Polku is all you need to have a devops-free fully operational stream processing system in a matter of minutes or hours rather than weeks.

Polku has advanced features such as partial support for out of order events, stateful transformations, a plug-in system for user-defined transformations written in Python, advanced error handling and monitoring, reprocessing, a configuration-based pipeline definition, and built-in analytics.

More importantly, Polku has a flat learning curve. Any engineer without specialist knowledge should be able to have a fully functional system in a matter of minutes. Defining custom transformations requires only basic Python skills. We believe Polku can be generally useful to organisations like FindHotel that intend to process up to tens of thousands of events per second, but that don't want to spend any more time than absolutely necessary setting up and maintaining streaming infrastructure.

We are going to open source Polku before PyGrunn so if you attend this talk chances are you can have your own Polku up and running in less time that it will take for me to go through my slides.
