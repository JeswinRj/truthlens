from urllib.parse import urlparse

TRUSTED_SOURCES = {
    "reuters.com": 95,
    "bbc.com": 95,
    "thehindu.com": 90,
    "apnews.com": 95,
    "cnn.com": 85,
    "indianexpress.com": 85,
    "ndtv.com": 80
}

def verify_source(url):

    try:

        domain = urlparse(url).netloc
        domain = domain.replace("www.", "")

        score = TRUSTED_SOURCES.get(
            domain,
            50
        )

        status = (
            "Trusted"
            if score >= 80
            else "Unknown"
        )

        return {
            "domain": domain,
            "credibility": score,
            "status": status
        }

    except Exception:
        return None
    
