#!/usr/bin/env python3

"""
Base of (deepnox.aiobox) module.

Module: deepnox.aiobox.base

This file is a part of (deepnox.aiobox) project.

(c) 2021, Deepnox SAS.
"""
import asyncio
from types import FunctionType


class Task(object):
    """
    A task.
    """

    def __init__(self,
                 loop: asyncio.AbstractEventLoop = None,
                 fn: FunctionType = None,
                 ):
        if not isinstance(fn, FunctionType):
            raise TypeError(f"Routine cannot be typed: {type(fn)}")
        self.loop = loop or asyncio.get_event_loop()
        self.fn = fn
