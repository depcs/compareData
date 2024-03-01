from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Aqui você pode adicionar o código para ler os arquivos CSV
        # Carregar os arquivos CSV
        df1 = pd.read_csv(request.files.get('file1'))
        df2 = pd.read_csv(request.files.get('file2'))

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

        return render_template('result.html', count_df1=count_df1, count_df2=count_df2, count_resultado_final=count_resultado_final)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=2020, host='127.0.0.1', debug=True, threaded=True)
