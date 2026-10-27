import sqlite3
import pandas as pd
import streamlit as st

# Configuração da Página
st.set_page_config(
    page_title="Mini Pipeline ETL/ELT", page_icon="📊", layout="wide"
)

st.title("📊 Mini Pipeline de Dados: ETL vs ELT")
st.write(
    "Faça o upload de um arquivo, escolha a estratégia de engenharia e visualize os resultados instantaneamente."
)

# 1. Upload do Arquivo Bruto (Ingestão)
uploaded_file = st.file_uploader(
    "Envie seu arquivo de dados (CSV ou Excel)", type=["csv", "xlsx"]
)

if uploaded_file is not None:
  # Leitura do arquivo bruto
  if uploaded_file.name.endswith(".csv"):
    df_raw = pd.read_csv(uploaded_file)
  else:
    df_raw = pd.read_excel(uploaded_file)

  st.subheader("📁 1. Dados Brutos (Raw Data)")
  st.dataframe(df_raw.head(), use_container_width=True)

  # Seleção da Estratégia
  st.markdown("---")
  strategy = st.radio(
      "Selecione a abordagem de engenharia de dados:",
      [
          "ETL (Extract, Transform, Load) - Transformação em memória antes de"
          " carregar",
          (
              "ELT (Extract, Load, Transform) - Carga bruta no banco +"
              " Transformação via SQL"
          ),
      ],
  )

  # Detectar colunas para agrupamento
  numeric_cols = df_raw.select_dtypes(include=["number"]).columns.tolist()
  text_cols = df_raw.select_dtypes(include=["object"]).columns.tolist()

  if not numeric_cols or not text_cols:
    st.warning(
        "O seu arquivo precisa conter pelo menos uma coluna de texto (para"
        " agrupar) e uma coluna numérica (para somar/calcular)."
    )
  else:
    st.markdown("### ⚙️ Parâmetros de Transformação")
    col1, col2 = st.columns(2)
    with col1:
      group_col = st.selectbox("Agrupar por:", text_cols)
    with col2:
      agg_col = st.selectbox("Métrica (Valor numérico):", numeric_cols)

    # Execução baseada na escolha
    if strategy.startswith("ETL"):
      st.info(
          "**Fluxo ETL:** Os dados são limpos e transformados pelo Pandas antes"
          " de serem exibidos."
      )

      # Transformação (Exemplo: Agrupamento e soma)
      df_transformed = df_raw.groupby(group_col)[agg_col].sum().reset_index()
      df_transformed.columns = [group_col, "Total"]

      st.subheader("✨ 2. Dados Transformados (ETL)")
      st.dataframe(df_transformed, use_container_width=True)

      st.subheader("📈 3. Visualização Gráfica")
      st.bar_chart(df_transformed.set_index(group_col)["Total"])

    else:
      st.info(
          "**Fluxo ELT:** Os dados brutos são salvos diretamente no banco de"
          " dados e a transformação ocorre via query SQL."
      )

      # Load: Carregar dados brutos no banco SQLite em memória
      conn = sqlite3.connect(":memory:")
      df_raw.to_sql("dados_brutos", conn, index=False, if_exists="replace")

      # Transform: Executar consulta SQL
      query = f"""
                SELECT 
                    "{group_col}" AS categoria, 
                    SUM("{agg_col}") AS total 
                FROM dados_brutos 
                GROUP BY "{group_col}"
                ORDER BY total DESC;
            """
      df_transformed = pd.read_sql(query, conn)
      conn.close()

      st.subheader("✨ 2. Dados Transformados via SQL (ELT)")
      st.dataframe(df_transformed, use_container_width=True)

      st.subheader("📈 3. Visualização Gráfica")
      st.bar_chart(df_transformed.set_index("categoria")["total"])