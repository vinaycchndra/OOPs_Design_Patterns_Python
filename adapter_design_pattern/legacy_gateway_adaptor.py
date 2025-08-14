from payment_processor import PaymentProcessor
from uuid import uuid4
from legacy_gateway import LegacyGateWay

class LegacyGatewayAdaptor(PaymentProcessor): 
    def __init__(self, legacy_gateway: LegacyGateWay):
        self.__amount = 0
        self.legacy_gateway = legacy_gateway
        
    def execute_transaction(self, amount: float = 0, currency: str = "Rupee"):
        self.__amount = amount 
        self.legacy_gateway.execute_transaction(amount*self.__get_dollar_to_rupee())
    
    def get_transaction_id(self):
        return self.legacy_gateway.get_transaction_id()

    def is_successful(self):
        return self.legacy_gateway.is_successful()
    
    def get_amount(self):
        return self.__amount

    def __get_dollar_to_rupee(self): 
        return 1/80

    def get_transaction_gateway(self):
        return "Legacy Gateway"
