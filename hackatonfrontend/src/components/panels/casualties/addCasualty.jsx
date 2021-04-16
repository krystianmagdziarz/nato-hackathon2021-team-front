import React, {useContext, useEffect, useState} from 'react';
import {Button, Select} from 'antd';
import {DataContext} from "../../../dataContext";
import {observer} from "mobx-react-lite";
import {casualtiesStore} from "../../../store/casualtiesStore";

const AddCasualty = observer(() => {
    const {casualties, updateCasualtyPosition} = casualtiesStore;
    const {clickPoint} = useContext(DataContext);
    const [casualty, setCasualty] = useState();

    // console.log(JSON.parse(JSON.stringify(casualties)));

    const {posX, posY} = clickPoint;

    const renderedCasualty = !casualty ? null : (
        <div style={{marginTop: '24px'}}>
            {
                Object.entries(casualties.find(({id}) => id === casualty)).map(item =>
                    (
                        <div key={item[0]} style={{textAlign: 'start'}}>
                            {`${item[0]}: ${item[1]}`}
                        </div>
                    ))
            }
        </div>
    );

    const renderTargetHospital = () => {
        // render check
        if (!casualty) return null;
        const item = casualties.find(({id}) => id === casualty);
        if (!item) return null;

        // logic
        const targetHospital = {...item.targetHospital};
        const aiDetection = targetHospital.ai_detection;
        const bestHospitalName = targetHospital.best_hospital && targetHospital.best_hospital.name;

        let content;

        if (aiDetection && bestHospitalName) {
            content = (
                <>
                    <div>
                        Treatment: {aiDetection} !
                    </div>
                    <div>
                        Hospital: {bestHospitalName}
                    </div>
                </>
            );
        } else if (aiDetection) {
            content = <div>Treatment: Buddy Care</div>
        } else {
            content = null;
        }

        return content && (
            <div style={{marginTop: '32px', color: 'red', textAlign: 'start'}}>
                {content}
            </div>
        )
    }

    return (
        <>
            <Select style={{width: '300px'}} value={casualty} onChange={setCasualty}>
                {casualties.map((casualty, index) => (
                    <Select.Option key={casualty.id} value={casualty.id}>{`Casualty ${index}`}</Select.Option>
                ))}
            </Select>
            {
                renderTargetHospital()
            }
            {
                renderedCasualty
            }
            <Button
                disabled={!casualty}
                onClick={async () => {
                    updateCasualtyPosition(casualty, posX, posY);
                }}
                style={{marginTop: '32px', width: '60px', alignSelf: 'flex-end'}}>
                Add
            </Button>
        </>
    );
});

export default AddCasualty;
