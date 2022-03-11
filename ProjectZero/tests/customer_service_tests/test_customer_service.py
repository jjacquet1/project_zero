from custom_exceptions.bad_customer_info import BadCustomerInfo
from dal_layer.customer_dao.customer_dao_imp import CustomerDAOImp
from entities.customer_class_information import Customer
from service_layer.customer_services.customer_service_imp import CustomerServiceImp

customer_dao = CustomerDAOImp()
customer_service = CustomerServiceImp(customer_dao)
duplicate_customer_id = Customer(0, "first name is fine", "last name is fine")
non_string_first_name = Customer(0, 12, "last name is fine")
non_string_last_name = Customer(0, "first name is fine", 13)
duplicate_customer_id_update = Customer(1, "first name is fine", "last name is fine")
non_string_first_name_update = Customer(1, 12, "last name is fine")
non_string_last_name_update = Customer(1, "first name is fine", 13)
limit_length_first_name = Customer(1, "123456789012345678901", "last name is fine")
limit_length_last_name = Customer(1, "first name is fine", "123456789012345678901")


def test_check_no_duplicate_id_create_customer():
    result = customer_dao.create_customer(duplicate_customer_id)
    assert result.customer_id != 1


def test_check_length_first_name_create_customer():
    result = customer_dao.create_customer(limit_length_first_name)
    assert result.customer_id != "1"


def test_check_length_last_name_create_customer():
    result = customer_dao.create_customer(limit_length_last_name)
    assert result.customer_id != 1


def test_catch_non_string_first_name_create_customer():
    result = customer_dao.create_customer(non_string_first_name)
    assert result.customer_id != "1"


def test_catch_non_string_last_name_create_customer():
    result = customer_dao.create_customer(non_string_last_name)
    assert result.customer_id != "1"


def test_catch_non_numeric_id():
    try:
        customer_service.service_get_customer_by_id("one")
        assert False
    except BadCustomerInfo as e:
        assert str(e) == "Please enter a valid customer id"


"""
update customer test
"""


def test_check_no_duplicate_id_update_customer():
    try:
        customer_service.service_create_customer(duplicate_customer_id_update)
        assert False
    except BadCustomerInfo as e:
        assert str(e) == "This id already exists in the database"


def test_catch_non_string_first_name_update_customer():
    try:
        customer_service.service_create_customer(non_string_first_name_update)
        assert False
    except BadCustomerInfo as e:
        assert str(e) == "Please enter a valid first name"


def test_catch_non_string_last_name_update_customer():
    try:
        customer_service.service_create_customer(non_string_last_name_update)
        assert False
    except BadCustomerInfo as e:
        assert str(e) == "Please enter a valid last name"


"""
delete customer test
"""


def test_catch_non_numeric_id_delete_customer():
    try:
        customer_service.service_delete_customer_by_id("one")
        assert False
    except BadCustomerInfo as e:
        assert str(e) == "Please enter a valid customer id"
