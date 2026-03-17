import React from 'react';
import { Navigate } from 'react-router-dom';

interface PrivateRouteProps {
  redirectPath?: string;
  children: any;
}

const PrivateRoute: React.FC<PrivateRouteProps> = ({
  redirectPath = '/app',
  children,
}) => {
  const isAuthenticated = Boolean(sessionStorage.getItem('access-token'));
  return isAuthenticated ? (
    <>{children}</>
  ) : (
    <Navigate to={redirectPath} replace />
  );
};

export default PrivateRoute;
