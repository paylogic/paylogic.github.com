:slug: viasock
:speaker: kilian-evang
:year: 2017
:title: Viasock: Automagically Serverize Your Scripts

The Unix command line is incredibly powerful. You can freely compose programs into pipelines, and Makefiles allow you to orchestrate complex data flows.

Things turn nasty when you have to run one program frequently as part of a pipeline, and that program takes a long time to start up, e.g., because it has to read a large model file. The solution is to turn the program into a server that keeps running and serves multiple requests. But this can be a headache: do I have to add client/server code to every such program? How do I ensure the server is running when my pipeline needs it? How do I ensure the server is restarted when the inputs to the program change? Do I have to change my entire workflow and give up on pipes and files?

Viasock is a program, written in Python, that solves these problems. It acts as a transparent wrapper for your script and turns it into a server, invisibly in the background. You won’t even notice, except that your pipelines are suddenly much faster.
