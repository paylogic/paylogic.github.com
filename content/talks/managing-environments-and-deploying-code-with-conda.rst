:slug: managing-environments-and-deploying-code-with-conda
:speaker: teake-nutma
:year: 2019
:title: Managing environments and deploying code with conda

Anaconda is a popular data science driven Python distribution. Its
package manager, conda, can however be used for much more than just
installing Anaconda. It can for example manage independent
environments for different Python versions, or even C libraries. And
its tooling makes it fairly easy to build and distribute
cross-platform packages. In fact, we recently migrated from a
homegrown solution to conda for the deployment of our astronomical
data reduction software.

In this talk I'll survey the current state of Python package managers,
explain why we chose conda, and describe our development and deploy
workflow with conda. I'll also highlight some of its lesser known nice
features and pain points.
