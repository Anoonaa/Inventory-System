# inventory_mod.py
# Display menu with all options
def display_menu():
    print("\nInventory System Menu:")
    print("1. View all items")
    print("2. Add an item")
    print("3. Delete an item")
    print("4. Quit")
    print("5. Search for an item")
    print("6. Update item quantity")
    print("7. Clear inventory")
    print("8. Find low stock items")

# View inventory
def view_inventory(inventory):
    if not inventory:
        print("No items in inventory.")
    else:
        print("\nInventory:")
        for i, (name, quantity) in enumerate(inventory.items(), 1):
            print(f"{i}. {name} (Quantity: {quantity})")

# Add item
def add_item(inventory, name, quantity):
    try:
        if not name.strip():
            raise ValueError("Item name cannot be empty.")
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity must be a positive number.")
        if name.lower() in (key.lower() for key in inventory):
            print(f"Item {name} already exists!")
            return False
        inventory[name] = quantity
        print(f"Added {name} with quantity {quantity}.")
        return True
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
        return False

# Delete item
def delete_item(inventory, name):
    try:
        for key in list(inventory.keys()):
            if key.lower() == name.lower():
                del inventory[key]
                print(f"Deleted {name}.")
                return True
        print(f"Item {name} not found.")
        return False
    except TypeError:
        print("Error: Invalid input type.")
        return False

# Search item
def search_item(inventory, name):
    try:
        for key, quantity in inventory.items():
            if key.lower() == name.lower():
                print(f"Found: {key} (Quantity: {quantity})")
                return (key, quantity)
        print(f"Item {name} not found.")
        return None
    except TypeError:
        print("Error: Invalid input type.")
        return None

# Update item
def update_item(inventory, name, quantity):
    try:
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity must be a positive number.")
        for key in inventory:
            if key.lower() == name.lower():
                inventory[key] = quantity
                print(f"Updated {key} to quantity {quantity}.")
                return True
        print(f"Item {name} not found.")
        return False
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
        return False

# Clear inventory
def clear_inventory(inventory):
    try:
        if not inventory:
            print("Inventory is already empty.")
            return False
        inventory.clear()
        print("Inventory cleared.")
        return True
    except TypeError:
        print("Error: Invalid inventory data.")
        return False

# Find low stock items
def find_low_stock(inventory, threshold):
    try:
        if not isinstance(threshold, int) or threshold < 0:
            raise ValueError("Threshold must be a non-negative number.")
        low_stock = []
        for name, quantity in inventory.items():
            if quantity <= threshold:
                low_stock.append((name, quantity))
        if not low_stock:
            print(f"No items with quantity at or below {threshold}.")
        else:
            print(f"\nLow stock items (quantity <= {threshold}):")
            for i, (name, quantity) in enumerate(low_stock, 1):
                print(f"{i}. {name} (Quantity: {quantity})")
        return low_stock
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
        return []
