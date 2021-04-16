import React from "react"
import {action, makeAutoObservable, runInAction} from "mobx"
import {fetchPatch} from "../utils/api/api";
import {coordinatesToGridPosition} from "../utils/map/coordinatesForPosition";


const fetchTargetHospital = async (id) => {
    try {
        const response = await fetch(`http://localhost:8000/patient/${id}/target-hospital/`);
        if (response.status === 200) {
            const itemData = await response.json();
            return {id, data: itemData};
        } else if (response.status === 205) {
            return {id, data: {ai_detection: 'Buddy care'}};
        }
        return ({id, data: null})
    } catch (e) {
        return ({id, data: null})
    }
}

class Casualties {
    casualties = [];

    constructor() {
        makeAutoObservable(this, {
            fetchCasualties: action.bound,
            updateCasualtyPosition: action.bound,
        });
    }

    get addedCasualties() {
        return this.casualties.filter((casualty) => casualty.grid_x !== null && casualty.grid_y !== null);
    }

    async fetchCasualties() {
        const response = await fetch('http://localhost:8000/patient/');
        const data = await response.json();

        const targetHospitalData = await Promise.all(
            data.map(async ({id}) => await fetchTargetHospital(id))
        );

        const dataWithTargetHospitals = data.map((item) => {
            const targetHospital = targetHospitalData.find(({id}) => id === item.id).data;
            return (
                {
                    ...item,
                    targetHospital,
                }
            );
        });

        runInAction(() => {
            this.casualties = dataWithTargetHospitals;
        })
    };

    async updateCasualtyPosition(id, posX, posY) {
        const position = coordinatesToGridPosition(posX, posY);
        const data = {
            id,
            grid_x: position[0],
            grid_y: position[1],
        }
        const response = await fetchPatch(`http://localhost:8000/patient/${id}/`, data);
        const targetHospitalData = await fetchTargetHospital(id);

        runInAction(() => {
            this.casualties = this.casualties.map((v) => {
                return v.id !== id ? v
                    : {...v, grid_x: data.grid_x, grid_y: data.grid_y, targetHospital: targetHospitalData.data};
            })
        })
    }

}

export const casualtiesStore = new Casualties();