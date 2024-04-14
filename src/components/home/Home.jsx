import React from 'react'
import Lottie from 'lottie-react'
import animationData from '../../assets/animation.json'
import { Button, Link } from '@nextui-org/react'
import './Home.css'
import TypewriterComponent from 'typewriter-effect'

const Home = () => {
  return (
    <div className='h-[87vh] hero-bg  w-full flex bg-slate-50 '>
        <div className='w-1/2 flex justify-center overflow-y-hidden items-center'>
            <Lottie animationData={animationData} />
        </div>
        <div className='w-1/2 flex flex-col justify-center items-center gap-12'>
            <div className='relative text-7xl font-bubblegum text-center'>

                <TypewriterComponent
                    options={{
                        strings: ['Welcome to Calm Zone!'],
                        autoStart: true,
                        loop: true,
                    }}
                />
            </div>
            <div className='text-4xl text-center px-12 font-open-sans leading-10'>We'll help you tame your anger monster and say goodbye to anxiety!</div>
            <div className='flex gap-6'>
                <Button as={Link} href='/connect' showAnchorIcon  className='p-8 bg-slate-900 text-white text-3xl font-semibold'>
                    Connect With Us!
                </Button>
                <Button as={Link} href='/activities' showAnchorIcon  className='p-8 bg-slate-900 text-white text-3xl font-semibold'>
                    Fun & Games                
                </Button>
            </div>
        </div>
    </div>
  )
}

export default Home