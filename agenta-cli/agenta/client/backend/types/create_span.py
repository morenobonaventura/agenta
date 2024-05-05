# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .llm_tokens import LlmTokens
from .span_kind import SpanKind
from .span_status_code import SpanStatusCode

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class CreateSpan(pydantic.BaseModel):
    id: str
    app_id: typing.Optional[str]
    variant_id: typing.Optional[str]
    variant_name: typing.Optional[str]
    inputs: typing.Optional[typing.Dict[str, typing.Any]]
    outputs: typing.Optional[typing.List[str]]
    config: typing.Optional[typing.Dict[str, typing.Any]]
    environment: typing.Optional[str]
    tags: typing.Optional[typing.List[str]]
    token_consumption: typing.Optional[int]
    name: str
    parent_span_id: typing.Optional[str]
    attributes: typing.Optional[typing.Dict[str, typing.Any]]
    spankind: str
    status: str
    user: typing.Optional[str]
    start_time: dt.datetime
    end_time: typing.Optional[dt.datetime]
    tokens: typing.Optional[LlmTokens]
    cost: typing.Optional[float]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {
            "by_alias": True,
            "exclude_unset": True,
            **kwargs,
        }
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {
            "by_alias": True,
            "exclude_unset": True,
            **kwargs,
        }
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}
