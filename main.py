import os
from openai import OpenAI

# Usa variável de ambiente (seguro)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

print("💰 Assistente Financeiro IA iniciado! Digite 'sair' para encerrar.")

while True:
    pergunta = input("Você: ")

    if pergunta.lower() in ["sair", "exit", "quit"]:
        print("Encerrando...")
        break

    # Simulação simples (exigência do desafio)
    if "juros" in pergunta.lower():
        print("💡 Exemplo: R$1000 a 10% ao ano por 2 anos = R$1210")
        continue

    try:
        resposta = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "Você é um assistente financeiro que explica investimentos, juros e finanças de forma simples para iniciantes."
                },
                {"role": "user", "content": pergunta}
            ]
        )

        print("🤖:", resposta.choices[0].message.content)

    except Exception as e:
        print("Erro ao acessar API:", e)
