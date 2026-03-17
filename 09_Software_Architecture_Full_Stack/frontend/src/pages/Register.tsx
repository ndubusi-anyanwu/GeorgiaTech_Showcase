import { useEffect, useState } from 'react';
import { Container, Typography, TextField, Button, Box } from '@mui/material';
import { usePost } from '../api/useFetch';
import * as yup from 'yup';
import { Formik, Form, Field } from 'formik';
import { useNavigate } from 'react-router-dom';

const registrationFormValues = {
  username: '',
  firstName: '',
  lastName: '',
  email: '',
  password: '',
};

function Register() {
  const [successMessage, setSuccessMessage] = useState('');
  const [errorMessage, setErrorMessage] = useState('');
  const { isError, isSuccess, trigger, result } = usePost('api/auth/register');
  const navigate = useNavigate();

  const validationSchema = yup.object({
    username: yup
      .string()
      .required('Username is required')
      .max(50, 'Username must be at most 50 characters'),
    firstName: yup.string().required('First name is required'),
    lastName: yup.string().required('Last name is required'),
    email: yup
      .string()
      .email('Invalid email format')
      .required('Email is required'),
    password: yup
      .string()
      .min(8, 'Password must be at least 8 characters')
      .required('Password is required'),
  });

  useEffect(() => {
    if (isSuccess) {
      if (result.isSuccess) {
        setSuccessMessage(result.message);
        setErrorMessage('');
         // Redirect to a log
        navigate('/login');
      }
      else {
        setErrorMessage(result.message);
        setSuccessMessage('');
      }
    } else if (isError) {
      setSuccessMessage('');
      setErrorMessage('Registration failed. Please try again.');
    }
  });

  const onSubmit = async (formData: typeof registrationFormValues) => {
    try {
      await trigger(formData);
    } catch (error) {
      setErrorMessage('An error occurred. Please try again later.');
      setSuccessMessage('');
    }
  };

  return (
    <Container maxWidth="sm">
      <Box sx={{ display: 'flex', flexDirection: 'column', gap: 2, mt: 4 }}>
        <Typography variant="h4" align="center">
          Register
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
          initialValues={registrationFormValues}
          validationSchema={validationSchema}
          onSubmit={onSubmit}
        >
          {({ isSubmitting, errors, touched }) => (
            <Form>
              <Box sx={{ mb: 2 }}>
                <Field
                  name="username"
                  as={TextField}
                  label="Username"
                  variant="outlined"
                  fullWidth
                  error={touched.username && !!errors.username}
                  helperText={touched.username && errors.username}
                />
              </Box>

              <Box sx={{ mb: 2 }}>
                <Field
                  name="firstName"
                  as={TextField}
                  label="First Name"
                  variant="outlined"
                  fullWidth
                  error={touched.firstName && !!errors.firstName}
                  helperText={touched.firstName && errors.firstName}
                />
              </Box>

              <Box sx={{ mb: 2 }}>
                <Field
                  name="lastName"
                  as={TextField}
                  label="Last Name"
                  variant="outlined"
                  fullWidth
                  error={touched.lastName && !!errors.lastName}
                  helperText={touched.lastName && errors.lastName}
                />
              </Box>

              <Box sx={{ mb: 2 }}>
                <Field
                  name="email"
                  as={TextField}
                  label="Email"
                  variant="outlined"
                  fullWidth
                  error={touched.email && !!errors.email}
                  helperText={touched.email && errors.email}
                />
              </Box>

              <Box sx={{ mb: 2 }}>
                <Field
                  name="password"
                  as={TextField}
                  label="Password"
                  variant="outlined"
                  type="password"
                  fullWidth
                  error={touched.password && !!errors.password}
                  helperText={touched.password && errors.password}
                />
              </Box>

              <Button
                type="submit"
                variant="contained"
                color="primary"
                fullWidth
                disabled={isSubmitting}
              >
                {isSubmitting ? 'Registering...' : 'Register'}
              </Button>
            </Form>
          )}
        </Formik>
      </Box>
    </Container>
  );
}

export default Register;
