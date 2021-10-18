from recipe import Recipe

def create_recipe(name, coffee=0, chocolate=0, milk=0, sugar=0, price=0.0):
    recipe = Recipe(name)
    recipe.coffee = coffee
    recipe.chocolate = chocolate
    recipe.milk = milk
    recipe.sugar = sugar
    recipe.price = price

if __name__ == '__main__':
    recipe1 = Recipe("Coffee with sugar")
    recipe1.coffee = 4
    recipe1.sugar = 2
    recipe1.milk = 0
    recipe1.price = 30.0
    print(recipe1)

    recipe2 = Recipe("Latte")
    recipe2.coffee = 3
    recipe2.sugar = 2
    recipe2.milk = 1
    recipe2.price = 40.0
    print(recipe2)


    recipe3 = create_recipe("Hot Chocolate",0,3,2,4,30.0)
    print(recipe3)

