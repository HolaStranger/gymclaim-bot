from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/cloudflow', methods=['GET', 'POST'])
def yellow_trigger():
    print("✅ Yellow.ai triggered me!")

    payload = request.get_json() or {}
    print("🟡 Payload:", payload)

    power_automate_url = "https://prod-42.southeastasia.logic.azure.com:443/workflows/b08b6a17391e465bbd05adc35e61cf9e/triggers/manual/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=SisWyS6-N1beQLvsPO7T0fYaKE8sxOu3PhdHyuSnJnk"
    headers = {"Content-Type": "application/json"}
    data = {
        "source": "yellow",
        "employee": payload.get("employee", "unknown")
    }

    response = requests.post(power_automate_url, headers=headers, json=data)
    print("🔁 Power Automate response:", response.status_code, response.text)

    return jsonify({"status": "sent to Power Automate"}), 200

if __name__ == '__main__':
    print("✅ Starting Flask app...")
    app.run(port=5000, debug=True)
