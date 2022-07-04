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
from typing import TYPE_CHECKING, overload

import urllib3

from cvat_api_client.api_client import ApiClient
from cvat_api_client.api_client import Endpoint as _Endpoint
from cvat_api_client.model.user_agreement import UserAgreement
from cvat_api_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types,
)

if TYPE_CHECKING:
    # Enable introspection. Can't work normally due to cyclic imports
    from cvat_api_client.apis import *
    from cvat_api_client.models import *


class RestrictionsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.terms_of_use_retrieve_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": [],
                "endpoint_path": "/api/restrictions/terms-of-use",
                "operation_id": "terms_of_use_retrieve",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "x_organization",
                    "org",
                    "org_id",
                ],
                "required": [],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "x_organization": (str,),
                    "org": (str,),
                    "org_id": (int,),
                },
                "attribute_map": {
                    "x_organization": "X-Organization",
                    "org": "org",
                    "org_id": "org_id",
                },
                "location_map": {
                    "x_organization": "header",
                    "org": "query",
                    "org_id": "query",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": [],
                "content_type": [],
            },
            api_client=api_client,
        )
        self.user_agreements_retrieve_endpoint = _Endpoint(
            settings={
                "response_type": (UserAgreement,),
                "auth": [],
                "endpoint_path": "/api/restrictions/user-agreements",
                "operation_id": "user_agreements_retrieve",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "x_organization",
                    "org",
                    "org_id",
                ],
                "required": [],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "x_organization": (str,),
                    "org": (str,),
                    "org_id": (int,),
                },
                "attribute_map": {
                    "x_organization": "X-Organization",
                    "org": "org",
                    "org_id": "org_id",
                },
                "location_map": {
                    "x_organization": "header",
                    "org": "query",
                    "org_id": "query",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/vnd.cvat+json"],
                "content_type": [],
            },
            api_client=api_client,
        )

    @overload
    def terms_of_use_retrieve(
        self,
        _return_http_data_only: typing.Literal[True] = True,
        _preload_content: typing.Literal[True] = True,
        **kwargs,
    ) -> None:
        ...

    @overload
    def terms_of_use_retrieve(
        self,
        _return_http_data_only: typing.Literal[False],
        _preload_content: typing.Literal[False],
        **kwargs,
    ) -> typing.Tuple[None, int, typing.Dict[str, str]]:
        ...

    @overload
    def terms_of_use_retrieve(
        self, _return_http_data_only: typing.Literal[False], **kwargs
    ) -> typing.Tuple[None, int, typing.Dict[str, str]]:
        ...

    @overload
    def terms_of_use_retrieve(
        self, _preload_content: typing.Literal[False], **kwargs
    ) -> urllib3.HTTPResponse:
        ...

    @overload
    def terms_of_use_retrieve(
        self,
        _return_http_data_only: typing.Literal[True],
        _preload_content: typing.Literal[False],
        **kwargs,
    ) -> urllib3.HTTPResponse:
        ...

    @overload
    def terms_of_use_retrieve(
        self,
        _return_http_data_only: typing.Literal[False],
        _preload_content: typing.Literal[False],
        **kwargs,
    ) -> urllib3.HTTPResponse:
        ...

    def terms_of_use_retrieve(
        self, **kwargs
    ) -> typing.Union[typing.Tuple[None, int, typing.Dict[str, str]], urllib3.HTTPResponse, None]:
        """Method provides CVAT terms of use  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.terms_of_use_retrieve(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            x_organization (str): [optional]
            org (str): Organization unique slug. [optional]
            org_id (int): Organization identifier. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Checked before _return_http_data_only.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _check_status (bool): whether to check response status
                for being positive or not.
                Default is True
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_check_status"] = kwargs.get("_check_status", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["_request_auths"] = kwargs.get("_request_auths", None)
        return self.terms_of_use_retrieve_endpoint.call_with_http_info(**kwargs)

    def terms_of_use_retrieve_raw(self, *args, **kwargs) -> urllib3.HTTPResponse:
        """
        The same as terms_of_use_retrieve(), but returns the response unprocessed.
        Equivalent to calling terms_of_use_retrieve with
        _preload_content = False and _check_status=False

        Method provides CVAT terms of use  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.terms_of_use_retrieve(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            x_organization (str): [optional]
            org (str): Organization unique slug. [optional]
            org_id (int): Organization identifier. [optional]
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        return self.terms_of_use_retrieve(
            *args, **kwargs, _preload_content=False, _check_status=False
        )

    @overload
    def user_agreements_retrieve(
        self,
        _return_http_data_only: typing.Literal[True] = True,
        _preload_content: typing.Literal[True] = True,
        **kwargs,
    ) -> UserAgreement:
        ...

    @overload
    def user_agreements_retrieve(
        self,
        _return_http_data_only: typing.Literal[False],
        _preload_content: typing.Literal[False],
        **kwargs,
    ) -> typing.Tuple[UserAgreement, int, typing.Dict[str, str]]:
        ...

    @overload
    def user_agreements_retrieve(
        self, _return_http_data_only: typing.Literal[False], **kwargs
    ) -> typing.Tuple[UserAgreement, int, typing.Dict[str, str]]:
        ...

    @overload
    def user_agreements_retrieve(
        self, _preload_content: typing.Literal[False], **kwargs
    ) -> urllib3.HTTPResponse:
        ...

    @overload
    def user_agreements_retrieve(
        self,
        _return_http_data_only: typing.Literal[True],
        _preload_content: typing.Literal[False],
        **kwargs,
    ) -> urllib3.HTTPResponse:
        ...

    @overload
    def user_agreements_retrieve(
        self,
        _return_http_data_only: typing.Literal[False],
        _preload_content: typing.Literal[False],
        **kwargs,
    ) -> urllib3.HTTPResponse:
        ...

    def user_agreements_retrieve(
        self, **kwargs
    ) -> typing.Union[
        typing.Tuple[UserAgreement, int, typing.Dict[str, str]], urllib3.HTTPResponse, UserAgreement
    ]:
        """Method provides user agreements that the user must accept to register  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.user_agreements_retrieve(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            x_organization (str): [optional]
            org (str): Organization unique slug. [optional]
            org_id (int): Organization identifier. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Checked before _return_http_data_only.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _check_status (bool): whether to check response status
                for being positive or not.
                Default is True
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            UserAgreement
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_check_status"] = kwargs.get("_check_status", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["_request_auths"] = kwargs.get("_request_auths", None)
        return self.user_agreements_retrieve_endpoint.call_with_http_info(**kwargs)

    def user_agreements_retrieve_raw(self, *args, **kwargs) -> urllib3.HTTPResponse:
        """
        The same as user_agreements_retrieve(), but returns the response unprocessed.
        Equivalent to calling user_agreements_retrieve with
        _preload_content = False and _check_status=False

        Method provides user agreements that the user must accept to register  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.user_agreements_retrieve(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            x_organization (str): [optional]
            org (str): Organization unique slug. [optional]
            org_id (int): Organization identifier. [optional]
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            UserAgreement
                If the method is called asynchronously, returns the request
                thread.
        """
        return self.user_agreements_retrieve(
            *args, **kwargs, _preload_content=False, _check_status=False
        )
