def main():
    inventory = Inventory()

    # Add products to the inventory
    product1 = Product(1, "Laptop", 10, 800)
    product2 = Product(2, "Phone", 20, 500)
    inventory.add_product(product1)
    inventory.add_product(product2)

    # Display the inventory
    inventory.display_inventory()

    # Remove a product
    inventory.remove_product(1)

    # Update product quantity
    inventory.update_product_quantity(2, 15)

    # Display the updated inventory
    inventory.display_inventory()

    # Place an order
    customer_name = "Rita"
    order_items = [
        {"product_id": 1, "quantity": 5},
        {"product_id": 2, "quantity": 3}
    ]
    order = Order(1, customer_name, order_items)
    order.process_order(inventory)

if __name__ == "__main__":
    main()