from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.client_service import ClientService

router = APIRouter()


@router.post("/add_new_client/")
async def add_client(client_id, phone_number,
                                  code_operator, tag):
    client = ClientService()
    client.add_new_client(client_id, phone_number,
                                  code_operator, tag)
    print(client.clients, client.clients[0])
    if client.get_client(client_id):
        return JSONResponse(status_code=200,
                            content={"message": f'uppend '
                                                f'client id ={client.get_client(client_id).client_id}'})
    else:
        return JSONResponse(status_code=404, content={"message": "Client not found"})

