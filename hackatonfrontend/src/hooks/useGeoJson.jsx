import {useMemo, useState, useEffect} from 'react';
import {grid} from "../utils/geojson/grid";
import {getTrace} from "../utils/geojson/trace";
import {granulation, height, width} from "../mapConfig";
import {getCoordinatesForGridPosition} from "../utils/map/coordinatesForPosition";
import {getHospital} from "../utils/geojson/hospital";
import {getCasualty} from "../utils/geojson/casualty";
import {Tooltip} from "react-leaflet";

export default function useGeoJson(hospitals, casualties, simulation) {
    const [timer, setTimer] = useState(0);

    useEffect(() => {
        setTimeout(() => {
            setTimer(time => time + 1);
        }, 2000);
    }, [timer]);

    const hospitalGeoJson = useMemo(() =>
        hospitals.map((hospital) => {
            return {name: hospital.name, coordinates: getCoordinatesForGridPosition(hospital.grid_x, hospital.grid_y)};
        }).map(({name, coordinates}) => {
                const children = <Tooltip permanent>{name}</Tooltip>
                return getHospital(coordinates[0], coordinates[1], name, children)
            }
        ), [hospitals]
    );

    const casualtiesGeoJson = useMemo(() => casualties
        .map((casualty) => {
            const buddyCare = casualty.targetHospital && casualty.targetHospital.ai_detection === 'Buddy care';

            return {
                pos: getCoordinatesForGridPosition(casualty.grid_x, casualty.grid_y),
                isBuddy: buddyCare,
            }
        })
        .map(({ pos, isBuddy }) => getCasualty(pos[0], pos[1], isBuddy)), [casualties])


    const casualtiesPathData = casualties.filter((item) => item.targetHospital && !!item.targetHospital.best_hospital).map((item) => {
        const {targetHospital} = item;
        return (
            {
                bestHospital: targetHospital.best_hospital,
                shortestPath: targetHospital.shortest_path,
                bestPath: targetHospital.best_path,
            }
        );
    });

    const reducedPaths = simulation ? casualtiesPathData.map(({shortestPath, bestPath}) => {
        const shiftLength = bestPath.length - (bestPath.length - timer % bestPath.length);
        const reducedBestPath = JSON.parse(JSON.stringify(bestPath));
        for(let i=0; i < shiftLength; i++){
            reducedBestPath.shift();
        }

        return {
            shortestPath: shortestPath,
            bestPath: reducedBestPath,
        }
    }) : casualtiesPathData;

    const casualtiesPathGeoJson = reducedPaths
        .reduce((acc, curr) => [...acc, getTrace(height, width, curr.shortestPath, 'red'), getTrace(height, width, curr.bestPath, 'orange')], [])

    const geoJson = [
        ...grid(height, width, granulation),
        ...hospitalGeoJson,
        ...casualtiesGeoJson,
        ...casualtiesPathGeoJson
    ]

    return {geoJson};
}