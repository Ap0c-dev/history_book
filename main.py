from app.database import create_app
from app.routes import config_routes
from app.auth import auth

app = create_app()

config_routes(app)
app.register_blueprint(auth, url_prefix='/auth')

if __name__ == '__main__':
    app.run(debug=True)
