$(document).ready(function () {
    cargarPartidos();
});

function cargarPartidos() {
    $.ajax({
        url: 'api/match/',  // Asegúrate de que esta URL coincide con tu ruta Django
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

    // Ordenar partidos por fecha descendente (más reciente primero)
    partidos.sort((a, b) => new Date(b.utcDate) - new Date(a.utcDate));

    partidos.forEach(partido => {
        const fecha = new Date(partido.utcDate).toLocaleString('es-ES');
        const equipoLocal = partido.homeTeam.name;
        const equipoVisitante = partido.awayTeam.name;
        const resultado = partido.score.fullTime.home + " - " + partido.score.fullTime.away;
        const competicion = partido.competition.name;
        const escudoLocal = partido.homeTeam.crest;
        const escudoVisitante = partido.awayTeam.crest;

        const $fila = $(`
            <tr>
                <td>${fecha}</td>
                <td class="nombre-escudo"><span>${equipoLocal}</span><img src="${escudoLocal}" alt="Escudo ${equipoLocal}"></td>
                <td>${resultado}</td>
                <td class="nombre-escudo"><img src="${escudoVisitante}" alt="Escudo ${equipoVisitante}"><span>${equipoVisitante}</span></td>
                <td>${competicion}</td>
            </tr>
        `);

        $tabla.append($fila);
    });
}


