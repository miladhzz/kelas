class Pizza:
    def __init__(self):
        self.dough = None
        self.sauce = None
        self.cheese = None
        self.toppings = []

    def __str__(self):
        return (
            f"Pizza(dough={self.dough}, sauce={self.sauce}, "
            f"cheese={self.cheese}, toppings={self.toppings})"
        )


class PizzaBuilder:
    def __init__(self):
        self._pizza = Pizza()

    def set_dough(self, dough):
        self._pizza.dough = dough
        return self  # برای زنجیره‌ای شدن

    def set_sauce(self, sauce):
        self._pizza.sauce = sauce
        return self

    def set_cheese(self, cheese):
        self._pizza.cheese = cheese
        return self

    def add_topping(self, topping):
        self._pizza.toppings.append(topping)
        return self

    def build(self):
        pizza = self._pizza
        self._pizza = Pizza()  # ریست برای ساخت بعدی
        return pizza


# ساخت پیتزا به صورت مرحله‌ای و خوانا
pizza = (
    PizzaBuilder()
    .set_dough("thin")
    .set_sauce("tomato")
    .set_cheese("mozzarella")
    .add_topping("mushroom")
    .add_topping("olive")
    .build()
)

print(pizza)
# Pizza(dough=thin, sauce=tomato, cheese=mozzarella, toppings=['mushroom', 'olive'])        