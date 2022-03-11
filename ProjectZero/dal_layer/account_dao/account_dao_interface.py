from abc import ABC, abstractmethod

from entities.account_class_information import Account


class AccountDAOInterface(ABC):

    @abstractmethod
    def create_account(self, account: Account) -> Account:
        pass

    @abstractmethod
    def get_account_by_id(self, account_id: int) -> Account:
        pass

    @abstractmethod
    def update_account_by_id(self, account: Account) -> Account:
        pass

    @abstractmethod
    def delete_account_by_id(self, account_id: int) -> bool:
        pass

    @abstractmethod
    def deposit_into_account_by_id(self, account_id: int) -> Account:
        pass

    @abstractmethod
    def withdraw_from_account_by_id(self, account_id: int) -> Account:
        pass
