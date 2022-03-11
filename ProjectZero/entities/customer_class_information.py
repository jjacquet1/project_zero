class Customer:

    def __init__(self, customer_id: int, customer_first_name: str, customer_last_name: str):
        self.customer_id = customer_id
        self.customer_first_name = customer_first_name
        self.customer_last_name = customer_last_name


def convert_to_dictionary(self):
    return {
        "customerId": self.customer_id,
        "customerFirstName": self.customer_first_name,
        "customerLastName": self.customer_last_name
    }
