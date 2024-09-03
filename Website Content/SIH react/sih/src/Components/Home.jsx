import React, { useState ,useCallback} from "react";
import { useNavigate } from "react-router-dom";
import './Home.css';


const Home = () => {
  const [value, setValue] = useState('');
  const naviagteTo=useNavigate();
  const handleJoin=useCallback(()=>{
    naviagteTo(`/room/${value}`);

  })
  
  return (
    <div className='Home-container'>
      <div className='Home-box'>
        <h1>Join Page</h1>
        <input 
          type='text'
          value={value}
          placeholder='Enter Your Room no'
          onChange={(e) => setValue(e.target.value)}
          className='room-input'
        />
        <button className='join-btn' onClick={handleJoin}>Join</button>
      </div>
    </div>
  );
}

export default Home;

