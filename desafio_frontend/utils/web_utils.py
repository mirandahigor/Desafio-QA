from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from faker import Faker
import os, time

fake = Faker()

# ---------------- Navegador ----------------
def iniciar_navegador():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    return driver

# ---------------- Practice Form ----------------
def preencher_formulario(driver):
    driver.find_element(By.ID, "firstName").send_keys(fake.first_name())
    driver.find_element(By.ID, "lastName").send_keys(fake.last_name())
    driver.find_element(By.ID, "userEmail").send_keys(fake.email())
    driver.find_element(By.XPATH, "//label[@for='gender-radio-1']").click()
    driver.find_element(By.ID, "userNumber").send_keys(str(fake.random_number(digits=10)))
    driver.find_element(By.ID, "subjectsInput").send_keys("Maths")
    driver.find_element(By.XPATH, "//label[@for='hobbies-checkbox-1']").click()
    driver.find_element(By.ID, "currentAddress").send_keys(fake.address())

def fazer_upload(driver):
    file_path = os.path.join(os.getcwd(), "files", "upload.txt")
    driver.find_element(By.ID, "uploadPicture").send_keys(file_path)

def submeter_formulario(driver):
    driver.find_element(By.ID, "submit").click()

def verificar_popup(driver):
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "example-modal-sizes-title-lg"))
    )

def fechar_popup(driver):
    driver.find_element(By.ID, "closeLargeModal").click()

# ---------------- Browser Windows ----------------
def abrir_nova_janela(driver):
    driver.find_element(By.ID, "windowButton").click()
    time.sleep(2)
    windows = driver.window_handles
    driver.switch_to.window(windows[1])
    return driver

def validar_mensagem_nova_janela(driver, msg):
    texto = driver.find_element(By.TAG_NAME, "h1").text
    assert msg in texto

def fechar_janela(driver):
    driver.close()
    windows = driver.window_handles
    driver.switch_to.window(windows[0])

# ---------------- Web Tables ----------------
def criar_registro(driver):
    driver.find_element(By.ID, "addNewRecordButton").click()
    driver.find_element(By.ID, "firstName").send_keys(fake.first_name())
    driver.find_element(By.ID, "lastName").send_keys(fake.last_name())
    driver.find_element(By.ID, "userEmail").send_keys(fake.email())
    driver.find_element(By.ID, "age").send_keys(str(fake.random_int(min=18, max=80)))
    driver.find_element(By.ID, "salary").send_keys(str(fake.random_int(min=1000, max=10000)))
    driver.find_element(By.ID, "department").send_keys("QA")
    driver.find_element(By.ID, "submit").click()

def editar_registro(driver):
    driver.find_element(By.XPATH, "//span[@title='Edit']").click()
    driver.find_element(By.ID, "salary").clear()
    driver.find_element(By.ID, "salary").send_keys("9999")
    driver.find_element(By.ID, "submit").click()

def deletar_registro(driver):
    driver.find_element(By.XPATH, "//span[@title='Delete']").click()

# ---------------- Progress Bar ----------------
def start_progress(driver):
    driver.find_element(By.ID, "startStopButton").click()

def parar_ate_25(driver):
    barra = driver.find_element(By.CLASS_NAME, "progress-bar")
    while int(barra.get_attribute("aria-valuenow")) < 25:
        time.sleep(0.05)
    driver.find_element(By.ID, "startStopButton").click()

def validar_valor(driver, max_val):
    barra = driver.find_element(By.CLASS_NAME, "progress-bar")
    assert int(barra.get_attribute("aria-valuenow")) <= max_val

def completar_e_reset(driver):
    driver.find_element(By.ID, "startStopButton").click()
    barra = driver.find_element(By.CLASS_NAME, "progress-bar")
    while int(barra.get_attribute("aria-valuenow")) < 100:
        time.sleep(0.05)
    driver.find_element(By.ID, "resetButton").click()

# ---------------- Sortable ----------------
def ordenar_sortable(driver):
    items = driver.find_elements(By.CSS_SELECTOR, "#demo-tabpane-list .list-group-item")
    items_text = [i.text for i in items]
    sorted_text = sorted(items_text)
    action = ActionChains(driver)
    for i, val in enumerate(sorted_text):
        target = items[i]
        source = driver.find_element(By.XPATH, f"//div[text()='{val}']")
        action.drag_and_drop(source, target).perform()
        time.sleep(0.2)
