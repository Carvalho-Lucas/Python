print("===== QUIZ PYTHONZUDO =====")
pontos = 0

resposta1 = input("1) Qual o comando usado para exibir algo na tela? ").lower()
if resposta1 == "print":
    print("✅ Correto!")
    pontos += 1
else:
    print("❌ Errado! Resposta certa: print")

resposta2 = input("2) Qual estrutura usamos para repetir um bloco de código? ").lower()
if resposta2 in ["for", "while"]:
    print("✅ Boa!")
    pontos += 1
else:
    print("❌ Oops! Esperado: for ou while")

resposta3 = input("3) Em Python, listas começam com índice em qual número? ")
if resposta3 == "0":
    print("✅ Isso aí, começa no zero!")
    pontos += 1
else:
    print("❌ Errou! O certo é 0")

print("\n===== RESULTADO FINAL =====")
print(f"Você fez {pontos} de 3 pontos.")
