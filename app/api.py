from typing import List, Optional

from models.client import ClientEntity
from utils.utils import validate_phone_number


class Api:
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

    def update_client(self, client_id: int, phone_number: str,
                 code_operator: str,
                 tag: str):
        client = self.get_client(client_id)

        if client:
            if phone_number:
                if validate_phone_number(phone_number):
                    self.clients[client_id].phone_number = phone_number
            if code_operator:
                self.clients[client_id].code_operator = code_operator
            if tag:
                self.clients[client_id].tag = tag
            return self.clients[client_id]
        return None
