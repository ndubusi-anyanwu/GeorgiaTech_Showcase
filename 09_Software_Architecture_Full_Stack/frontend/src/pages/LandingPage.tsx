import { useNavigate } from 'react-router-dom';
import { Button, Container, Typography, Box } from '@mui/material';

const LandingPage = () => {
    const navigate = useNavigate();

    return (
        <Container maxWidth="sm">
            <Box sx={{ display: 'flex', flexDirection: 'column', gap: 2, mt: 4 }}>
                <Typography variant="h3" component="h1" gutterBottom>
                    Welcome to the Pokémon Battle Tournament!
                </Typography>
                <Typography variant="body1" color="textSecondary" paragraph>
                    Showcase your Pokémon's skills and claim victory!
                </Typography>
                <Box sx={{ display: 'flex', justifyContent: 'center', gap: 2, marginTop: 2 }}>
                    <Button onClick={() => navigate('/login')} className="login-button" variant="outlined"
                        color="primary">
                        Login
                    </Button>
                    <Button onClick={() => navigate('/register')} className="register-button" variant="outlined"
                        color="primary">
                        Register
                    </Button>
                </Box>
            </Box>
        </Container>
    );
};

export default LandingPage;