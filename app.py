from flask import Flask, render_template, request
from main import get_system_info, compare_systems
import json

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    # System A = the computer running the Flask app
    system_info = get_system_info()

    system_b = None
    comparison = None
    error = None

    # Check if a JSON file was uploaded
    if request.method == "POST":
        file = request.files["system_b"]

        try:
            system_b = json.load(file)
            comparison = compare_systems(system_info, system_b)

        except json.JSONDecodeError as e:
            system_b = None
            comparison = None
            error = f"Invalid JSON file: {e.msg} (line {e.lineno}, column {e.colno})"

    return render_template(
        "index.html",
        system_info=system_info,
        system_b=system_b,
        comparison=comparison,
        error=error
    )


if __name__ == "__main__":
    app.run(port=5001, debug=True)