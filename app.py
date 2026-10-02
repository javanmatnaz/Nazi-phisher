from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/" , methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        with open('users.txt', 'a') as f:
           f.write(f"{username},{password}\n")

    return render_template('index.html')
if __name__ == "__main__":
    app.run(debug=True)