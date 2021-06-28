from .repository import AbstractRepository
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserLogin
from app.services.security import get_password_hash, verify_password
from app.repositories.models import User


class SqlAlchemyRepository(AbstractRepository):
    
    def create(self, db: Session, user: UserCreate):
        obj = self.model(
            fullName=user.fullName,
            cpf=user.cpf,
            email=user.email,
            password=get_password_hash(user.password))
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj
    
    def list_by_email(self, db: Session, email: str):
        return db.query(self.model).filter(self.model.email == email).first()
    
    def list_by_id(self, db: Session, id: str):
        return db.query(self.model).filter(self.model.id == id).first()
    
    def authenticate(self, db: Session, user: UserLogin):
        userInfo = self.list_by_email(db, email=user.email)
        if not userInfo:
            return None
        if not verify_password(user.password, userInfo.password):
            return None
        return userInfo
    
    def list(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass


userDb = SqlAlchemyRepository(User)
