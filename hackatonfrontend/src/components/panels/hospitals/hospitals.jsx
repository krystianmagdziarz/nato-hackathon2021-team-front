import React, {useEffect, useState} from "react";
import {Card, Col, Row, Select, Statistic, Tabs, Tag} from 'antd';
import {observer} from "mobx-react-lite";
import {hospitalsStore} from "../../../store/hospitalsStore";
import HospitalInfo from "./hospitalInfo";
import DescInfo from "./descInfo";

const Hospitals = observer(() => {
        const {hospitals, fetchHospitals, getHospitals} = hospitalsStore;
        const [hospital, setHospital] = useState();

        const [hospitalCapabilities, setHospitalCapabilities] = useState();

        useEffect(() => {
            if(!hospital && hospitals.length > 0){
                setHospital(hospitals[0].id)
            }
        }, [hospitals]);

        useEffect(() => {
            if (hospitals.length === 0) {
                fetchHospitals();
            }
        }, []);

        useEffect(() => {
            if (hospital) {
                const asyncFetch = async () => {
                    const response = await fetch(`http://localhost:8000/hospital-capabilities/${hospital}/`)
                    const data = await response.json();
                    setHospitalCapabilities(data);
                }
                asyncFetch();
            }
        }, [hospital]);

        const modes = [
            {
                title: 'Description',
                content: <HospitalInfo hospital={hospital} hospitals={hospitals}/>,
            },
            {
                title: 'Possibilities',
                content: <DescInfo hospitalCapabilities={hospitalCapabilities} />,
            }
        ]
        const [mode, setMode] = useState(modes[0].title);


        return (
            <>
                <div style={{display: 'flex', flexDirection: 'row'}}>
                    <Select value={hospital} onChange={setHospital} style={{width: '300px'}}>
                        {
                            hospitals.map((item) => (
                                <Select.Option key={item.id} value={item.id}>{item.name}</Select.Option>
                            ))
                        }
                    </Select>
                    {
                        hospital && (
                            <Select style={{marginLeft: '32px', width: '250px'}} value={mode} onChange={setMode}>
                                {
                                    modes.map((item) => (
                                        <Select.Option key={item.title} value={item.title}
                                                       onChange={setMode}>{item.title}</Select.Option>
                                    ))
                                }
                            </Select>
                        )
                    }

                </div>

                <div style={{marginTop: '24px'}}>
                    {
                        modes.find(({title}) => title === mode).content
                    }
                </div>
            </>
        )
    }
)

export default Hospitals;
