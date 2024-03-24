from utils.utils import validate_phone_number


class ClientEntity:
    def __init__(self, client_id: int,
                 phone_number: str,
                 code_operator: str,
                 tag: str):
        try:
            validate_phone_number(phone_number)
            self.client_id = client_id
            self.phone_number = phone_number
            self.code_operator = code_operator
            self.tag = tag
        except ValueError as e:
            print(f"Error creating client: {e}")