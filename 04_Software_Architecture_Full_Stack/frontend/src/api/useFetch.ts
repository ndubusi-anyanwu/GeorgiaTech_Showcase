import { useState } from 'react';
import { useDebouncedCallback } from 'use-debounce';
import { useNavigate } from 'react-router-dom';

const useFetch = (callbackFn?: () => void) => {
  const [isError, setIsError] = useState(false);
  const [isSuccess, setIsSuccess] = useState(false);
  const [result, setResult] = useState<any>(null);
  const navigate = useNavigate();

  const request = async (endpoint: string, options: RequestInit) => {
    try {
      const accessToken = sessionStorage.getItem('access-token');
      if (accessToken) {
        options.headers = {
          ...options.headers, // Spread existing headers if any
          'Authorization': `Bearer ${accessToken}`, // Add Authorization header
          'Content-Type': 'application/json',
        };
      }

      const response = await fetch(`http://localhost:8080/${endpoint}`, options);

      if (response.status == 401) {
        console.warn("Refreshing token.");

        const storedRefreshToken = sessionStorage.getItem('refresh-token');
        const accessToken = sessionStorage.getItem('access-token') ?? '';
        const refreshReponse = await fetch('http://localhost:8080/api/auth/refresh-token', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${accessToken}`
          },
          body: JSON.stringify({ refreshToken: storedRefreshToken })
        });

        if (refreshReponse.ok) {
          const { accessToken, refreshToken } = await response.json();
          sessionStorage.setItem('access-token', accessToken);
          sessionStorage.setItem('refresh-token', refreshToken);
          sessionStorage.setItem('user-role', result.userRole);
        } else {
          // handle refresh failure (logout or request re-authentication)
          console.error('Token refresh failed. Redirecting to login page.');
          sessionStorage.removeItem('access-token');
          sessionStorage.removeItem('refresh-token');
          sessionStorage.removeItem('user-role');
          navigate('/login');
        }
      }
      else {
        if (!response.ok) {
          console.error(`Response status: ${response.status}`);
          setIsError(true);
          setIsSuccess(false);
        } else {
          console.log(`${endpoint} ${options.method} success`);
          response.json().then((res) => {
            setIsError(false);
            setIsSuccess(true);
            callbackFn && callbackFn();
            setResult(res);
          });
        }
      }

    } catch (error: any) {
      console.error(error.message);
      setIsError(true);
      setIsSuccess(false);
    }
  };

  return { isError, isSuccess, request, result };
};

export const useGet = (endpoint: string, callbackFn?: () => void) => {
  const { request, ...fetchResults } = useFetch(callbackFn);

  const trigger = useDebouncedCallback(async (params?: string) => {
    await request(`${endpoint}?${params ?? ''}`, { method: 'GET' });
  }, 100);

  return { ...fetchResults, trigger };
};

export function usePost<T>(endpoint: string, callbackFn?: () => void) {
  const { request, ...fetchResults } = useFetch(callbackFn);

  const trigger = async (body: T) => {
    await request(endpoint, {
      method: 'POST',
      body: JSON.stringify(body),
      headers: {
        'Content-Type': 'application/json',
      },
    });
  };

  return { ...fetchResults, trigger };
}
