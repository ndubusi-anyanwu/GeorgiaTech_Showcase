import { array, InferType, number, object, string } from 'yup';
import { PokemonSummary, Temp } from '../../../types';

export const schema = object({
  pokemon: array(object({ id: string(), temperature: number() })).min(2),
  seed: number().positive().integer().optional(),
  maxTurns: number().positive().integer().optional(),
  background: string(),
});

export const getInitialValues = (
  pokemon: PokemonSummary[],
  isTournament: boolean
) => {
  const seed = sessionStorage.getItem('seed') ?? ('' as any);
  return {
    pokemon: isTournament
      ? [
          {
            id: `${pokemon[0].id}-${pokemon[0].template}`,
            temperature: Temp.Balanced,
          },
          {
            id: `${pokemon[1].id}-${pokemon[1].template}`,
            temperature: Temp.Balanced,
          },
          {
            id: `${pokemon[2].id}-${pokemon[2].template}`,
            temperature: Temp.Balanced,
          },
          {
            id: `${pokemon[3].id}-${pokemon[3].template}`,
            temperature: Temp.Balanced,
          },
        ]
      : [
          {
            id: `${pokemon[0].id}-${pokemon[0].template}`,
            temperature: Temp.Balanced,
          },
          {
            id: `${pokemon[1].id}-${pokemon[1].template}`,
            temperature: Temp.Balanced,
          },
        ],
    seed,
    maxTurns: '' as any,
    background: 'path',
  };
};

export const mapValuesToRequest = ({
  pokemon,
  ...values
}: InferType<typeof schema>) => {
  return {
    pokemon: pokemon!.map(({ id: pid, temperature }) => {
      const [id, shouldInit] = pid!.split('-');
      return {
        id,
        shouldInit: shouldInit === 'true',
        temperature,
      };
    }),
    ...values,
  };
};
