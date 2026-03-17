import { useField } from 'formik';
import { getWeaknesses, types } from '../lib/formValues';
import { useEffect } from 'react';
import { Type } from '../../../types';

const TypeSelect = () => {
  const [{ value: selectedTypes }, , { setValue: setTypes }] =
    useField<Type[]>('types');
  const [{ value: weaknesses }, , { setValue: setWeaknesses }] =
    useField<Type[]>('weaknesses');

  useEffect(() => {
    setWeaknesses(getWeaknesses(selectedTypes));
  }, [selectedTypes]);

  return (
    <div style={{ display: 'flex', flexDirection: 'row' }}>
      <div
        style={{
          display: 'flex',
          flexDirection: 'column',
          marginBottom: '2rem',
          textAlign: 'left',
          marginRight: '2rem',
        }}
      >
        <label style={{ marginBottom: 4 }}>Types</label>
        {types.map((typeName, type) => (
          <button
            type="button"
            disabled={
              selectedTypes.length === 2 && !selectedTypes.includes(type)
            }
            style={{
              backgroundColor: selectedTypes.includes(type)
                ? 'magenta'
                : 'grey',
              width: '10rem',
            }}
            key={type}
            onClick={() => {
              if (selectedTypes.includes(type)) {
                setTypes(
                  selectedTypes.filter(
                    (selectedType: number) => selectedType !== type
                  )
                );
              } else {
                setTypes([...selectedTypes, type]);
              }
            }}
          >
            {typeName}
          </button>
        ))}
      </div>
      <div
        style={{
          display: 'flex',
          flexDirection: 'column',
          marginBottom: '2rem',
          textAlign: 'left',
        }}
      >
        <label style={{ marginBottom: 4 }}>Weaknesses</label>
        {weaknesses.map((index, key) => (
          <p style={{ fontStyle: 'italic', lineHeight: 0.5 }} key={key}>
            {types[index]}
          </p>
        ))}
      </div>
    </div>
  );
};

export default TypeSelect;
