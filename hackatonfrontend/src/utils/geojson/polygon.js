import {granulation, height, width} from "../../mapConfig";

export const getHospitalPolygon = (posX, posY) => {
    const hg = height / granulation;
    const wg = width / granulation;

    const start = [posX - wg/4, posY + hg / 4];

    return (
        {
            "type": "Polygon",
            "coordinates": [[
                start,
                [start[0] + wg/2, start[1]],
                [start[0] + wg/2, posY - hg/4],
                [start[0], posY - hg/4],
                start
            ]],
        }
    )
}