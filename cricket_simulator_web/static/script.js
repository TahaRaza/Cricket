// Team names (replace with your actual teams)
const teams = ["India", "Australia", "England"];

// DOM elements
const teamASelect = document.getElementById('team-a');
const teamBSelect = document.getElementById('team-b');
const matchResultsDiv = document.getElementById('match-results');

// Populate team dropdown menus
function populateTeams() {
  teams.forEach(team => {
    const option = document.createElement('option');
    option.value = team;
    option.text = team;
    teamASelect.appendChild(option);
    teamBSelect.appendChild(option.cloneNode(true)); // Clone to avoid duplicate references
  });
}

populateTeams(); // Call the function to populate menus

// Simulate match function (placeholder for now)
function simulateMatch() {
  // Implement your logic to simulate the match (random scores, winner calculation)
  const winner = teams[Math.floor(Math.random() * teams.length)];
  const message = `The winner is: ${winner}`;
  displayMatchResults(message);
}

// Display match results
function displayMatchResults(message) {
  matchResultsDiv.textContent = message;
}

// Handle form submission
const form = document.getElementById('team-selection-form');
form.addEventListener('submit', function(event) {
  event.preventDefault(); // Prevent default form submission behavior
  const teamA = teamASelect.value;
  const teamB = teamBSelect.value;
  // You can optionally send team selections to Python here using AJAX
  // For now, call the simulateMatch function directly
  simulateMatch();
});
