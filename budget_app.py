class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.total = 0
        self.spent = 0

    def deposit(self, amount, description = ""):
        self.ledger.append({"amount": amount, "description": description})
        self.total += amount

    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            self.total -= amount
            self.spent += amount
            return True
        else:
            return False

    def check_funds(self, amount):
        if self.total < amount:
            return False
        else:   
            return True

    def get_balance(self):
        return self.total

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, description = f"Transfer to {category.name}")
            category.deposit(amount, description = f"Transfer from {self.name}")
            return True
        else:
            return False

    def __repr__(self):
        title = self.name.center(30, "*")
    
        line = ""
        for item in self.ledger:
            desc = item["description"]
            form = "{:.2f}".format(item["amount"])
            line += desc[0:23] + " " + (form + "\n").rjust(len(title)-len(desc))
            
        
        display = title + "\n" + line + "Total: " + str(self.total)

        return display

#chart
def create_spend_chart(categories):

    totalspent = 0
    for category in categories:
        totalspent += category.spent

    percents = []
    for category in categories:
        perc = category.spent/totalspent * 100
        percents.append(perc)
        
    line = "Percentage spent by category"
    for n in range(100,-10,-10):
        line +=  "\n" + " "*(3-len(str(n))) + str(n) + "| " 
        for perc in percents:
            if perc >= n:
                line += "o  "
            else:
                line += "   "

    separator = "\n" + "    " + "-" + "---"*len(categories)

    bottom = ""
    largest = 0
    for category in categories:
        if len(category.name) > largest:
            largest = len(category.name)
    for n in range(largest):
        bottom += "     "
        for category in categories:
            if len(category.name) > n:
                bottom += category.name[n] + "  "
            else:
                bottom += "   "
        if largest - 1 != n:
            bottom += "\n"

    show = line + separator + "\n" + bottom

    return show

