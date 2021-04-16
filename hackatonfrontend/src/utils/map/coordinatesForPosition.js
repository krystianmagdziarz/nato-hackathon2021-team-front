import {granulation, height, width} from "../../mapConfig";

const wg = width / granulation;
const hg = height / granulation;

export function getCoordinatesForGridPosition(posX, posY) {
    const horizontalPosMod = posX.charCodeAt(0) - 65;
    const verticalPosMod = granulation - (parseInt(posY, 10));
    return [horizontalPosMod * wg + wg / 2, verticalPosMod * hg + hg / 2];
}

export function coordinatesToGridPosition(posX, posY) {
    const gridPosX = String.fromCharCode(Math.floor(posX / wg) + 65);
    const gridPosY = granulation - Math.floor(posY / hg);
    return [gridPosX, `${gridPosY}`]
}