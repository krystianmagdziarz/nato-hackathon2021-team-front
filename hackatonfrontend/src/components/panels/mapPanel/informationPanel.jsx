import React, {useState} from 'react';
import {Select} from 'antd';
import Hospitals from "../hospitals/hospitals";
import CasualtyInfo from "../casualties/casualtyInfo";

const selectItems = [
    'Hospitals',
    'Patients',
]

export default function InformationPanel() {
    const [selectedInputType, setSelectedInputType] = useState(selectItems[0]);


    const renderPanel = () => {
        if (selectedInputType === 'Hospitals') return <Hospitals/>;
        if (selectedInputType === 'Patients') return <CasualtyInfo/>;
        else return null;
    }

    return (
        <div style={{display: 'flex', flexDirection: 'column', justifyContent: 'flex-start'}}>
            <Select style={{width: '300px'}} value={selectedInputType} onChange={setSelectedInputType}>
                {
                    selectItems.map((v) => (
                        <Select.Option key={v} value={v}>{v}</Select.Option>
                    ))
                }
            </Select>
            <div style={{display: 'flex', flexDirection: 'column', marginTop: '24px', alignItems: 'start'}}>
                {renderPanel()}
            </div>
        </div>
    )
}