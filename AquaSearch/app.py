from flask import Flask, render_template, request

app = Flask(__name__)


# -----------------------------
# DEPTH LIMITED SEARCH
# -----------------------------
def dls(graph, current, goal, depth, path):

    path.append(current)

    # Target found
    if current == goal:
        return True

    # Depth limit reached
    if depth == 0:
        path.pop()
        return False

    # Visit neighbouring tanks
    for neighbour in graph.get(current, []):

        if dls(graph, neighbour, goal, depth - 1, path):
            return True

    path.pop()

    return False


# -----------------------------
# HOME PAGE
# -----------------------------
@app.route("/")
def home():

    return render_template("index.html")


# -----------------------------
# RUN DLS
# -----------------------------
@app.route("/search", methods=["POST"])
def search():

    start = request.form["start"]
    goal = request.form["goal"]
    depth = int(request.form["depth"])

    # Water tank network
    graph = {

        "Main Tank": ["Tank A", "Tank B"],

        "Tank A": ["A1", "A2"],

        "Tank B": ["B1", "B2"],

        "A1": ["A1a", "A1b"],

        "A2": ["A2a"],

        "B1": ["B1a"],

        "B2": ["B2a"],

        "A1a": [],

        "A1b": [],

        "A2a": [],

        "B1a": [],

        "B2a": []
    }

    path = []

    found = dls(
        graph,
        start,
        goal,
        depth,
        path
    )

    # Calculate target depth
    target_depth = None

    def find_depth(node, current_depth):

        nonlocal target_depth

        if node == goal:
            target_depth = current_depth
            return

        for child in graph.get(node, []):

            if target_depth is None:
                find_depth(
                    child,
                    current_depth + 1
                )

    find_depth(start, 0)

    return render_template(

        "index.html",

        found=found,

        path=path,

        start=start,

        goal=goal,

        depth=depth,

        target_depth=target_depth
    )


if __name__ == "__main__":

    app.run(debug=True)