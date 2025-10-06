from flask import Flask

app = Flask(__name__)

@app.get('/health')
def health():
    return {"status": 200}  # Исправил синтаксис словаря и двоеточие внутри ключа

@app.get("/")
def root():
    return 'Hello world!'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)  # Добавил запятую между аргументами

# @app.route('/')
# def hello():
#     return 'Hello, Flask!'

# if __name__ == '__main__':
#     app.run(debug=True)
