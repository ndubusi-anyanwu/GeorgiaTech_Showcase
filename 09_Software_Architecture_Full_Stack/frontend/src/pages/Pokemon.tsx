import { useState } from 'react';
import PokemonForm from '../components/PokemonForm/PokemonForm';
import PokemonList from '../components/PokemonList/PokemonList';

const Pokemon = () => {
  const [isFormOpen, setIsFormOpen] = useState(false);

  return (
    <div style={{ margin: '2rem' }}>
      <h1>Pokemon</h1>
      {isFormOpen ? (
        <PokemonForm onClose={() => setIsFormOpen(false)} />
      ) : (
        <PokemonList onOpenForm={() => setIsFormOpen(true)} />
      )}
    </div>
  );
};

export default Pokemon;
