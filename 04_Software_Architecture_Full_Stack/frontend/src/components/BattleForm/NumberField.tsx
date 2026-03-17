import Button from '@mui/material/Button';
import FormLabel from '@mui/material/FormLabel';
import Stack from '@mui/material/Stack';
import Typography from '@mui/material/Typography';
import { ErrorMessage, Field, useField } from 'formik';
import { formatLabel } from './lib/formatLabel';

type NumberFieldProps = {
  name: string;
  placeholder: string;
};

const NumberField = ({ name, placeholder }: NumberFieldProps) => {
  const [{ value }, , { setValue }] = useField(name);

  return (
    <Stack justifyContent="left" sx={{ marginY: '1rem' }}>
      <FormLabel
        htmlFor={name}
        sx={{
          width: '12rem',
          textAlign: 'left',
          color: 'primary.contrastText',
        }}
      >
        {formatLabel(name)}
      </FormLabel>
      <Stack direction="row" spacing={1.5}>
        <Field name={name} type="number" placeholder={placeholder} />
        <Button disabled={!value} onClick={() => setValue('')}>
          Clear {name}
        </Button>
      </Stack>
      <Typography textAlign="left">
        <ErrorMessage name={name} />
      </Typography>
    </Stack>
  );
};

export default NumberField;
