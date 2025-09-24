from behave import given, when, then
from utils.web_utils import *
import time
from selenium.webdriver.common.by import By

# ---------------- Acessar site ----------------
@given('que eu acesso o site "{url}"')
def step_impl(context, url):
    context.driver = iniciar_navegador()
    context.driver.get(url)

# ---------------- Practice Form ----------------
@when("escolho a opção Forms")
def step_impl(context):
    context.driver.find_element(By.XPATH, "//h5[text()='Forms']").click()

@when("clico no submenu Practice Form")
def step_impl(context):
    context.driver.find_element(By.XPATH, "//span[text()='Practice Form']").click()

@when("preencho o formulário com valores aleatórios")
def step_impl(context):
    preencher_formulario(context.driver)

@when("faço upload de um arquivo")
def step_impl(context):
    fazer_upload(context.driver)

@when("submeto o formulário")
def step_impl(context):
    submeter_formulario(context.driver)

@then("um popup deve aparecer")
def step_impl(context):
    verificar_popup(context.driver)

@then("fecho o popup")
def step_impl(context):
    fechar_popup(context.driver)
    time.sleep(3)  # espera para ver o popup
    context.driver.quit()

# ---------------- Browser Windows ----------------
@when("escolho a opção Alerts, Frame & Windows")
def step_impl(context):
    context.driver.find_element(By.XPATH, "//h5[text()='Alerts, Frame & Windows']").click()

@when("clico no submenu Browser Windows")
def step_impl(context):
    context.driver.find_element(By.XPATH, "//span[text()='Browser Windows']").click()

@when("clico no botão New Window")
def step_impl(context):
    abrir_nova_janela(context.driver)

@then('uma nova janela deve abrir com a mensagem "{msg}"')
def step_impl(context, msg):
    validar_mensagem_nova_janela(context.driver, msg)

@then("fecho a nova janela")
def step_impl(context):
    fechar_janela(context.driver)
    context.driver.quit()

# ---------------- Web Tables ----------------
@when("escolho a opção Elements")
def step_impl(context):
    context.driver.find_element(By.XPATH, "//h5[text()='Elements']").click()

@when("clico no submenu Web Tables")
def step_impl(context):
    context.driver.find_element(By.XPATH, "//span[text()='Web Tables']").click()

@when("crio um novo registro")
def step_impl(context):
    criar_registro(context.driver)

@when("edito o registro criado")
def step_impl(context):
    editar_registro(context.driver)

@when("deleto o registro criado")
def step_impl(context):
    deletar_registro(context.driver)

@when("crio 12 registros dinamicamente")
def step_impl(context):
    for _ in range(12):
        criar_registro(context.driver)

@when("deleto todos os registros criados")
def step_impl(context):
    rows = context.driver.find_elements(By.XPATH, "//span[@title='Delete']")
    for row in rows:
        row.click()
        time.sleep(0.2)

# ---------------- Progress Bar ----------------
@when("escolho a opção Widgets")
def step_impl(context):
    context.driver.find_element(By.XPATH, "//h5[text()='Widgets']").click()

@when("clico no submenu Progress Bar")
def step_impl(context):
    context.driver.find_element(By.XPATH, "//span[text()='Progress Bar']").click()

@when("clico no botão Start")
def step_impl(context):
    start_progress(context.driver)

@then("paro antes dos 25%")
def step_impl(context):
    parar_ate_25(context.driver)

@then("valido que a progress bar <= 25%")
def step_impl(context):
    validar_valor(context.driver, 25)

@then("clico novamente até 100% e reseto")
def step_impl(context):
    completar_e_reset(context.driver)

# ---------------- Sortable ----------------
@when("escolho a opção Interactions")
def step_impl(context):
    context.driver.find_element(By.XPATH, "//h5[text()='Interactions']").click()

@when("clico no submenu Sortable")
def step_impl(context):
    context.driver.find_element(By.XPATH, "//span[text()='Sortable']").click()

@then("coloco os elementos na ordem crescente")
def step_impl(context):
    ordenar_sortable(context.driver)
    context.driver.quit()
