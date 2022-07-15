"""
    CVAT REST API

    REST API for Computer Vision Annotation Tool (CVAT)  # noqa: E501

    The version of the OpenAPI document: alpha (2.0)
    Contact: nikita.manovich@intel.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations

import re  # noqa: F401
import sys  # noqa: F401
import typing
from typing import TYPE_CHECKING

from cvat_sdk.exceptions import ApiAttributeError
from cvat_sdk.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    OpenApiModel,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)

if TYPE_CHECKING:
    # Enable introspection. Can't work normally due to cyclic imports
    from cvat_sdk.apis import *
    from cvat_sdk.models import *


def lazy_import():
    from cvat_sdk.model.comment_read import CommentRead
    from cvat_sdk.model.comment_read_owner import CommentReadOwner

    globals()["CommentRead"] = CommentRead
    globals()["CommentReadOwner"] = CommentReadOwner


class IssueRead(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      position ([float]):

      comments ([CommentRead]):

      id (int): [optional]  # noqa: E501

      frame (int): [optional]  # noqa: E501

      job (int): [optional]  # noqa: E501

      owner (CommentReadOwner): [optional]  # noqa: E501

      assignee (CommentReadOwner): [optional]  # noqa: E501

      created_date (datetime): [optional]  # noqa: E501

      updated_date (datetime): [optional]  # noqa: E501

      resolved (bool): [optional]  # noqa: E501


      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.

    """

    allowed_values = {}

    validations = {}

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (
            bool,
            date,
            datetime,
            dict,
            float,
            int,
            list,
            str,
            none_type,
        )  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            "position": ([float],),  # noqa: E501
            "comments": ([CommentRead],),  # noqa: E501
            "id": (int,),  # noqa: E501
            "frame": (int,),  # noqa: E501
            "job": (int,),  # noqa: E501
            "owner": (CommentReadOwner,),  # noqa: E501
            "assignee": (CommentReadOwner,),  # noqa: E501
            "created_date": (datetime,),  # noqa: E501
            "updated_date": (datetime,),  # noqa: E501
            "resolved": (bool,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None

    # member type declarations
    id: int  # noqa: E501
    """
    [optional]
    """

    frame: int  # noqa: E501
    """
    [optional]
    """

    position: typing.List[float]  # noqa: E501
    """
    [float]
    """

    job: int  # noqa: E501
    """
    [optional]
    """

    owner: CommentReadOwner  # noqa: E501
    """
    [optional]
    """

    assignee: CommentReadOwner  # noqa: E501
    """
    [optional]
    """

    created_date: datetime  # noqa: E501
    """
    [optional]
    """

    updated_date: datetime  # noqa: E501
    """
    [optional]
    """

    comments: typing.List[CommentRead]  # noqa: E501
    """
    [CommentRead]
    """

    resolved: bool  # noqa: E501
    """
    [optional]
    """

    attribute_map = {
        "position": "position",  # noqa: E501
        "comments": "comments",  # noqa: E501
        "id": "id",  # noqa: E501
        "frame": "frame",  # noqa: E501
        "job": "job",  # noqa: E501
        "owner": "owner",  # noqa: E501
        "assignee": "assignee",  # noqa: E501
        "created_date": "created_date",  # noqa: E501
        "updated_date": "updated_date",  # noqa: E501
        "resolved": "resolved",  # noqa: E501
    }

    read_only_vars = {
        "id",  # noqa: E501
        "frame",  # noqa: E501
        "job",  # noqa: E501
        "created_date",  # noqa: E501
        "updated_date",  # noqa: E501
        "resolved",  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, position, comments, *args, **kwargs):  # noqa: E501
        """IssueRead - a model defined in OpenAPI

        Args:
            position ([float]):
            comments ([CommentRead]):

        Keyword Args:
            id (int): [optional]  # noqa: E501

            frame (int): [optional]  # noqa: E501

            job (int): [optional]  # noqa: E501

            owner (CommentReadOwner): [optional]  # noqa: E501

            assignee (CommentReadOwner): [optional]  # noqa: E501

            created_date (datetime): [optional]  # noqa: E501

            updated_date (datetime): [optional]  # noqa: E501

            resolved (bool): [optional]  # noqa: E501

            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
        """
        from cvat_sdk.configuration import Configuration

        _check_type = kwargs.pop("_check_type", True)
        _spec_property_naming = kwargs.pop("_spec_property_naming", True)
        _path_to_item = kwargs.pop("_path_to_item", ())
        _configuration = kwargs.pop("_configuration", Configuration())
        _visited_composed_classes = kwargs.pop("_visited_composed_classes", ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments."
                        % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.position = position
        self.comments = comments
        for var_name, var_value in kwargs.items():
            if (
                var_name not in self.attribute_map
                and self._configuration is not None
                and self._configuration.discard_unknown_keys
                and self.additional_properties_type is None
            ):
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set(
        [
            "_data_store",
            "_check_type",
            "_spec_property_naming",
            "_path_to_item",
            "_configuration",
            "_visited_composed_classes",
        ]
    )

    @convert_js_args_to_python_args
    def __init__(self, position, comments, *args, **kwargs):  # noqa: E501
        """IssueRead - a model defined in OpenAPI

        Args:
            position ([float]):
            comments ([CommentRead]):

        Keyword Args:
            id (int): [optional]  # noqa: E501

            frame (int): [optional]  # noqa: E501

            job (int): [optional]  # noqa: E501

            owner (CommentReadOwner): [optional]  # noqa: E501

            assignee (CommentReadOwner): [optional]  # noqa: E501

            created_date (datetime): [optional]  # noqa: E501

            updated_date (datetime): [optional]  # noqa: E501

            resolved (bool): [optional]  # noqa: E501

            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
        """
        from cvat_sdk.configuration import Configuration

        _check_type = kwargs.pop("_check_type", True)
        _spec_property_naming = kwargs.pop("_spec_property_naming", False)
        _path_to_item = kwargs.pop("_path_to_item", ())
        _configuration = kwargs.pop("_configuration", Configuration())
        _visited_composed_classes = kwargs.pop("_visited_composed_classes", ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments."
                        % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.position = position
        self.comments = comments
        for var_name, var_value in kwargs.items():
            if (
                var_name not in self.attribute_map
                and self._configuration is not None
                and self._configuration.discard_unknown_keys
                and self.additional_properties_type is None
            ):
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(
                    f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                    f"class with read only attributes."
                )
