class Customer:
    def __init__(self, name, email, phone, birthday):
        self.name = name
        self.email = email
        self.phone = phone
        self.birthday = birthday

    @classmethod
    def init_from_data(clc, data):
        return clc(data['name'], data['email'], data['phone'], data['birthday'])

    def display(self):
        print(f'name={self.name:20}, email={self.email:30}, phone={self.phone:10}, birthday={self.birthday:10}')


    def covert_to_json(self):
        return {
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "birthday": self.birthday
        }
