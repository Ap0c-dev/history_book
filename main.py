from app.database import create_app
from app.routes import config_routes
from app.auth import auth
import os

app = create_app()
app.config['SECRET_KEY'] = os.urandom(24).hex()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/data_history_book.sqlite'
config_routes(app)

app.register_blueprint(auth, url_prefix='/auth')

if __name__ == '__main__':
    app.run(debug=True)