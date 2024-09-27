from list_customer import ListCustomer
from utils import *

def main():
    list_customers = ListCustomer()
    while True:
        print('\n\tWelcome to Manager Customer System')
        print('\t\t1. Create new Customer')
        print('\t\t2. Customer list')
        print('\t\t3. Update customer by name')
        print('\t\t4. Export customers to JSON')
        print('\t\t5. Exit')
        choice = input('Enter your choice: ')

        if choice == '1':
            customer = inputCustomer()
            
            list_customers.addCustomer(customer)

        if choice == '2':
            print("List of Customer")
            list_customers.findAll()

        if choice == '3':
            name = input('Enter your name of customer you want to update: \t')
            list_customers.updateByName(name)

        if choice == '4':
            list_customers.exportCustomers()

        if choice == '5':
            break


main()
