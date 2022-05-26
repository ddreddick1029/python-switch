# Function to emulate switch cases in Python
# Credit to W3Schools & Shashank Mishra from GeeksforGeeks
def item_cases(switch):
    selection = {
        0: "Hot Dog",
        1: "French Fries",
        2: "Beer",
    }

    # .get generates an output ig argument supplied is applicable,
    # otherwise, the string will be returned.
    return selection.get(switch, "No Value")


# Runs the code
if __name__ == "__main__":
    switch = 3
    print("You have selected: " + (item_cases(switch)))
