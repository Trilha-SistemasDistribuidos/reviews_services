import requests
from django.conf import settings

def get_users(user_id):
    try:
        headers = {
            'Authorization': f'Bearer {settings.USERS_SERVICE_TOKEN}'
        }
        response = requests.get(
            f"{settings.USERS_SERVICE_URL}/api/usuario/{user_id}/",  # Singular
            headers=headers  # <-- Adicione os headers
        )
        if response.status_code == 401:
            raise Exception("Token de serviço inválido")
        return response.json() if response.status_code == 200 else None
    except requests.exceptions.RequestException:
        return None