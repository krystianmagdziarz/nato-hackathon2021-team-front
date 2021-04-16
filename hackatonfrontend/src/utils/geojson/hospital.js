import {getHospitalPolygon} from "./polygon";

export const getHospital = (posX, posY, name, children) => {
    let color;
    if(name === 'Civilian Hospital'){
        color = 'blue';
    }else if(name === 'MF - B - 1'){
        color = 'orange';
    }else{
        color = 'green';
    }


    return ({
        data: getHospitalPolygon(posX, posY),
        style: {color: color, weight: 3},
        children,
    });
}