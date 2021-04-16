export const getDanger = (x, y, danger) => ({
    danger: danger,
    coordinates: generatePoints(x, y, danger),
})

const generatePoints = (posX, posY, danger) => {
    const max = 10;
    const min = 1;
    const random = () => Math.floor(Math.random() * (max - min)) + min;
    const getAddPos = (i) => {
        const randomNumber = random();
        const isMinus = randomNumber % 2 === 0;
        return isMinus ? -i : i;
    }

    let itemsNumber = Math.floor(danger / 10);
    itemsNumber = itemsNumber === 0 ? 1 : itemsNumber;

    return Array.from(Array(itemsNumber).keys()).map((v) => [
        posX + getAddPos(v),
        posY + getAddPos(v),
    ])
}