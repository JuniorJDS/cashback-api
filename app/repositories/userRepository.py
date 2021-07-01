from .repository import AbstractRepository
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate
from app.services.security import get_password_hash, verify_password
from app.repositories.models import User


class UserRepository(AbstractRepository):
    
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

    def get_by_email(self, db: Session, email: str):
        return db.query(self.model).filter(self.model.email == email).first()
    
    def get_by_id(self, db: Session, id: str):
        return db.query(self.model).filter(self.model.id == id).first()
    
    def authenticate(self, db: Session, email: str, password: str):
        userInfo = self.get_by_email(db, email=email)
        if not userInfo:
            return None
        if not verify_password(password, userInfo.password):
            return None
        return userInfo
    
    def delete(self, db: Session, obj):
        db.delete(obj)
        db.commit()
        return True


userDb = UserRepository(User)
