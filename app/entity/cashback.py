

class Cashback():
    """ Calcular Cashback para a quantidade de vendas """

    @classmethod
    def compute_cashback(cls, value):
        if value <= 1000.00:
            print('10% de Cashback')
        elif value > 1000.00 and value <= 1500.00:
            print('15% de Cashback')
        elif value > 1500.00:
            print('20% de Cashback')


#cash = Cashback()
#cash.compute_cashback(1200)

from cryptography.fernet import Fernet
key = Fernet.generate_key()
print(key)
