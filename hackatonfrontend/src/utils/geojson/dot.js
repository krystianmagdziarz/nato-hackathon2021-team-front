export const getDot = (posX, posY) => {
    return (
        {
            "type": "LineString",
            "coordinates": [[posX, posY], [posX, posY]],
        }
    )
}