class Order:
    def __init__(self, order_id, customer_name, items):
        self.order_id = order_id
        self.customer_name = customer_name
        self.items = items  


    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.price * item.quantity
        return total

    def process_order(self, inventory):
        for item in self.items:
            for product in inventory.products:
                if product.product_id == item.product_id:
                    if product.quantity >= item.quantity:
                        product.quantity -= item.quantity
                        print(f"{item.quantity} {item.name} added to order.")
                    else:
                        print(f"Insufficient stock for {item.name}.")
                else:
                    print(f"Product {item.name} not found.")