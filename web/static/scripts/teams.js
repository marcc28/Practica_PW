let equipos = [];
let teamId = null;
$(document).ready(function () {
    loadTeams();
    $('#cerrar-modal').on('click', () => {
        $('#modal-overlay').addClass('hidden');
        $('#visualize-modal').addClass('hidden');
    });

    $('#cerrar-modal-edit').on('click', () => {
        $('#modal-overlay').addClass('hidden');
        $('#edit-modal').addClass('hidden');
    });

    // Abrir modal para crear equipo
    $('#btn-crear-equipo').on('click', () => {
        $('#modal-overlay').removeClass('hidden');
        $('#create-modal').removeClass('hidden');
    });

    // Cerrar modal crear equipo
    $('#cerrar-crear-modal').on('click', () => {
        $('#create-modal').addClass('hidden');
        $('#modal-overlay').addClass('hidden');
    });

    $('#btn-delete-team').on('click', function (e) {
        e.preventDefault()
        $.ajax({
            url: `/team/${teamId}/delete/`, method: 'DELETE', contentType: 'application/json', headers: {
                'X-CSRFToken': getCookie('csrftoken')
            }, success: function () {
                loadTeams()
                $('#modal-overlay').addClass('hidden');
                $('#edit-modal').addClass('hidden');
            }, error: function () {
                alert('Error al eliminar equipo');
            }
        });
    })

    $('#buscador').on('input', function () {
        const texto = $(this).val().toLowerCase();
        const filtrados = equipos.filter(eq => eq.name.toLowerCase().includes(texto));
        renderEquipos(filtrados);
    });

    $('#form-editar-equipo').on('submit', function (e) {
        e.preventDefault();

        const equipoId = $(this).data('equipo-id');

        const datosActualizados = {
            name: $('#modal-nombre-input').val(),
            crest: $('#modal-crest-input').val(),
            founded: $('#modal-fundado-input').val(),
            venue: $('#modal-estadio-input').val(),
            coach: $('#modal-coach-input').val()
        };

        $.ajax({
            url: `/team/${equipoId}/edit`, method: 'PUT', contentType: 'application/json', headers: {
                'X-CSRFToken': getCookie('csrftoken')
            }, data: JSON.stringify(datosActualizados), success: function () {
                loadTeams()
                $('#modal-overlay').addClass('hidden');
                $('#edit-modal').addClass('hidden');
            }, error: function () {
                alert('Error al actualizar equipo');
            }
        });
    });


    // Guardar equipo nuevo
    $('#btn-guardar-equipo').on('click', function (e) {
        e.preventDefault();

        const form = $('#form-crear-equipo')[0]; // obtener DOM nativo

        if (!form.checkValidity()) {
            form.reportValidity(); // muestra mensajes de error nativos
            return; // salir, no seguir
        }

        const nombre = $('#create-name').val();
        const crest = $('#create-crest').val();
        const fundado = $('#create-founded').val();
        const estadio = $('#create-venue').val();
        const entrenador = $('#create-coach').val();


        $.ajax({
            url: '/team/create/',  // Aquí va el POST
            method: 'POST', contentType: 'application/json', headers: {
                'X-CSRFToken': getCookie('csrftoken')
            }, data: JSON.stringify({
                name: nombre, crest: crest, founded: fundado, venue: estadio, coach: entrenador
            }), success: function (data) {
                loadTeams()
                $('#modal-overlay').addClass('hidden');
                $('#create-modal').addClass('hidden');
            }, error: function (xhr, status, error) {
                console.error('Error al crear equipo:', error);
                alert('Error al crear el equipo');
            }
        });
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
            <td>${equipo.coach?.name || equipo.coach || 'Desconocido'}</td>
            <td>
                <a href="/teams/${equipo.id}/" title="View details">
                    More
                </a>
            </td>
        </tr>`);

        $tr.on('click', function () {
            $(this).addClass('equipo-seleccionado');

            const userId = document.body.dataset.userId;

            // Prevenir conflicto con clic en enlace
            if ($(event.target).is('a')) return;

            if (equipo["creador_id"] == userId) {
                teamId = equipo.id;
                showEditModal(equipo);
            } else {
                mostrarModal(equipo);
            }
        });
        $ul.append($tr);
    });
}


function mostrarModal(equipo) {
    const userId = document.body.dataset.userId;
    // O si usaste window.USER_ID
    $('#modal-nombre').text(equipo.name || "Desconocido");
    $('#modal-fundado').text(equipo.founded || 'Desconocido');
    $('#modal-estadio').text(equipo.venue || 'Desconocido');
    $('#modal-entrenador').text(equipo.coach?.name || 'Desconocido');
    $('#modal-tla').text(equipo.tla || 'Desconocido');
    $('#modal-web').attr('href', equipo.website || 'Desconocido');
    $('#modal-web').text(equipo.website || 'Desconocido');


    $('#modal-overlay').removeClass('hidden')
    $('#visualize-modal').removeClass('hidden')
}

function showEditModal(equipo) {
    $('#modal-nombre-input').val(equipo.name || "");
    $('#modal-fundado-input').val(equipo.founded || "");
    $('#modal-estadio-input').val(equipo.venue || "");
    $('#modal-crest-input').val(equipo.crest || "");
    $('#modal-coach-input').val(equipo.coach || "");

    // Guardar ID del equipo actual para usarlo luego al guardar
    $('#form-editar-equipo').data('equipo-id', equipo.id);
    $('#modal-overlay').removeClass('hidden')
    $('#edit-modal').removeClass('hidden')
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function loadTeams() {
    $.ajax({
        url: 'api/teams', // Cambia por tu URL real o endpoint local
        method: 'GET', success: function (response) {
            $('#mensaje-error').hide();
            equipos = response;
            renderEquipos(equipos)
        }, error: function (xhr, status, error) {
            $('#mensaje-error').show();
            console.error('Error al recuperar datos:', error);
        }
    });
}
