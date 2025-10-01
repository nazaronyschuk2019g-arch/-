def format_price(price: float) -> str:
    return f"ціна: {price:.2f} грн"



def check_availability(**products):

  
    return products



def make_order(order: list, catalog: dict, action: str):
   
  

    for item in order:
        if item not in catalog or not catalog[item][1]:
            return f"Товар '{item}
            


    if action == "check":
        return f"Загальна {format_price(total)}"
    elif action == "buy":
        return f"Ви успішно купили товари: {', '.join(order)} на суму {format_price(total)}"
    else:
        return "Невідома дія. Використовуйте 'buy' або 'check'."




catalog = {
    "яблуко": (15.5, True),
    "банан": (28.0, False),
    "груша": (30.0, True)
}

print(format_price(123.456))  # -> ціна: 123.46 грн
print(check_availability(яблуко=True, банан=False, груша=True))

print(make_order(["яблуко", "груша"], catalog, "check"))  # Перегляд ціни
print(make_order(["яблуко", "груша"], catalog, "buy"))    # Купівля
print(make_order(["яблуко", "банан"], catalog, "buy"))    # Є відсутній товар
