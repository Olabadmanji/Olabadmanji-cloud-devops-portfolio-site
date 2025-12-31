
const API_URL = "https://YOUR_API_ID.execute-api.REGION.amazonaws.com/prod";


fetch('events.json')
  .then(response => response.json())
  .then(data => {
    const eventsDiv = document.getElementById('events');
    data.forEach(event => {
      eventsDiv.innerHTML += `
        <h3>${event.title}</h3>
        <p>${event.date}</p>
        <p>${event.description}</p>
        <hr>
      `;
    });
  });


function subscribe() {
  const email = document.getElementById('email').value;

  fetch(`${API_URL}/subscribe`, {
    method: 'POST',
    body: JSON.stringify({ email })
  })
  .then(() => alert("Check your email to confirm subscription"));
}


function createEvent() {
  const title = document.getElementById('title').value;
  const date = document.getElementById('date').value;
  const description = document.getElementById('description').value;

  fetch(`${API_URL}/create-event`, {
    method: 'POST',
    body: JSON.stringify({ title, date, description })
  })
  .then(() => alert("Event created successfully"));
}
