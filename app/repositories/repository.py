from abc import ABC, abstractmethod

class AbstractRepository(ABC):

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
