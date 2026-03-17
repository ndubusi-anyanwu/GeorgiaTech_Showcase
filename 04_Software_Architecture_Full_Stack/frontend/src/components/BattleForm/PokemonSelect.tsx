import { Field, useField } from 'formik';
import { BattlePokemonRequest, PokemonSummary } from '../../types';
import { useMemo } from 'react';

type Props = {
  index: number;
  list: PokemonSummary[];
};

const PokemonSelect = ({ index, list }: Props) => {
  const [{ value: pokemon }] = useField<BattlePokemonRequest[]>('pokemon');

  const listOptions = useMemo(() => {
    let firstTemplate = list.findIndex(
      (p, i, l) => i > 0 && p.template && !l[i - 1].template
    );
    if (firstTemplate === -1) firstTemplate = 0;

    const veteranOptions = list
      .slice(0, firstTemplate)
      .map(({ id, name, wins }, i) => (
        <option
          key={i}
          value={`${id}-false`}
          disabled={pokemon.some((p) => {
            const [pid, shouldInit] = p.id.split('-');
            return parseInt(pid) === id && shouldInit === 'false';
          })}
        >
          {name} | won {wins} battles
        </option>
      ));
    const templateOptions = list.slice(firstTemplate).map(({ id, name }, i) => (
      <option key={i} value={`${id}-true`}>
        {name}
      </option>
    ));

    if (veteranOptions.length) {
      return (
        <>
          <optgroup label="Veterans">{veteranOptions}</optgroup>
          <optgroup label="Templates">{templateOptions}</optgroup>
        </>
      );
    }

    return templateOptions;
  }, [pokemon]);

  return (
    <Field name={`pokemon.${index}.id`} as="select">
      {listOptions}
    </Field>
  );
};

export default PokemonSelect;
