'use strict';

//const sendPostalCode = document.getElementById('send-postal-code');
const inputPostalCode = document.getElementById('id_postal_code');
const selectSettlement = document.getElementById('id_settlement');
const inputState = document.getElementById('id_state');
const inputCity = document.getElementById('id_city');



inputPostalCode.addEventListener('blur', ()=>{

    const apiUrl = `/api/get-postal-code/${inputPostalCode.value}/`;

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