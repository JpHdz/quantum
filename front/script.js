function runCode() {
  const code = document.getElementById("codeInput").value;
  console.log(code);
  fetch("http://127.0.0.1:5000/run", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ code: code }),
  })
    .then((response) => response.json())
    .then((data) => {
      document.getElementById("outputArea").textContent = data.output;
    })
    .catch((error) => console.error("Error:", error));
}
