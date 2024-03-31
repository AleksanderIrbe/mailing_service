from datetime import datetime


class MessageEntity:
    def __init__(self, message_id: int,
                 initial_datetime: datetime,
                 status: bool,
                 mailing_id: int,
                 client_id: int):
        self.message_id = message_id
        self.initial_datetime = initial_datetime
        self.status = status
        self.mailing_id = mailing_id
        self.client_id = client_id
