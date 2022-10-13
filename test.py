class Rental_Property_Calc():
                # \/ \/ -- Took out the parameters, we don't need these to instantiate the class
                # because we don't know what they are yet!
    def __init__(self):
        self.cash = None
        self.investment = None
        self.expenses = None
        self.income = None
        # set to None ^^^^ -- since we don't know what these are yet
    def find_income(self):
        income_list = []
        # ^^^  Do we need this?  If we're modifying self.income I would leave it as an int.
        income = int(input("Please enter total Monthly Rental Income: $ "))
        # income_list.append(income)
        self.income = income
        #
        # self.find_income = print("Your TOTAL MONTHLY INCOME is: $", sum(income_list))
        # self.find_expenses()
        # ^^^^^ -- let's run the methods as an execution method (I usually call it run, see at the bottom)

    # This \/ \/ \/ --> isn't how I would do this but that doesn't make it wrong.
    #  I recommend doing    a = input(x)
    #                       b = input(x)
    #                self.expenses = a + b + c
    def find_expenses(self):
        expense_list = []
        #           \/ \/ \/ --it looks like you're trying to access an attribut here not a method right?
        cash = self.find_income - sum(expense_list) * 12
        a, b, c, d, e, f, g = int(input("Let's Find Your Monthly Expenses")).split()
        print(int(input("Enter your MORTGAGE:$", a)))
        print(int(input("Enter your PROPERTY MANAGEMENT COST:$", b )))
        print(int(input("Enter your TAXES:$", c)))
        print(int(input("Enter your INSURANCE COST:$", d)))
        print(int(input("Enter your VACANCY SAVINGS:$", e)))
        print(int(input("Enter your REPAIRS:$", f)))
        print(int(input("Enter your CAPITAL EXPENSES:$", g)))
        expense_list.append()
        print(f"Your TOTAL MONTHLY EXPENSES ARE:$", sum(expense_list))
        print(f"Your annual CASH FLOW is:", cash)
        self.find_investment()

    def find_investment(self):
        find_investment = int(input("Please enter your TOTAL INVESTMENT in this property: $ "))
        print(f"Your Return on Investment for this property is:" + self.cash // find_investement)
    
    # EXAMPLE \/ \/ \/ 
    # def run(self):
    #     x  = input('welcome to my calc, please enter <whatever> to do <whatever>')
    #     while True:
    #         if x == <whatever>:
    #             self.run this method!



x = Rental_Property_Calc()
x.find_expenses()





 