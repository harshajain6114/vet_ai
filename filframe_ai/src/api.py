from flask import Flask, jsonify, request
import os
import json
from filframe_ai.crew import VeterinaryInsightsAI

app = Flask(__name__)
import os

@app.route("/run", methods=["POST"])
def run_crew():
    try:
        # Set the correct path
        dataset_file = request.json.get("dataset", "data/cat_patients.json")

        # Convert to absolute path
        dataset_path = os.path.join(os.path.dirname(__file__), dataset_file)
        dataset_path = os.path.abspath(dataset_path)

        # Debugging: Print the path being used
        print(f"🔍 Looking for dataset at: {dataset_path}")

        # Check if the file exists
        if not os.path.exists(dataset_path):
            return jsonify({"error": f"❌ File not found: {dataset_path}"}), 400

        # Run the crew with the correct dataset path
        inputs = {"dataset": dataset_path}
        result = VeterinaryInsightsAI().crew().kickoff(inputs=inputs)

        return jsonify({"message": "✅ Crew started successfully!", "result": str(result)}), 200

    except FileNotFoundError as e:
        return jsonify({"error": f"Missing file: {e}"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500



if __name__ == "__main__":
    app.run(debug=True, port=5000)  # Set debug=False in production
