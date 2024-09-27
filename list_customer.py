import pandas as pd
from pymongo import MongoClient
from customer import Customer
from utils import *
from db_config import DB_CONFIG


class ListCustomer:
    def __init__(self):
        client = MongoClient(**DB_CONFIG)
        db = client['CustomersDB']
        self.customer_details = db['customers']

    def addCustomer(self, customer):
        data = customer.covert_to_json()
        self.customer_details.insert_one(data)
        print("Customer Inserted successfully")

    def findAll(self):
        dicts = self.customer_details.find({})
        for d in dicts:
            customer = Customer.init_from_data(d)
            customer.display()

    def updateByName(self, sName):
        my_query = {"name": sName}
        customer = self.customer_details.find({"name": sName})

        if customer:
            print('\nModify Customer Data with name=', sName)
            new_customer = inputCustomer()
            data = new_customer.covert_to_json()
            update_value = {"$set": data}
            
            if self.customer_details.update_one(my_query, update_value) != 0:
                print('Updated Successful')
            else:
                print('Update Fail')
        else:
            print('No customer has name:', sName)


    def exportCustomers(self):
        dicts = self.customer_details.find({})
        if dicts is None:
            print('Customers Not Found')
        else:
            df = pd.DataFrame(dicts)
            df.to_csv('output.csv', index=False)
            print("Data exported to 'output.csv'")