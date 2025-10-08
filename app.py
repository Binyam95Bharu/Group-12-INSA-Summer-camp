from flask import Flask, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required, JWTManager
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this in your actual application!
jwt = JWTManager(app)

# Dummy user data
users = {
    "testuser": {
        "password": "password"
    }
}

@app.route("/api/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username in users and users[username]["password"] == password:
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
    return jsonify({"msg": "Bad username or password"}), 401

@app.route("/api/dashboard", methods=["GET"])
@jwt_required()
def dashboard():
    # Placeholder data for the dashboard
    dashboard_data = {
        "active_simulations": 5,
        "critical_alerts": 3,
        "system_health": 98,
        "defense_score": 85
    }
    return jsonify(dashboard_data)

@app.route("/api/simulations", methods=["GET", "POST"])
@jwt_required()
def simulations():
    if request.method == "POST":
        # Logic to create a new simulation
        return jsonify({"msg": "Simulation created successfully"})
    else:
        # Placeholder data for simulations
        simulations_data = [
            {"id": 1, "name": "Test Simulation 1", "status": "Running"},
            {"id": 2, "name": "Test Simulation 2", "status": "Completed"}
        ]
        return jsonify(simulations_data)

@app.route("/api/alerts", methods=["GET"])
@jwt_required()
def alerts():
    # Placeholder data for alerts
    alerts_data = [
        {"id": 1, "severity": "Critical", "message": "Unauthorized access attempt detected"},
        {"id": 2, "severity": "High", "message": "Suspicious file modification detected"}
    ]
    return jsonify(alerts_data)

@app.route("/api/settings", methods=["GET", "POST"])
@jwt_required()
def settings():
    if request.method == "POST":
        # Logic to update settings
        return jsonify({"msg": "Settings updated successfully"})
    else:
        # Placeholder data for settings
        settings_data = {
            "theme": "dark",
            "notifications": True
        }
        return jsonify(settings_data)

if __name__ == "__main__":
    app.run(debug=True)
