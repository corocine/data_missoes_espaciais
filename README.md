# Painel de Análise de Missões Espaciais

Este é um painel de análise de missões espaciais construído com Streamlit. Ele visualiza dados de missões espaciais, permitindo aos usuários explorar lançamentos por ano, empresa, país e muito mais.

## Tecnologias Utilizadas


| Tecnologia          | Badge                                                                                             | Descrição                                                                                                       |
| :------------------ | :------------------------------------------------------------------------------------------------ | :---------------------------------------------------------------------------------------------------------------- |
| **Python**    | ![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)          | Linguagem principal do projeto.                                                                                   |
| **Streamlit** | ![Streamlit](https://img.shields.io/badge/Streamlit-1.10%2B-red?style=for-the-badge&logo=streamlit) | Framework utilizado para a criação do dashboard web interativo.                                                 |
| **Pandas**    | ![Pandas](https://img.shields.io/badge/Pandas-1.4%2B-blue?style=for-the-badge&logo=pandas)          | Biblioteca para manipulação e análise de dados.                                                                |
| **Plotly**    | ![Plotly](https://img.shields.io/badge/Plotly-5.9%2B-purple?style=for-the-badge&logo=plotly)        | Biblioteca para a criação de gráficos interativos.                                                             |
| Parquet             | ![Parquet](https://img.shields.io/badge/Parquet-Apache-yellow?style=for-the-badge&logo=apache)      | Formato de arquivo colunar utilizado para armazenar os dados processados, otimizando a leitura e o armazenamento. |

## Como Executar o Projeto

1. **Clone o repositório:**

   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd <NOME_DO_DIRETORIO>
   ```
2. **Crie e ative um ambiente virtual:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
   ```
3. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```
4. **Execute a aplicação Streamlit:**

   ```bash
   streamlit run main.py
   ```
5. Abra seu navegador e acesse `http://localhost:8501`.

---
