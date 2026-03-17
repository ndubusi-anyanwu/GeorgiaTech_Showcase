import { PropsWithChildren } from 'react';

type CardSectionProps = {
  label: string;
} & PropsWithChildren;

const CardSection = ({ children, label }: CardSectionProps) => (
  <>
    <h2>{label}</h2>
    <div
      style={{
        display: 'flex',
        flexDirection: 'row',
        alignItems: 'center',
        flexWrap: 'wrap',
      }}
    >
      {children}
    </div>
  </>
);

export default CardSection;
