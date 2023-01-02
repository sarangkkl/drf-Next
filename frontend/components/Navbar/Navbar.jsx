import React,{useState,useEffect} from 'react';
import style from './Navbar.module.css';
import { PersonOutlineOutlinedIcon,FavoriteBorderOutlinedIcon,ShoppingCartOutlinedIcon,SearchIcon } from '../../assets/icons';
import { IconButton,Drawer } from '../../assets';
import { logo } from '../../assets/images';
import { MobileNavigation,OverlayCart } from '../';
import Link from 'next/link';




const Navbar = () => {
  const [isDrawerOpen,setIsDrawerOpen] = useState(false);
  const [categories,setCategories] = useState();
  useEffect(() => {
    var requestOptions = {
      method: 'GET',
      redirect: 'follow'
    };
    
    fetch(`http://127.0.0.1:8000/api/products/getCategories`, requestOptions)
      .then(response => response.text())
      .then(result => {

        setCategories(JSON.parse(result))
      })
      .catch(error => console.log('error', error));
      
  }, [])
  
  let user = true;
  return (
    <div className='container mx-auto'>
        <div className={`${style.navbar__container}`}>
              <div className={style.nav__logo__container}>
                 <Link href={'/'}><img src={logo.src}/></Link>
              </div>
              <div className={style.search__container}>
                <input type='text' placeholder='Search Product & Brand' className='border-2 border-gray-300 p-2 rounded-md' />
                <IconButton><SearchIcon/></IconButton>
              </div>
              <div className={style.action__container}>
                {user ? <div className=''>
                  
                    <IconButton>
                      <Link href="/account">
                        <PersonOutlineOutlinedIcon />
                      </Link>
                    
                    </IconButton>
                    
                 
                  
                    <IconButton>
                      <FavoriteBorderOutlinedIcon />
                    </IconButton>
                  
                  <IconButton onClick={()=>{setIsDrawerOpen(true)}}>
                    <ShoppingCartOutlinedIcon />
                  </IconButton>
                </div>:<>
                <button className='bg-blue-500 text-white p-2 rounded-md'>Login</button>
                <button className='bg-blue-500 text-white p-2 rounded-md'>Register</button>
                </>}
                
              </div>
        </div>
        <div className={`${style.header__container} flex`}>
        {categories && categories.map((item,index)=>(
          <Link href={item.slug} className='px-3 py-1 text-xl font-bold uppercase hover:text-pink-600' key={item.slug}>
          {item.category_name}
          </Link>
        ))}
      </div>
        <MobileNavigation setIsDrawerOpen={setIsDrawerOpen}/>
        <Drawer anchor="right" open={isDrawerOpen} onClose={() => { setIsDrawerOpen(false) }}>
            <div style={{
              width: '95vw',
              maxWidth: '500px',
            }}>
              
                <OverlayCart setIsDrawerOpen={setIsDrawerOpen}/>
            </div>
          </Drawer>
    </div>
  )
}

export default Navbar