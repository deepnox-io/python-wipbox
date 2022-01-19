#!/usr/bin/env python3

"""
Extended classes used for managing enumerations.

Module: deepnox.core.enums

This file is a part of LoadGuard Runner.

(c) 2021, Deepnox SAS.

"""
from enum import Enum, unique


class DeepnoxEnum(Enum):
    """
    Extended base class to manage enumeration.
    """

    def __str__(self):
        return self.value

@unique
class UniqueEnum(DeepnoxEnum):
    """
    Extended base class to manage enumeration.
    """


