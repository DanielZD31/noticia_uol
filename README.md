# **Objetivo:** 📜  
Este código tem como objetivo obter as últimas notícias do feed RSS da UOL 📰 e exibi-las ao usuário.

# **Ações:** 🔄
1. Importa as bibliotecas necessárias (`requests` 🌐 e `feedparser` 📑).
2. Define a função `get_latest_news(num_news=10)`, que:
   - Faz uma solicitação GET para o feed RSS da UOL 🌍.
   - Analisa o conteúdo do feed RSS utilizando a biblioteca `feedparser` 🔍.
   - Extrai os títulos e links das notícias e retorna essas informações como uma lista de dicionários 📋.
3. Define a função `main()`, que:
   - Chama `get_latest_news()` para obter as últimas notícias 🔔.
   - Imprime as notícias, incluindo o título e o link de cada uma 🖨️.

# **Entrada:** 🎯
- Nenhuma entrada direta é fornecida pelo usuário. O script solicita o feed RSS da UOL diretamente 🌐.

# **Decisão:** ⚖️
- O código verifica se a solicitação HTTP foi bem-sucedida (status code 200 ✅).
- Se o feed contiver entradas, o código as processa e exibe as notícias 🔄.
- Caso contrário, uma mensagem de erro é retornada ❌.

# **Ações a serem executadas:** 🛠️
1. Fazer uma solicitação HTTP GET para obter o conteúdo do feed RSS da UOL 🌍.
2. Processar o conteúdo do feed RSS para extrair as últimas notícias 📰.
3. Exibir as notícias ou uma mensagem de erro, caso não consiga obter as notícias ⚠️.

# **Média de avaliação:** 🏅
- Simplicidade e clareza no código 🧑‍💻.
- Funcionalidade básica de obtenção de notícias de um feed RSS 📬.

# **Execução:** ▶️
- O programa exibe as 10 últimas notícias ou uma mensagem de erro, dependendo do sucesso da solicitação 💻.
