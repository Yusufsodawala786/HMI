import React from 'react'
import drawing from '../../assets/drawing.png';
import jigsaw from '../../assets/jigsaw.png';
import balloon from '../../assets/balloon.png';
import { Image, Link } from '@nextui-org/react';

const Activities = () => {
  return (
    <div className='bg-slate-100 flex flex-col justify-around min-h-[87vh]'>
        <h1 className='text-center text-4xl font-bubblegum'>Discover Calm: Activities to Soothe Anger and Anxiety</h1>
        <div className='flex justify-around'>
            <Link href='/activities/colorsplash' className='w-[30%] h-[70vh] bg-red-200 rounded-3xl border-pink-900 border-4 flex flex-col items-center   cursor-pointer'>
                <div className='text-4xl font-bubblegum h-1/5 flex justify-center w-full items-center '>ColorSplash</div>
                <div className='h-4/5 flex justify-center items-center'>
                    <Image  src={drawing} alt='drawing' />    
                </div>
            </Link>
            <Link href='/activities/peacepuzzles' className='w-[30%] h-[70vh] bg-red-200 rounded-3xl border-pink-900 border-4 flex flex-col items-center    cursor-pointer'>
                <div className='text-4xl font-bubblegum h-1/5 flex justify-center w-full items-center '>PeacePuzzles</div>
                <div className='h-4/5 flex justify-center items-center'>
                    <Image  src={jigsaw} alt='jigsaw' />
                </div>
            </Link>
            {/* <Link href='/activities/burstbliss' className='w-[30%] h-[70vh] bg-red-200 rounded-3xl border-pink-900 border-4 flex flex-col items-center   cursor-pointer'>
                <div className='text-4xl font-bubblegum h-1/5 flex justify-center w-full items-center '>BurstBliss</div>
                <div className='h-4/5 flex justify-center items-center'>
                    <Image  src={balloon} alt='drawing' />
                </div>
            </Link> */}
        </div>
    </div>
  )
}

export default Activities