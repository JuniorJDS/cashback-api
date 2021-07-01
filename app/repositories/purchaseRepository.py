from sqlalchemy.orm import Session

from app.schemas.purchase import PurchaseCreate
from app.repositories.models import Purchase
from .repository import AbstractRepository


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
    
    def get_by_id(self, db: Session, id: str):
        return db.query(self.model).filter(self.model.id == id).first()
    
    def update(self, db: Session, id: str, purchase):
        db.query(self.model).filter(self.model.id == id).update(purchase)
        db.commit()
        return self.get_by_id(db, id)
    
    def delete(self, db: Session, obj):
        db.delete(obj)
        db.commit()
        return True


purchaseDb = purchaseRepository(Purchase)
