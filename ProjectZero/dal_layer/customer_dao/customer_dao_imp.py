from custom_exceptions.id_not_found import IdNotFound
from dal_layer.customer_dao.customer_dao_interface import CustomerDAOInterface
from entities.customer_class_information import Customer


class CustomerDAOImp(CustomerDAOInterface):
    #  customers_list = []
    # id_generator = 2

    def __init__(self):
        customer_needed_for_id_catch = Customer(1, "Julio", "Jacquet")
        self.customers_list = []
        self.id_generator = 2
        self.customers_list.append(customer_needed_for_id_catch)

    # user joins bank with unique customer id
    def create_customer(self, customer: Customer) -> Customer:
        customer.customer_id = self.id_generator
        self.id_generator += 1
        self.customers_list.append(customer)
        return customer

    # user is able to view user information if correct id is entered
    def get_customer_information_by_id(self, customer_id: int) -> Customer:
        for customer in self.customers_list:
            if customer.customer_id == customer_id:
                return customer
            raise IdNotFound("No customer matches the id given: please try again!")

    # user ends relationship with the bank
    def delete_customer_by_id(self, customer_id: int) -> bool:
        for customer in self.customers_list:
            if customer.customer_id == customer_id:
                self.customers_list.remove(customer)
                return True
            raise IdNotFound("No customer matches the id given: please try again!")

    def update_customer_by_id(self, customer: Customer) -> Customer:
            for customer_in_list in self.customers_list:
                if customer.customer_id == customer_in_list.customer_id:
                    customer_in_list = customer
                    return customer_in_list
            raise IdNotFound("No customer matches the id given: please try again!")
