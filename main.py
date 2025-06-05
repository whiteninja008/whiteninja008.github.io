from flask import Flask, jsonify, render_template
import subprocess

app = Flask(__name__)

def get_saved_wifi_passwords():
    profiles_output = subprocess.check_output(["netsh", "wlan", "show", "profiles"], encoding='utf-8')
    profiles = []
    for line in profiles_output.split('\n'):
        if "All User Profile" in line:
            profile = line.split(":")[1].strip()
            profiles.append(profile)

    wifi_details = []
    for profile in profiles:
        try:
            profile_info = subprocess.check_output(
                ["netsh", "wlan", "show", "profile", profile, "key=clear"],
                encoding='utf-8'
            )
            password = None
            for line in profile_info.split('\n'):
                if "Key Content" in line:
                    password = line.split(":")[1].strip()
                    break
            wifi_details.append({"SSID": profile, "Password": password})
        except subprocess.CalledProcessError:
            wifi_details.append({"SSID": profile, "Password": None})

    return wifi_details

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/wifi-passwords')
def wifi_passwords():
    return jsonify(get_saved_wifi_passwords())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

