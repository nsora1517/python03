import sys


def main() -> None:
    args = sys.argv[1:]
    inventory: dict[str, int] = {}
    print("=== Inventory System Analysis ===")
    for arg in args:
        card = arg.split(":")
        if len(card) != 2:
            print(f"Error - invalid parameter '{arg}'")
            continue
        try:
            num = int(card[1])
        except ValueError as e:
            print(f"Quantity error for '{card[0]}': {e}")
            continue
        if card[0] in inventory:
            print(f"Redundant item '{card[0]}' - discarding")
            continue
        inventory[card[0]] = num

    if len(inventory) == 0:
        return

    total = sum(inventory.values())
    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    print(f"Total quantity of the {len(inventory)}"
          f" items: {total}")

    items = list(inventory.keys())
    most = items[0]
    least = items[0]
    for name in inventory.keys():
        qty = inventory[name]
        if inventory[name] > inventory[most]:
            most = name
        if inventory[name] < inventory[least]:
            least = name
        percent = round(qty / total * 100, 1)
        print(f"Item {name} represents {percent}%")
    print(f"Item most abundant: {most} with quantity {inventory[most]}")
    print(f"Item least abundant: {least} with quantity {inventory[least]}")
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
