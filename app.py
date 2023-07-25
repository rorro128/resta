from flask import Flask, render_template, json, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route('/showMenu')
def showMenu():
    menus = [
    {
        "nombre": "Menú 1",
        "items": [
            {"nombre": "Hamburguesa", "precio": 10},
            {"nombre": "Pizza", "precio": 12},
            {"nombre": "Ensalada", "precio": 8}
        ]
    },
    {
        "nombre": "Menú 2",
        "items": [
            {"nombre": "Sopa", "precio": 5},
            {"nombre": "Pasta", "precio": 10},
            {"nombre": "Postre", "precio": 6}
        ]
    }
    ]
    return render_template('table.html', menus=menus)

if __name__ == "__main__":
	app.run(debug=True)