let todosLosPartidos = [];

$(document).ready(function () {
    cargarPartidos();
    $('#selector-jornada').on('change', function () {
        const jornadaSeleccionada = parseInt($(this).val());
        mostrarPartidosDeJornada(jornadaSeleccionada);
    });
});

function cargarPartidos() {
    $.ajax({
        url: 'api/match/',
        method: 'GET',
        success: function (partidos) {
            $('#mensaje-error').hide();
            todosLosPartidos = partidos;

            const jornadas = obtenerJornadas(partidos);
            poblarSelectorJornadas(jornadas);

            const jornadaPorDefecto = Math.max(...jornadas);
            $('#selector-jornada').val(jornadaPorDefecto);
            mostrarPartidosDeJornada(jornadaPorDefecto);
        },
        error: function () {
            $('#mensaje-error').show();
        }
    });
}

function obtenerJornadas(partidos) {
    const jornadasSet = new Set();
    partidos.forEach(p => {
        if (p.matchday != null) {
            jornadasSet.add(p.matchday);
        }
    });
    return Array.from(jornadasSet).sort((a, b) => a - b);
}

function poblarSelectorJornadas(jornadas) {
    const $selector = $('#selector-jornada');
    $selector.empty();
    jornadas.forEach(jornada => {
        $selector.append(`<option value="${jornada}">Matchday ${jornada}</option>`);
    });
}

function mostrarPartidosDeJornada(jornada) {
    const filtrados = todosLosPartidos.filter(p => p.matchday === jornada);
    renderizarPartidos(filtrados);
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

    $('#cerrar-popup').on('click', function () {
        $('#popup-partido').fadeOut();
    });

    $('#popup-partido').on('click', function (e) {
        if (e.target === this) {
            $(this).fadeOut();
        }
    });
}
