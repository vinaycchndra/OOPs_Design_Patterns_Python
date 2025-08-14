from abc import ABC, abstractmethod

class PaymentProcessor(ABC): 
    
    @abstractmethod
    def execute_transaction(): 
        pass
    
    @abstractmethod
    def is_successful(): 
        pass

    @abstractmethod
    def get_transaction_id(): 
        pass
    
    @abstractmethod
    def get_amount(self): 
        pass
    
    @abstractmethod
    def get_transaction_gateway(): 
        pass