import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GOOGLE_FACTCHECK_API_KEY")


def google_fact_check(query):

    url = "https://factchecktools.googleapis.com/v1alpha1/claims:search"

    params = {
        "query": query,
        "key": API_KEY
    }

    try:

        response = requests.get(
            url,
            params=params,
            timeout=10
        )

        data = response.json()

        results = []

        claims = data.get("claims", [])

        for claim in claims[:5]:

            claim_text = claim.get(
                "text",
                "Unknown Claim"
            )

            reviews = claim.get(
                "claimReview",
                []
            )

            for review in reviews:

                results.append({

                    "claim":
                        claim_text,

                    "publisher":
                        review.get(
                            "publisher",
                            {}
                        ).get(
                            "name",
                            "Unknown"
                        ),

                    "rating":
                        review.get(
                            "textualRating",
                            "Unknown"
                        ),

                    "url":
                        review.get(
                            "url",
                            ""
                        )
                })

        return results

    except Exception as e:

        print("Fact Check Error:", e)

        return []