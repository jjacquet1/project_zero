from abc import ABC

from custom_exceptions.id_not_found import IdNotFound
from dal_layer.account_dao.account_dao_interface import AccountDAOInterface
from entities.account_class_information import Account


class AccountDAOImp(AccountDAOInterface, ABC):
    account_list = [Account(1, 1, "Jay", "Bee", 22)]
    id_generator = 2

    def __init__(self):
        self.account_balance = 0

    # user can create a new bank account
    def create_account(self, account: Account) -> Account:
        account.account_id = self.id_generator
        self.id_generator += 1
        self.account_list.append(account)
        return account

    # user can view the balance of a specific account
    # if user enters an incorrect account id, exception is raised and user receives message.
    def get_account_by_id(self, account_id: int) -> Account:
        for account in self.account_list:
            if account.account_id == account_id:
                return account
        raise IdNotFound("No account matches the id given: please try again!")

    # user can close any of my bank accounts
    def delete_account_by_id(self, account_id: int) -> bool:
        for account in self.account_list:
            if account.account_id == account_id:
                self.account_list.remove(account)
                return True
        raise IdNotFound("No account matches the id given: please try again!")

    def update_account_by_id(self, account: Account) -> Account:
        for old_account in self.account_list:
            if old_account.account_id == account.account_id:
                old_account = account
                return old_account
        raise IdNotFound("No account matches the id given: please try again!")

    # user can make a deposit to a specific account
    def deposit_into_account_by_id(self, account_id: int) -> int:
        for account in self.account_list:
            if account.account_id == account_id:
                amount = int(input("Enter amount to be deposited: "))
                self.account_balance += amount
                return amount

    # user can withdraw a specific account
    def withdraw_from_account_by_id(self, account_id: int) -> int:
        for account in self.account_list:
            if account.account_id == account_id:
                amount = int(input("Enter withdrawal amount: "))
                self.account_balance -= amount
                return amount
