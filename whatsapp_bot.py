from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

def enviar_mensagem(contato, mensagem, primeira_vez):
    tempo_espera = 40 if primeira_vez == "sim" else 10 # <---- editar aqui caso necessário

    options = Options()
    options.add_argument(r"--user-data-dir=C:\CAMINHO\DO\SEU\PERFIL") # <----- editar aqui
    nav = webdriver.Chrome(options=options)
    nav.get("https://web.whatsapp.com")
    time.sleep(tempo_espera)

    try:
        barra_pesquisa = nav.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div/div/div/p')
        barra_pesquisa.click()
        barra_pesquisa.send_keys(contato + Keys.ENTER)
        time.sleep(2)

        campo_mensagem = nav.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div[1]/p')
        campo_mensagem.click()
        campo_mensagem.send_keys(mensagem + Keys.ENTER)
        time.sleep(4)

        print("✅ Mensagem enviada com sucesso!")

    except Exception as e:
        print(f"❌ Erro: {e}")

    finally:
        nav.quit()

if __name__ == "__main__":
    contato = input("Nome do contato: ")
    mensagem = input("Sua mensagem: ")
    primeira_vez = input("Primeira vez usando? (sim/nao): ").strip().lower()

    enviar_mensagem(contato, mensagem, primeira_vez)
