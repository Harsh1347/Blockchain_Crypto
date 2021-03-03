import '../App.css';
import React, { useState, useEffect } from 'react'
import logo from '../assets/logo.png'

function App() {

  const [walletInfo, setwalletInfo] = useState({})

  useEffect(() => {
    fetch('http://127.0.0.1:5000/wallet/info')
      .then(response => response.json())
      .then(json => setwalletInfo(json))
  }, [])

  const { address, balance } = walletInfo

  return (
    <div className="App">
      <img className="logo" src={logo} alt="PyChain logo" />
      <h3>Welcome to PyChain</h3>
      <div className='WalletInfo'>
        <div>Address:{address}</div>
        <div>Balance:{balance}</div>

      </div>
    </div>
  );
}

export default App;
