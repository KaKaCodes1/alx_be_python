weatherInput = input("What's the weather like today? (sunny/rainy/cold): ")

if weatherInput.lower() == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weatherInput.lower() == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weatherInput.lower() == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")