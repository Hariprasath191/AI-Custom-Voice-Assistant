let selectedTone = "neutral";

function setTone(tone) {
  selectedTone = tone;
  document.querySelectorAll(".tones button").forEach(b => b.classList.remove("active"));
  event.target.classList.add("active");
}

async function generate() {
  const text = document.getElementById("text").value;
  const speed = document.getElementById("speed").value;
  const pitch = document.getElementById("pitch").value;

  if (!text) {
    alert("Enter text");
    return;
  }

  const res = await fetch("/generate", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      text,
      speed,
      pitch,
      tone: selectedTone
    })
  });

  const data = await res.json();
  if (data.success) {
    const audio = document.getElementById("audio");
    audio.src = data.audio_url;
    audio.play();
  } else {
    alert(data.error);
  }
}
