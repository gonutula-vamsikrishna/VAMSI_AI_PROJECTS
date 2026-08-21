function updateWaterLevel() {

    // Get slider
    const slider =
        document.getElementById("depthSlider");

    // Get selected depth
    const depth =
        parseInt(slider.value);


    // Get elements
    const water =
        document.getElementById("water");

    const depthValue =
        document.getElementById("depthValue");

    const percentage =
        document.getElementById("waterPercentage");

    const message =
        document.getElementById("waterMessage");

    const status =
        document.getElementById("tankStatus");


    // Display depth
    depthValue.innerText = depth;


    /*
        Convert depth to water percentage

        Depth 0 → 20%
        Depth 1 → 40%
        Depth 2 → 60%
        Depth 3 → 80%
        Depth 4 → 100%
        Depth 5 → 100%
    */

    let waterLevel;


    if (depth === 0) {

        waterLevel = 20;

    }

    else if (depth === 1) {

        waterLevel = 40;

    }

    else if (depth === 2) {

        waterLevel = 60;

    }

    else if (depth === 3) {

        waterLevel = 80;

    }

    else {

        waterLevel = 100;

    }


    // Change tank water height
    water.style.height =
        waterLevel + "%";


    // Display percentage
    percentage.innerText =
        waterLevel + "%";


    // Change message
    if (waterLevel <= 20) {

        message.innerText =
            "💧 Low water level";

        status.innerText =
            "LOW";

    }

    else if (waterLevel <= 60) {

        message.innerText =
            "💧 Water level increasing";

        status.innerText =
            "NORMAL";

    }

    else if (waterLevel < 100) {

        message.innerText =
            "💧 Tank is almost full";

        status.innerText =
            "HIGH";

    }

    else {

        message.innerText =
            "💧 Tank is completely full";

        status.innerText =
            "FULL";

    }

}



/*
    Send slider value to Flask
*/

function sendDepth() {

    const depth =
        document.getElementById(
            "depthSlider"
        ).value;


    document.getElementById(
        "hiddenDepth"
    ).value = depth;

}



/*
    Run once when page loads
*/

window.onload = function() {

    updateWaterLevel();

};