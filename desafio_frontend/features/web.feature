Feature: Automação completa do site DemoQA
  Para validar todos os fluxos do site DemoQA
  Como testador
  Eu quero automatizar formulários, janelas, tabelas, progress bar e sortable

  Scenario: Preencher formulário Practice Form
    Given que eu acesso o site "https://demoqa.com/"
    When escolho a opção Forms
    And clico no submenu Practice Form
    And preencho o formulário com valores aleatórios
    And faço upload de um arquivo
    And submeto o formulário
    Then um popup deve aparecer
    And fecho o popup

  Scenario: Validar nova janela Browser Windows
    Given que eu acesso o site "https://demoqa.com/"
    When escolho a opção Alerts, Frame & Windows
    And clico no submenu Browser Windows
    And clico no botão New Window
    Then uma nova janela deve abrir com a mensagem "This is a sample page"
    And fecho a nova janela

  Scenario: Manipular Web Tables
    Given que eu acesso o site "https://demoqa.com/"
    When escolho a opção Elements
    And clico no submenu Web Tables
    And crio um novo registro
    And edito o registro criado
    And deleto o registro criado
    And crio 12 registros dinamicamente
    And deleto todos os registros criados

  Scenario: Controlar Progress Bar
    Given que eu acesso o site "https://demoqa.com/"
    When escolho a opção Widgets
    And clico no submenu Progress Bar
    And clico no botão Start
    Then paro antes dos 25%
    And valido que a progress bar <= 25%
    And clico novamente até 100% e reseto

  Scenario: Ordenar elementos Sortable
    Given que eu acesso o site "https://demoqa.com/"
    When escolho a opção Interactions
    And clico no submenu Sortable
    Then coloco os elementos na ordem crescente
