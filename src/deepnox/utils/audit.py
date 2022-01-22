#!/usr/bin/env python3

"""
Auditing utilities.

This file is a part of python-wipbox project.

(c) 2021, Deepnox SAS.
"""

import asyncio
import time
import logging
from functools import wraps


from deepnox import loggers

LOGGER = loggers.factory(__name__)
""" The main LOGGER. """


def timeit(logger: logging.Logger, trace_params: bool = False):
    """
    A decorator to trace time execution.

    :param logger: The LOGGER.
    :param trace_params: Should I trace parameters?
    """

    def _timeit(f):
        @wraps(f)
        def wrap(*args, **kwargs):
            ts = time.monotonic()
            result = f(*args, **kwargs)
            te = time.monotonic()
            extra_trace = {
                'func_name': f.__name__,
                'execution_time': (te - ts),
            }
            if trace_params is True:
                extra_trace.update({'parameters': {'args': args, 'kwargs': kwargs}})
            logger.info(f'Execution time: {f.__name__}', extra=extra_trace)
            return result

        return wrap

    return _timeit


def async_timeit(func):
    async def process(func, *args, **params):
        if asyncio.iscoroutinefunction(func):
            print('this function is a coroutine: {}'.format(func.__name__))
            return await func(*args, **params)
        else:
            print('this is not a coroutine')
            return func(*args, **params)

    async def helper(*args, **params):
        print('{}.time'.format(func.__name__))
        start = time.time()
        result = await process(func, *args, **params)

        # Test normal function route...
        # result = await process(lambda *a, **p: print(*a, **p), *args, **params)

        print('>>>', time.time() - start)
        return result

    return helper


async def compute(x, y):
    print('Compute %s + %s ...' % (x, y))
    await asyncio.sleep(1.0)  # asyncio.sleep is also a coroutine
    return x + y


@timeit
async def print_sum(x, y):
    result = await compute(x, y)
    print('%s + %s = %s' % (x, y, result))

# loop = asyncio.get_event_loop()
# loop.run_until_complete(print_sum(1, 2))
# loop.close()
