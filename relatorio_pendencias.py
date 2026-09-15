import pandas as pd

# Cria o DataFrame com os funcionários
df = pd.DataFrame({
    "Nome": ["André Coutinho", "Mariana Silva", "Carlos Oliveira"],
    "CPF": ["111.111.111-11", "222.222.222-22", "333.333.333-33"],
    "Status": ["Regular", "Pendente", "Regular"]
})

# Filtra apenas os funcionários pendentes
pendencias = df[df["Status"] == "Pendente"]

# Salva o relatório em Excel
pendencias.to_excel("relatorio_pendencias.xlsx", index=False)

print("Relatório de pendências criado com sucesso!")
print(pendencias)
