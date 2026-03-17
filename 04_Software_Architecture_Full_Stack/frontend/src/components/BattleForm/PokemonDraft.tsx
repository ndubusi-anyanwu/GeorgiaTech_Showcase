import { Field, FieldArray, useField } from 'formik';
import { BattlePokemonRequest, PokemonSummary, Temp } from '../../types';
import Stack from '@mui/material/Stack';
import Button from '@mui/material/Button';
import PokemonSelect from './PokemonSelect';

type PokemonDraftProps = {
  isTournament?: boolean;
  pokemonList: PokemonSummary[];
};

const PokemonDraft = ({ isTournament, pokemonList }: PokemonDraftProps) => {
  const [{ value: pokemon }, , { setValue }] =
    useField<BattlePokemonRequest[]>('pokemon');
  return (
    <FieldArray name="pokemon">
      {({ remove, push }) => (
        <Stack direction="column" spacing={1.5} justifyContent="center">
          {pokemon?.map((_, index) => (
            <Stack
              direction="row"
              key={index}
              spacing={1}
              sx={{ height: '2.5rem' }}
            >
              <PokemonSelect index={index} list={pokemonList} />
              <Field name={`pokemon.${index}.temperature`} as="select">
                <option value={Temp.Aggressive}>Aggressive</option>
                <option value={Temp.Balanced}>Balanced</option>
                <option value={Temp.Defensive}>Defensive</option>
              </Field>
              {isTournament && (
                <Button
                  disabled={pokemon?.length <= 4}
                  type="button"
                  onClick={() => remove(index)}
                  variant="outlined"
                >
                  Remove
                </Button>
              )}
            </Stack>
          ))}
          {isTournament && (
            <Button
              disabled={pokemon?.length >= pokemonList.length}
              type="button"
              onClick={() => {
                const unusedPokemon = pokemonList.filter((pl) =>
                  pokemon.every((p) => parseInt(p.id.split('-')[0]) !== pl.id)
                );

                if (unusedPokemon.length === 1 && !(pokemonList.length % 2)) {
                  push(unusedPokemon[0].name);
                } else if (pokemon?.length % 2) {
                  setValue([
                    ...pokemon,
                    {
                      id: `${unusedPokemon[0].id}-${unusedPokemon[0].template}`,
                      temperature: Temp.Balanced,
                    },
                  ]);
                } else {
                  setValue([
                    ...pokemon,
                    {
                      id: `${unusedPokemon[0].id}-${unusedPokemon[0].template}`,
                      temperature: Temp.Balanced,
                    },
                    {
                      id: `${unusedPokemon[0].id}-${unusedPokemon[0].template}`,
                      temperature: Temp.Balanced,
                    },
                  ]);
                }
              }}
              variant="outlined"
            >
              Draft another pokemon
            </Button>
          )}
        </Stack>
      )}
    </FieldArray>
  );
};

export default PokemonDraft;
