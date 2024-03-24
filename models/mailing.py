from datetime import datetime
from typing import Dict


class MailingEntity:
    def __init__(self, mailing_id: int,
                 start_datetime: datetime,
                 finish_datetime: datetime,
                 message_text: str,
                 client_filter: Dict[str, any]):
        self.mailing_id = mailing_id
        self.start_datetime = start_datetime
        self.finish_datetime = finish_datetime
        self.message_text = message_text
        self.client_filter = client_filter
