from app import adicionar_tarefa, listar_tarefas



while True:
    print("==== MENU ===")
    print("1 Adicionar tarefas")
    print("2 Listar tarefas")
    print("3 Sair")
    
    opcao = input("Selecione uma opcao:")
    
    if opcao == "1":
        print("=== Adicionar uma nova tarefa ====")
        titulo = input("Titulo da tarefa:")
        descricao = input("Descricao da tarefa:")
        
        adicionar_tarefa(titulo, descricao)
        
    elif opcao == "2":
        listar_tarefas()
        
    elif opcao == "3":
        print('Encerrando o sistema...')
        break
    
    else:
        print("Opcao invalida.")