#!/usr/bin/env python3

"""
This package provides simple routines for defining models or schemas.

Package: deepnox.models

This file is a part of python-wipbox project.

(c) 2021, Deepnox SAS.
"""

__import__("pkg_resources").declare_namespace(__name__)
from typing import Union, Any, Dict

import pydantic


class ExtendedBaseModel(pydantic.BaseModel):
    """
    An extended Pydantic model to support definition of properties.

    Resources:

    - https://github.com/samuelcolvin/pydantic/issues/935#issuecomment-554378904
    - https://stackoverflow.com/questions/63264888/pydantic-using-property-getter-decorator-for-a-field-with-an-alias

    """

    @classmethod
    def get_properties(cls):
        return [prop for prop in cls.__dict__ if isinstance(cls.__dict__[prop], property)]

    def dict(
            self,
            *,
            include: Union['AbstractSetIntStr', 'DictIntStrAny'] = None,
            exclude: Union['AbstractSetIntStr', 'DictIntStrAny'] = None,
            by_alias: bool = False,
            skip_defaults: bool = None,
            exclude_unset: bool = False,
            exclude_defaults: bool = False,
            exclude_none: bool = True,
    ) -> Dict[str, Any]:
        """Override the dict function to include our properties"""
        attribs = super().dict(
            include=include,
            exclude=exclude,
            by_alias=by_alias,
            skip_defaults=skip_defaults,
            exclude_unset=exclude_unset,
            exclude_defaults=exclude_defaults,
            exclude_none=exclude_none
        )
        props = self.get_properties()

        # Include and exclude properties
        if include:
            props = [prop for prop in props if prop in include]
        if exclude:
            props = [prop for prop in props if prop not in exclude]
        if exclude_none:
            props = [prop for prop in props if getattr(self, prop) is not None]

        # Update the attribute dict with the properties
        if props:
            attribs.update({prop: getattr(self, prop) for prop in props})
        return attribs
