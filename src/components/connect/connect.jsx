import React from 'react'
import Map from './Map'
import {Input} from "@nextui-org/react";
import {Button, ButtonGroup} from "@nextui-org/react";
import Swal from 'sweetalert2'
const Connect = () => {

  const handleSubmit = () => {
    // alert("Query has been submitted");
    Swal.fire ({
      title: 'Query Submitted!',
      text: 'We will get back to you soon!',
      icon: 'success',
      confirmButtonText: 'OK'

    })
    setTimeout(() => {
      window.location.reload();
    }, 2000);

    // window.location.reload(); // Reloading the page
  };

  return (
    <div className=' hero-bg h-[87vh]'>
        <span className='flex h-[20vh]  justify-center items-center font-bubblegum text-7xl'>Connect with us! </span><br/>
        <div className='flex justify-between items-center gap-10 pr-24 '>
        <Map />
        <div className='w-[50%] flex flex-col justify-center items-center bg-[#2e312f] rounded-xl '>
        <span className='text-3xl font-bubblegum text-white pt-5'>Submit Your Query!</span>
        <div  className="w-[100%] flex flex-col justify-center items-center  gap-4 p-10 ">
          <Input type='text' label='Name' className='w-[70%]'/>
          <Input type='text' label='Contact No' className='w-[70%]'/>
          <Input type='text' label='Query' className='w-[70%]'/>
          <Button color='primary' className='w-[30%] font-bubblegum text-xl' onClick={handleSubmit}>
            Submit
          </Button>
        </div>
        </div>
        </div>
    </div>
  )
}

export default Connect