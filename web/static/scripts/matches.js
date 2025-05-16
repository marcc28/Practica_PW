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
            <tr style="cursor:pointer;">
                <td>${fecha}</td>
                <td class="nombre-escudo"><span>${equipoLocal}</span><img src="${escudoLocal}" alt="Escudo ${equipoLocal}"></td>
                <td>${resultado}</td>
                <td class="nombre-escudo"><img src="${escudoVisitante}" alt="Escudo ${equipoVisitante}"><span>${equipoVisitante}</span></td>
                <td>${competicion}</td>
            </tr>
        `);

        // Evento click para mostrar popup
        $fila.on('click', function () {
            const detalleHtml = `
                <div class="popup-header">
                    <div class="competicion">${competicion}</div>
                    <div class="fecha">${fecha}</div>
                </div>
                <div class="popup-marcador">
                    <div class="equipo local">
                        <img src="${escudoLocal}" alt="Escudo ${equipoLocal}">
                        <div class="nombre">${equipoLocal}</div>
                    </div>
                    <div class="resultado">${resultado}</div>
                    <div class="equipo visitante">
                        <img src="${escudoVisitante}" alt="Escudo ${equipoVisitante}">
                        <div class="nombre">${equipoVisitante}</div>
                    </div>
                </div>
            `;

            $('#contenido-partido').html(detalleHtml);
            $('#popup-partido').fadeIn();
        });

        $tabla.append($fila);
    });

    // Cerrar popup al clicar en la X
    $('#cerrar-popup').on('click', function () {
        $('#popup-partido').fadeOut();
    });

    // También cerrar popup si se hace click fuera del contenido
    $('#popup-partido').on('click', function (e) {
        if (e.target === this) {
            $(this).fadeOut();
        }
    });
}
