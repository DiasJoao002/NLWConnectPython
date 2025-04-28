# 📅 NLW Connect - Projeto de Gerenciamento de Eventos em Flask

🇧🇷 - 👋 Bem-vindo, esse é um projeto backend desenvolvido em Python utilizando o framework Flask. O sistema permite o gerenciamento de eventos, links de eventos e inscritos, oferecendo uma API REST para manipulação desses dados.

🇺🇸 - 👋 Welcome, this is a backend project developed in Python using the Flask framework. The system allows management of events, event links, and subscribers, providing a REST API for data manipulation.


## 🛠️ Tecnologias Utilizadas / Technologies Used
- Python 3
- Flask 3.
- SQLAlchemy 2.0.4
- Greenlet
- Jinja2
- SQLite (via schema.sql)
- pytest (para testes / for testing)
- Outros pacotes auxiliares (click, colorama, etc. / other auxiliary packages)


## 🎯 Funcionalidades / Features

1- Criação, edição e listagem de eventos.  
  Creation, editing, and listing of events.

2- Gerenciamento de links associados aos eventos.  
  Management of links associated with events.

3- Cadastro e gerenciamento de inscritos para os eventos.  
  Registration and management of subscribers for events.

4- API REST para integração com frontends ou outros serviços.  
  REST API for integration with frontends or other services.

5- Validação de dados para criação de eventos e inscritos.  
  Data validation for event and subscriber creation.


## ⚙️ Como Rodar o Projeto / How to Run the Project

Clone o repositório / Clone the repository:

    ```bash
    git clone https://github.com/seu-usuario/nlw_connect_python.git
    cd nlw_connect_python
    cd nlw_connect_python
    ```

Instale as dependências / Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

Execute o projeto / Run the project:

    ```bash
    python run.py
    ```

O servidor estará disponível em `http://localhost:3000`.  
The server will be available at `http://localhost:3000`.


## 📂 Estrutura de Pastas / Folder Structure

```
/src
  /controllers       -> Lógica de controle e rotas da aplicação / Application control logic and routes
  /model             -> Definição das entidades e repositórios para acesso a dados / Definition of entities and repositories for data access
  /main              -> Configuração do servidor e rotas principais / Server configuration and main routes
  /validators        -> Validação dos dados de entrada / Input data validation
/init
  schema.sql         -> Script de criação do banco de dados / Database creation script
run.py              -> Script para iniciar o servidor / Script to start the server
requirements.txt    -> Dependências do projeto / Project dependencies
```


## 🔍 Pré-requisitos / Prerequisites

- Python 3 instalado na sua máquina. (Recomenda-se usar um ambiente virtual)  
  Python 3 installed on your machine. (Virtual environment recommended)

- Banco de dados SQLite (já configurado via schema.sql)  
  SQLite database (already configured via schema.sql)

- Editor de código (VS Code, PyCharm, etc.)  
  Code editor (VS Code, PyCharm, etc.)


## 🛠️ Ferramentas Auxiliares / Auxiliary Tools

- Postman: Para testar requisições e respostas HTTP da API.  
  Postman: To test HTTP requests and responses of the API.
- DBeaver: Para gerenciamento visual do banco de dados SQLite.  
  DBeaver: For visual management of the SQLite database.


## 💡 Lições Aprendidas / Lessons Learned

- Desenvolvimento de API REST com Flask.  
  Development of REST API with Flask.

- Uso de SQLAlchemy para ORM e manipulação de banco de dados.  
  Use of SQLAlchemy for ORM and database manipulation.

- Organização de projeto backend em múltiplas camadas.  
  Organization of backend project in multiple layers.

- Validação e tratamento de dados de entrada.  
  Validation and handling of input data.

- Testes unitários com pytest.  
  Unitary testing with pytest.


## 🤝 Contribuições / Contributions

Contribuições são bem-vindas!    
Abra uma issue ou envie um pull request para melhorias.

Contributions are welcome!
Open an issue or submit a pull request for improvements.


## 📝 Licença / License

Este projeto está licenciado sob a licença MIT.  
Consulte o arquivo LICENSE para mais informações.

This project is licensed under the MIT license.  
See the LICENSE file for more information.
