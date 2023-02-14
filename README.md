## <center>Arquitetura do Projeto</center>
<h3><center> Python + Pytest + Selenium : </center></h3>

---------------------------------------------------
<h3> Características: </h3>

- Linguagem de desenvolvimento - Python

- Versão do Python - 3.10

- Ambiente de desenvolvimento - PyCharm Community

- Orquestrador de testes - PyTest

- Gerenciamento de dependência - PipEnv

- Relatório de testes automatizados - Allure

- Framework interação com interface - Selenium


---------------------------------------------------
<h3> Pré requisitos: </h3>

- Instalar Python:

  https://www.python.org/downloads/

- Instalação do Allure na maquina de teste:

  https://docs.qameta.io/allure/#_installing_a_commandline

- Instalando Gerenciador de Dependencias PipEnv
 
  `pip install --user pipenv`

- Instalando as dependências do projeto:    

    `pipenv install`

    `pip install -r requirements.txt`

- Caso alguma dependencia não seja instalada, instale-a separadamente
  
  `pipenv install nome_dependencia`

- Criando ou atualizando o arquivo requirements
  
  `pipenv lock -r > requirements.txt`


- Instalando depedencia local pyodbc. A depedencia oficial pyodbc não está disponível ainda para a versão 3.10 do Python. 
Enquanto isso, é necessário a instalação da dependencia local:

  `pipenv install pyodbc-4.0.32-cp310-cp310-win_amd64.whl`

<h4>**Obs: Não esqueça de incluir o Allure, Python e Pipenv nas variáveis de ambiente do Windows.**</h4>

---------------------------------------------------
<h3> Execução dos testes: </h3>

- Executa todos os testes:

  `pytest -v -s`

- Executa os testes de uma classe específica:

  `pytest -v -s tests/login-tests/test_login.py::TestLogin`

- Executa os testes de um marcador específico:

  `pytest -v -s -m smoke`

- Executa os testes e gera um relatório basico no diretório desejado:

  `pytest --html=./report/report.html`

- Executa os testes e gera o relatório do Allure no diretório desejado:

  `pytest -v -s --alluredir=./report/allure-results`

- Abre o relatório temporario no browser:
 
  `allure serve ./report/allure-results`

- Gera o relatório no formato .html numa pasta específica:

  `allure generate ./report/allure-results -o ./report/allure-results/html`

<h4>**Obs: Para abrir o relatório em no formato html, é necessário desabilitar uma diretiva de segurança do navegador.
Recomenda-se realizar a configuração em um navegador que não é utilizado no dia a dia de trabalho:** </h4>

Desabilitando configuração de segurança no Firefox
- Abrir Firefox:
- Digitar na url: about:config
- Alterar o valor `security.fileuri.strict_origin_policy` para _falso_.


---------------------------------------------------

<h3>Convenção de escrita </h3>

**Pacotes**

Nome de pacotes são escritos com letra minuscula. Palavras separadas por underscore. 

ex: `allure_reports`

**Classes**

Arquivos da classe são escritos com letra minuscula. Palavras separadas por underscore. ex: page_base
Nome da classe são escritos no padrão CamelCase. 

ex: `PageBase`

**Métodos**

Métodos são escritos com letra minuscula. Palavras separadas por underscore. 

ex: `digitar_usuario()`

**Variáveis**

Variáveis são escritas com letra minuscula, suas palavras separadas por underscore. 

ex: `usuario_valido`

**Constantes**

Contantes são escritas com letra maiúscula, duas palavras separadas por underscore. 

ex: `LOGIN_FIELD`

**Arquivo**

Arquivos são escritos com letra minuscula. Palavras separadas por underscore. 

ex: `dados_cliente_csv.csv`

**Métodos de Testes**

Métodos de testes devem obrigatoriamente possuir o prefixo test_. 

ex: `test_login_incorreto`

**Classes de Testes**

Classes de testes devem obrigatoriamente possuir o prefixo test_. 

ex: `test_login`

