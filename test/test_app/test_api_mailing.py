from datetime import datetime

from app.mailing_service import MailingService
from models.mailing import MailingEntity


class TestMailingService:
    def test_add_new_mailing1(self):
        api = MailingService()
        api.add_new_mailing(mailing_id=0, start_datetime=datetime.now(),
                            finish_datetime=datetime.now(),
                            message_text='test message',
                            client_filter={'tag': 'new_customer'})

        assert len(api.mailings) == 1
        assert isinstance(api.mailings[0], MailingEntity)
        assert api.mailings[0].mailing_id == 0
        assert api.mailings[0].start_datetime.strftime("%Y-%m -%d") == datetime.now().strftime("%Y-%m -%d")
        assert api.mailings[0].finish_datetime.strftime("%Y-%m -%d") == datetime.now().strftime("%Y-%m -%d")
        assert api.mailings[0].message_text == 'test message'
        assert api.mailings[0].client_filter == {'tag': 'new_customer'}


    def test_update_mailing1(self):
        api = MailingService()
        api.add_new_mailing(mailing_id=0, start_datetime=datetime.now(),
                            finish_datetime=datetime.now(),
                            message_text='test message',
                            client_filter={'tag': 'new_customer'})
        api.add_new_mailing(mailing_id=1, start_datetime=datetime.now(),
                            finish_datetime=datetime.now(),
                            message_text='test1 message',
                            client_filter={'tag': 'new_customer'})
        api.update_mailing(1, message_text='test update message',
                           client_filter={'tag': 'new_customer'})
        assert len(api.mailings) == 2
        assert isinstance(api.mailings[1], MailingEntity)
        assert api.mailings[1].mailing_id == 1
        assert api.mailings[1].message_text == 'test update message'

    def test_delete_mailing(self):
        api = MailingService()
        api.add_new_mailing(mailing_id=0, start_datetime=datetime.now(),
                            finish_datetime=datetime.now(),
                            message_text='test message',
                            client_filter={'tag': 'new_customer'})
        api.add_new_mailing(mailing_id=1, start_datetime=datetime.now(),
                            finish_datetime=datetime.now(),
                            message_text='test1 message',
                            client_filter={'tag': 'new_customer'})
        assert len(api.mailings) == 2

        api.delete_mailing(1)
        assert len(api.mailings) == 1
        assert api.mailings[0].message_text == 'test message'
