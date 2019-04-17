:slug: file-system-caching-a-backend-implementation-for-dogpilecache
:speaker: alessio-bogon
:year: 2019
:title: File system caching: a backend implementation for dogpile.cache

Dogpile.cache is a library that provides caching primitives and it
natively supports backends like Memcached, Redis, and a simple file
system implementation. In Paylogic, we needed a more advanced file
system implementation, and eventually, we wrote our own file system
backend.

In this talk, I will briefly introduce the dogpile.cache architecture,
discuss the limitations of the native file system backend and why at
Paylogic we decided to implement a more advanced backend.

In this journey, we will explore some of the less-used file system
locking primitives of \*nix systems and how we (ab)used them, the
difficulty of testing when concurrency is involved and some lessons
learned during the development. We will also see some python WTFs
about file objects.
