```markdown
# 🤖 Automação de WhatsApp com Python + Selenium

Automatize o envio de mensagens no WhatsApp Web utilizando **Python** e **Selenium**.  
Ideal para interações automatizadas, testes ou como base para bots de atendimento.

## 🛠 Tecnologias Utilizadas

- Python 3.10+
- Selenium WebDriver
- Google Chrome

---

## 📁 Estrutura do Projeto

```
📦 whatsapp-bot
├── 📄 requisitos.txt         # Dependências do projeto
├── 📄 whatsapp_bot.py        # Código principal da automação
└── 📄 README.md              # Documentação
```

---

## 🚀 Como usar

1. **Clone este repositório:**

git clone https://github.com/felipemalard/automacao-whatsapp.git
cd automacao-whatsapp


2. **Instale as dependências:**

pip install -r requisitos.txt


3. **Configure o caminho do seu perfil do Chrome:**

No `whatsapp_bot.py`, edite a linha abaixo com o caminho do seu perfil local:

```python
options.add_argument(r"--user-data-dir=C:\CAMINHO\DO\SEU\PERFIL")
```

> Isso mantém sua sessão salva e evita o escaneamento do QR Code em execuções futuras. 

4. **Ajuste o tempo de espera (se necessário):**

```python
tempo_espera = 40 if primeira_vez == "sim" else 10
```

- `40 segundos`: para escanear o QR Code na **primeira execução**
- `10 segundos`: para execuções futuras (usuário já logado)

> Ajuste de acordo com a velocidade da sua internet e resposta do WhatsApp Web.

5. **Execute o script:**

```bash
python whatsapp_bot.py
```

Siga as instruções no terminal para enviar sua mensagem personalizada.

---

## ⚠️ Aviso Legal

> Este projeto é destinado exclusivamente para fins **educacionais**.  
> O uso indevido para **spam**, **marketing não autorizado** ou **mensagens em massa sem consentimento** é de inteira responsabilidade do usuário.

---

## 💼 Sobre mim

Desenvolvedor Python focado em automações e soluções inteligentes para negócios.  
Buscando oportunidades para aplicar minha paixão por tecnologia e entregar valor através da programação.

📫 Entre em contato:

- LinkedIn: www.linkedin.com/in/felipemalard
- E-mail: felipemalard1@gmail.com

---

## 📝 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

## 💡 Precisa de algo personalizado?

✅ Modifico esse código para sua necessidade  
✅ Crio outras automações para sua empresa ou rotina  
✅ Dou suporte para evolução do projeto
```
