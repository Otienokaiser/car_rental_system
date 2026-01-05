// Load vehicles for index.html
async function loadVehicles() {
  const vehiclesContainer = document.getElementById('vehicles');
  const noVehiclesMessage = document.getElementById('no-vehicles');

  if (!vehiclesContainer || !noVehiclesMessage) return;

  try {
    const response = await fetch('/api/vehicles');
    if (!response.ok) throw new Error('Failed to fetch vehicles');

    const vehicles = await response.json();

    if (vehicles.length === 0) {
      noVehiclesMessage.style.display = 'block';
      vehiclesContainer.style.display = 'none';
      return;
    }

    noVehiclesMessage.style.display = 'none';
    vehiclesContainer.style.display = 'grid';

    vehiclesContainer.innerHTML = '';

    vehicles.forEach(vehicle => {
      const vehicleDiv = document.createElement('div');
      vehicleDiv.classList.add('vehicle-card');

      vehicleDiv.innerHTML = `
        <img src="${vehicle.images[0]}" alt="${vehicle.name}" />
        <div class="vehicle-content">
          <div class="vehicle-name">${vehicle.name}</div>
          <div class="vehicle-desc">${vehicle.description}</div>
          <div class="vehicle-price">Price: ${vehicle.price}</div>
        </div>
      `;

      vehiclesContainer.appendChild(vehicleDiv);
    });
  } catch (error) {
    vehiclesContainer.innerHTML = `<p style="color:red;">Error loading vehicles.</p>`;
    noVehiclesMessage.style.display = 'none';
    console.error(error);
  }
}

// Run loadVehicles on index page only
if (document.getElementById('vehicles')) {
  window.onload = loadVehicles;
}

// Placeholder for other page scripts, e.g., login, signup, rent forms
// You can add event listeners and fetch calls here later
