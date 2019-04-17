:slug: testing-your-infrastructure-code
:speaker: ruben-homs
:year: 2019
:title: Testing your infrastructure code

Writing code to setup parts of your infrastructure isn't
new. Configuration management has been a part of most infrastructure
teams toolkits for a while now. However, unfortunately writing your
infrastructure code once and forgetting about it is the norm rather
than the exception. And, surprise surprise, things eventually break!
Repositories stop serving packages, GPG signatures change, and subtle
details to the way you implement your infrastructure code can cause
bugs. Those bugs are then only discovered when you have to deploy a
new instance of a service because it failed in the weekend after
you've had one too many drink. This defeats the whole point of having
your infrastructure as code. You need it to work always, especially in
case of an emergency.  In this talk I will explain how I solved this
issue by introducing Python tests for our SaltStack code and how we
continuously test this. Note that this technique will work with other
configuration management systems besides SaltStack.
