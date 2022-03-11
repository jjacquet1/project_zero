from custom_exceptions.bad_account_info import BadAccountInfo
from entities.account_class_information import Account
from service_layer.account_services.account_service_interface import AccountServiceInterface


class AccountServiceImp(AccountServiceInterface):

    def service_create_account(self, account: Account) -> Account:
        if len(account.first_name) > 20:
            raise BadAccountInfo("First name is too long")
        elif len(account.last_name) > 20:
            raise BadAccountInfo("Last name is too long")
        for p in self.account_dao.account_list:
            if p.team_id == account.team_id and p.jersey_number == account.jersey_number:
                raise BadAccountInfo("Jersey number already taken")
        return self.account_dao.create_account(account)

    def service_get_account_information_by_id(self, account_id: int) -> Account:
        if type(account_id) == int:
            return self.account_dao.get_account_by_id(account_id)
        else:
            raise BadAccountInfo("Please provide a valid Id")

    def service_update_account_information(self, account: Account) -> Account:
        if len(account.first_name) > 20:
            raise BadAccountInfo("First name is too long")
        elif len(account.last_name) > 20:
            raise BadAccountInfo("Last name is too long")
        for p in self.account_dao.account_list:
            if p.customer_id == account.customer_id:
                raise BadAccountInfo("Account number already taken")
        return self.account_dao.update_account_by_id(account)

    def service_delete_account_by_id(self, account_id: int) -> bool:
        if type(account_id) == int:
            return self.account_dao.delete_account_by_id(account_id)
        else:
            raise BadAccountInfo("Please provide a valid Id")