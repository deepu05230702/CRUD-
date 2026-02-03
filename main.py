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
    print("Press CTRL+C to stop the server.")
    print("Use the registered endpoints to interact with the user API.")
    print("Available endpoints:")
    print("POST /users - Create a new user")        
    print("GET /users/<id> - Read user information")
    print("PUT /users/<id> - Update user information")
    print("DELETE /users/<id> - Delete a user")
    print("Make sure to send the appropriate data in the request body for POST and PUT requests.")
    print("Check the console for any errors or logs.")
    print("Happy coding!")