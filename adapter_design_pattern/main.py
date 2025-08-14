from ecommerce import Ecommerce
from in_house_payment_processor import InhousePaymentProcessor
from legacy_gateway_adaptor import LegacyGatewayAdaptor
from legacy_gateway import LegacyGateWay

def main(): 
    # Making transaction with in-house processor...
    amount = 160
    inhouse_payment_processor = InhousePaymentProcessor()
    Ecommerce.checkout(amount, inhouse_payment_processor)

    # Making transaction with Legacy gateway processor...
    amount = 160
    legacy_gateway = LegacyGateWay()
    legacy_payment_processor = LegacyGatewayAdaptor(legacy_gateway=legacy_gateway)
    Ecommerce.checkout(amount, legacy_payment_processor)

if __name__ == "__main__": 
    main()
