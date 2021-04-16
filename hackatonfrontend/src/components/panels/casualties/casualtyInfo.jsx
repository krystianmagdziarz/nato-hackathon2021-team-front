import React, {useState, useEffect} from 'react';
import {observer} from "mobx-react-lite";
import {casualtiesStore} from "../../../store/casualtiesStore";
import {Card, Col, Row, Select, Statistic} from "antd";
import styles from './casualtyInfo.module.scss';

const CasualtyInfo = observer(() => {
    const {addedCasualties} = casualtiesStore;
    const [selectedCasualty, setSelectedCasualty] = useState();

    const selectedItem = addedCasualties.find(({id}) => selectedCasualty === id);
    const rawData = selectedItem ? JSON.parse(JSON.stringify(selectedItem)) : null;

    useEffect(() => {
        if(addedCasualties.length > 0 && !selectedCasualty){
            setSelectedCasualty(addedCasualties[0].id)
        }
    }, [addedCasualties]);

    return (
        <div style={{display: 'flex', flexDirection: 'column'}}>
            <Select style={{width: '300px'}} value={selectedCasualty} onChange={setSelectedCasualty}>
                {
                    addedCasualties.map((v, index) => (
                        <Select.Option key={v.id} value={v.id}>{`Casualty ${index}`}</Select.Option>
                    ))
                }
            </Select>
            <div style={{marginTop: '24px'}}>
                {
                    rawData && (
                        <>
                            <div style={{display: 'flex', flexDirection: 'row', marginBottom: '12px'}}>
                                <Card style={{width: '50%', marginRight: '24px', border: '1px solid blue'}}>
                                    <Statistic title={'AI Treatment Detection'} value={rawData.targetHospital.ai_detection}/>
                                </Card>
                                {
                                    rawData.targetHospital.best_hospital && (
                                        <Card style={{color: 'red', width: '50%'}}>
                                            <Statistic title={'Target hospital'}
                                                       value={rawData.targetHospital.best_hospital.name}/>
                                        </Card>
                                    )
                                }
                            </div>
                            <Card style={{width: '80%', marginBottom: '24px'}}>
                                <Statistic title={'Notes'} value={rawData.notes}/>
                            </Card>
                            <Row justify="space-between" gutter={[8, 12]}>
                                {
                                    Object.entries(rawData)
                                        .filter((item) => item[1] !== null)
                                        .filter((item) => item[0] !== 'id')
                                        .filter((item) => item[1] !== Object(item[1]))
                                        .filter((item) => item[0] !== 'selected_hospital')
                                        .filter((item) => item[0] !== 'notes')
                                        .map(item => {
                                            return (
                                                <Col span={6}>
                                                    <Card className={styles.card}>
                                                        <Statistic title={item[0].replaceAll('_', ' ')}
                                                                   value={item[1]}/>
                                                    </Card>
                                                </Col>
                                            );
                                        })
                                }
                            </Row>
                        </>
                    )
                }
            </div>
        </div>
    );
})

export default CasualtyInfo;