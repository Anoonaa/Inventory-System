# inventory.py
# Import module
import inventory_mod

# Initialize dictionary
inventory = {}

# Main loop
while True:
    try:
        # Show menu
        inventory_mod.display_menu()
        # Get choice
        choice = input("Enter your choice (1-8): ")
        # Handle choice
        match choice:
            case "1":
                inventory_mod.view_inventory(inventory)
            case "2":
                name = input("Enter item name: ")
                quantity_str = input("Enter quantity: ")
                quantity = int(quantity_str)
                inventory_mod.add_item(inventory, name, quantity)
            case "3":
                name = input("Enter item name to delete: ")
                inventory_mod.delete_item(inventory, name)
            case "4":
                print("Exiting program...")
                break
            case "5":
                name = input("Enter item name to search: ")
                inventory_mod.search_item(inventory, name)
            case "6":
                name = input("Enter item name to update: ")
                quantity_str = input("Enter quantity: ")
                quantity = int(quantity_str)
                inventory_mod.update_item(inventory, name, quantity)
            case "7":
                inventory_mod.clear_inventory(inventory)
            case "8":
                threshold_str = input("Enter low stock threshold: ")
                threshold = int(threshold_str)
                inventory_mod.find_low_stock(inventory, threshold)
            case _:
                print("Invalid choice. Please enter 1, 2, 3, 4, 5, 6, 7, or 8.")
    except ValueError:
        print("Invalid input. Please enter a valid number for quantities or threshold.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
