import {Card, Col, Row, Statistic} from "antd";
import React from "react";

export default function HospitalInfo({hospital, hospitals}){
    if (!hospital) return null;

    return (
        <div style={{display: 'flex', flexDirection: 'row', flexWrap: 'wrap', paddingRight: '64px'}}>
            <Row justify="space-between" gutter={[8, 12]}>
                {
                    Object.entries(hospitals.find(({id}) => id === hospital)).map(item => {
                        return (
                            <Col span={8}>
                                <Card style={{overflow: 'hidden', textOverflow: 'ellipsis', textTransform: 'capitalize', height: '128px'}}>
                                    <Statistic title={item[0].replaceAll('_', ' ')} value={item[1]}/>
                                </Card>
                            </Col>
                        );
                    })
                }
            </Row>
        </div>
    );
}