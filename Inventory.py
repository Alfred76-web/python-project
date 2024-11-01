class Inventory:  

    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self,product_id):
        for product in self.products:
            if product.product_id == product_id:
                self.products.remove(product)
                print(f"Product   
 {product.name} removed.")
                return
        print("Product not found.")

    def update_product_quantity(self, product_id, new_quantity):
        for product in self.products:
            if product.product_id == product_id:
                product.quantity = new_quantity
                print(f"Quantity   
 of {product.name} updated to {new_quantity}.")
                return
        print("Product not found.")

    def display_inventory(self):
        print("inventory:")
        for product in self.products:
            print(product)