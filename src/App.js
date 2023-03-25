import { useSelector } from 'react-redux';
import './App.css';
import TopNavbar from './Components/TopNavbar/TopNavbar';
import { themeMode } from './Redux/themeSlice';

function App() {
  const theme = useSelector(themeMode);


  return (
    <div data-theme={theme} className="">
      <TopNavbar />
    </div>
  );
}

export default App;
