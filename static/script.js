// Toggle display for lists at the bottom
function toggleList(id) {
    var el = document.getElementById(id);
    if (el.style.display === "none" || el.style.display === "") {
        el.style.display = "block";
    } else {
        el.style.display = "none";
    }
}
function renderList(items) {
    if (!items) return "";
    
    // If backend sent a stringified list
    if (typeof items === "string") {
        items = items.replace("[", "")
                     .replace("]", "")
                     .replace(/'/g, "")
                     .split(",");
    }

    return `<ul>${items.map(i => `<li>${i.trim()}</li>`).join("")}</ul>`;
}


function predict() {
    const symptoms = document.getElementById("symptoms").value;

    fetch("/predict", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({symptoms: symptoms})
    })
    .then(res => res.json())
    .then(data => {

        let emergencyAlert = "";
        if (data.emergency) {
            emergencyAlert = `
            <div class="emergency">
                ⚠ EMERGENCY SYMPTOMS DETECTED. SEEK MEDICAL HELP IMMEDIATELY.
            </div>`;
        }

        let warning = "";
        if (data.consult_doctor) {
            warning = `<p class="warning">⚠ Low confidence prediction. Please consult a doctor.</p>`;
        }

        let reasonsList = "<ul>";
        data.reasons.forEach(r => {
            reasonsList += `<li>${r[0]}</li>`;
        });
        reasonsList += "</ul>";

        document.getElementById("result").innerHTML = `
            ${emergencyAlert}
            <h3>Disease: ${data.disease}</h3>
            <p><b>Confidence:</b> ${data.confidence}%</p>
            ${warning}
            <h4>Why this disease?</h4>
            ${reasonsList}
            <p><b>Description:</b> ${data.description}</p>
            <p><b>Precaution:</b> ${data.precaution}</p>
            <p><b>Medicines:</b></p>
            ${renderList(data.medications)}

            <p><b>Diet:</b></p>
            ${renderList(data.diet)}

            <p><b>Workout:</b></p>
            ${renderList(data.workout)}

        `;
    });
}
