const getPolygon = (coordinates) => ({
    "type": "Polygon",
    "coordinates": [coordinates],
    "style": gridStyle,
});

export const grid = (height, width, granulation) => {
    const result = [];
    const hg = height / granulation;
    const wg = width / granulation;

    for (let i = 0; i < granulation; i++) {
        for (let j = 0; j < granulation; j++) {
            const polygon = getPolygon([
                [j*wg, i*hg],
                [j*wg + wg, i*hg],
                [j*wg + wg, i*hg + hg],
                [j*wg, i*hg + hg],
                [j*wg, i*hg]
            ])
            result.push({
                data: polygon,
                style: polygon.style,
            });
        }
    }
    return result;
}

export const gridStyle = {
    color: 'blue',
    stroke: true,
    weight: 0.1,
    fill: true,
    fillColor: 'transparent',
}

const getGridLine = (coordinates) => ({
    "type": "LineString",
    "coordinates": coordinates,
    "style": {
        //all SVG styles allowed
        "fill": "red",
        "stroke-width": "3",
        "fill-opacity": 0.6
    },
})