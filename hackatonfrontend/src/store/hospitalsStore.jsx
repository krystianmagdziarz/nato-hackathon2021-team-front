import React from "react"
import {makeAutoObservable, computed, runInAction, action} from "mobx"
import {fetchPatch} from "../utils/api/api";

class Hospitals {
    hospitals = [];

    constructor() {
        makeAutoObservable(this, {
            fetchHospitals: action.bound,
            moveHospital4AfterAttack: action.bound,
        });
    }

    async fetchHospitals() {
        const response = await fetch('http://localhost:8000/hospital/');
        const data = await response.json();
        runInAction(() => {
            this.hospitals = data;
        })
    };

    async moveHospital4AfterAttack() {
        const id = 4;
        const response = await fetchPatch(`http://localhost:8000/hospital/${id}/`, {
            grid_y: '11',
        });


        runInAction(() => {
            this.hospitals = this.hospitals.map((v) =>
                v.id !== id
                    ? v
                    : {...v, grid_y: '8'});
        })

    }

}

export const hospitalsStore = new Hospitals();