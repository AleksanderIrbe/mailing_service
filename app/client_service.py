from typing import List, Optional

from models.client import ClientEntity
from utils.utils import validate_phone_number


class ClientService:
    clients: List[ClientEntity] = []

    def get_client(self, client_id: int) -> Optional[ClientEntity]:
        for c in self.clients:
            if c.client_id == client_id:
                return c
        return None

    def add_new_client(self, client_id: int,
                       phone_number: str,
                       code_operator: str,
                       tag: str):
        new_client = ClientEntity(client_id, phone_number,
                                  code_operator, tag)
        self.clients.append(new_client)

    # def update_client(self, client_id: int, phone_number: str,
    #              code_operator: str,
    #              tag: str):
    def update_client(self, client_id: int, **kwargs):
        client = self.get_client(client_id)
        if client:
            for key, value in kwargs.items():
                if key == 'phone_number' and not validate_phone_number(value):
                    continue
                setattr(self.clients[client_id], key, value)

        return None

    def delete_client(self, client_id: int):
        client = self.get_client(client_id)
        if client:
            self.clients.remove(client)
            return True
        return False