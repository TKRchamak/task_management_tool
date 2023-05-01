import { useSelector } from 'react-redux';
import { createBrowserRouter, Link, RouterProvider } from 'react-router-dom';
import './App.css';
import DrawerLayout from './Layouts/DrawerLayout/DrawerLayout';
import { themeMode } from './Redux/themeSlice';
import Home from './Pages/Home/Home';

function App() {
  const theme = useSelector(themeMode);

  const router = createBrowserRouter([
    {
      path: "/",
      element: <DrawerLayout> <Home /> </DrawerLayout>,
    },
    {
      path: "/about",
      element: <DrawerLayout> <div>this is about page</div>  </DrawerLayout>,
    },
    {
      path: "/profile",
      element: <DrawerLayout> <div>this is profile page</div>  </DrawerLayout>,
    },
  ]);

  return (
    <div data-theme={theme} className="">
      <RouterProvider router={router} />
    </div>
  );
}

export default App;
