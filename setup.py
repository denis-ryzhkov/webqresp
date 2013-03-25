# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name='webqresp',
    version='0.1.0',
    description='Web load test measuring how many concurrent users will get response to their actions quickly - within a second.',
    long_description='''
Usage::

    webqresp http://example.com/
    webqresp --response-seconds=0.5 http://example.com/

Criterion:

    Maximal number of concurrent requests to the slowest URL
    while each request gets successful response within a second.

Why:

* Popular criterion Requests Per Second (RPS, req/s) has a great flaw of being confusing when comparing measurement before and after optimization. Please see `explanation <http://www.therailsway.com/2009/1/6/requests-per-second/>`_.
* Another criterion - Milliseconds Per Request (ms/req) calculated as 1000/(req/s) as proposed in the article above also has flaws:
    * It shows real response duration experienced by a user only when requests are sent sequentially, not concurrently:
        * Let's take 100,000 requests and send them to a server in a sequence, waiting for each response before sending the next request. If server processes all this in 10 seconds, it is giving 10,000 req/s, and each request gets response in 0.1 ms - great!
        * Now let's send 100,000 requests at the same time, not waiting for responses. If server processes all this in 10 seconds, it is giving the same 10,000 req/s, however while this criterion still shows false 0.1 ms, each request may get response in up to 10 seconds - that is not acceptable.
    * It still keeps proportion ambiguity:
        * Let's take 10,000 req/s == 0.1 ms/req == 10,000 concurrent requests with 1 second for each response - this is acceptable.
        * The same 10,000 req/s == 0.1 ms/req == 100,000 requests with 10 seconds for each response - this is not acceptable.
* Our criterion is constructed so that:
    * It cares about real response duration for each user in the worst concurrent case.
    * It is not a proportion. It is not ambiguous. Once 1 second is reached or failure occurs, it stops incrementing concurrent requests and returns the result.
* Single slowest URL is chosen to save time configuring the tool, because anyway "A chain is only as strong as its weakest link".
* You may adjust default response time of 1 second to a time required for your product.

''',
    url='https://github.com/denis-ryzhkov/webqresp',
    author='Denis Ryzhkov',
    author_email='denisr@denisr.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Testing :: Traffic Generation',
    ],
    scripts=['scripts/webqresp'],
    install_requires=[
        'gevent',
        'requests',
    ],
)