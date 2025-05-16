$(document).ready(function () {
    cargarPartidos();
});

function cargarPartidos() {
    $.ajax({
        url: 'api/matches/',  // Asegúrate de que esta URL coincide con tu ruta Django
        method: 'GET',
        success: function (partidos) {
            $('#mensaje-error').hide();
            renderizarPartidos(partidos);
        },
        error: function () {
            $('#mensaje-error').show();
        }
    });
}

function renderizarPartidos(partidos) {
    const $tabla = $('#tabla-matches tbody');
    $tabla.empty();

    partidos.forEach(partido => {
        const fecha = new Date(partido.utcDate).toLocaleString('es-ES');
        const equipoLocal = partido.homeTeam.name;
        const equipoVisitante = partido.awayTeam.name;
        const resultado = partido.score.fullTime.home + " - " + partido.score.fullTime.away;
        const competicion = partido.competition.name;

        const $fila = $(`
            <tr>
                <td>${fecha}</td>
                <td>${equipoLocal}</td>
                <td>${resultado}</td>
                <td>${equipoVisitante}</td>
                <td>${competicion}</td>
            </tr>
        `);

        $tabla.append($fila);
    });
}
