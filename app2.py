from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# ✅ Power Automate URL (your actual trigger URL)
POWER_AUTOMATE_URL = (
    "https://prod-42.southeastasia.logic.azure.com:443/workflows/"
    "b08b6a17391e465bbd05adc35e61cf9e/triggers/manual/paths/invoke?"
    "api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&"
    "sig=SisWyS6-N1beQLvsPO7T0fYaKE8sxOu3PhdHyuSnJnk"
)

@app.route('/cloudflow', methods=['POST'])
def trigger_cloudflow():
    try:
        print("📨 Request received from Yellow.ai or test tool")

        # Get payload from request body
        payload = request.get_json(force=True) or {}
        print("📦 Payload received:", payload)

        # Construct data to send to Power Automate
        data = {
            "source": "yellow",
            "bmsid": payload.get("bmsid", "not_provided")
        }

        headers = {"Content-Type": "application/json"}

        # Send request to Power Automate
        response = requests.post(POWER_AUTOMATE_URL, headers=headers, json=data)
        print("🔁 Power Automate Response:", response.status_code, response.text)

        # Return Power Automate's response to Yellow.ai
        return jsonify(response.json()), response.status_code
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)
