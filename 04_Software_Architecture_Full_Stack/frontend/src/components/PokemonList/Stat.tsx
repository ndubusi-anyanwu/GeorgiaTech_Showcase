import { PropsWithChildren } from 'react';

type StatProps = {
  label: string;
} & PropsWithChildren;

const Stat = ({ children, label }: StatProps) => (
  <div
    style={{
      display: 'flex',
      flexDirection: 'column',
      marginRight: '0.5rem',
    }}
  >
    <p style={{ marginTop: '0rem', marginBottom: '0rem' }}>{label}</p>
    <p
      style={{
        marginTop: '0rem',
        marginBottom: '0.5rem',
        fontWeight: 800,
      }}
    >
      {children}
    </p>
  </div>
);

export default Stat;
