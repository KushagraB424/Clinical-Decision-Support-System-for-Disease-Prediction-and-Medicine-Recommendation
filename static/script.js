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
            <p><b>Medicines:</b> ${data.medications}</p>
            <p><b>Workout:</b> ${data.workout}</p>
            <p><b>Diet:</b> ${data.diet}</p>
        `;
    });
}
