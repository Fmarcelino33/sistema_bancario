# 👋 Simulador Sistema Bancário

## 🚀 Sistema desenvolvido em linguagem Python

O intuíto do projeto era desenvolver um simulador de sistema bancário a partir do código base desenvolvido pelo professor do curso @decarvalhogui.

---

## 🛠️ Comandos Usados (Hard Skills)

- **Raciocínio do código**:

| **Comando**                          | **Descrição**                                                                                   |
|--------------------------------------|-----------------------------------------------------------------------------------------------|
| **menu = """..."""**                 | Define uma string multilinha que representa o menu de opções para o usuário.                   |
| **saldo = 1000**                     | Inicializa a variável `saldo` com o valor de 1000, representando o saldo inicial.             |
| **limite = 1000**                    | Define o limite máximo de saque por operação.                                                 |
| **extrato = ""**                     | Inicializa a variável `extrato` como uma string vazia para armazenar o histórico de transações.|
| **numero_saques = 0**                | Inicializa a variável `numero_saques` com 0, para contar o número de saques realizados.       |
| **LIMITE_SAQUES = 3**                | Define o limite máximo de saques que podem ser realizados.                                    |
| **while True:**                      | Inicia um loop infinito que continuamente exibe o menu e espera pela entrada do usuário.      |
| **opcao = input(menu)**              | Solicita ao usuário que escolha uma opção do menu e armazena a escolha na variável `opcao`.   |
| **if opcao == "d":**                 | Verifica se o usuário escolheu a opção de depósito.                                           |
| **elif opcao == "s":**               | Verifica se o usuário escolheu a opção de saque.                                              |
| **elif opcao == "e":**               | Verifica se o usuário escolheu a opção de extrato.                                            |
| **elif opcao == "q":**               | Verifica se o usuário escolheu a opção de sair.                                               |
| **valor = float(input(...))**        | Solicita ao usuário que insira o valor do depósito ou saque e converte para float.            |
| **if valor > 0:**                    | Verifica se o valor do depósito ou saque é positivo.                                          |
| **saldo += valor**                   | Adiciona o valor do depósito ao saldo atual.                                                  |
| **extrato += f"...\n"**              | Registra a transação (depósito ou saque) no extrato.                                          |
| **print(f"...")**                    | Exibe mensagens de sucesso ou erro para o usuário.                                            |
| **excedeu_saldo = ...**              | Verifica se o valor do saque excede o saldo disponível.                                       |
| **excedeu_limite = ...**             | Verifica se o valor do saque excede o limite permitido.                                       |
| **excedeu_saques = ...**             | Verifica se o número de saques excede o limite permitido.                                     |
| **saldo -= valor**                   | Subtrai o valor do saque do saldo atual.                                                      |
| **numero_saques += 1**               | Incrementa o contador de saques realizados.                                                   |
| **print("Não foram realizadas movimentações." if not extrato else extrato)** | Exibe o extrato ou uma mensagem indicando que não houve movimentações. |
| **break**                            | Sai do loop infinito e encerra o programa.                                                    |
| **else:**                            | Executa caso o usuário insira uma opção inválida.                                             |
| **print("Operação inválida...")**    | Exibe uma mensagem de erro para opções inválidas.                                             |
---    
- **Linguagem usada**:
  - **Python Básico** 🐍
---    
- **Comandos Usados**

| **Comando**               | **Descrição**                                                                 |
|---------------------------|-------------------------------------------------------------------------------|
| **menu = """..."""**      | Define uma string multilinha que representa o menu de opções para o usuário.   |
| **while True:**           | Inicia um loop infinito que continuamente exibe o menu e espera pela entrada do usuário. |
| **opcao = input(menu)**   | Solicita ao usuário que escolha uma opção do menu e armazena a escolha na variável `opcao`. |
| **valor = float(input(...))** | Solicita ao usuário que insira um valor numérico e converte para o tipo `float`. |
| **if**                   | Verifica uma condição. Se for verdadeira, executa o bloco de código associado. |
| **elif**                 | Verifica uma condição adicional caso a condição do `if` anterior seja falsa.   |
| **else:**                | Executa um bloco de código caso todas as condições anteriores (`if` e `elif`) sejam falsas. |
| **break**                | Sai imediatamente de um loop (como `while` ou `for`).                          |
| **print**                | Exibe uma mensagem ou valor no console.                                        |

---

## 🎯 Objetivos

Fixar a usabilidade e raciocínio dos comandos ensinados na aula.
---

## 📫 Mais sobre mim?

- **LinkedIn**: (https://www.linkedin.com/in/fmarcelino)
- **Email**: fmarcelino26@gmail.com

---

**Obrigado por visitar meu perfil!** 😊
