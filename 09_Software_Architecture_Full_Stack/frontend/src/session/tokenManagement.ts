import { useEffect } from 'react';

const useTokenManagement = () => {
    const refreshToken = async () => {
        const storedRefreshToken = sessionStorage.getItem('refresh-token');
        const accessToken = sessionStorage.getItem('access-token');
        const response = await fetch('http://localhost:8080/api/auth/refresh-token', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${accessToken}`
            },
            body: JSON.stringify({ refreshToken: storedRefreshToken })
        });

        if (response.ok) {
            const { accessToken, refreshToken, userRole } = await response.json();
            sessionStorage.setItem('access-token', accessToken);
            sessionStorage.setItem('refresh-token', refreshToken);
            sessionStorage.setItem('user-role', userRole);
            return accessToken;
        } else {
            // handle refresh failure (logout or request re-authentication)
            console.error('Token refresh failed');
        }
    };

    useEffect(() => {
        const initiateTokenRefresh = () => {
            const accessToken = sessionStorage.getItem('access-token');
            if (accessToken) {
                const expiryTime = parseJwtExpiryTime(accessToken);
                if (expiryTime) {
                    const timeToExpiry = expiryTime - Date.now(); // Time remaining until expiry

                    if (timeToExpiry <= 0) {
                        sessionStorage.removeItem('access-token');
                        sessionStorage.removeItem('refresh-token');
                        sessionStorage.removeItem('user-role');
                        // Token has already expired, refresh immediately
                        refreshToken();
                    } else if (timeToExpiry <= 5 * 60 * 1000) {
                        // Token expires in less than 5 minutes, refresh now
                        refreshToken();
                    } else {
                        // Token is valid for more than 5 minutes, schedule refresh
                        const timeToRefresh = timeToExpiry - (5 * 60 * 1000); // Refresh 5 minutes before expiry
                        setTimeout(refreshToken, timeToRefresh);
                    }
                }
            }
        };

        initiateTokenRefresh();
    }, []);
};

function parseJwtExpiryTime(token: String) {
    if (!token) return null;

    try {
        // Split the token to access the payload part (second part)
        const payloadBase64 = token.split('.')[1];

        // Decode the base64 payload and parse it as JSON
        const decodedPayload = JSON.parse(atob(payloadBase64));

        // Return the expiration time in milliseconds
        return decodedPayload.exp * 1000; // `exp` in seconds, so multiply by 1000
    } catch (error) {
        console.error('Failed to parse JWT token:', error);
        return null;
    }
}

export default useTokenManagement;