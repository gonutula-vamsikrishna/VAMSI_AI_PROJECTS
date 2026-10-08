document
.getElementById("startBtn")
.addEventListener(
"click",
startRobot
);

async function startRobot(){

    document
    .getElementById("status")
    .innerHTML =
    "🟢 Robot Activated";

    document
    .getElementById("bar")
    .style.width = "100%";

    const response =
    await fetch("/start");

    const data =
    await response.json();

    document
    .getElementById("currentState")
    .innerHTML =

    `
    <b>Robot Location:</b>
    ${data.current_state.robot_location}

    <br><br>

    <b>Product Location:</b>
    ${data.current_state.product_location}

    <br><br>

    <b>Customer:</b>
    ${data.current_state.customer}

    <br><br>

    <b>Delivery Status:</b>
    Pending
    `;

    document
    .getElementById("path")
    .innerHTML =

    `
    ${data.path.join(" ➜ ")}
    `;

    document
    .getElementById("cost")
    .innerHTML =

    `
    <h1>
    ${data.cost}
    </h1>

    Lowest Cost Path Found
    `;

    showStrips(data.strips);

    animateRobot();
}

function showStrips(steps){

    let html = "";

    steps.forEach(
    (step,index)=>{

        html +=
        `
        <p>

        ✅ Step
        ${index+1}

        :

        ${step}

        </p>
        `;

    });

    document
    .getElementById("strips")
    .innerHTML =
    html;
}

async function animateRobot(){

    const robot =
    document
    .getElementById(
    "robot"
    );

    const warehouse =
    document
    .getElementById(
    "Warehouse"
    );

    const A =
    document
    .getElementById(
    "A"
    );

    const House2 =
    document
    .getElementById(
    "House2"
    );

    highlightNode(
    warehouse
    );

    await sleep(1000);

    moveRobot(
    robot,
    warehouse
    );

    document
    .getElementById(
    "status"
    )
    .innerHTML =

    "🏭 Robot At Warehouse";

    await sleep(2000);

    highlightNode(A);

    moveRobot(
    robot,
    A
    );

    document
    .getElementById(
    "status"
    )
    .innerHTML =

    "📦 Product Picked From Warehouse A";

    await sleep(2500);

    highlightNode(
    House2
    );

    moveRobot(
    robot,
    House2
    );

    document
    .getElementById(
    "status"
    )
    .innerHTML =

    "🚚 Delivering Product To House2";

    await sleep(3000);

    document
    .getElementById(
    "status"
    )
    .innerHTML =

    `
    <span
    class="success">

    🎉 GOAL STATE ACHIEVED

    <br><br>

    ✅ Product Delivered

    <br><br>

    🏠 House2

    </span>
    `;

    document
    .getElementById(
    "currentState"
    )
    .innerHTML +=

    `
    <br><br>

    <b style='color:#00ff88'>

    Delivered Successfully

    </b>
    `;
}

function moveRobot(
robot,
target
){

    const x =
    target.offsetLeft
    + 15;

    const y =
    target.offsetTop
    + 15;

    robot.style.left =
    x + "px";

    robot.style.top =
    y + "px";
}

function highlightNode(
node
){

    const nodes =
    document
    .querySelectorAll(
    ".node"
    );

    nodes.forEach(
    n =>
    n.classList.remove(
    "activeNode"
    )
    );

    node.classList.add(
    "activeNode"
    );
}

function sleep(ms){

    return new Promise(
    resolve =>
    setTimeout(
    resolve,
    ms
    )
    );
}