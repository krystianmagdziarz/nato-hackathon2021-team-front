import AddDanger from "../danger/addDanger";
import AddCasualty from "../casualties/addCasualty";
import React, {useState} from 'react';
import {Select} from 'antd';
import LaunchNuclearAttack from "../nuclear/nuclear";

const selectItems = [
    'Danger',
    'Casualty',
    'Nuclear attack',
]

export default function AddObjectPanel() {
    const [selectedInputType, setSelectedInputType] = useState(selectItems[0]);

    const renderPanel = () => {
        if (selectedInputType === 'Danger') return <AddDanger/>;
        else if (selectedInputType === 'Casualty') return <AddCasualty/>;
        else if(selectedInputType === 'Nuclear attack') return <LaunchNuclearAttack />;
        else return null;
    }

    return (
        <div style={{display: 'flex', flexDirection: 'column', width: '100%'}}>
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
    );
}