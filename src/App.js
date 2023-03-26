import { useSelector } from 'react-redux';
import { createBrowserRouter, Link, RouterProvider } from 'react-router-dom';
import './App.css';
import DrawerLayout from './Layouts/DrawerLayout/DrawerLayout';
import { themeMode } from './Redux/themeSlice';

function App() {
  const theme = useSelector(themeMode);

  const router = createBrowserRouter([
    {
      path: "/",
      element: <DrawerLayout> <div>this is home page</div> </DrawerLayout>,
    },
    {
      path: "/about",
      element: <DrawerLayout> <div>this is about page</div>  </DrawerLayout>,
    },
  ]);

  return (
    <div data-theme={theme} className="">
      <RouterProvider router={router} />
    </div>
  );
}

export default App;
