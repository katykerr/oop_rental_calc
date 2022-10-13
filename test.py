class Rental_Property_Calc():

    def __init__(self, cash, investment, expenses, income):
        self.cash = cash
        self.investment = investment
        self.expenses = expenses
        self.income = income

    def find_income(self):
        income_list = []
        income = int(input("Please enter total Monthly Rental Income: $ "))
        income_list.append(income)
        self.find_income = print("Your TOTAL MONTHLY INCOME is: $", sum(income_list))
        self.find_expenses()

    def find_expenses(self):
        expense_list = []
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


roi = Rental_Property_Calc(cash, investment, expenses, income)





 