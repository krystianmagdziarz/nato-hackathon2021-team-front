import {getDot} from "./dot";

export const getCasualty = (posX, posY, isBuddy) => ({
    data: getDot(posX, posY),
    style: {color: isBuddy ? 'green' : 'red', weight: 10}
})