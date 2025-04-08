print("digite sua nota e o número de faltas e eu te direi qual é a sua situação")
nota1 = float(input("digite sua nota"))
nota2 = float(input("digite sua nota"))
media = (nota1 + nota2 + nota3) / 3
if media <7 and media >=0:
    print("você foi reprovado")
elif media >=7 and media <=10:
    print("você foi aprovado")
else:
    print("invalido")