import math

from utils.model_loader import RF, VECTORIZER
from utils.text_preprocessing import wordopt
from utils.emotion_analyzer import get_emotion_scores
from utils.fact_checker import google_fact_check
from utils.source_verifier import verify_source
from utils.news_search import search_related_news


def label_name(value):
    if value == 1:
        return "Real News"
    else:
        return "Fake News"


def compute_manipulation_score(fear, anger, sadness):
    weighted_sum = (
        (0.5 * fear)
        + (0.3 * anger)
        + (0.2 * sadness)
    )

    scaled = 1 / (
        1 + math.exp(-10 * (weighted_sum - 0.3))
    )

    return round(scaled * 100, 2)


def analyze_news(news_text):

    # Clean text
    cleaned_text = wordopt(news_text)

    # Vectorize
    vector = VECTORIZER.transform([cleaned_text])

    # Prediction
    prediction = RF.predict(vector)[0]

    confidence = float(
        round(
            max(
                RF.predict_proba(vector)[0]
            ) * 100,
            2
        )
    )

    # Emotion Analysis
    emotion_data = get_emotion_scores(news_text)

    fear = emotion_data.get("fear", 0)
    anger = emotion_data.get("anger", 0)
    sadness = emotion_data.get("sadness", 0)

    manipulation_score = compute_manipulation_score(
        fear,
        anger,
        sadness
    )

    if manipulation_score < 30:
        risk_level = "LOW"
    elif manipulation_score < 60:
        risk_level = "MODERATE"
    else:
        risk_level = "HIGH"

    # Fact Check
    fact_checks = google_fact_check(
        news_text[:100]
    )

    # Related News
    try:
        related_news = search_related_news(
            news_text[:80]
        )
    except Exception:
        related_news = []

    # Source Verification
    source_info = None

    if news_text.startswith("http"):
        try:
            source_info = verify_source(news_text)
        except Exception:
            source_info = None

    # Credibility Score
    credibility = confidence

    credibility -= (
        manipulation_score * 0.3
    )

    for fact in fact_checks:

        rating = fact["rating"].lower()

        if "false" in rating:
            credibility -= 20

        elif "true" in rating:
            credibility += 15

    credibility = max(
        0,
        min(100, credibility)
    )

    # Dynamic Explanation
    if prediction == 0:

        explanation = (
            "The article was classified as Fake News because "
            "the Random Forest model detected patterns "
            "commonly associated with misinformation. "
            "Related fact-check results also suggest that "
            "similar claims have been identified by "
            "professional fact-checking organizations."
        )

    else:

        explanation = (
            "The article was classified as Real News because "
            "the model found characteristics similar to "
            "verified news articles and did not detect "
            "significant misinformation signals."
        )

    # Final Output
    return {

        "prediction": label_name(prediction),

        "confidence": confidence,

        "top_emotions": emotion_data["top_3_emotions"],

        "manipulation_score": manipulation_score,

        "risk_level": risk_level,

        "fact_checks": fact_checks,

        "related_news": related_news,

        "source_info": source_info,

        "credibility_score": round(
            credibility,
            2
        ),

        "explanation": explanation

    }