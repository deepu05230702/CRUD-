from flask import Flask

from create_user import create_bp
from read_user import read_bp
from update_user import update_bp
from delete_user import delete_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(create_bp)
app.register_blueprint(read_bp)
app.register_blueprint(update_bp)
app.register_blueprint(delete_bp)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
    print("Server is running on http://0.0.0.0:5000")