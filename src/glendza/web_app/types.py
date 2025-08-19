import typing

from django.db import models
from django.db.models.query import QuerySet

T = typing.TypeVar("T", bound=models.Model)

GenericQuerySet = QuerySet[T]
