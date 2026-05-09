def calculate_discount(item_name, price, promo_code):
    
    code = promo_code.upper() if promo_code else ""
    
    if code == "SAVE10":
        discount_rate = 0.10
    elif code == "HALFOFF":
        discount_rate = 0.50
    else:
        discount_rate = 0.0
        
    return price * (1 - discount_rate)
    
    print(calcuate_discount("cereal", 100, "SAVE10"))
