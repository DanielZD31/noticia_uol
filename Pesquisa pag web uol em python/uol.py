import requests  # Importa a biblioteca requests para fazer solicitações HTTP
import feedparser  # Importa a biblioteca feedparser para analisar feeds RSS

def get_latest_news(num_news=10):
    # URL do feed RSS da UOL
    rss_url = "https://rss.uol.com.br/feed/noticias.xml"
    
    # Faz uma solicitação GET para a URL do feed RSS
    response = requests.get(rss_url)
    
    # Verifica se a solicitação foi bem-sucedida
    if response.status_code == 200:
        # Analisa o feed RSS
        feed = feedparser.parse(response.text)
        
        # Verifica se há entradas no feed
        if feed.entries:
            latest_news = []  # Lista para armazenar as últimas notícias
            
            # Itera sobre as primeiras 'num_news' entradas no feed
            for entry in feed.entries[:num_news]:
                # Extrai o título e o link de cada entrada e adiciona a lista
                latest_news.append({
                    "title": entry.title,
                    "link": entry.link
                })
            
            # Retorna a lista de dicionários contendo as últimas notícias
            return latest_news
        else:
            return "Não foi possível encontrar notícias."
    else:
        return "Falha ao obter o feed RSS."

def main():
    # Obtém as últimas notícias da UOL
    latest_news = get_latest_news()
    
    # Verifica se as últimas notícias foram obtidas com sucesso
    if isinstance(latest_news, list):
        # Imprime as 10 últimas notícias
        print("As 10 últimas notícias da UOL:")
        for i, news in enumerate(latest_news, start=1):
            print(f"{i}. Título: {news['title']}")
            print(f"   Link: {news['link']}")
            print()
    else:
        # Se não foi possível obter as notícias, imprime a mensagem de erro
        print(latest_news)

if __name__ == "__main__":
    main()  # Chama a função main() para iniciar o programa
