from flask import Flask

app = Flask(__name__)


@app.route("/")
def main_page():
    return "<h1>Миссия Колонизация Марса</h1>"


@app.route("/index")
def index():
    return "<h1>И на Марсе будут яблони цвести!</h1>"


@app.route("/promotion")
def promotion():
    return ("<h1>Человечество вырастает из детства.</h1>"
            "<h1>Человечеству мала одна планета.</h1>"
            "<h1>Мы сделаем обитаемыми безжизненные пока планеты.</h1>"
            "<h1>И начнем с Марса!</h1>"
            "<h1>Присоединяйся!</h1>")


@app.route("/image_mars")
def image_mars():
    return """
            <!doctype html>
                <html lang="en">
                    <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <link rel="stylesheet" href="static\css\main.css">
                        <title>Привет, Яндекс!</title>
                    </head>
                    <body>
                        <h1>Жди нас, Марс!</h1>
                        <br>
                        <img src='static\img\OSIRIS_Mars_true_color.jpg.webp'>
                        <div class="alert alert-primary" role="alert">
                            Человечество вырастает из детства.
                        </div>
                        <div class="alert alert-success" role="alert">
                            Человечеству мала одна планета.
                        </div>
                        <div class="alert alert-danger " role="alert">
                            Мы сделаем обитаемыми безжизненные пока планеты
                        </div>
                        <div class="alert alert-secondary" role="alert">
                            И начнем с Марса!
                        </div>
                        <div class="alert alert-dark" role="alert">
                            Присоединяйся!
                        </div>

                    </body>
                </html>
            """


if __name__ == "__main__":
    app.run(port=8000, host="127.0.0.1")
