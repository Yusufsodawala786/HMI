import React from 'react'
import { GoogleMap, useLoadScript, MarkerF } from '@react-google-maps/api'

const Map = () => {
    const {isLoaded, loadError} = useLoadScript
  return (
    <div className='h-[57vh] flex justify-start items-end pl-10 pb-5'>
        {/* <iframe src="https://www.google.com/maps/d/u/0/embed?mid=1wc-_PKwn_aJqhqnMoZW2ag5yM8EmSyQ&ehbc=2E312F" width="640" height="480"></iframe> */}
        {/* <iframe src="https://www.google.com/maps/d/u/0/embed?mid=1wc-_PKwn_aJqhqnMoZW2ag5yM8EmSyQ&ehbc=2E312F" width="640" height="480"></iframe> */}
        <iframe src="https://www.google.com/maps/d/u/0/embed?mid=1wc-_PKwn_aJqhqnMoZW2ag5yM8EmSyQ&ehbc=2E312F" width="600" height="400"></iframe>
    </div>
  )
}

export default Map