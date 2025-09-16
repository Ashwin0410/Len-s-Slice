toppings = ["pepperoni","pineapple","cheese","sausage","olives","anchovies","mushroom"]
prices = [2,6,1,3,2,7,2]
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)
num_pizzas = len(toppings)
print(f"We sell {num_pizzas} different kinds of pizza!")
pizza_and_prices = list(zip(prices,toppings))
print(pizza_and_prices)
pizza_and_prices.sort()
print(pizza_and_prices)
cheapest_pizza = pizza_and_prices[:5]
print(cheapest_pizza)
priciest_pizza = pizza_and_prices[-1]
pizza_and_prices.pop(6)
pizza_and_prices.insert(6,(2.5,"peppers"))
pizza_and_prices.sort()
print(pizza_and_prices)
three_cheapest=pizza_and_prices[:3]
print(three_cheapest)
