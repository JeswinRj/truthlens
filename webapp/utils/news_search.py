from gnews import GNews

google_news = GNews(
    language="en",
    country="US",
    max_results=5
)

def search_related_news(query):

    try:

        results = google_news.get_news(query)

        articles = []

        for item in results[:5]:

            articles.append({

                "title":
                    item.get(
                        "title",
                        ""
                    ),

                "publisher":
                    item.get(
                        "publisher",
                        {}
                    ).get(
                        "title",
                        "Unknown"
                    ),

                "url":
                    item.get(
                        "url",
                        ""
                    )

            })

        return articles

    except Exception as e:

        print("News Search Error:", e)

        return []
