:slug: symbolic-fitting-using-symfit
:speaker: martin-roelfs
:year: 2019
:title: Symbolic Fitting using symfit

Data fitting problems are very common in disciplines as varied as
economics, physics, and psychology, just to name a few. Although very
powerful tools for this purpose already exist in the python ecosystem,
I found during my own research as a theoretical physicist that I was
missing a tool which stays close to mathematics as I would write it on
paper, but which could then be used to fit experimental data.

SymPy offers the kind of computer algebra system which is becoming
ever more indispensable in modern research, but it speaks a completely
different language from commonly used fitting tools such as
scipy.minimize. To address this problem I developed symfit, a unifying
wrapper around both of these libraries. Using symfit, models can be
expressed symbolically and fitted numerically, with very little effort
required from the user.
 
During this talk I will outline some of the data fitting challenges
that were overcome using symfit, focusing on the coding
aspect. Examples include fitting to ordinary differential equation
(ODE) based models, Tikhonov/Ridge regression, global fitting to
multiple data sets with shared parameters, global minimization using
Differential Evolution, and many more.
