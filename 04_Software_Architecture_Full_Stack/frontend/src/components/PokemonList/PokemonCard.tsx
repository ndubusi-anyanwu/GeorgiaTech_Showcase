import { Pokemon } from '../../types';
import Stat from './Stat';
import CardSection from './CardSection';
import Chip from '@mui/material/Chip';
import Stack from '@mui/material/Stack';

type PokemonCardProps = {
  pokemon: Pokemon | null;
  onClose: () => void;
};

const PokemonCard = ({ pokemon, onClose }: PokemonCardProps) => {
  if (!pokemon) return;

  const {
    id,
    name,
    types,
    weaknesses,
    attackSkills,
    defenseSkills,
    gender,
    spriteUrl,
    ...stats
  } = pokemon;

  const isUnknown = gender === 2;

  return (
    <div
      style={{
        display: 'flex',
        flexDirection: 'column',
        backgroundColor: 'grey',
        borderRadius: '0.25rem',
        padding: '1rem',
        position: 'absolute',
        top: '3rem',
        right: '2rem',
        width: '40%',
        justifyContent: 'left',
      }}
    >
      <button onClick={onClose} style={{ width: '8rem' }}>
        Close
      </button>
      <img
        style={{
          width: 128,
          height: 128,
        }}
        src={spriteUrl}
      />
      <Stack
        direction="row"
        spacing={0.5}
        sx={{ marginTop: 2, marginBottom: 1 }}
      >
        <h2 style={{ marginRight: `${isUnknown ? 0.5 : 0.25}rem` }}>{name}</h2>
        {!isUnknown && (
          <img
            src={`${gender ? 'female' : 'male'}.svg`}
            style={{ width: '1rem', height: '1rem', marginRight: '0.25rem' }}
          />
        )}
        {types.map((type, index) => (
          <Chip key={index} label={type} variant="outlined" />
        ))}
      </Stack>
      <Stack direction="row" spacing={0.5}>
        {weaknesses.map((type, index) => (
          <Chip key={index} label={type} />
        ))}
      </Stack>
      <CardSection label="Attacks">
        {attackSkills.map((attack, index) => (
          <Stat key={index} label={attack.name}>
            {attack.damage}
          </Stat>
        ))}
      </CardSection>
      <CardSection label="Defenses">
        {defenseSkills.map((defense, index) => (
          <Stat key={index} label={defense.name}>
            {defense.damageReduction}
          </Stat>
        ))}
      </CardSection>
      <CardSection label="Stats">
        {Object.keys(stats).map((stat, index) => (
          <Stat key={index} label={stat}>
            {stats[stat as keyof typeof stats]}
          </Stat>
        ))}
      </CardSection>
    </div>
  );
};

export default PokemonCard;
