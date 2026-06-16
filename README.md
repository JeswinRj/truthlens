#  TruthLens

### Fake News Detection & Fact Verification Platform

TruthLens is a machine learning-based web application that detects fake news articles, analyzes emotional manipulation, and verifies claims using Google's Fact Check API.

The platform combines Natural Language Processing (NLP), Machine Learning, Emotion Analysis, and Fact Verification to provide a comprehensive credibility assessment of news content.

---

## Features

### Fake News Detection

* Random Forest Classifier
* TF-IDF Vectorization
* Trained on Fake.csv and True.csv datasets
* Confidence Score Generation

### Emotion Analysis

* DistilBERT Emotion Classification Model
* Detects:

  * Fear
  * Anger
  * Sadness
  * Joy
  * Other emotions

### Manipulation Detection

Uses emotional signals to estimate potential emotional manipulation.

Outputs:

* Manipulation Score
* Risk Level:

  * Low
  * Moderate
  * High

### Fact Verification

Integrated with:

* Google Fact Check Tools API

Displays:

* Verified Claims
* Fact-Checking Publisher
* Verdict
* Reference Links

### Credibility Assessment

Combines:

* ML Confidence
* Emotional Manipulation Indicators
* Fact Check Results

to generate an overall credibility score.

---

## Technology Stack

### Backend

* Python
* Flask

### Machine Learning

* Scikit-learn
* Random Forest
* TF-IDF Vectorizer

### Deep Learning

* Hugging Face Transformers
* DistilBERT Emotion Model

### APIs

* Google Fact Check Tools API

### Frontend

* HTML
* CSS
* Bootstrap 5

---

## Project Structure

```text
fake-news-detector/

├── notebook/
│   └── Fake_News_Training.ipynb
│
├── webapp/
│   ├── app.py
│   │
│   ├── models/
│   │   ├── random_forest.pkl
│   │   └── vectorizer.pkl
│   │
│   ├── utils/
│   │   ├── predictor.py
│   │   ├── model_loader.py
│   │   ├── emotion_analyzer.py
│   │   ├── fact_checker.py
│   │   ├── source_verifier.py
│   │   └── news_search.py
│   │
│   ├── templates/
│   │   ├── index.html
│   │   └── result.html
│   │
│   ├── static/
│   │   └── style.css
│   │
│   ├── requirements.txt
│   └── .env
│
├── screenshots/
│
├── README.md
│
└── .gitignore
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/truthlens.git

cd truthlens/webapp
```

### Create Virtual Environment

```bash
python3 -m venv venv
```

Activate:

#### macOS/Linux

```bash
source venv/bin/activate
```

#### Windows

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure API Key

Create:

```text
.env
```

Add:

```env
FACTCHECK_API_KEY=YOUR_API_KEY
```

---

## Run Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## Example Workflow

1. Enter a news article or claim.
2. Random Forest predicts Fake or Real.
3. Emotion Analysis is performed.
4. Manipulation Score is calculated.
5. Google Fact Check API is queried.
6. Final credibility assessment is displayed.

---

## Future Improvements

* News Source Credibility Ranking
* Related News Discovery
* Explainable AI Dashboard
* Multi-language Fact Verification
* LLM-Based Claim Extraction
* Real-Time News Monitoring

---

## Author

Jeswin Raj

MSc Computer Science (Data Science)

Research Interests:

* Artificial Intelligence
* Machine Learning
* Reinforcement Learning
* Misinformation Detection
* Data Science

---




