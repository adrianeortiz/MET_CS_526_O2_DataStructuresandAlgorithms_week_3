"""
You are working for a promising new social media startup called "AlgoBook."

 The CEO would like to be able to input any individual at the company and figure out the budget of their organization.

The organization hierarchy is modeled as a tree where:
- individual contributors (IC) are leaf nodes
- organization managers (M) are internal nodes.

When figuring out an employee's organization there are two cases to consider:
1. If the employee is an M (internal node), their organization is the subtree rooted at their corresponding node.
2. If an employee is an IC (leaf node), their organization is the subtree rooted at their manager's corresponding node.

 An organization’s budget is the sum of the budgets of every person in the organization (M and IC).

A node in the organization tree should at least have:
- The employee id
- The budget of that employee
- A list of direct reports
- The employee's manager

This program has two main components:
1. The constructor for the organization class, which will take in a list of Employee objects, must con-
 vert the list into a tree data structure and store it as a class field. Each employee object has the following:
 - employeeId
 - managerId (or null if it is the CEO/root)
 - budget

 As a hint, it will make things easier if you also store a mapping of employeeId to EmployeeTreeN-
 odes as a second class field.

2. The getOrgBudget function will take in an employee id and return the total budget of that employees organization.

You are given the following in the starter code:
- The stubbed Organization class
- An Employee class
- An EmployeeTreeNode class with suggested fields
- Unit tests

 You may modify the EmployeeTreeNode class but may not change the Employee class.

 You must use a Tree data structure to store the organization and must use a tree traversal
 algorithm to compute an organization’s budget.

You must also provide an explanation of the running time of the getOrgBudget method

Code Author: <Your Name Here>

Running Time Analysis of get_org_budget
--------------------
<Your analysis here>
"""


class Employee:
    def __init__(self, employee_id, manager_id, budget):
        self.employee_id = employee_id
        self.manager_id = manager_id
        self.budget = budget


class EmployeeTreeNode:
    def __init__(self, employee: Employee):
        self.id = employee.employee_id
        self.budget = employee.budget
        self.manager_id = employee.manager_id
        # The below fields need to be set after instantiation
        self.reports = []
        self.manager_node = None
        self.is_manager = False


class AlgoBookOrganization:
    def __init__(self, employees):
        pass

    def get_org_budget(self, employee_id):
        return None


"""
DO NOT EDIT BELOW THIS
Below is the unit testing suite for this file.
It provides all the tests that your code must pass to get full credit.
"""


class TestAlgoBookOrganization:
    def run_unit_tests(self):
        self.test_simple_ceo()
        self.test_simple_individual()
        self.test_simple_manager()
        self.test_employee_not_found()
        self.test_many_reports()
        self.test_entire_org()

    def print_test_result(self, test_name, result):
        color = "\033[92m" if result else "\033[91m"
        reset = "\033[0m"
        print(f"{color}[{result}] {test_name}{reset}")

    def test_answer(self, test_name, result, expected):
        if result == expected:
            self.print_test_result(test_name, True)
        else:
            self.print_test_result(test_name, False)
            print(f"Expected: {expected} \nGot:      {result}")

    def test_simple_ceo(self):

        org = AlgoBookOrganization([
            Employee(123, None, 1000),
            Employee(233, 123, 1000),
            Employee(301, 233, 100),
            Employee(302, 233, 200),
            Employee(305, 234, 1000),
            Employee(304, 234, 0),
            Employee(303, 234, 0),
            Employee(234, 123, 2000),
            Employee(235, 123, 3000)

        ])
        result = org.get_org_budget(123)
        expected = 8300

        self.test_answer("test_simple_ceo", result, expected)

    def test_simple_individual(self):

        org = AlgoBookOrganization([
            Employee(123, None, 1000),
            Employee(233, 123, 1000),
            Employee(301, 233, 100),
            Employee(302, 233, 200),
            Employee(305, 234, 1000),
            Employee(304, 234, 0),
            Employee(303, 234, 0),
            Employee(234, 123, 2000),
            Employee(235, 123, 3000)

        ])
        result = org.get_org_budget(235)
        expected = 8300

        self.test_answer("test_simple_individual", result, expected)

    def test_simple_manager(self):

        org = AlgoBookOrganization([
            Employee(123, None, 1000),
            Employee(233, 123, 1000),
            Employee(301, 233, 100),
            Employee(302, 233, 200),
            Employee(305, 234, 1000),
            Employee(304, 234, 0),
            Employee(303, 234, 0),
            Employee(234, 123, 2000),
            Employee(235, 123, 3000)
        ])
        result = org.get_org_budget(233)
        expected = 1300

        self.test_answer("test_simple_manager", result, expected)

    def test_employee_not_found(self):
        org = AlgoBookOrganization([
            Employee(123, None, 1000),
            Employee(233, 123, 1000),
            Employee(301, 233, 100),
            Employee(302, 233, 200),
            Employee(305, 234, 1000),
            Employee(304, 234, 0),
            Employee(303, 234, 0),
            Employee(234, 123, 2000),
            Employee(235, 123, 3000)
        ])
        result = org.get_org_budget(404)
        expected = 0

        self.test_answer("test_employee_not_found", result, expected)

    def test_many_reports(self):
        org = AlgoBookOrganization([
            Employee(123, None, 1000),
            Employee(233, 123, 1000),
            Employee(301, 233, 50),
            Employee(302, 233, 50),
            Employee(305, 233, 1000),
            Employee(304, 233, 0),
            Employee(303, 233, 0),
            Employee(234, 233, 2000),
            Employee(235, 233, 3000)
        ])
        result = org.get_org_budget(233)
        expected = 7100

        self.test_answer("test_many_reports", result, expected)

    def test_entire_org(self):
        org = AlgoBookOrganization([
            Employee(1, None, 1000),  # CEO
            Employee(2, 1, 500),  # Manager 1
            Employee(3, 1, 600),  # Manager 2
            Employee(4, 2, 200),  # Manager 3
            Employee(5, 2, 300),  # Employee 1
            Employee(6, 3, 400),  # Employee 2
            Employee(7, 3, 200),  # Employee 3
            Employee(8, 4, 100),  # Employee 4
            Employee(9, 4, 100),  # Employee 5
            Employee(10, 4, 100),  # Employee 6
        ])
        results = [org.get_org_budget(i) for i in range(1, 11)]
        expected = [3500, 1300, 1200, 500, 1300, 1200, 1200, 500, 500, 500]

        self.test_answer("test_entire_org", results, expected)


if __name__ == '__main__':
    test_runner = TestAlgoBookOrganization()
    test_runner.run_unit_tests()