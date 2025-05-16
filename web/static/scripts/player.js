let jugadores = [];
let playerId = null;
$(document).ready(function () {
    loadPlayers();

    $('#cerrar-modal').on('click', () => {
        $('#modal-overlay').addClass('hidden');
        $('#visualize-modal').addClass('hidden');
    });

    $('#close-edit-modal').on('click', () => {
        $('#modal-overlay').addClass('hidden');
        $('#edit-modal').addClass('hidden');
    });

    $('#btn-crear-jugador').on('click', () => {
        $('#modal-overlay').removeClass('hidden');
        $('#create-modal').removeClass('hidden');
    });

    $('#cerrar-crear-modal').on('click', () => {
        $('#create-modal').addClass('hidden');
        $('#modal-overlay').addClass('hidden');
    });

    $('#buscador').on('input', function () {
        const texto = $(this).val().toLowerCase();
        const filtrados = jugadores.filter(j => j.name.toLowerCase().includes(texto));
        renderJugadores(filtrados);
    });
    $('#btn-guardar-jugador').on('click', function (e) {
        e.preventDefault();

        const form = $('#form-crear-jugador')[0];
        if (!form.checkValidity()) {
            form.reportValidity();
            return;
        }

        const data = {
            name: $('#create-name').val(),
            birth_date: $('#create-age').val(),
            position: $('#create-position').val(),
            team: $('#create-team').val(),
            nationality: $('#create-nationality').val()
        };


        $.ajax({
            url: '/players/create/',
            method: 'POST',
            contentType: 'application/json',
            headers: {
                'X-CSRFToken': getCookie('csrftoken')
            },
            data: JSON.stringify(data),
            success: function () {
                loadPlayers();
                $('#create-modal').addClass('hidden');
                $('#modal-overlay').addClass('hidden');
            },
            error: function () {
                alert('Error al crear el jugador');
            }
        });
    });

    $('#form-editar-jugador').on('submit', function (e) {
        e.preventDefault();

        const datosActualizados = {
            name: $('#modal-nombre-input').val(),
            birth_date: $('#modal-edad-input').val(),
            position: $('#modal-posicion-input').val(),
            team: $('#edit-team').val(),
            nationality: $('#modal-nationality-input').val()
        };


        $.ajax({
            url: `/players/${playerId}/edit`,
            method: 'PUT',
            contentType: 'application/json',
            headers: {
                'X-CSRFToken': getCookie('csrftoken')
            },
            data: JSON.stringify(datosActualizados),
            success: function () {
                loadPlayers();
                $('#buscador').val("");
                $('#modal-overlay').addClass('hidden');
                $('#edit-modal').addClass('hidden');
            },
            error: function () {
                alert('Error al actualizar jugador');
            }
        });
    });


    $('#btn-delete-player').on('click', function (e) {
        e.preventDefault()
        $.ajax({
            url: `/players/${playerId}/delete/`,
            method: 'DELETE',
            contentType: 'application/json',
            headers: {
                'X-CSRFToken': getCookie('csrftoken')
            },
            success: function () {
                loadPlayers();
                $('#buscador').val("");
                $('#modal-overlay').addClass('hidden');
                $('#edit-modal').addClass('hidden');
            },
            error: function () {
                alert('Error al eliminar player');
            }
        });
    })
});

function renderJugadores(lista) {
    const $tbody = $('#tabla-jugadores tbody');
    $tbody.empty();

    lista.forEach(jugador => {
        const birthDate = jugador.birth_date || jugador.dateOfBirth || 'Desconocida';

        const $tr = $(`<tr>
            <td>${jugador.name}</td>
            <td>${birthDate}</td>
            <td>${jugador.position}</td>
            <td class="nombre-escudo"><span>${jugador.team || 'Desconocido'}</span><img class="escudo-equipo" src="${jugador.crest}" alt="Escudo: ${jugador.team || 'Desconocido'}"></td>
            <td>${jugador.nationality}</td>
        </tr>`);

        $tr.on('click', function () {
            const userId = document.body.dataset.userId;
            if (jugador.creator_id == userId) {
                playerId = jugador.id
                showEditModal(jugador);
            } else {
                mostrarModal(jugador);
            }
        });

        $tbody.append($tr);
    });
}

function mostrarModal(jugador) {
    const birthDate = jugador.birth_date || jugador.dateOfBirth || 'Desconocida';

    $('#modal-nombre').text(jugador.name || "Desconocido");
    $('#modal-edad').text(birthDate);
    $('#modal-posicion').text(jugador.position || 'Desconocida');
    $('#modal-equipo').text(jugador.team || 'Desconocido');
    $('#modal-overlay').removeClass('hidden');
    $('#visualize-modal').removeClass('hidden');
}

function showEditModal(jugador) {
    const birthDate = jugador.birth_date || jugador.dateOfBirth || '';

    $('#modal-nombre-input').val(jugador.name || "");
    $('#modal-edad-input').val(birthDate);
    $('#modal-posicion-input').val(jugador.position || "");
    $('#modal-nationality-input').val(jugador.nationality || "");

    //replace first with the second
    $('#modal-equipo-input').val(jugador.team || "");
    $('#edit-team').val(jugador.team_id || "")

    $('#form-editar-jugador').data('jugador-id', jugador.id);
    $('#modal-overlay').removeClass('hidden');
    $('#edit-modal').removeClass('hidden');
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

function loadPlayers() {
    $.ajax({
        url: 'api/players',
        method: 'GET',
        success: function (response) {
            $('#mensaje-error').hide();

            jugadores = response.map(j => ({
                ...j,
                birth_date: j.birth_date || j.dateOfBirth
            }));

            // Ordenar alfabéticamente por nombre, ignorando mayúsculas/minúsculas
            jugadores.sort((a, b) => a.name.toLowerCase().localeCompare(b.name.toLowerCase()));

            renderJugadores(jugadores);
        },
        error: function () {
            $('#mensaje-error').show();
        }
    });
}

