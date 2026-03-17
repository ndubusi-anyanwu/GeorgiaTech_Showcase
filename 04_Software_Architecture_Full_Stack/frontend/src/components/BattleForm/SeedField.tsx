import { useField } from 'formik';
import { useEffect } from 'react';
import NumberField from './NumberField';

const SeedField = () => {
  const [{ value }] = useField('seed');

  useEffect(() => {
    sessionStorage.setItem('seed', value);
  }, [value]);

  return <NumberField name="seed" placeholder="12345" />;
};

export default SeedField;
