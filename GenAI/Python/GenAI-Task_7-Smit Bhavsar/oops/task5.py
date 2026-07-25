#Task 5: Abstraction
from abc import ABC, abstractmethod
class Payment(ABC):
    
    @abstractmethod
    def process_payment(self, amount):
        pass
    
class CreditcardPayment(Payment):
    def process_payment(self, amount):
        return f"payment Proccessed for {amount} by credit card"
    
class UPIPayment(Payment):
    def process_payment(self, amount):
        return f"payment Proccessed for {amount} by UPI"
    
creditcard = CreditcardPayment()
print(creditcard.process_payment(5000))

upi = UPIPayment()
print(upi.process_payment(5000))