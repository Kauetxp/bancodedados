from menuDef import exibeMenu
from time import sleep
x = 0
print("\n=====>>>>> SUPER BANCO DE DADOS 2000 <<<<<=====\n")
sleep(2)
while x == 0:
    exibeMenu()
    sleep(1)
    n = input("\nDeseja realizar outra operação? (s/n)")
    if n.lower() == "n":
        x = 1
    print("...")
    sleep(0.5)
    print("...")
    sleep(0.5)
    print("...")
    sleep(0.5)
print("\nPrograma finalizado, até a próxima!\n")


