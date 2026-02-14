import sys

def get_args():
    elements = {}
    try:
        for arg in sys.argv[1:]:
            key, value = arg.split(":")
            elements.update({key: int(value)})
    except ValueError as err:
        print(f"Error details - Type: ValueError, Args: (\"{err}\",)")
    return elements
        
def total_items(elements: dict):
    total = 0
    for value in elements.values():
        total += value
    return total
        
def unique_items(elements: dict):
    result = 0
    for key in elements.keys():
        result+=1
    return result

def current_inventory(elements: dict, total: int):
    for key, value in sorted(elements.items(), key=lambda kv: kv[1], reverse=True):
        percentage = (value / total)*100
        unit_word = "units" if value > 1 else "unit"
        print(f"{key}: {value} {unit_word} ({percentage:.1f}%)")
    
def statistics(elements: dict):
    max_key, max_value = None, -1
    min_key, min_value = None, 1
    for key, value in elements.items():
        if value > max_value:
            max_key, max_value = key, value
        if  value <= min_value:
            min_key, min_value = key, value
    unit_word1 = "units" if max_value > 1 else "unit"
    unit_word2 = "units" if min_value > 1 else "unit"
    print(f"Most abundant: {max_key} ({max_value} {unit_word1})")
    print(f"Least abundant: {min_key} ({min_value} {unit_word2})")

def item_categories(elements: dict):
    moderate = {}
    scarce = {}
    max_key, max_value = None, -1
    for key, value in elements.items():
        if value > max_value:
            max_key, max_value = key, value
    for key, value in elements.items():
        if value >= max_value:
            moderate[max_key] = max_value
        else:
            scarce[key] = value
    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}")

def stock_management(elements: dict):
    restock = []
    for key, value in elements.items():
        if value <= 1:
            restock.append(key)
    return restock


def inventory_system():
    print("=== Inventory System Analysis ===")

    elements = get_args()
    total = total_items(elements)
    print(f"Total items in inventory: {total}")

    unique = unique_items(elements)
    print(f"Unique item types: {unique}")

    print("\n=== Current Inventory ===")
    current_inventory(elements, total)

    print("\n=== Inventory Statistics ===")
    statistics(elements)

    print("\n=== Item Categories ===")
    item_categories(elements)
    
    print("\n=== Management Suggestions ===")
    restock = stock_management(elements)
    print(f"Restock needed: {restock}")
    
    print("\n=== Dictionary Properties Demo ===")
    print("Dictionary keys:", end=" ")
    print(*elements.keys(), sep=", ")
    print("Dictionary values:", end=" ")
    print(*elements.values(), sep=", ")
    
    print()
    print(f"Sample lookup - 'sword' in inventory: {"sword" in elements}")
    
if __name__ == "__main__":
    inventory_system()