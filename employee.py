class Employee(object):
    """docstring forEmployee."""

    def __init__(self,  name, designation, salesMadeThisWeek):
        self.name = name
        self.designation = designation
        self.salesMadeThisWeek = salesMadeThisWeek

    def hasAchievedTarget(self):
        if self.salesMadeThisWeek >= 5:
            print("Target Achieved")
        else:
            print("Target not Achieved")


John = Employee("Ben", "Sales Executive", 6)
John.hasAchievedTarget()
