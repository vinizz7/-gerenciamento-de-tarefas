import json
import os

def carregar_estoque():
    with open("tarefas.json", "r") as arquivo:
        return json.load(arquivo)
    
def salvar_estoque():
    with open("tarefas.json", "w") as arquivo:
        json.dump(dados, arquivo, indent=4) # type: ignore
        
        
def carregar_tarefas():
    if not os.path.exists("tarefas.json"):
        return []
    
    with open("tarefas.json", "r", encoding="utf-8") as arquivo:
        try:
            return json.load(arquivo) 
        except json.JSONDecodeError:
            return []
        
def salvar_tarefas(lista_tarefas):
    with open("tarefas.json", "w", encoding="utf-8") as arquivo:
        json.dump(lista_tarefas, arquivo, indent=4, ensure_ascii=False)


def adicionar_tarefa(titulo, descricao):
    tarefas = carregar_tarefas()
    novo_id = len(tarefas) + 1
    
    nova_tarefa = {
        "id": novo_id,
        "titulo": titulo,
        "descricao": descricao,
        "concluida": False
    }       
    
    tarefas.append(nova_tarefa)
    
    salvar_tarefas(tarefas)
    
    print(f"Tarefa {titulo} adicionadada com sucesso")
    
    
def listar_tarefas():
    tarefas = carregar_tarefas()
    if not tarefas:
        print("Nenhuma tarefa foi encontrada")
        
    print("------LISTA DE TAREFAS------")
    for tarefa in tarefas:
        status = "Concluida" if tarefa["concluida"] else "Pendente"
        print(f"""
    ID: {tarefa["id"]} 
    Titulo: {tarefa["titulo"]}
    Descricao: {tarefa["descricao"]}
    Status: {status}
              
              """)