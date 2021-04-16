export const getLine = (coordinates) => {
    return (
        {
            "type": "LineString",
            "coordinates": coordinates,
        }
    )
}