from transformers import pipeline

emotion_classifier = pipeline(
    "text-classification",
    model="bhadresh-savani/distilbert-base-uncased-emotion",
    top_k=None
)

def get_emotion_scores(text):

    results = emotion_classifier(text[:512])

    emotions = sorted(
        results[0],
        key=lambda x: x["score"],
        reverse=True
    )

    top_3 = emotions[:3]

    emotion_dict = {
        e["label"]: round(e["score"] * 100, 2)
        for e in top_3
    }

    fear = next(
        (e["score"] for e in results[0]
         if e["label"] == "fear"),
        0
    )

    anger = next(
        (e["score"] for e in results[0]
         if e["label"] == "anger"),
        0
    )

    sadness = next(
        (e["score"] for e in results[0]
         if e["label"] == "sadness"),
        0
    )

    return {
        "top_3_emotions": emotion_dict,
        "fear": fear,
        "anger": anger,
        "sadness": sadness
    }