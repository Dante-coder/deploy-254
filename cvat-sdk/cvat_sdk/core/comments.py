# Copyright (C) 2022 CVAT.ai Corporation
#
# SPDX-License-Identifier: MIT

from __future__ import annotations

from cvat_sdk.api_client import apis, models
from cvat_sdk.core.model_proxy import (
    ModelCreateMixin,
    ModelDeleteMixin,
    ModelListMixin,
    ModelRetrieveMixin,
    ModelUpdateMixin,
    build_model_bases,
)

_CommentEntityBase, _CommentRepoBase = build_model_bases(
    models.CommentRead, apis.CommentsApi, api_member_name="comments_api"
)


class Comment(
    models.ICommentRead,
    _CommentEntityBase,
    ModelUpdateMixin[models.IPatchedCommentWriteRequest],
    ModelDeleteMixin,
):
    _model_partial_update_arg = "patched_comment_write_request"


class CommentsRepo(
    _CommentRepoBase,
    ModelListMixin[Comment],
    ModelCreateMixin[Comment, models.ICommentWriteRequest],
    ModelRetrieveMixin[Comment],
):
    _entity_type = Comment
