from datetime import datetime

from app.mailing_service import MailingService
from models.mailing import MailingEntity


class TestMailingService:
    def test_add_new_mailing1(self):
        api = MailingService()
        api.add_new_mailing(mailing_id=0, start_datetime=datetime.now().strftime("%Y-%m -%d"),
                            finish_datetime=datetime.now().strftime("%Y-%m -%d"),
                            message_text='test message',
                            client_filter={'tag': 'new_customer'})

        assert len(api.mailings) == 1
        assert isinstance(api.mailings[0], MailingEntity)
        assert api.mailings[0].mailing_id == 0
        assert api.mailings[0].start_datetime == datetime.now().strftime("%Y-%m -%d")
        assert api.mailings[0].finish_datetime == datetime.now().strftime("%Y-%m -%d")
        assert api.mailings[0].message_text == 'test message'
        assert api.mailings[0].client_filter == {'tag': 'new_customer'}