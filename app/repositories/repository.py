from abc import ABC, abstractmethod
from .orm import Base
from typing import TypeVar, Type

ModelType = TypeVar("ModelType", bound=Base)


class AbstractRepository(ABC):

    def __init__(self, model: Type[ModelType]) -> None:
        self.model = model
