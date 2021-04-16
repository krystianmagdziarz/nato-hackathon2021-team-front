import React, {useContext} from 'react';
import styles from './nuclear.module.scss';
import {DataContext} from "../../../dataContext";
import nuclear from '../../../assets/nuclear.svg';
import {dangersStore} from "../../../store/dangerStore";

export default function LaunchNuclearAttack() {
    const {nuclearAttack, setNuclearAttack} = useContext(DataContext);
    const { launchNuclearAttack } = dangersStore;

    return (
        <div style={{display: 'flex', flexDirection: 'column', width: '100%', justifyContent: 'center', alignItems: 'center', paddingTop: '64px'}}>
            {
                nuclearAttack && (
                    <>
                        <div style={{fontSize: '40px', marginBottom: '32px', color: 'red'}}>Nuclear Threat!</div>
                        <img src={nuclear} style={{height: '300px', width: '300px'}}/>
                    </>
                )
            }

            {
                !nuclearAttack && (
                    <a className={styles.button2} onClick={() => {
                        setTimeout(() => {
                            launchNuclearAttack();
                            setNuclearAttack(true);
                        }, 200);
                    }}/>
                )
            }

        </div>
    );
}