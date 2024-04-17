
## TODO: Invertory Data 모든 물류센터가 같이 사용하는 데이터가 존재해야함

class InventoryData:
    def __init__(self,product_list, product_count):
        self.inventory = dict(zip(product_list, product_count))

    # Create or Update Inventory
    def create_or_update_product(self, product_name, count):
        self.inventory[product_name] = count

    # Read Inventory
    def read_product_count(self, product_name):
        return self.inventory.get(product_name, None)

    # Update Inventory Count
    def update_product_count(self, product_name, count):
        if product_name in self.inventory:
            self.inventory[product_name] = count
        else:
            print(f"{product_name} 상품이 존재하지않습니다")

    def delete_product(self, product_name):
        if product_name in self.inventory:
            del self.inventory[product_name]
            print(f"{product_name} 지워졌습니다")
        else:
            print(f"{product_name} 상품이 존재하지않습니다 ")
    def print_inventory(self):
        if not self.inventory:
            print("Inventory is empty.")
        for product_name, count in self.inventory.items():
            print(f"Product: {product_name}, Count: {count}")

# Example usage
inventory = InventoryData(['Apple', 'Banana'], [10, 20])

# Create or update a product
inventory.create_or_update_product('Orange', 15)

# Read a product count
print(inventory.read_product_count('Apple'))  # Output: 10

# Update a product count
inventory.update_product_count('Banana', 25)

# Delete a product
inventory.delete_product('Apple')
