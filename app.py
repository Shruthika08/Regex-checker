from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        test_string = request.form["test_string"]
        regex_pattern = request.form["regex_pattern"]
        matches = find_matches(test_string, regex_pattern)
        return render_template("index.html", matches=matches, test_string=test_string, regex_pattern=regex_pattern)
    return render_template("index.html")

def find_matches(test_string, regex_pattern):
    matches = re.findall(regex_pattern, test_string)
    return matches

@app.route("/validate_email", methods=["GET", "POST"])
def validate_email():
    if request.method == "POST":
        email = request.form["email"]
        regex_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'  # Regular expression for email validation
        is_valid = bool(re.match(regex_pattern, email))
        return render_template("validate_email.html", email=email, is_valid=is_valid)
    return render_template("validate_email.html")

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)