import React, {useContext, useState} from 'react';
import {Button, Slider} from 'antd';
import {DataContext} from "../../../dataContext";
import {dangersStore} from "../../../store/dangerStore";

export default function AddDanger() {
    const {clickPoint, setClickPoint, dangers, setDangers} = useContext(DataContext);
    const [danger, setDanger] = useState(30);

    const {posX, posY} = clickPoint;

    return (
        <>
            <Slider value={danger} onChange={setDanger} on style={{width: '300px'}}/>
            <Button
                disabled={!clickPoint.visible}
                onClick={() => {
                    dangersStore.addDanger(posX, posY, danger);
                    // setClickPoint(clickPoint => ({...clickPoint, visible: false}))
                }}
                style={{marginTop: '32px', width: '60px', alignSelf: 'flex-end'}}>
                Add
            </Button>
        </>
    );
}