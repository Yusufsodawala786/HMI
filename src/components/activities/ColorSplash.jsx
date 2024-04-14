import React,{useEffect, useRef, useState} from "react";
import Color1 from "./Color1";
import { CirclePicker } from "react-color";
import './ColorSplash.css';
import { Button } from "@nextui-org/react";
import color1 from "../../assets/color1.svg";
import brush from "../../assets/brush.png";
import Color3 from "./Color3";


const ColorSplash = () => {
    const [fillColors, setFillColors] = useState(Array(75).fill("white"));
    const [currentColor, setCurrentColor] = useState("white");
    const [isDownloading, setIsDownloading] = useState(false)
    const handleClick = (event) =>{
        const clickedPath = event.target; // Get the clicked element
        console.log(clickedPath); // Log the clicked element to the console
        clickedPath.style.fill = currentColor; // Change the fill color of the clicked element

    }
    useEffect(() => {
        const paths = document.querySelectorAll("path");
        paths.forEach((path, i) => {
            path.style.fill = "white";
        });
    }, []);

        // const onFillColor = (i) => {
        //     let newFillColors = fillColors.slice(0);
        //     newFillColors[i] = currentColor;
        //     setFillColors(newFillColors);
        // };
    const download = () => {
        setIsDownloading(true);
        const svg = document.querySelector("#svgToDownload");
        const canvas = document.createElement('canvas');
        const ctx = canvas.getContext('2d');

        const svgString = new XMLSerializer().serializeToString(svg);
        const DOMURL = window.URL || window.webkitURL || window;
        const img = new Image();
        const svgBlob = new Blob([svgString], { type: 'image/svg+xml;charset=utf-8' });

        const url = DOMURL.createObjectURL(svgBlob);

        const link = document.createElement('a');
        document.body.appendChild(link); // Append link to body here

        new Promise((resolve, reject) => {
            img.onload = resolve;
            img.onerror = reject;
            img.src = url;
        }).then(() => {
            ctx.drawImage(img, 0, 0);
            const png = canvas.toDataURL('image/png');

            link.download = 'image.png';
            link.href = png;
            link.click(); // Move link.click() inside onload function
            document.body.removeChild(link); // Remove link after click
        }).catch((error) => {
            console.error('Error in loading image: ', error);
        });
        setIsDownloading(false)
    }
    return (
        <>
        <div className="flex flex-col hero-bg min-h-[87vh] justify-center items-center">
            <h1 className="font-bubblegum  text-4xl h-[10vh] flex justify-center items-center">
            Color Splash - Color the below image using the color palette
            </h1>
            <div className="w-full flex">
            <div className="w-1/2 p-6 h-[70vh] ">
                {/* <img src={color1} alt="color1" /> */}
                <Color1 onClick={handleClick}   />
            </div>

            <div className="flex w-1/2 flex-col justify-center gap-6 text-center items-center text-4xl">
                <span className="font-bold">Pick any color from below!</span>

                <CirclePicker 
                    onChange={(color) => setCurrentColor(color.hex)}
                    circleSize={40}
                    circleSpacing={10}
                    colors={[
                        "#000000", "#111111", "#222222", "#333333", "#444444",
                        "#555555", "#666666", "#777777", "#888888", "#999999",
                        "#FF0000", "#FF3333", "#FF6666", "#FF9999", "#FFCCCC",
                        "#00FF00", "#33FF33", "#66FF66", "#99FF99", "#CCFFCC",
                        "#0000FF", "#3333FF", "#6666FF", "#9999FF", "#CCCCFF",
                        "#FFFF00", "#FFFF33", "#FFFF66", "#FFFF99", "#FFFFCC",
                        "#800080", "#9932CC", "#8A2BE2", "#9370DB", "#BA55D3",
                        "#FFA500", "#FF9933", "#FF8C00", "#FF7F50", "#FF6347",
                        "#00FFFF", "#33FFFF", "#66FFFF", "#99FFFF", "#CCFFFF",
                        "#FFC0CB", "#FF69B4", "#FF1493", "#DB7093", "#FFB6C1",
                        "#808000", "#008000", "#008080", "#000080", "#AAAAAA", 
                        "#BBBBBB", "#CCCCCC", "#DDDDDD", "#EEEEEE", "#FFFFFF"
                    ]}  
                />
                <Button onClick={download} isLoading={isDownloading} className="bg-slate-900 text-3xl p-9 text-white">
                    {isDownloading?"Downloading":"Download your masterpiece!"}
                </Button>
            </div>

            </div>
        </div>
        </>
    );
};

export default ColorSplash;
