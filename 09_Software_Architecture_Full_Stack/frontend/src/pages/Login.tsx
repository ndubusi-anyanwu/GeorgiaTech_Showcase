import { Formik, Form, Field } from 'formik';
import * as Yup from 'yup';
import { TextField, Button, Box, Typography } from '@mui/material';
import { useEffect, useState } from 'react';
import { usePost } from '../api/useFetch';
import { useNavigate } from 'react-router-dom';

const loginFormValues = {
  username: '',
  password: ''
};
// Validation schema using Yup
const validationSchema = Yup.object({
  username: Yup.string().required('Username is required'),
  password: Yup.string().min(8, 'Password should be at least 8 characters').required('Password is required')
});

const Login = () => {
  const [successMessage, setSuccessMessage] = useState('');
  const [errorMessage, setErrorMessage] = useState('');
  const { isError, isSuccess, trigger, result } = usePost('api/auth/login');
  const navigate = useNavigate();

  const onSubmit = async (formData: typeof loginFormValues, { resetForm }: any) => {
    try {
      await trigger(formData);
      resetForm();
    } catch (error) {
      setErrorMessage('An error occurred. Please try again later.');
      setSuccessMessage('');
    }
  };

  useEffect(() => {
    if (isSuccess) {
      // Store the token in sessionStorage
      if (result?.accessToken && result?.refreshToken) {
        sessionStorage.setItem('access-token', result.accessToken);
        sessionStorage.setItem('refresh-token', result.refreshToken);
        sessionStorage.setItem('user-role', result.userRole);
      }
      // display message while redirecting
      setSuccessMessage("Login successful. Redirecting to the Application.");
      setErrorMessage('');
      // Redirect to a new route
      navigate('/battle');

    } else if (isError) {
      setSuccessMessage('');
      setErrorMessage('Login failed. Please try again.');
    }
  });

  return (
    <Box
      display="flex"
      flexDirection="column"
      alignItems="center"
      justifyContent="center"
      height="100vh"
    >
      <Typography variant="h4" mb={3}>
        Login
      </Typography>
      {successMessage && (
        <Typography variant="body1" color="success.main" align="center">
          {successMessage}
        </Typography>
      )}
      {errorMessage && (
        <Typography variant="body1" color="error.main" align="center">
          {errorMessage}
        </Typography>
      )}

      <Formik
        initialValues={loginFormValues}
        validationSchema={validationSchema}
        onSubmit={onSubmit}
      >
        {({ errors, touched }) => (
          <Form style={{ width: '300px' }}>
            <Box mb={2}>
              <Field
                as={TextField}
                label="Username"
                name="username"
                fullWidth
                error={touched.username && Boolean(errors.username)}
                helperText={touched.username && errors.username}
              />
            </Box>
            <Box mb={2}>
              <Field
                as={TextField}
                label="Password"
                name="password"
                type="password"
                fullWidth
                error={touched.password && Boolean(errors.password)}
                helperText={touched.password && errors.password}
              />
            </Box>
            <Button
              type="submit"
              variant="contained"
              color="primary"
              fullWidth
            >
              Login
            </Button>
          </Form>
        )}
      </Formik>
    </Box>
  );
};

export default Login;