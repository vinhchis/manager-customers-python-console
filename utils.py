from customer import Customer
def get_input(mess):
    while True:
        try:
            user_input = input(mess)

            if not user_input.strip():
                raise ValueError("Input cannot be blank")

            return user_input

        except ValueError as e:
            print(e)


def inputCustomer():
    print('\tGet Customer Information')
    name = get_input('Enter your name: ')
    email = get_input('Enter your email: ')
    phone = get_input('Enter your phone: ')
    birthday = get_input('Enter your birthday: ')

    customer = Customer(name, email, phone, birthday)
    return customer