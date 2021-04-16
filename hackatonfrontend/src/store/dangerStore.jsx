import React from "react"
import {makeAutoObservable, computed, runInAction, action} from "mobx"
import {getCoordinatesForGridPosition} from "../utils/map/coordinatesForPosition";
import {coordinatesToGridPosition} from "../utils/map/coordinatesForPosition";
import {fetchPost} from "../utils/api/api";
import {hospitalsStore} from "./hospitalsStore";

const fromDto = (item) => {
    const coordinates = getCoordinatesForGridPosition(item.grid_x, item.grid_y);
    const danger = item.range;

    return ({
        x: coordinates[0],
        y: coordinates[1],
        danger,
    });
}

class Dangers {
    dangers = [];

    constructor() {
        makeAutoObservable(this, {
            fetchDangers: action.bound,
            addDanger: action.bound,
            launchNuclearAttack: action.bound,
        });
    }

    async fetchDangers() {
        const response = await fetch('http://localhost:8000/threat/');
        const data = await response.json();
        const dtoData = data.map(fromDto);

        runInAction(() => {
            this.dangers = dtoData;
        })
    };

    async addDanger(x, y, danger) {
        const pos = coordinatesToGridPosition(x, y);
        const dto = ({
            "grid_x": pos[0],
            "grid_y": pos[1],
            range: Math.floor(danger),
        });

        const response = await fetchPost('http://localhost:8000/threat/', dto);
        const data = await response.json();
        const fromDtoData = fromDto(data);

        runInAction(() => {
            this.dangers.push(fromDtoData);
        })
    }

    async launchNuclearAttack() {
        const pos1 = getCoordinatesForGridPosition('P', '12');
        const pos2 = getCoordinatesForGridPosition('P', '13');
        const pos3 = getCoordinatesForGridPosition('Q', '12');
        const pos4 = getCoordinatesForGridPosition('Q', '13');
        const pos5 = getCoordinatesForGridPosition('R', '13');

        this.addDanger(pos1[0], pos1[1], 100);
        this.addDanger(pos2[0], pos2[1], 100);
        this.addDanger(pos3[0], pos3[1], 60);
        this.addDanger(pos4[0], pos4[1], 60);
        this.addDanger(pos5[0], pos5[1], 60);
        hospitalsStore.moveHospital4AfterAttack();

    }

}

export const dangersStore = new Dangers();