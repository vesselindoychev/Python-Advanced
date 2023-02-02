def shopping_list(budget, **kwargs):
    total_price = 0
    basket = 0
    res = []
    if budget < 100:

        return f"You do not have enough budget."

    else:
        for i in kwargs.items():
            product = i[0]
            product_price = i[1][0]
            quantity = i[1][1]

            total_price = quantity * product_price

            if budget >= total_price:
                budget -= total_price
                basket += 1
                # print(f'You bought {product} for {total_price:.2f} leva.')
                res.append(f'You bought {product} for {total_price:.2f} leva.\n')
            if basket == 5:
                return "".join(res)

        return "".join(res)


print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))
print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))
print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
