import { Image } from '@nextui-org/react'
import React from 'react'


const Printables = () => {
  return (
    <div className='min-h-[87vh] bg-blue-50 '>
        <h1 className='text-center text-4xl p-6 font-bubblegum'>Printables</h1>
        <div className='text-center text-3xl pb-6'>Download files for your little monster for printing!!</div>
        <div className='flex justify-center gap-6'>
            <div className='w-[30%] p-6 h-[70vh] rounded-lg bg-white flex flex-col gap-6 justify-center items-center'>
                <span className='text-3xl font-bubblegum'>Coloring Pages</span>
                <a download='/printable1.jpg' href='/printable1.jpg' target='_blank' className='flex justify-around w-full gap-6 p-6 shadow-lg border-3 rounded-large  items-center '>
                    <div className='w-1/6'>
                        <Image src='/printable1.jpg' />
                    </div>
                    <span className='w-5/6 text-2xl'>Download Color Page 1</span>
                </a>
                <a download='/printable2.jpg' target='_blank' href='/printable2.jpg' className='flex justify-around w-full gap-6 p-6 shadow-lg border-3 rounded-large  items-center '>
                    <div className='w-1/6'>
                        <Image src='/printable2.jpg' />
                    </div>
                    <span className='w-5/6 text-2xl'>Download Color Page 2</span>
                </a>
                <a href='/printable3.jpg' download='/printable3.jpg' className='flex justify-around w-full gap-6 p-6 shadow-lg border-3 rounded-large  items-center '>
                    <div className='w-1/6'>
                        <Image src='/printable3.jpg' />
                    </div>
                    <span className='w-5/6 text-2xl'>Download Color Page 3</span>
                </a>
                
            </div>
            <div className='w-[30%] p-6 h-[70vh] rounded-lg bg-white flex flex-col gap-6 justify-center items-center'>
                <span className='text-3xl font-bubblegum'>Jigsaw Puzzle</span>
                <a download='/printable4.png' href='/printable1.jpg' target='_blank' className='flex justify-around w-full gap-6 p-6 shadow-lg border-3 rounded-large  items-center '>
                    <div className='w-1/6'>
                        <Image src='/printable4.png' />
                    </div>
                    <span className='w-5/6 text-2xl'>Download Jigsaw 1</span>
                </a>
                <a download='/printable5.png' target='_blank' href='/printable2.jpg' className='flex justify-around w-full gap-6 p-6 shadow-lg border-3 rounded-large  items-center '>
                    <div className='w-1/6'>
                        <Image src='/printable5.png' />
                    </div>
                    <span className='w-5/6 text-2xl'>Download Jigsaw 2</span>
                </a>
                <a href='/printable6.png' download='/printable3.jpg' className='flex justify-around w-full gap-6 p-6 shadow-lg border-3 rounded-large  items-center '>
                    <div className='w-1/6'>
                        <Image src='/printable6.png' />
                    </div>
                    <span className='w-5/6 text-2xl'>Download Jigsaw 3</span>
                </a>
                
            </div>     
            <div className='w-[30%] p-6 h-[70vh] rounded-lg bg-white flex flex-col gap-6 justify-center items-center'>
            <span className='text-3xl font-bubblegum'>Story Book</span>
                <a download='/printable7.pdf' href='/printable1.jpg' target='_blank' className='flex justify-around w-full gap-6 p-6 shadow-lg border-3 rounded-large  items-center '>
                    <div className='w-1/6'>
                        <Image src='/printable4.png' />
                    </div>
                    <span className='w-5/6 text-2xl'>Download Story Book 1</span>
                </a>
                <a download='/printable8.pdf' target='_blank' href='/printable2.jpg' className='flex justify-around w-full gap-6 p-6 shadow-lg border-3 rounded-large  items-center '>
                    <div className='w-1/6'>
                        <Image src='/printable5.png' />
                    </div>
                    <span className='w-5/6 text-2xl'>Download Story Book 2</span>
                </a>
                <a href='/printable9.pdf' download='/printable3.jpg' className='flex justify-around w-full gap-6 p-6 shadow-lg border-3 rounded-large  items-center '>
                    <div className='w-1/6'>
                        <Image src='/printable6.png' />
                    </div>
                    <span className='w-5/6 text-2xl'>Download Story Book 3</span>
                </a>
                            </div>

        </div>
    </div>
  )
}

export default Printables