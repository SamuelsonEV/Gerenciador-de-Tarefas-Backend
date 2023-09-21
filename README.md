# API Gerenciador de tarefas

Este é um projeto de MVP (Minimum Viable Product) de uma API Flask para gerenciar tarefas num estilo TODO list (Lista de Afaseres).
Ela permite adicionar, visualizar, remover e modificar tarefas da base de dados. 

O objetivo principal deste gerenciador é fornecer uma ferramenta útil de lembretes.

## Requisitos

* Python 3.* ou docker instalado (opiconalmente docker-compose) 

* Git instalado para clonar o repositório, e após clonar ir ao diretório raiz, pelo terminal.

* Segur os paços listados a seguir

## Como Utilizar

Para utilizar esta API, siga os passos abaixo:
### 1. Executando:
#### Executando com docker-compose
Abrir um terminal diretorio raiz do projeto e executar:
```shell
docker-compose up
```
#### Executando com docker
Abrir um terminal no diretorio raiz do projeto e executar:
```shell
docker run -it -v $PWD:/app -w /app --name api-task-manager --network host --rm python:3.8-slim-buster /app/entrypoint.sh 
```
#### Executando diretamente no interpretador Python local.
Abrir um terminal no diretorio raiz do projeto e executar:
```shell
pip install -r requirements.txt
flask run --host 0.0.0.0 --port 5000
```

### 2. Acesse a [documentação Swagger](http://localhost:5000/openapi/swagger#/) para obter detalhes sobre as rotas e os parâmetros necessários.


### 3. Inserindo dados iniciais
#### Usando Docker (Caso tenha utilizado Docker no passo 1.)
Abrir um terminal no diretorio raiz do projeto e executar:
```shell
docker exec api-task-manager bash -c 'python /app/sample_data.py'
```
#### Usando docker-compose (Caso tenha utilizado Docker no passo 1.)
Abrir um terminal no diretorio raiz do projeto e executar:
```shell
docker-compose exec api-task-manager bash -c 'python /app/sample_data.py'
```
#### Diretamente no interpretador Python local.
Abrir um terminal no diretorio raiz do projeto e executar:
```shell
python ./sample_data.py
```


## Documentação Swagger

Para obter a documentação completa desta API no estilo Swagger, acesse: 
[http://localhost:5000//openapi/swagger#/](http://localhost:5000/openapi/swagger#/)

## Rotas da API

- [POST] `/tarefa`

  Adiciona uma nova tarefa à base de dados.

  - **Entrada**: Um objeto JSON com os dados da tarefa.
  - **Saída**: Uma representação da tarefa cadastrada.

- [GET] `/tarefa`

  Retorna informações de uma tarefa com base no seu título.

- [DELETE] `/tarefa`

  Remove uma tarefa com base no seu título.

- [GET] `/tarefas`

  Retorna uma listagem de todas as tarefas cadastradas.

- [DELETE] `/tarefa_id`

  Remove uma tarefa com base no seu Id.

- [GET] `/tarefa_id`

  Retorna uma tarefa com base no seu Id.

- [GET] `/tarefa_id_concluida`

  Modifica o campo que representa a conclusão de uma tarefa com Id específico.


## Notas de Versão

### Versão 1.0.0 (setembro/2023)

- Implementação inicial da API.
- Funcionalidade de adicionar, visualizar, remover e modificar tarefas.

## Autor

Este projeto foi desenvolvido por Samuelson E. V. e pode ser encontrado no [GitHub](https://github.com/samuelsonev).

## Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo [LICENSE](https://www.mit.edu/~amini/LICENSE.md) para obter detalhes.
