def exibeMenu():
    from consulta0 import consultas
    from editar import editar2
    from exibe0 import exibindo
    from insere0 import inserindo
    from excluir0 import exclui
    
    print("Bem vindo ao menu do meu banco de dados!")
    print("Digite o que você deseja fazer:")
    print("""
        1 - Exibir
        2 - Inserir
        3 - Editar
        4 - Excluir
        5 - Consulta (Não irá trazer nenhum resultado)
    """)
    opcao = 0
    while opcao <1 or opcao>5:
        opcao = int(input("Digite uma opção: "))
    if opcao == 1:
        exibindo()
        print("\nOperação finalizada")
    if opcao == 2:
        inserindo()
        print("\nOperação finalizada")
    if opcao == 3:
        editar2()
        print("\nOperação finalizada")
    if opcao == 4:
        exclui()
        print("\nOperação finalizada")
    if opcao == 5:
        consultas()
        print("\nOperação finalizada")
        
    
    #consultas()
    #editar2()
    #exclui()
    #exibindo()
    #inserindo()
