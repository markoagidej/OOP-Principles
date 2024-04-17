
# Task 1: Define Budget Category Class

class BudgetCategory:
    def __init__(self, name, budget):
        self.__name = name
        self.__budget = budget


# Task 2: Implement Getters and Setters

    def get_category_name(self):
        return self.__name 

    def set_category_name(self, new_name):
        self.__name = new_name

    def get_category_budget(self):
        return self.__budget 

    def set_category_budget(self, new_budget):
        if new_budget >= 0:
            self.__budget = new_budget
        else:
            print("Must enter a number 0 or higher!")


# Task 3: Add Budget Functionality

    def add_expense(self, amount):
        if amount > 0:
            self.__budget -= amount
        else:
            print("Must enter a number higher than 0!")


#Task 4: Display Budget Details

    def display_category_summary(self):
        print(f"Budget category \"{self.get_category_name()}\" has a current budget of {self.get_category_budget()}")


food_category = BudgetCategory("Food", 500)
food_category.add_expense(100)
food_category.display_category_summary()