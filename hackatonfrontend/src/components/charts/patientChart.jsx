import {useState, useEffect} from 'react';
import {Line} from "@ant-design/charts";
import {observer} from "mobx-react-lite";
import {casualtiesStore} from "../../store/casualtiesStore";


const PatientChart = observer(() => {
    const [data, setData] = useState([])
    const [time, setTime] = useState(0);

    const { addedCasualties } = casualtiesStore;

    useEffect(() => {
        setTimeout(() => {
            setTime(time => time + 1);
        }, 1000);
    }, [time]);

    useEffect(() => {
        const time = new Date();
        const newSet = [...data, {
            time: `${time.getHours()}:${time.getMinutes()}:${time.getSeconds()}`,
            value: addedCasualties.length
        }];
        if (newSet.length > 5) {
            newSet.shift();
        }
        setData(newSet)
    }, [time]);

    return (
        <Line data={data} height={150} xField={'time'} yField={'value'}/>
    );
})

export default PatientChart;