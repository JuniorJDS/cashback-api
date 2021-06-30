from .repository import AbstractRepository
from sqlalchemy.orm import Session
from app.schemas.purchase import PurchaseCreate, PurchaseUpdate
from app.services.security import get_password_hash, verify_password
from app.repositories.models import Purchase


class purchaseRepository(AbstractRepository):
    
    def create(self, db: Session, purchase: PurchaseCreate):
        obj = self.model(
            cod=purchase.cod,
            price=purchase.price,
            data=purchase.data,
            percentCashBack=purchase.percentCashBack,
            valueCashBack=purchase.valueCashBack,
            status=purchase.status,
            userId=purchase.userId)
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    def list_by_user(self, db: Session, userId: str):
        return db.query(self.model).filter(self.model.userId == userId).all()
    
    def list_by_id(self, db: Session, id: str):
        return db.query(self.model).filter(self.model.id == id).first()
    
    def update(self, db: Session, id: str, purchase):
        db.query(self.model).filter(self.model.id == id).update(purchase)
        db.commit()
        return self.list_by_id(db, id)
    
    def delete(self, db: Session, obj):
        db.delete(obj)
        db.commit()
        return True


purchaseDb = purchaseRepository(Purchase)
