from custom_exceptions.bad_account_info import BadAccountInfo
from dal_layer.account_dao.player_dao_imp import AccountDAOImp
from entities.account_class_information import Account
from service_layer.account_services.player_service_imp import AccountServiceImp

player_dao = AccountDAOImp()
player_service = AccountServiceImp(player_dao)

"""
Note: this is not an exhaustive lists of tests: just some examples of different types of tests you could write
"""


def test_catch_first_name_too_long_create():
    account = Account(0, 1, "This is too long of a first name", "this is fine", 1000)
    try:
        player_service.service_create_player(account)
        assert False
    except BadAccountInfo as e:
        assert str(e) == "First name is too long"


def test_catch_last_name_too_long_create():
    account = Account(0, 1, "this is fine", "This is too long of a last name", 1000)
    try:
        player_service.service_create_player(account)
        assert False
    except BadAccountInfo as e:
        assert str(e) == "Last name is too long"


def test_non_int_provided_for_id_get_account():
    try:
        player_service.service_get_player_information_by_id("1")
    except BadAccountInfo as e:
        assert str(e) == "Please provide a valid Id"


def test_catch_first_name_too_long_update():
    player = Account(1, 1, "This is too long of a first name", "this is fine", 1000)
    try:
        player_service.service_update_player_information(player)
        assert False
    except BadAccountInfo as e:
        assert str(e) == "First name is too long"


def test_catch_last_name_too_long_update():
    player = Account(0, 1, "this is fine", "This is too long of a last name", 1000)
    try:
        player_service.service_update_player_information(player)
        assert False
    except BadAccountInfo as e:
        assert str(e) == "Last name is too long"


def test_non_int_provided_for_id_delete():
    try:
        player_service.service_delete_player_by_id("1")
    except BadAccountInfo as e:
        assert str(e) == "Please provide a valid Id"
