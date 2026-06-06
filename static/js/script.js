
// Load languages automatically
async function loadLanguages() {
    let res = await fetch("/languages");
    let data = await res.json();

    let source = document.getElementById("source");
    let target = document.getElementById("target");

    data.forEach(lang => {
        let option1 = new Option(lang.name, lang.code);
        let option2 = new Option(lang.name, lang.code);

        source.add(option1);
        target.add(option2);
    });
}

loadLanguages();

// Translate text
async function translateText() {

    let text = document.getElementById("text").value;
    let source = document.getElementById("source").value;
    let target = document.getElementById("target").value;

    document.getElementById("loading").classList.remove("hidden");

    let formData = new FormData();
    formData.append("text", text);
    formData.append("source", source);
    formData.append("target", target);

    try {
        let res = await fetch("/translate", {
            method: "POST",
            body: formData
        });

        let data = await res.json();

        document.getElementById("loading").classList.add("hidden");

        if (data.success) {
            document.getElementById("output").innerText = data.translatedText;
        } else {
            document.getElementById("error").innerText = data.error;
        }

    } catch (err) {
        document.getElementById("loading").classList.add("hidden");
        document.getElementById("error").innerText = err.message;
    }
}

// Copy text
function copyText() {
    let text = document.getElementById("output").innerText;
    navigator.clipboard.writeText(text);
}

// Text to speech
function speakText() {
    let text = document.getElementById("output").innerText;
    let speech = new SpeechSynthesisUtterance(text);
    speechSynthesis.speak(speech);
}