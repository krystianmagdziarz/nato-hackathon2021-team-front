import './App.css';
import React, {useEffect, useState, useMemo} from 'react';
import Leaflet from "./components/leaflet/leaflet";
import {DataContext} from "./dataContext";
import MapPanel from "./components/panels/mapPanel/mapPanel";
import useGeoJson from "./hooks/useGeoJson";
import {observer} from "mobx-react-lite";
import {hospitalsStore} from "./store/hospitalsStore";
import {dangersStore} from "./store/dangerStore";
import {getDanger} from "./utils/geojson/danger";
import {height, width} from "./mapConfig";
import {casualtiesStore} from "./store/casualtiesStore";
import {Card, Col, Layout, Row} from "antd";
import styles from './App.module.scss';
import {Line} from "@ant-design/charts";
import PatientChart from "./components/charts/patientChart";
import nato from './assets/nato.svg';
import cpi from './assets/cpi.png';

const {Header, Content} = Layout;

const App = observer(() => {
    const [clickPoint, setClickPoint] = useState({
        visible: false,
        posX: 0,
        posY: 0,
    });
    const [nuclearAttack, setNuclearAttack] = useState(false);
    const [simulation, setSimulation] = useState(true);

    const {hospitals, fetchHospitals} = hospitalsStore;
    const {dangers, fetchDangers} = dangersStore;
    const {casualties, addedCasualties, fetchCasualties} = casualtiesStore;

    useEffect(() => {
        if (hospitals.length === 0) {
            fetchHospitals();
        }
        if (dangers.length === 0) {
            fetchDangers();
        }
        if (casualties.length === 0) {
            fetchCasualties();
        }
    }, []);

    useEffect(() => {
        fetchCasualties();
    }, [dangers.length])


    const dangerData = useMemo(() => dangers.map(({x, y, danger}) => getDanger(x, y, danger)), [dangers.length]);
    const rawCasualties = useMemo(() => JSON.parse(JSON.stringify(addedCasualties)), [addedCasualties]);
    const rawHospitals = useMemo(() => JSON.parse(JSON.stringify(hospitals)), [hospitals]);

    const {geoJson} = useGeoJson(rawHospitals, rawCasualties, simulation);


    return (
        <div className="App">
            <Layout>
                <DataContext.Provider value={{
                    clickPoint,
                    setClickPoint,
                    nuclearAttack,
                    setNuclearAttack,
                    simulation,
                    setSimulation,
                }}>
                    <>
                        <Header style={{height: '70px', display: 'flex', flexDirection: 'row', alignItems: 'center', justifyContent: 'center', background: 'white'}}>
                            <img src={nato} style={{width: '50px', height: '50px', marginRight: '96px'}}/>
                            <div style={{color: 'black', fontSize: '22px', letterSpacing: '0.4px'}}>Military Rescue Supervisor Panel</div>
                            <img src={cpi} style={{width: '60px', height: '60px', marginLeft: '96px'}}/>
                        </Header>
                        <Content>
                            <div style={{display: 'flex', flexDirection: 'row'}}>

                                <div style={{
                                    display: 'flex', flexDirection: 'column', marginTop: '32px', marginLeft: '32px'
                                }}>
                                    <Leaflet height={height} width={width} geoJsonData={geoJson}
                                             dangerData={dangerData}/>
                                    <div style={{minHeight: "16vh", marginTop: '0px', marginBottom: '20px'}}>
                                        <Card title="Map Legend" style={{height: '100%'}}>
                                            <div className={styles.legendContent}>
                                                <Row gutter={[8, 12]} style={{width: '100%'}}>
                                                    <Col span={6}>Hospitals
                                                        <span className={`${styles.legendItem} hospital-dot`}/>
                                                        <span className={`${styles.legendItem} hospital-dot2`}/>
                                                        <span className={`${styles.legendItem} hospital-dot3`}/>
                                                    </Col>

                                                    <Col span={6}>Casualty<span className={`${styles.legendItem} casualty-dot`}/></Col>
                                                    <Col span={6}>Casualty (Buddy care)<span className={`${styles.legendItem} casualty-dot2`}/></Col>
                                                    <Col span={6}>Danger <span
                                                        className={`${styles.legendItem} gradient-dot`}/></Col>
                                                    <Col span={6}>Route (danger) <span
                                                        className={`${styles.legendItem} danger-route`}/></Col>
                                                    <Col span={6}>Route (safe) <span
                                                        className={`${styles.legendItem} safe-route`}/></Col>

                                                </Row>
                                            </div>
                                        </Card>
                                    </div>
                                </div>
                                <div style={{
                                    display: 'flex', flexDirection: 'column', marginRight: '32px',
                                    marginLeft: '32px'
                                }}>
                                    <MapPanel clickPoint={clickPoint}
                                              setClickPoint={setClickPoint}
                                              style={{
                                                  width: '100%',
                                                  height: '74vh',
                                                  marginBottom: '24px',
                                                  marginTop: '32px',
                                                  overflow: 'auto',
                                              }}
                                    />
                                    <Card style={{height: '16vh'}}>
                                        <PatientChart/>
                                    </Card>
                                </div>
                            </div>
                        </Content>
                    </>
                </DataContext.Provider>
            </Layout>
        </div>
    );
})

export default App;
