import time
from datetime import datetime
import random
import subprocess
from os import system
# random "OK" btn: sounds good, will do...
SECONDS_PER_HOUR = 3600
HOURS_PER_DAY = 24

START_TIME = 9
END_TIME = 19
FREQUENCY = 1
# todo have questions in a list then move to seporate list until all through the list, then replenish the list/repeat

QUESTIONS = ["Have you taken a break today?",
             "Snack?",
             "Go for a walk.",
             "Every moment is a fresh beginning. - T.S Eliot",
             "Change the world by being yourself. - Amy Poehler",
             "Everything you can imagine is real. - Pablo Picasso",
             "Whatever you do, do it well. - Walt Disney",
             "All limitations are self-imposed. - Oliver Wendell Holmes",
             "Problems are not stop signs, they are guidelines. - Robert H. Schiuller",
             "Oh, the things you can find, if you don't stay behind. - Dr. Seuss",
             "Determine your priorities and focus on them. - Eileen McDargh",
             "Yesterday you said tomorrow. Just do it. - Nike",
             "I don't need it to be easy, I need it to be worth it. - Lil Wayne",
             "Doubt kills more dreams than failure - Suzy Kassem",
             "There is no substitute for hard work. - Thomas Edison",
             "Strive for greatness. - Lebron James",
             "Let the beauty of what you love be what you do. - Rumi",
             "I will remember and recover, not forgive and forget. - Unknown",
             "I have nothing to lose but something to gain. - Eminem",
             "Any fool can write code that a computer can understand. Good programmers write code that humans can understand. - Martin Fowler",
             "First, solve the problem. Then, write the code. - John Johnson",
             "Experience is the name everyone gives to their mistakes - Oscar Wilde",
             "In order to be irreplaceable, one must always be different - Coco Chanel",
             "Knowledge is power. - Francis Bacon",
             "Perfection is achieved not when there is nothing more to add, but rather when there is nothing more to take away. - Antoine de Saint-Exupery",
             "Code is like humor. When you have to explain it, it's bad. - Cory House",
             "Fix the cause, not the symptom. - Steve Maguire",
             "Optimism is an occupational hazard of programming: feedback is the treatment. - Kent Beck",
             "When to use iterative development? You should use iterative development only on projects that you want to succeed. - Martin Fowler",
             "Simplicity is the soul of efficiency. - Austin Freeman",
             "Before software can be reusable it first has to be usable. - Ralph Johnson",
             "Make it work, make it right, make it fast. - Kent Beck"]


applescript = """
display dialog "%s"¬
with title "This is a pop-up window"¬
with icon caution¬
buttons {"NEW", "OK"}
return button returned of result
"""


def main():
    while True:
        current_hour = datetime.now().hour
        print("HOUR", current_hour)
        if current_hour in range(START_TIME, END_TIME):
            response = "NEW"
            while response == "NEW":
                response = subprocess.run(
                    "osascript -e '{}'".format(applescript % random.choice(QUESTIONS)), shell=True, capture_output=True).stdout.strip().decode('utf-8')
        else:
            print("else pkill")
            subprocess.run(
                "pkill -9 -f hourlyQuestions.py", shell=True)
        time.sleep(SECONDS_PER_HOUR*FREQUENCY)

    # bytes("mystring", 'utf-8')


if __name__ == "__main__":
    # system("alias stopQuestions='pkill -9 -f hourlyQuestions.py' && ls")
    # subprocess.run(
        # "alias stopQuestions='pkill -9 -f hourlyQuestions.py'", shell=True)
    main()
