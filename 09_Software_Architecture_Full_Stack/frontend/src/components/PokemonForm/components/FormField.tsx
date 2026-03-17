import { Field, useField } from 'formik';
import { PropsWithChildren } from 'react';

type FormFieldProps = {
  label?: string;
  name: string;
  type?: 'select' | 'number' | 'text';
} & PropsWithChildren;

const FormField = ({
  children,
  label,
  name,
  type = 'text',
}: FormFieldProps) => {
  const [, { touched, error }] = useField(name);

  const hasError = touched && error;

  return (
    <div
      style={{
        display: 'flex',
        flexDirection: 'column',
        marginBottom: hasError ? 0 : '2rem',
        textAlign: 'left',
      }}
    >
      <label style={{ marginBottom: 4 }} htmlFor={name}>
        {label ?? name}
      </label>
      {type === 'select' ? (
        <Field name={name} as="select">
          {children}
        </Field>
      ) : (
        <Field name={name} type={type} />
      )}
      {hasError && (
        <p style={{ color: 'red', marginTop: 0, marginBottom: '0.5rem' }}>
          {error}
        </p>
      )}
    </div>
  );
};

export default FormField;
