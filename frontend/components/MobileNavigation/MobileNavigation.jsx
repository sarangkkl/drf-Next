import  style from './MobileNavigation.module.css';
import React from 'react';
import { HomeIcon,MenuIcon,PersonOutlineOutlinedIcon,ShoppingCartOutlinedIcon } from '../../assets/icons'
import { IconButton } from '../../assets';
import Link from 'next/link';

const MobileNavigation = ({setIsDrawerOpen}) => {
  return (
    <div className={style.mobile__navigation__container}>
        <div className={style.mobile__nav}>
        <IconButton>
                <MenuIcon />
        </IconButton>
        <IconButton>
                <Link href='/'><HomeIcon /></Link>
        </IconButton>
        <IconButton>
                <Link href='/account'><PersonOutlineOutlinedIcon/></Link>
                
        </IconButton>
        <IconButton onClick={()=>{setIsDrawerOpen(true)}}>
                <ShoppingCartOutlinedIcon />
        </IconButton>
        </div>

    </div>
  )
}

export default MobileNavigation