import { Button, Image, Link, Popover, PopoverContent, PopoverTrigger } from '@nextui-org/react'
import React, { useState } from 'react'
import logo from '../../assets/logo.jpeg';
import { Icon } from '@iconify/react';


const Navbar = () => {
    const [hover, setHover] = useState(false)
    
    return (
        <div className='w-full h-[13vh] p-4 flex justify-between items-center border-b-0 shadow-md'>
            <div className='flex gap-6 items-center w-1/5'>
                <Image src={logo} alt='logo' width={80} height={80} />
                <Link href='/' className='font-bubblegum text-blue-700 text-4xl'>Calm Zone</Link>
            </div>
            <nav className='w-4/5 flex justify-around font-bold text-3xl font-open-sans'>
                <Link className='text-2xl text-black' href='/'>
                    <Icon icon="ion:home" />&nbsp;&nbsp;Home
                </Link>
                <Link className='text-2xl text-black' href='/learn'>
                    <Icon icon="mdi:about" />&nbsp;&nbsp;Learn
                </Link>
                <Popover isOpen={hover} placement=''  className='cursor-pointer flex justify-center items-center gap-3'>
                    <PopoverTrigger>
                        <Button
                            as={Link}
                            href='/activities'  
                            onMouseOver={()=>{
                                setHover(true)
                            }} 
                            onMouseLeave={()=>{
                                setHover(false)
                            }}
                            
                        
                            className='text-2xl bg-white font-bold !opacity-100' 
                        >
                            <Icon icon="fluent:broad-activity-feed-16-filled" />
                            <span className='text-black '>Activities</span>
                            <Icon icon="ion:chevron-down-outline" />
                        </Button>
                    </PopoverTrigger>
                    <PopoverContent
                        onMouseOver={()=>{
                            setHover(true)
                        }}
                        onMouseLeave={()=>{
                            setHover(false)
                        }}
                        className='flex font- p-5 flex-col gap-6'
                    >
                        <Link href='/activities/colorsplash' className='text-xl flex gap-3 font-bold text-black'>
                            <Icon icon="fluent:color-16-filled" />
                            <span>ColorSplash</span> 
                        </Link>
                        <Link href='/activities/peacepuzzles' className='text-xl flex gap-3 font-bold text-black'>
                        <Icon icon="mdi:jigsaw" />
                            <span>PeacePuzzles</span>
                        </Link>
                    </PopoverContent>
                </Popover>
                <Link className='text-2xl text-black' href='/printables'>
                    <Icon icon="ion:print" />&nbsp;&nbsp;Printables
                </Link>
                
            </nav>
        </div>
    )
}

export default Navbar