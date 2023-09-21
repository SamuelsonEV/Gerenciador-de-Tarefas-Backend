import requests

api_url = 'http://localhost:5000'

nomes_de_tarefas = [
    "Task 1",
    "Task 2",
    "Task 3",
]

for titulo_tarefa in nomes_de_tarefas:

    payload = {'titulo': titulo_tarefa}
    response = requests.post(f"{api_url}/tarefa", data=payload)



    if response.status_code == 200:
        print("Tarefa adicionada com sucesso")
    elif response.status_code == 409:
        print("Tarefa com mesmo título já existe !!!")
    else:
        print(f"Erro {response.status_code}: {response.text}")

print("Inserção de dados iniciais finalizada")

