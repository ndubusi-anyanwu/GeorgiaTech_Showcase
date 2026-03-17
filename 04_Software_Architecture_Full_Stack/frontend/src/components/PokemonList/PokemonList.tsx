import { useEffect, useState } from 'react';
import { useGet } from '../../api/useFetch';
import { Pokemon, PokemonName } from '../../types';
import PokemonCard from './PokemonCard';

type PokemonListProps = {
  onOpenForm: () => void;
};

const PokemonList = ({ onOpenForm }: PokemonListProps) => {
  const { isSuccess, result, trigger: getPokemonList } = useGet('pokemon/list');
  const { result: resultPokemon, trigger: getPokemon } = useGet('pokemon');

  const [selectedPokemon, setSelectedPokemon] = useState<Pokemon | null>(null);

  useEffect(() => {
    getPokemonList();
  }, []);

  useEffect(() => {
    setSelectedPokemon(resultPokemon);
  }, [resultPokemon]);

  const userRole = sessionStorage.getItem("user-role");

  return (
    <div
      style={{
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'center',
      }}
    >
      {(userRole === "ADMIN" || userRole === 'TRAINER') && <button
        onClick={onOpenForm}
        style={{ marginBottom: '2rem', height: '4rem' }}
      >
        Create a pokemon
      </button>}
      {isSuccess &&
        (result as PokemonName[]).map(({ id, name }, index) => (
          <button
            key={index}
            onClick={() => {
              if (resultPokemon?.id === id) {
                setSelectedPokemon(resultPokemon);
              } else {
                getPokemon(`id=${id}`);
              }
            }}
            style={{ marginBottom: '1rem', width: '20rem' }}
          >
            {name}
          </button>
        ))}
      <PokemonCard
        pokemon={selectedPokemon}
        onClose={() => setSelectedPokemon(null)}
      />
    </div>
  );
};

export default PokemonList;
