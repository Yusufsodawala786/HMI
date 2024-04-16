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
                        "Black", "White", "Gray", "Silver", "DarkGray",
"Red", "Maroon", "Crimson", "Tomato", "FireBrick",
"Orange", "DarkOrange", "Coral", "Gold", "DarkGoldenrod",
"Yellow", "LemonChiffon", "Gold", "Khaki", "DarkKhaki",
"Green", "Lime", "ForestGreen", "Olive", "DarkOliveGreen",
"Blue", "Navy", "RoyalBlue", "DodgerBlue", "SteelBlue",
"Purple", "Indigo", "MediumPurple", "BlueViolet", "DarkOrchid",
"Pink", "HotPink", "DeepPink", "LightPink", "PaleVioletRed",
"Turquoise", "MediumTurquoise", "LightSeaGreen", "CadetBlue", "DarkCyan",
"Teal", "DarkSlateGray", "Aquamarine", "MediumAquamarine", "MediumSpringGreen",
"Brown", "SaddleBrown", "Sienna", "Chocolate", "Peru",
"Violet", "Plum", "Orchid", "Magenta", "MediumOrchid",
"Lavender", "Thistle", "MediumSlateBlue", "SlateBlue", "DarkSlateBlue"

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
