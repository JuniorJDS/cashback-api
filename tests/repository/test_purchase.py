from app.repositories.purchaseRepository import purchaseDb
from app.repositories.purchaseRepository import PurchaseCreate


def test_list_purchase_by_user(db, purchase):
    
    res = purchaseDb.list_by_user(db, purchase.userId)
    result = res[0]
    
    assert result.cod == purchase.cod
    assert result.price == purchase.price
    assert result.percentCashBack == purchase.percentCashBack


def test_list_purchase_by_id(db, purchase):
    
    result = purchaseDb.get_by_id(db, purchase.id)
    
    assert result.cod == purchase.cod
    assert result.price == purchase.price
    assert result.percentCashBack == purchase.percentCashBack


def test_list_purchase_by_no_valid_id(db):
    
    result = purchaseDb.get_by_id(db, "0c2380e4-7821-4068-be13-e09c95486fd9")

    assert result is None


def test_update(db, purchase):

    _purchase = {
        "status": "Aprovado"
    }

    result = purchaseDb.update(db, purchase.id, _purchase)

    assert result.status == 'Aprovado'

