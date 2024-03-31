from datetime import datetime
from typing import List, Optional, Dict

from models.mailing import MailingEntity
from utils.utils import validate_phone_number


class MailingService:
    mailings: List[MailingEntity] = []

    def get_mailing(self, mailing_id: int) -> Optional[MailingEntity]:
        for c in self.mailings:
            if c.mailing_id == mailing_id:
                return c
        return None

    def add_new_mailing(self, mailing_id: int,
                        start_datetime: datetime,
                        finish_datetime: datetime,
                        message_text: str,
                        client_filter: Dict[str, any]):
        new_mailing = MailingEntity(mailing_id, start_datetime,
                                    finish_datetime, message_text,
                                    client_filter)
        self.mailings.append(new_mailing)

    # def update_mailing(self, mailing_id: int, phone_number: str,
    #              code_operator: str,
    #              tag: str):
    def update_mailing(self, mailing_id: int, **kwargs):
        mailing = self.get_mailing(mailing_id)
        if mailing:
            for key, value in kwargs.items():
                setattr(self.mailings[mailing_id], key, value)
        return None

    def delete_mailing(self, mailing_id: int):
        mailing = self.get_mailing(mailing_id)
        if mailing:
            self.mailings.remove(mailing)
            return True
        return False
