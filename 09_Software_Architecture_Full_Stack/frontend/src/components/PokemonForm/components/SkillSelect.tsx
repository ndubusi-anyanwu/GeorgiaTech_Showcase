import { FieldArray, useField } from 'formik';
import FormField from './FormField';

type SkillSelectProps = {
  name: 'attack' | 'defense';
};

const attackInit = { name: '', type: false, damage: 0 };
const defenseInit = { name: '', type: true, damageReduction: 0 };

const SkillSelect = ({ name }: SkillSelectProps) => {
  const fieldName = `${name}Skills`;
  const isAttack = name === 'attack';

  const [{ value: skills }] = useField<any[]>(fieldName);

  return (
    <div
      style={{
        display: 'flex',
        flexDirection: 'column',
        marginBottom: '2rem',
        textAlign: 'left',
      }}
    >
      <label style={{ marginBottom: 4 }}>{name}</label>
      <FieldArray
        name={fieldName}
        render={(arrayHelpers) => (
          <div>
            {skills.map((_skill, index) => (
              <div
                key={index}
                style={{ border: '1px solid grey', marginBottom: '0.5rem' }}
              >
                <FormField label="name" name={`${fieldName}.${index}.name`} />
                <FormField
                  label={isAttack ? 'damage' : 'damage reduction'}
                  name={`${fieldName}.${index}.${
                    isAttack ? 'damage' : 'damageReduction'
                  }`}
                  type="number"
                />
                <button
                  type="button"
                  onClick={() => arrayHelpers.remove(index)}
                >
                  -
                </button>
              </div>
            ))}
            <button
              type="button"
              onClick={() =>
                arrayHelpers.push(isAttack ? attackInit : defenseInit)
              }
            >
              +
            </button>
          </div>
        )}
      />
    </div>
  );
};

export default SkillSelect;
