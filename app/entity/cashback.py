

class Cashback():
    """ Calcular Cashback para a quantidade de vendas """

    @classmethod
    def compute_cashback(cls, price):
        if price <= 1000.00:
            return 0.01*price, 10
        elif price > 1000.00 and price <= 1500.00:
            return 0.015*price, 15
        elif price > 1500.00:
            return 0.02*price, 20

cash = Cashback()
