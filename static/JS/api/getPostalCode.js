'use strict';

const sendPostalCode = document.getElementById('send-postal-code');
const inputPostalCode = document.getElementById('postal-code-input');
const selectSettlement = document.getElementById('settlements-select');
const inputState = document.getElementById('state-input');
const inputCity = document.getElementById('city-input');



sendPostalCode.addEventListener('click', ()=>{
    const apiUrl = `/tools/api/get-postal-code/${inputPostalCode.value}/`;

    fetch(apiUrl)
    .then(response => {
        if (!response.ok) {
            throw new Error("Error en la solicitud");
        }
        return response.json();
    })
    .then(data => {
        // Actualiza el select de settlements
        selectSettlement.innerHTML = ""; // Limpia las opciones existentes
        data.settlements.forEach(settlement => {
            const option = document.createElement("option");
            option.value = settlement.id;
            option.textContent = settlement.name;
            selectSettlement.appendChild(option);
        });

        // Actualiza los campos de input para city y state
        inputCity.value = data.city.name;
        inputState.value = data.state.name;
    })
    .catch(error => {
        // Maneja los errores
        console.error("Error: " + error.message);
        // Aquí podrías mostrar un mensaje de error en tu interfaz si lo deseas
    });
});