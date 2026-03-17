import Button from '@mui/material/Button';
import Stack from '@mui/material/Stack';
import Typography from '@mui/material/Typography';
import { Form, Formik } from 'formik';
import { useNavigate } from 'react-router-dom';
import { getInitialValues, mapValuesToRequest, schema } from './lib/formValues';
import { useGet, usePost } from '../../api/useFetch';
import { useEffect } from 'react';
import SeedField from './SeedField';
import PokemonDraft from './PokemonDraft';
import SubmitButton from './SubmitButton';
import NumberField from './NumberField';
import BackgroundCarousel from './BackgroundCarousel';

type BattleFormProps = {
  isTournament: boolean;
  onClose: () => void;
};

const BattleForm = ({ isTournament, onClose }: BattleFormProps) => {
  const navigate = useNavigate();
  const { result: pokemonList, trigger } = useGet('battle/pokemon');
  const { result: battleId, trigger: initBattle } = usePost('battle');

  useEffect(() => {
    trigger();
  }, []);

  useEffect(() => {
    battleId && navigate(`/battle/${battleId}`);
  }, [battleId]);

  const type = isTournament ? 'tournament' : 'battle';

  if (!pokemonList || pokemonList.length < 2) return;

  return (
    <Stack
      direction="column"
      spacing={5}
      justifyContent="left"
      sx={{ paddingTop: '2rem', paddingX: '2rem' }}
    >
      <Button onClick={onClose} sx={{ width: '8rem' }} variant="outlined">
        Back
      </Button>
      <Stack direction="column" justifyContent="center" spacing={1}>
        <Typography variant="h4">Select the pokemon for your {type}</Typography>
        <Formik
          initialValues={getInitialValues(pokemonList, isTournament)}
          validationSchema={schema}
          onSubmit={(values) => initBattle({ ...mapValuesToRequest(values) })}
        >
          {({ values }) => (
            <Form>
              <PokemonDraft
                isTournament={isTournament}
                pokemonList={pokemonList}
              />
              <SeedField />
              <NumberField name="maxTurns" placeholder="12" />
              <BackgroundCarousel />
              <SubmitButton disabled={!!(values.pokemon.length % 2)}>
                Start the {type}
              </SubmitButton>
            </Form>
          )}
        </Formik>
      </Stack>
    </Stack>
  );
};

export default BattleForm;
