import FormLabel from '@mui/material/FormLabel';
import Stack from '@mui/material/Stack';
import { Field } from 'formik';

const BackgroundCarousel = () => {
  return (
    <Stack justifyContent="left" sx={{ marginY: '1rem', width: '12rem' }}>
      <FormLabel
        htmlFor="background"
        sx={{ width: '2rem', color: 'primary.contrastText' }}
      >
        Background
      </FormLabel>
      <Field name="background" as="select" style={{ height: '2rem' }}>
        <option value="beach">Beach</option>
        <option value="cave">Cave</option>
        <option value="forest">Forest</option>
        <option value="gym1">Gym 1</option>
        <option value="gym2">Gym 2</option>
        <option value="gym3">Gym 3</option>
        <option value="path">Path</option>
        <option value="volcano">Volcano</option>
      </Field>
    </Stack>
  );
};

export default BackgroundCarousel;
