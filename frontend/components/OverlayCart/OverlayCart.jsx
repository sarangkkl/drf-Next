import React from 'react';
import { CloseIcon } from '../../assets/icons';
import { empty } from '../../assets/images'

const OverlayCart = ({setIsDrawerOpen}) => {
  const cart = []
  return (
    <div className='w-11/12 mx-auto'>
      <div className='flex justify-between items-center p-4'>
          <h1 className='text-2xl  font-bold'>Shopping cart</h1>
          <div className='cursor-pointer border-2 border-neutral-900	'>
            <CloseIcon onClick={()=>{setIsDrawerOpen(false)}}/>
          </div>
      </div>
      <div className='	'>
        {cart.length === 0 ? <div className='text-center'>
          <h1 className='text-2xl font-bold'><img src={empty.src}/></h1>
          Your cart is empty
        </div>:<div className='flex justify-between items-center p-4'></div>}
      </div>
    </div>
  )
}

export default OverlayCart