import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import './index.css';
import {
  createBrowserRouter,
  Navigate,
  RouterProvider,
} from 'react-router-dom';
import Error from './pages/Error.tsx';
import App from './App.tsx';
import Battle from './pages/Battle.tsx';
import Pokemon from './pages/Pokemon.tsx';
import Users from './pages/Users.tsx';
import Login from './pages/Login.tsx';
import Register from './pages/Register.tsx';
import BattleInit from './pages/BattleInit.tsx';
import LandingPage from './pages/LandingPage.tsx';
import PrivateRoute from './PrivateRoute.tsx';

const router = createBrowserRouter([
  {
    path: '/app',
    element: <LandingPage />,
    errorElement: <Error />,
  },
  {
    path: '/',
    element: (
      <PrivateRoute>
        <App />
      </PrivateRoute>
    ),
    errorElement: <Error />,
    children: [
      {
        path: '', // Empty child path of /app
        element: <Navigate to="/battle" replace />, // Redirect to /app/battle
      },
      {
        path: 'battle',
        element: <BattleInit />,
      },
      {
        path: 'battle/:battleId',
        element: <Battle />,
      },
      {
        path: 'pokemon',
        element: <Pokemon />,
      },
      {
        path: 'users',
        element: <Users />,
      },
    ],
  },
  {
    path: 'login',
    element: <Login />,
  },
  {
    path: 'register',
    element: <Register />,
  },
]);

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <RouterProvider router={router} />
  </StrictMode>
);
