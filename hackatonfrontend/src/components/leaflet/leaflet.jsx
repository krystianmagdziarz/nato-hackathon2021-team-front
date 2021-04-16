import React, {useContext, useMemo} from "react";
import L from "leaflet";
import {GeoJSON, ImageOverlay, LayerGroup, Map, Tooltip} from "react-leaflet";
import "leaflet/dist/leaflet.css";
import map from '../../assets/map.png';
import {v4 as uuidv4} from 'uuid';
import {DataContext} from "../../dataContext";
import {getDot} from "../../utils/geojson/dot";
import HeatmapLayer from 'react-leaflet-heatmap-layer';
import {getHospitalPolygon} from "../../utils/geojson/polygon";

export default function Leaflet({height, width, geoJsonData, dangerData}) {
    const {clickPoint, setClickPoint} = useContext(DataContext);

    const bounds = [
        [height, 0],
        [0, width],
    ]

    const dangerLayer = useMemo(() => {
        return (
            dangerData.map(({danger, coordinates}) => (
                <HeatmapLayer
                    key={coordinates}
                    points={coordinates}
                    longitudeExtractor={m => m[0]}
                    latitudeExtractor={m => m[1]}
                    intensityExtractor={() => danger * 5}
                />
            ))
        );
    }, [dangerData])

    return (

        <Map
            crs={L.CRS.Simple}
            bounds={bounds}
            maxBound={bounds}
            maxZoom={4.9}
            attributionControl={true}
            draggable={false}
            doubleClickZoom={false}
        >
            <LayerGroup>
                {
                    dangerLayer
                }
                <ImageOverlay
                    url={map}
                    bounds={[
                        [height, 0],
                        [0, width],
                    ]}
                />
                {geoJsonData.map(({data, style, children}) => (
                    <GeoJSON
                        key={uuidv4()}
                        data={data}
                        style={() => data.style || style}
                        onEachFeature={(feature, layer) => {
                            layer.on({
                                click: (e) => {
                                    setClickPoint({
                                        ...clickPoint,
                                        visible: true,
                                        posX: e.latlng.lng,
                                        posY: e.latlng.lat,
                                    })
                                }
                            })
                        }}
                    >
                        {children}
                    </GeoJSON>
                ))}
                {
                    clickPoint.visible && (
                        <GeoJSON
                            key={uuidv4()}
                            data={getDot(clickPoint.posX, clickPoint.posY)}
                            style={{color: 'yellow', weight: '10'}}
                        />
                    )
                }

            </LayerGroup>
        </Map>
    );
}