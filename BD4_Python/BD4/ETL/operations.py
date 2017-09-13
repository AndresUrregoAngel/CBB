

def convert(x):
    y = x.upper()
    return y

def reduction (qty,price,reduction = 0.2):
    if int(qty) <= 26:
        price = price - (price * reduction)
    return price

#y = reduction(14,399.95)
#print(y)