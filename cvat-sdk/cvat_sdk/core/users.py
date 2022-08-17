# Copyright (C) 2022 CVAT.ai Corporation
#
# SPDX-License-Identifier: MIT

from __future__ import annotations

from cvat_sdk.api_client import apis, models
from cvat_sdk.core.model_proxy import (
    ModelDeleteMixin,
    ModelListMixin,
    ModelRetrieveMixin,
    ModelUpdateMixin,
    build_model_bases,
)

_UserEntityBase, _UserRepoBase = build_model_bases(
    models.User, apis.UsersApi, api_member_name="users_api"
)


class User(
    models.IUser, _UserEntityBase, ModelUpdateMixin[models.IPatchedUserRequest], ModelDeleteMixin
):
    _model_partial_update_arg = "patched_user_write_request"


class UsersRepo(
    _UserRepoBase,
    ModelListMixin[User],
    ModelRetrieveMixin[User],
):
    _entity_type = User
