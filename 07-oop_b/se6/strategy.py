# --- 1) اینترفیس مشترک (قرارداد) ---
class DiscountStrategy:
    def calculate(self, price):
        raise NotImplementedError

# --- 2) استراتژی‌های مشخص ---
class NoDiscount(DiscountStrategy):
    def calculate(self, price):
        return price

class TenPercent(DiscountStrategy):
    def calculate(self, price):
        return price * 0.9

class BlackFriday(DiscountStrategy):
    def calculate(self, price):
        return price * 0.5 if price > 100 else price * 0.8

# --- 3) Context: کسی که استراتژی را استفاده می‌کند ---
class Order:
    def __init__(self, price, strategy: DiscountStrategy):
        self.price = price
        self.strategy = strategy

    def set_strategy(self, strategy: DiscountStrategy):
        self.strategy = strategy

    def total(self):
        return self.strategy.calculate(self.price)

# --- 4) استفاده ---
order = Order(200, TenPercent())
print(order.total())          # 180.0

order.set_strategy(BlackFriday())
print(order.total())          # 100.0  (چون 200 > 100)