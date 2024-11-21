from flask import Flask, request
import os

app = Flask(__name__)

# Path to the file
FILE_PATH = "data/user_inputs.txt"

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Get user input
        user_input = request.form.get("user_input")
        if user_input:
            # Ensure the directory exists
            os.makedirs(os.path.dirname(FILE_PATH), exist_ok=True)
            # Write the input directly to the file
            with open(FILE_PATH, "a") as file:
                file.write(user_input + "\n")

    # Read all inputs from the file
    try:
        with open(FILE_PATH, "r") as file:
            user_inputs = file.readlines()
    except FileNotFoundError:
        user_inputs = []

    # Generate HTML response dynamically
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Flask Input App</title>
    </head>
    <body>
        <h1>Submit Your Input</h1>
        <form method="POST">
            <input type="text" name="user_input" placeholder="Enter something" required>
            <button type="submit">Submit</button>
        </form>
        <h2>Submitted Inputs:</h2>
        <ul>
    """
    for input_item in user_inputs:
        html += f"<li>{input_item.strip()}</li>"
    html += """
        </ul>
    </body>
    </html>
    """
    return html


if __name__ == "__main__":
    # Ensure the directory exists
    os.makedirs(os.path.dirname(FILE_PATH), exist_ok=True)
    # Ensure the file exists before the app starts
    open(FILE_PATH, "a").close()
    app.run(host="0.0.0.0", port=5000)
