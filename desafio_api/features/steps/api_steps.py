from behave import given, when, then
from utils.api_client import ApiClient

api = ApiClient()

@given('que eu criei um usuário com username "{username}" e senha "{password}"')
def step_impl(context, username, password):
    context.username = username
    context.password = password
    context.user_id = api.create_user(username, password)

@when("eu gero o token de acesso")
def step_impl(context):
    context.token = api.generate_token(context.username, context.password)

@then("o usuário deve estar autorizado")
def step_impl(context):
    result = api.is_authorized(context.username, context.password)
    assert result is True

@then("eu listo os livros disponíveis")
def step_impl(context):
    context.books = api.get_books()
    assert len(context.books) > 0

@when("eu alugo dois livros de minha escolha")
def step_impl(context):
    chosen_books = [context.books[0]["isbn"], context.books[1]["isbn"]]
    api.add_books(context.user_id, context.token, chosen_books)
    context.chosen_books = chosen_books

@then("os livros alugados devem aparecer nos detalhes do usuário")
def step_impl(context):
    user_data = api.get_user(context.user_id, context.token)
    rented_books = [book["isbn"] for book in user_data["books"]]
    for isbn in context.chosen_books:
        assert isbn in rented_books
