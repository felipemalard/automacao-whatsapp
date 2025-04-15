```markdown
# 🤖 Automação de WhatsApp com Python + Selenium

Este projeto envia mensagens automáticas no WhatsApp Web usando Python.

---

## 🚀 Como usar

1. Instale as dependências:

```bash
pip install -r requisitos.txt
```

2. Edite o caminho do perfil do Chrome dentro do código:

```python
options.add_argument(r"--user-data-dir=C:\CAMINHO\DO\SEU\PERFIL")
```

3. Edite o tempo de execução caso necessário:
    tempo_espera = 40 if primeira_vez == "sim" else 10 
    -> O primeiro número (no caso o 40) determina o tempo em segundos para a execução do comando se o usuário marcar "nao" como opção
        - Esse tempo deve ser maior que o segundo, porque é necessário ter o tempo para o usuário escanear o Qr Code
        - Ajuste para o seu caso e a velocidade da sua internet
    -> O segundo número (10) determina o tempo em segundos para a execução do comando se o usuário marcar "sim" como opção
        - Nessa caso o usuário já executou o código pela primeira vez e já está logado no whatsapp web
        - Dessa forma pode ser um tempo mais curto.
        - Ajuste para o seu caso e a velocidade da sua internet
   observação: caso o tempo esteja incorreto o código apresentará erros e dessa forma mostrará ao usuário a necessidade de ajustar
   
4. Execute o script:

```bash
python whatsapp_bot.py
```

Siga as instruções no terminal para enviar a mensagem.

---

## ⚠️ Aviso

Este projeto é para fins **educacionais**. Evite usar para spam ou envios em massa sem consentimento.
```

---

Se quiser, também posso te ajudar a:

✅ Modificar esse código para a sua necessidade
✅ Criar outras automações para sua empresa
