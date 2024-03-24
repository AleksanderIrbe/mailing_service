from models.client import ClientEntity
from app.api import Api

class TestNewClient:
    def test_add_new_client1(self):
        api = Api()
        api.add_new_client(client_id=1, phone_number='79123456789',
                           code_operator='123', tag='new_customer')

        assert len(api.clients) == 1
        assert isinstance(api.clients[0], ClientEntity)
        assert api.clients[0].client_id == 1
        assert api.clients[0].phone_number == '79123456789'
        assert api.clients[0].code_operator == '123'
        assert api.clients[0].tag == 'new_customer'

    def test_add_new_client2(self):
        api = Api()
        api.add_new_client(client_id=1, phone_number='7912345',
                           code_operator='123', tag='new_customer')

        assert len(api.clients) == 1
        assert isinstance(api.clients[0], ClientEntity)
        assert api.clients[0].client_id == 1
        assert api.clients[0].phone_number == '7912345'
        assert api.clients[0].code_operator == '123'
        assert api.clients[0].tag == 'new_customer'

    def test_update_client1(self):
        api = Api()
        api.add_new_client(client_id=0, phone_number='79123456789',
                           code_operator='123', tag='new_customer')
        api.add_new_client(client_id=1, phone_number='79123456789',
                           code_operator='123', tag='new_customer')
        api.update_client(1, phone_number='71234567899', code_operator=None,
                          tag=None)
        assert len(api.clients) == 2
        assert isinstance(api.clients[1], ClientEntity)
        assert api.clients[1].client_id == 1
        assert api.clients[1].phone_number == '71234567899'
        assert api.clients[1].code_operator == '123'
        assert api.clients[1].tag == 'new_customer'

