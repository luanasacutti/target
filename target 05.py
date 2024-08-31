def inverter_string(s):
    # Inicialize uma string vazia para o resultado
    resultado = ''

    # Percorra a string original do final para o início
    for i in range(len(s) - 1, -1, -1):
        resultado += s[i]  # Adicione o caractere ao resultado

    return resultado


# Exemplo de uso com entrada definida
entrada = "Exemplo de string"
resultado = inverter_string(entrada)
print("String invertida:", resultado)

# Exemplo de uso com entrada do usuário
entrada_usuario = input("Digite a string que deseja inverter: ")
resultado_usuario = inverter_string(entrada_usuario)
print("String invertida:", resultado_usuario)
