from flask import Flask, render_template, request
from utils.predictor import analyze_news

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    news = request.form['news']

    result = analyze_news(news)

    print("\n========================")
    print(result)
    print("========================\n")

    return render_template(
        'result.html',
        result=result
    )
if __name__ == '__main__':
    app.run(debug=True)
