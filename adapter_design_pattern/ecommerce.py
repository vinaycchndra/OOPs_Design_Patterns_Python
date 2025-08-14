from payment_processor import PaymentProcessor

class Ecommerce:
    @classmethod
    def checkout(cls, amount: float, payment_processor: PaymentProcessor):
        payment_processor.execute_transaction(amount)
        if payment_processor.is_successful(): 
            print(f"Transaction of amount : {payment_processor.get_amount()} is successful with {payment_processor.get_transaction_gateway()} processor with transaction id: {payment_processor.get_transaction_id()}.")
        else:
            print(f"Transaction is failed with {payment_processor.get_transaction_gateway()} processor.")
            

