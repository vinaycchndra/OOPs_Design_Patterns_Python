from uuid import uuid4
from payment_processor import PaymentProcessor

class InhousePaymentProcessor(PaymentProcessor): 
    def __init__(self):
        self.__is_successful = None
        self.__transaction_id = None
        self.__amount = 0
    
    def execute_transaction(self, amount: float, currency: str = "Rupee"):
        self.__transaction_id = f'{currency}:{uuid4()}'
        self.__amount = amount
        self.__is_successful = True
    
    def get_transaction_id(self):
        return self.__transaction_id        

    def is_successful(self):
        return self.__is_successful
    
    def get_amount(self):
        return self.__amount
    
    def get_transaction_gateway(self):
        return "In House Transaction"