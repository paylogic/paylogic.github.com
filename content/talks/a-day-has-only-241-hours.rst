:slug: a-day-has-only-24-plus-minus-1-hours
:speaker: miroslav-sedivy
:year: 2019
:title: A Day Has Only 24±1 Hours

On the last Sunday of October you may get “one more hour of sleep” but
also may spend much more time debugging code dealing with the
timezones, daylight saving time shifts and datetime stuff in general.

Invention of the geographers in the 19th century, time zones became a
true victim of short-sighted political decisions during the 20th and
21st centuries. And it is still our duty to keep track of this whole
fiddling with our clocks.

We'll look at a few pitfalls you may encounter when working with
datetimes in Python. We'll discover the pytz module and explain why
pytz.all_timezones contains over 500 individual timezones, with a
slight focus on the Netherlands and surrounding countries. We'll also
find the reason why pytz is not part of the standard Python, why it
gets updated so often and why even that won't solve all your problems.

Two centuries of propaganda and chaos in thirty minutes. Maybe that
will make you want to avoid time zones in your code altogether!
