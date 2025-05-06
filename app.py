from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Dictionary of motivational responses
responses = {
    "stuck": [
        "Lilly, even Sensei started as a noob. Keep going!",
        "You're not stuck, you're learning. One step at a time!",
        "Break it down. Solve the smallest part first!"
    ],
    "tired": [
        "Rest, but don’t quit. Even warriors need sleep!",
        "Tired? That means you're working hard. Take 5, then get back at it!",
        "The grind is real, but so is your potential!"
    ],
    "bored": [
        "Bored? Try making this project cooler—maybe add a GUI next?",
        "Boredom is a sign to level up! Pick a harder challenge.",
        "Turn that boredom into curiosity. What's something you've never coded before?"
    ],
   "lazy": [
        "you are not lazy, you just not building the momentum because you think that you cant do it",
        "lazyness is an illusion, lazy mind with talent does the its work more efficiently",
        "fuck your lazyass and lock in"
    ],
    "distracted": [
        "FOCUS",
        "No time to get distracted chigga"
    ]
}

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""
    if request.method == "POST":
        mode = request.form["feeling"]

        # Save response
        with open("progress_log.txt", "a") as file:
            file.write(mode + "\n")

        if mode in responses:
            message=random.choice(responses[mode])
        else:
            message="No matter what, keep going, Lilly! You're on the right path!"

    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
