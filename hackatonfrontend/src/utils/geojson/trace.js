import {granulation} from "../../mapConfig";
import {getLine} from "./line";

export const getTrace = (height, width, nodes, color) => {
    const coordinates = nodes.map((node) => {
        const horizontalPos = node.slice(0, 1).charCodeAt(0) - 65;
        const verticalPos = granulation - (parseInt(node.slice(1, node.length), 10));
        const wg = width / granulation;
        const hg = height / granulation;
        return [horizontalPos * wg + wg / 2, verticalPos * hg + hg / 2];
    });

    return ({
        data: getLine(coordinates),
        style: {color: color ? color : '#FFA500', lineJoin: 'bevel', weight: 5, dashArray: "20 20"}
    })
}



