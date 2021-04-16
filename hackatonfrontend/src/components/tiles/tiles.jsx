import React, {useRef, useEffect} from 'react';

export default function Tiles() {

    const canvasRef = useRef();

    useEffect(() => {
        const context = canvasRef.current.getContext('2d');

        context.fillStyle = '#000000';
        context.beginPath();
        context.arc(50, 100, 20, 0, 2 * Math.PI);
        context.fill();

    }, []);


    return <canvas ref={canvasRef} style={{background: 'teal'}}/>
}