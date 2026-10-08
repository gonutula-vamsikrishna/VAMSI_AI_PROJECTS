from flask import Flask, render_template, jsonify

app = Flask(__name__)

# UCS Graph
graph = {
    "Warehouse": {"A": 2, "B": 4, "C": 6, "D": 8},
    "A": {"House1": 3, "House2": 4},
    "B": {"House3": 5},
    "C": {"House4": 3},
    "D": {"House5": 2},
    "House1": {},
    "House2": {},
    "House3": {},
    "House4": {},
    "House5": {}
}


def ucs(start, goal):
    frontier = [(0, start, [start])]
    visited = set()

    while frontier:

        frontier.sort()
        cost, node, path = frontier.pop(0)

        if node == goal:
            return path, cost

        if node in visited:
            continue

        visited.add(node)

        for neighbor, edge_cost in graph[node].items():
            if neighbor not in visited:
                frontier.append(
                    (
                        cost + edge_cost,
                        neighbor,
                        path + [neighbor]
                    )
                )

    return None, None


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/start")
def start_robot():

    current_state = {
        "robot_location": "Warehouse",
        "product_location": "A",
        "customer": "House2",
        "delivered": False
    }

    strips_steps = [
        "Robot Activated",
        "Go To Warehouse A",
        "Pick Product",
        "Apply UCS Search",
        "Move To House2",
        "Deliver Product",
        "Goal State Achieved"
    ]

    path, cost = ucs("Warehouse", "House2")

    return jsonify({
        "current_state": current_state,
        "strips": strips_steps,
        "path": path,
        "cost": cost,
        "goal": "House2"
    })


if __name__ == "__main__":
    app.run(debug=True)