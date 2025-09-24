import requests

class ApiClient:
    BASE_URL = "https://demoqa.com"

    # Criar usuário
    def create_user(self, username, password):
        url = f"{self.BASE_URL}/Account/v1/User"
        body = {"userName": username, "password": password}
        response = requests.post(url, json=body)
        response.raise_for_status()
        return response.json()["userID"]

    # Gerar token
    def generate_token(self, username, password):
        url = f"{self.BASE_URL}/Account/v1/GenerateToken"
        body = {"userName": username, "password": password}
        response = requests.post(url, json=body)
        response.raise_for_status()
        return response.json()["token"]

    # Confirmar autorização
    def is_authorized(self, username, password):
        url = f"{self.BASE_URL}/Account/v1/Authorized"
        body = {"userName": username, "password": password}
        response = requests.post(url, json=body)
        response.raise_for_status()
        return response.json()

    # Listar livros
    def get_books(self):
        url = f"{self.BASE_URL}/BookStore/v1/Books"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()["books"]

    # Alugar livros
    def add_books(self, user_id, token, book_ids):
        url = f"{self.BASE_URL}/BookStore/v1/Books"
        headers = {"Authorization": f"Bearer {token}"}
        body = {"userId": user_id, "collectionOfIsbns": [{"isbn": b} for b in book_ids]}
        response = requests.post(url, headers=headers, json=body)
        response.raise_for_status()
        return response.json()

    # Detalhes do usuário
    def get_user(self, user_id, token):
        url = f"{self.BASE_URL}/Account/v1/User/{user_id}"
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
