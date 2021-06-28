from abc import ABC, abstractmethod
from .orm import Base
from typing import TypeVar, Type

ModelType = TypeVar("ModelType", bound=Base)


class AbstractRepository(ABC):

    def __init__(self, model: Type[ModelType]) -> None:
        self.model = model

    @abstractmethod
    def create(self):
        raise NotImplementedError
    
    @abstractmethod
    def list(self):
        raise NotImplementedError
    
    @abstractmethod
    def list_by_id(self):
        raise NotImplementedError

    @abstractmethod
    def update(self):
        raise NotImplementedError

    @abstractmethod
    def delete(self):
        raise NotImplementedError
