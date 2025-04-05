class Mobile:
    def set_details(self, company, model, price):
        self.company = company
        self.model = model
        self.price = price

    def display_details(self):
        print(f"Company: {self.company}, Model: {self.model}, Price: ${self.price}")

mobile = Mobile()
mobile.set_details("Samsung", "Galaxy S21", 799)
mobile.display_details()
