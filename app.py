from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/deploy-status")
def deploy_status():
    return render_template("deploy_status.html")


@app.route("/legacy-release/")
def legacy_release():
    return render_template("legacy_release.html")


@app.route("/legacy-release/deployment.json")
def deployment_file():
    return send_from_directory(
        os.path.join(app.root_path, "legacy"),
        "deployment.json"
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)