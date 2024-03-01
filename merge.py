import pandas as pd

# Carregar os arquivos CSV
df1 = pd.read_csv("MemberStatusDB-PRD.MemberWithIndex_01.csv")
df2 = pd.read_csv("MemberStatusDB-PRD.Member_02.csv")

# Contar linhas nos DataFrames originais
count_df1 = len(df1)
count_df2 = len(df2)
print(f"Linhas no Arquivo 1: {count_df1}")
print(f"Linhas no Arquivo 2: {count_df2}")

# Encontrar CPFs únicos em df1 que não estão em df2
MemberNumber_unicos_df1 = ~df1['MemberNumber'].isin(df2['MemberNumber'])

# Filtrar df1 para manter apenas esses CPFs únicos
df1_unicos = df1[MemberNumber_unicos_df1]

# Concatenar df1 (filtrado) e df2
resultado_final = pd.concat([df1_unicos, df2], ignore_index=True)

# Salvar o resultado em um novo arquivo CSV
resultado_final.to_csv("arquivo_merge.csv", index=False)

# Contar linhas no DataFrame resultante
count_resultado_final = len(resultado_final)
print(f"Linhas no Arquivo Mergeado: {count_resultado_final}")