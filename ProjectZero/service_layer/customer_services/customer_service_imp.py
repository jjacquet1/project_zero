from custom_exceptions.bad_customer_info import BadCustomerInfo
from dal_layer.customer_dao.customer_dao_interface import CustomerDAOInterface
from entities.customer_class_information import Customer
from service_layer.customer_services.customer_service_interface import CustomerServiceInterface


class CustomerServiceImp(CustomerServiceInterface):

    def __init__(self, customer_dao: CustomerDAOInterface):
        self.customer_dao = customer_dao

    # customer is created
    # customer first and last names may not exceed 20 characters
    def service_create_customer(self, customer: Customer) -> Customer:
        if len(customer.customer_first_name) > 20:
            raise BadCustomerInfo("First name is too long")
        elif len(customer.customer_last_name) > 20:
            raise BadCustomerInfo("Last name is too long")
        for existing_customer in self.customer_dao.customers_list:
            if existing_customer.customer_id == customer.customer_id:
                raise BadCustomerInfo("This customer id already exists")
        return self.customer_dao.create_customer(customer)

    def service_get_customer_by_id(self, customer_id: int) -> Customer:
        if type(customer_id) == int:
            return self.customer_dao.get_customer_information_by_id(customer_id)
        else:
            raise BadCustomerInfo("Please enter a valid customer id")

    def service_update_customer_by_id(self, customer: Customer) -> Customer:
        if type(customer.customer_first_name) != str:
            raise BadCustomerInfo("please enter a valid first name")
        elif type(customer.customer_last_name) != str:
            raise BadCustomerInfo("please enter a valid last name")
        for existing_customer in self.customer_dao.customers_list:
            if existing_customer.customer_id == customer.customer_id:
                raise BadCustomerInfo("This customer id already exists")
        return self.customer_dao.update_customer_by_id(customer)

    def service_delete_customer_by_id(self, customer_id: int) -> bool:
        pass

    def service_get_customer_information_by_id(self, customer_id: int) -> Customer:
        if type(customer_id) == int:
            return self.customer_dao.get_customer_information_by_id(customer_id)
        else:
            raise BadCustomerInfo("Please enter a valid customer id")
