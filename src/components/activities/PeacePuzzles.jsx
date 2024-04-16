import React, { useState } from 'react'
import jigsaw1 from '../../assets/jigsaw1.jpg';
import jigsaw2 from '../../assets/jigsaw2.jpg';
import jigsaw3 from '../../assets/jigsaw3.jpg';
import { JigsawPuzzle } from 'react-jigsaw-puzzle';
import "react-jigsaw-puzzle/lib/jigsaw-puzzle.css"
import './PeacePuzzles.css'
import {Modal, ModalContent, ModalHeader, ModalBody, ModalFooter, Button, useDisclosure, Image} from "@nextui-org/react";
import congrats from '../../assets/congrats.json'
import Lottie from 'lottie-react';

import audio from '../../assets/audio.mp3'
const images = [jigsaw1, jigsaw2, jigsaw3]

const PeacePuzzles = () => {
    const [currentPuzzle, setCurrentPuzzle] = useState(0)
    const {isOpen, onOpen, onOpenChange} = useDisclosure();
    const [timer, setTimer] = useState(0)
    const [gameStarted, setGameStarted] = useState(false)
    const [intervalId, setintervalId] = useState()
    const startTimer = () => {
        setintervalId(setInterval(() => {
            setTimer((timer) => timer + 1)

        }, 1000))
    }
    const stopTimer = () => {
        clearInterval(intervalId)
    }
    const resetTimer = () => {
        setTimer(0)
        //clear interval
        clearInterval(intervalId)
    }

    const formatTime = (time) => {
        const getSeconds = `0${time % 60}`.slice(-2);
        const minutes = `${Math.floor(time / 60)}`;
        const getMinutes = `0${minutes % 60}`.slice(-2);
        const getHours = `0${Math.floor(time / 3600)}`.slice(-2);
        return `${getHours} : ${getMinutes} : ${getSeconds}`;
    };


    const handleCompletion = () => {
        stopTimer();
        const audioToBePlayed = new Audio(audio)
        audioToBePlayed.play()
        onOpen()
    }
    return (
        <>
        <div className='flex flex-col hero-bg min-h-[87vh] justify-center items-center'>
            <h1 className='font-bubblegum text-4xl h-[10vh] flex justify-center items-center'>Peace Puzzles - Solve the below Jigsaw Puzzle</h1>
            <div className='h-[75vh] flex  w-full '>
                <div className='w-3/5 flex justify-center'>
                    <JigsawPuzzle
                        imageSrc={images[currentPuzzle]}
                        rows={3}
                        columns={3}
                        onSolved={handleCompletion}
                    />
                </div>
                <div className='flex justify-center items-center text-6xl'>
                        {
                            gameStarted ? (
                            <div className='flex flex-col gap-12 text-center'>
                                <div className='flex flex-col'>
                                    <span>Timer:</span>
                                    {formatTime(timer)}
                                </div>
                                <button className=' bg-slate-900 text-white p-6 flex justify-center items-center rounded-3xl' onClick={() => {
                                    resetTimer();
                                    setGameStarted(false);
                                }}>Reset Timer</button>
                            </div>

                            ) : (
                                <button className=' bg-slate-900 text-white p-6 flex justify-center items-center rounded-3xl' onClick={() => {
                                    startTimer();
                                    setGameStarted(true);
                                }}>Start Timer</button>
                            )

                        }
                </div>

            </div>
        </div>
        <Modal isOpen={isOpen} onOpenChange={onOpenChange}>
            <ModalContent>
            {(onClose) => (
                <>
                <ModalHeader className="flex flex-col gap-1">You Completed the puzzle!!</ModalHeader>
                <ModalBody>
                    {/* <Image src={images[currentPuzzle]} alt="puzzle" width={300} height={300} /> */}
                    <Lottie animationData={congrats} />
                    <p>You have successfully completed the puzzle</p>
                    <p>Time Taken: {formatTime(timer)}</p>
                </ModalBody>
                <ModalFooter>
                    <Button color="danger" variant="light" onPress={onClose}>
                    Close
                    </Button>
                    <Button color="primary" onPress={
                        ()=>{
                            setCurrentPuzzle((currentPuzzle+1)%images.length);
                            onClose();
                            resetTimer();
                            setGameStarted(false);
                        }
                    }>
                    Try Next Puzzle
                    </Button>
                </ModalFooter>
                </>
            )}
            </ModalContent>
        </Modal>
        </>
    )
}

export default PeacePuzzles