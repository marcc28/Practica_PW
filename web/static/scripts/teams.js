$(document).ready(function () {
    $.ajax({
        url: 'api/teams', // Cambia por tu URL real o endpoint local
        method: 'GET',
        success: function (response) {
            $('#mensaje-error').hide();
            console.log(response)
            const equipos = response.teams;
            console.log(equipos)
            renderEquipos(equipos)
        },
        error: function (xhr, status, error) {
            $('#mensaje-error').show();
            console.error('Error al recuperar datos:', error);
        }
    });

    $('#cerrar-modal').on('click', () => {
        $('#modal-overlay').addClass('hidden');
    });

    $('#buscador').on('input', function () {
        const texto = $(this).val().toLowerCase();
        const filtrados = equipos.filter(eq => eq.name.toLowerCase().includes(texto));
        renderEquipos(filtrados);
    });
});

function renderEquipos(lista) {
    const $ul = $('#tabla-equipos tbody')
    $ul.empty();
    lista.forEach(equipo => {
        const $tr = $(`<tr>
                        <td><img src="${equipo.crest}" alt="escudo de ${equipo.name}"></td>
                        <td>${equipo.name}</td>
                        <td>${equipo.founded}</td>
                        <td>${equipo.venue}</td>
                        <td>${equipo.coach?.name || 'Desconocido'}</td>
        </tr>`);
        $tr.on('click', function () {
            $('.equipo-item').removeClass('equipo-seleccionado');

            // Marca como seleccionado el actual
            $(this).addClass('equipo-seleccionado');

            // Mostrar modal u otra acción
            mostrarModal(equipo);
        })
        $ul.append($tr);
    });
}


function mostrarModal(equipo) {
    $('#modal-nombre').text(equipo.name || "Desconocido");
    $('#modal-fundado').text(equipo.founded || 'Desconocido');
    $('#modal-estadio').text(equipo.venue || 'Desconocido');
    $('#modal-overlay').removeClass('hidden')
}

