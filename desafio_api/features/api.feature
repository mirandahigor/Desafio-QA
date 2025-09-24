Feature: Desafio API
  Para validar o fluxo da API DemoQA
  Como um testador
  Eu quero criar usuário, gerar token, autorizar, listar e alugar livros

  Scenario: Criar usuário, alugar livros e verificar detalhes
    Given que eu criei um usuário com username "teste_python123" e senha "SenhaForte123!"
    When eu gero o token de acesso
    Then o usuário deve estar autorizado
    And eu listo os livros disponíveis
    When eu alugo dois livros de minha escolha
    Then os livros alugados devem aparecer nos detalhes do usuário
