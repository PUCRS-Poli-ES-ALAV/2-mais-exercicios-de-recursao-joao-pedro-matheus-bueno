def permutations(s):
    # Se a string tiver comprimento 1 ou 0, só existe uma permutação
    if len(s) <= 1:
        return [s]
    
    # Lista para armazenar todas as permutações
    perm_list = []
    
    # Iterar sobre cada caractere da string
    for i in range(len(s)):
        # Fixamos o caractere na posição i e geramos as permutações dos outros caracteres
        remaining = s[:i] + s[i+1:]  # Substring sem o caractere s[i]
        for perm in permutations(remaining):  # Recursivamente geramos permutações
            perm_list.append(s[i] + perm)  # Adicionamos o caractere s[i] nas permutações geradas
    
    return perm_list

# Testando a função
result = permutations("joaopedrokriger")
print(result)  # Exemplo de saída: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
