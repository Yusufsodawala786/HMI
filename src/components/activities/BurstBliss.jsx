import React, { useState, useEffect, useRef } from 'react';

const BurstBliss = () => {
    const [balloons, setBalloons] = useState([]);
    const [score, setScore] = useState(0);
    const [isGameStarted, setIsGameStarted] = useState(false);
    const [isGameOver, setIsGameOver] = useState(false);
    const gameAreaRef = useRef(null);

    const createBalloon = () => {
        const balloon = {
            id: Math.random().toString(36).substring(2, 15), // Unique ID
            x: Math.random() * (gameAreaRef.current.offsetWidth - 50), // Random X position
            y: gameAreaRef.current.offsetHeight, // Start at the bottom
            color: getRandomColor(), // Random color
        };
        setBalloons((prevBalloons) => [...prevBalloons, balloon]);
    };

    const getRandomColor = () => {
        const letters = '0123456789ABCDEF';
        let color = '#';
        for (let i = 0; i < 6; i++) {
            color += letters[Math.floor(Math.random() * 16)];
        }
        return color;
    };

    const moveBalloons = () => {
        setBalloons((prevBalloons) =>
            prevBalloons
                .map((balloon) => ({ ...balloon, y: balloon.y - 5 }))
                .filter((balloon) => balloon.y > 0)
        );
    };

    const handleBalloonClick = (id) => {
        setBalloons((prevBalloons) => prevBalloons.filter((balloon) => balloon.id !== id));
        setScore((prevScore) => prevScore + 1);
    };

    const startGame = () => {
        setIsGameStarted(true);
        setIsGameOver(false);
        setScore(0);
        setBalloons([]);
    };

    const endGame = () => {
        setIsGameStarted(false);
        setIsGameOver(true);
    };

    useEffect(() => {
        if (isGameStarted) {
            const balloonInterval = setInterval(createBalloon, 2000);
            const moveInterval = setInterval(moveBalloons, 50);

            return () => {
                clearInterval(balloonInterval);
                clearInterval(moveInterval);
            };
        }
    }, [isGameStarted]);

    useEffect(() => {
        if (isGameStarted && balloons.length === 0) {
            endGame();
        }
    }, [isGameStarted, balloons]);

    return (
        <div className="balloon-game">
            <div className="game-area" ref={gameAreaRef}>
                {balloons.map((balloon) => (
                    <div
                        key={balloon.id}
                        className="balloon"
                        style={{
                            left: balloon.x + 'px',
                            top: balloon.y + 'px',
                            backgroundColor: balloon.color,
                        }}
                        onClick={() => handleBalloonClick(balloon.id)}
                    />
                ))}
            </div>

            <div className="controls">
                {!isGameStarted && !isGameOver && (
                    <button onClick={startGame}>Start Game</button>
                )}
                {isGameOver && (
                    <div className="game-over">
                        Game Over! Your score: {score}
                    </div>
                )}
            </div>
        </div>
    );
};

export default BurstBliss;