"""Point d'entrée : `python app.py` (dev) ou `flask --app app run`."""
from portfolio import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
