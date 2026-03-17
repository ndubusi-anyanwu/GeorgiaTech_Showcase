import { Outlet } from 'react-router-dom';
import './App.css';
import Navbar from './components/Navbar';
import useTokenManagement from './session/tokenManagement';

const App = () => {
  useTokenManagement();
  return (
    <div style={{ display: 'flex', height: '100vh' }}>
      <div style={{ flex: '15%' }}>
        <Navbar />
      </div>
      <div style={{ flex: '85%', overflow: 'auto', margin: '1rem' }}>
        <Outlet />
      </div>
    </div>
  );
};

export default App;
