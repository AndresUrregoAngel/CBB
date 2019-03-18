

def discount(qty,price,qtyv):
    """This method valides the qty and
    assign a discount based on the qty"""
    if qty >= qtyv:
        price = price - (price * 20 /100)

    return price


def upper_case(description):

    return description.upper()


