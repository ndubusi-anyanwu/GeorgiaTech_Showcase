import { Form, Formik } from 'formik';
import { initialValues, schema } from './lib/formValues';
import FormField from './components/FormField';
import TypeSelect from './components/TypeSelect';
import SkillSelect from './components/SkillSelect';
import { Pokemon } from '../../types';
import { usePost } from '../../api/useFetch';

type PokemonFormProps = {
  onClose: () => void;
};

const PokemonForm = ({ onClose }: PokemonFormProps) => {
  const { trigger: savePokemon } = usePost<Pokemon>('pokemon', onClose);

  return (
    <Formik
      initialValues={initialValues}
      validationSchema={schema}
      onSubmit={(values) => savePokemon(values)}
    >
      {({ isValid }) => (
        <Form>
          <div
            style={{ display: 'flex', flexDirection: 'column', width: '20rem' }}
          >
            <button onClick={onClose} type="button">
              Back
            </button>
            <FormField name="name" />
            <TypeSelect />
            <SkillSelect name="attack" />
            <SkillSelect name="defense" />
            {/* STATS */}
            <FormField name="hp" type="number" />
            <FormField name="attack" type="number" />
            <FormField name="defense" type="number" />
            <FormField name="specialAttack" type="number" />
            <FormField name="specialDefense" type="number" />
            <FormField name="speed" type="number" />
            <FormField name="critRate" type="number" />
            <FormField name="height" type="number" />
            <FormField name="weight" type="number" />
            <FormField name="category" />
            <FormField name="abilities" />
            <FormField name="gender" type="select">
              <option value={0}>Male</option>
              <option value={1}>Female</option>
              <option value={2}>Unknown</option>
            </FormField>
            {/* SUBMIT */}
            <button disabled={!isValid} type="submit">
              Save
            </button>
          </div>
        </Form>
      )}
    </Formik>
  );
};

export default PokemonForm;
