from .repository import AbstractRepository


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        self.session = session
    
    def create(self):
        pass
    
    def list(self):
        pass
    
    def list_by_id(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass
