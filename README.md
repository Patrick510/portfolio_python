# Como Executar a Aplicação de Portfólio (Python + Flask)

Este guia detalha o processo para configurar e executar sua aplicação de portfólio desenvolvida com Python e Flask.

---

## Pré-requisitos

Certifique-se de que os seguintes itens estejam instalados no seu ambiente:

1. **Python**:

   - Baixe e instale a versão mais recente do Python 3.x a partir do [site oficial do Python](https://www.python.org/).
   - Durante a instalação, marque a opção para adicionar o Python ao PATH.
   - Após a instalação, verifique a versão do Python e do `pip` com os comandos:
     ```bash
     python --version
     pip --version
     ```

2. **Virtualenv** (opcional, mas recomendado):
   - Instale com o comando:
     ```bash
     pip install virtualenv
     ```

---

## Passo a Passo

1. **Clone o Repositório (opcional)**
   Caso o projeto esteja em um repositório Git, você pode cloná-lo com o comando:

   ```bash
   git clone <URL_DO_REPOSITORIO>
   ```

   Navegue até o diretório do projeto:

   ```bash
   cd <NOME_DO_DIRETORIO>
   ```

2. **Crie e Ative um Ambiente Virtual (opcional, mas recomendado)**
   Crie um ambiente virtual para isolar as dependências do projeto:

   ```bash
   python -m venv venv
   ```

   Ative o ambiente virtual:

   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

3. **Instale as Dependências**
   Certifique-se de que o arquivo `requirements.txt` está presente no diretório raiz do projeto e execute:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configuração de Ambiente**
   Verifique se há um arquivo `.env.example` no projeto. Caso exista:

   - Renomeie para `.env`:
     ```bash
     cp .env.example .env
     ```
   - Ajuste as variáveis de ambiente conforme necessário.

5. **Inicie o Servidor de Desenvolvimento**
   Execute o seguinte comando para iniciar o servidor Flask:

   ```bash
   python app.py
   ```

   > Substitua `app.py` pelo nome do arquivo principal da aplicação, se for diferente.

6. **Acesse a Aplicação**
   O terminal exibirá um endereço local, como:
   ```
   * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
   ```
   Abra este endereço em seu navegador para acessar a aplicação.

---

## Solução de Problemas

- **Erro "ModuleNotFoundError":**

  - Certifique-se de que todas as dependências foram instaladas corretamente com `pip install -r requirements.txt`.

- **Erro "python: command not found":**

  - Verifique se o Python está instalado e corretamente adicionado ao PATH do sistema.

- **Problemas ao ativar o ambiente virtual:**

  - No Windows, certifique-se de que a execução de scripts está habilitada. Execute o seguinte comando no PowerShell como administrador:
    ```bash
    Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
    ```

- **Porta em uso:**
  - Caso a porta 5000 esteja em uso, você pode especificar outra porta ao iniciar a aplicação:
    ```bash
    python app.py --port=5001
    ```

---

Agora sua aplicação está configurada e pronta para uso!
