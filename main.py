from flask import Flask, request, render_template
import openai

app = Flask(__name__)

# Замените "your_openai_api_key_here" на ваш ключ API OpenAI
openai.api_key = ""

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_name = request.form['user_name']
        user_query = request.form['user_query']
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Вы общаетесь с ChatGPT, основанным на GPT-4."},
                {"role": "user", "content": user_query},
            ]
        )
        return render_template('index.html', answer=response.choices[0].message['content'], user_name=user_name, user_query=user_query)
    return render_template('index.html', answer=None)

if __name__ == '__main__':
    app.run(debug=True)
