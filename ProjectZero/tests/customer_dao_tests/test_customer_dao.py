from custom_exceptions.id_not_found import IdNotFound
from dal_layer.customer_dao.customer_dao_imp import CustomerDAOImp
from entities.customer_class_information import Customer

customer_dao = CustomerDAOImp()


def test_create_team_success():
    test_customer = Customer(0, "John", "Doe")
    result = customer_dao.create_customer(test_customer)
    assert result.customer_id != 0


def test_catch_non_unique_id():
    test_customer = Customer(1, "James", "Jones")
    result = customer_dao.create_customer(test_customer)
    assert result.customer_id != 1


# def test_get_customer_info_by_id_success():
# customer_to_get = Customer(0, "this customer is being created for testing", "The test")
# customer_object_for_getting_id = customer_dao.create_customer(customer_to_get)
# result = customer_dao.get_customer_information_by_id(customer_object_for_getting_id.customer_id)
# assert result.customer_id == customer_object_for_getting_id

def test_get_customer_info_by_id_success():
    result = customer_dao.get_customer_information_by_id(1)
    assert result.customer_id == 1


def test_get_customer_using_non_existent_id():
    try:
        customer_dao.get_customer_information_by_id(0)
        assert False
    except IdNotFound as e:
        assert str(e) == "No customer matches the id given: please try again!"


def test_update_customer_by_id_success():
    new_customer_name = Customer(1, "James", "Jones")
    result = customer_dao.update_customer_by_id(new_customer_name)
    assert result.customer_first_name == "James"


def test_update_customer_using_non_existent_id():
    try:
        new_customer_name = Customer(0, "James", "Jones")
        customer_dao.get_customer_information_by_id(new_customer_name)
        assert False
    except IdNotFound as e:
        assert str(e) == "No customer matches the id given: please try again!"


def test_delete_customer_by_id_success():
    result = customer_dao.delete_customer_by_id(1)
    assert result


def test_delete_customer_with_non_existent_id():
    try:
        customer_dao.delete_customer_by_id(0)
        assert False
    except IdNotFound as e:
        assert str(e) == "No customer matches the id given: please try again!"
