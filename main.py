from app.database import create_app
from app.routes import config_routes

app = create_app()
config_routes(app)

if __name__ == '__main__':
    app.run(debug=True)