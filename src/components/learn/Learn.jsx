import React, { useState } from 'react'
import anger from '../../assets/anger.png'
import angerJson from '../../assets/anger.json'
import anxiety from '../../assets/anxiety.png'
import emotion from '../../assets/emotion.json'
import calm from '../../assets/calm.json'
import breathe from '../../assets/breathe.json'
import focus from '../../assets/focus.json'
import Lottie from 'lottie-react'

import { Button, Image } from '@nextui-org/react'
import './Learn.css'
import ReactCardFlip from 'react-card-flip'

const Learn = () => {
  const [flippedAnger, setFlippedAnger] = useState(false)
  const [flippedAnxiety, setFlippedAnxiety] = useState(false)
  const data = [
    {
      title: 'Anger',
      description: 'Anger is like a fiery dragon inside us, making us feel real hot and bothered. It\'s like a big storm that can make us feel like we\'re going to explode. But it\'s okay to feel angry sometimes. It\'s just our heart\'s way of telling us that something isn\'t right.',
      image: anger,
      className: 'anger-bg',
      state: flippedAnger,
      stateSetter: setFlippedAnger
    },
    {
      title: 'Anxiety',
      description: 'Anxiety is like a little worried bug that tickles our tummy and makes us feel nervous. It\'s when we\'re scared about something that might happen or when we feel unsure about what\'s going on. But we can be brave and talk about our worries to make the bug feel smaller and less scary.',
      image: anxiety,
      className: 'anxiety-bg',
      state: flippedAnxiety,
      stateSetter: setFlippedAnxiety
    }
  ]
  return (
    <div className='bg-slate-100'>
      <div className='min-h-[87vh] flex border-b-2 bg-slate-100'>
          <div className='w-1/2 flex  items-center justify-center flex-col gap-6'>
            <span className='text-6xl font-bubblegum'>Learn about Emotions</span>  
            <p className='p-6 text-2xl text-center'>
              Emotions are like colors for our feelings. Just like how you feel happy when you see your favorite toy or sad when you miss someone, emotions are how our hearts tell us how we're feeling inside. They can be like a big hug when we're happy or a gentle pat when we're feeling calm.
            </p>
          </div>
          <div className='w-1/2 flex text-6xl items-center justify-center flex-col gap-6'>
            <Lottie animationData={emotion} />
          </div>
      </div>
      <div className='text-6xl pt-12  font-bubblegum text-center'>Explore Emotions</div>
      <div className=' flex justify-around  py-12 gap-6'>
        {
          data.map((item, index) => {
            return( <ReactCardFlip  isFlipped={item.state} flipDirection="horizontal">
            <div
              onClick={()=>{item.stateSetter(!item.state)}}
              className={`w-[45vw] h-[80vh] bg-white ${item.className} rounded-3xl flex flex-col gap-6 py-12 justify-center items-center text-center cursor-pointer`}>
              <div className='flex flex-col gap-12 justify-center text-center items-center '>
                <span className='text-6xl font-bubblegum'>{item.title}</span>
                <Image src={item.image} width='240' height='300' />
                <span color='primary' className='text-4xl p-6'>Click to Learn More!</span>
              </div>
            </div>
            <div
              onClick={()=>{item.stateSetter(!item.state)}}
              className={`w-[45vw] h-[80vh] bg-white ${item.className} rounded-3xl flex flex-col gap-6 py-12 justify-center items-center cursor-pointer`}>
              <p className='px-12 text-3xl  text-center font-open-sans text-black font-semibold'>
                {item.description}
              </p>
            </div>
          </ReactCardFlip>)
          
            
        }
        )}
      </div>
      <div className='flex '>
        <div className='w-1/2'>
          <Lottie animationData={calm} />
        </div>
        <div className='w-1/2 flex flex-col gap-6 justify-center items-center p-8 text-center text-3xl'>
          <span className='text-4xl font-semibold'>
            Hello, amazing pals!
          </span> 
          <span>
            Sometimes, we feel really big emotions like <strong className='text-red-900'>anger</strong> or <strong className='text-slate-800'>anxiety</strong>, and you know what? That's totally <strong className='text-blue-950'>normal and okay!</strong> It's like having magical powers hidden inside us. Anger might feel like a <strong className='text-red-950'>fierce dragon</strong>, and anxiety is like a <strong className='text-blue-900'>fluttering butterfly</strong> in our tummy. But just like superheroes, we can learn to control these feelings and use them for good adventures! Let's go on this journey together and learn how to be the bravest heroes of all!
          </span>
        </div>
      </div>
      <div className='flex'>
        <div className='w-1/2 flex flex-col gap-6 justify-center items-center p-8 text-center text-3xl'>
          <span className='text-4xl font-semibold'>
            Let's take a deep breath!
          </span> 
          <span>
            When we feel big emotions like anger or anxiety, it's like a big storm inside us. But we can calm the storm by taking a deep breath. Just like how we blow out candles on a birthday cake, we can blow away our worries and feel calm and peaceful. Let's take a deep breath together and feel the magic of being calm and brave!
          </span>
        </div>
        <div className='w-1/2'>
          <Lottie animationData={breathe} />
        </div>

      </div>
      <div className='flex'>
        <div className='w-1/2'>
          <Lottie animationData={focus} />
        </div>
        <div className='w-1/2 flex flex-col gap-6 justify-center items-center p-8 text-center text-3xl'>
          <span className='text-4xl font-semibold'>
            Focus on the good things!
          </span> 
          <span>
            When we're feeling overwhelmed by big emotions, like a storm swirling inside us, mindfulness can be our superpower. It's like putting on a magical cloak that helps us focus on the present moment. Just like when we watch a butterfly flutter by, we can gently guide our thoughts back to what's happening right now. Let's take a deep breath and imagine ourselves floating on a calm river, letting go of worries and embracing the peacefulness of the present.
          </span>
        </div>
      </div>
    </div>
  )
}

export default Learn