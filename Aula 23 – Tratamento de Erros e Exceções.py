try:                                    # OPERACAO
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except(ValueError, TypeError):          # CASO DER ERRO, APARECE ESSA MENSAGEM
    print('Tivemos um problema com o tipo de dados.')
except ZeroDivisionError:
    print('Não é possível dividir por 0')
except Exception as erro:
    print(f"O erro encontrado foi o {erro.__class__}")
else:                                   # CASO DER CERTO, MOSTRA A OPERACAO e NAO MOSTRA O ERRO
    print(f"O resultado é {r}")
finally:                                # CLAUSULA OPICIONAL, SEMPRE VAI APARECER.
    print('Obrigado! Volte sempre =)')