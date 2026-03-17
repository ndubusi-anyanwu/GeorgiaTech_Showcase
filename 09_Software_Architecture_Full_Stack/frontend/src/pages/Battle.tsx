import { useParams } from 'react-router-dom';
import { useGet } from '../api/useFetch';
import { useEffect } from 'react';
import { Battle as BattleType } from '../types';
import Typography from '@mui/material/Typography';
import Stack from '@mui/material/Stack';
import BattleCarousel from '../components/Battle/BattleCarousel';

const Battle = () => {
  const { battleId } = useParams();
  const { result: battle, trigger } = useGet(`battle/${battleId}`);
  useEffect(() => {
    trigger();
  }, []);

  if (!battle) return <Typography>Loading...</Typography>;

  const { isTournament } = battle as BattleType;

  return (
    <Stack direction="column" spacing={3}>
      <Typography variant="h1">
        {isTournament ? 'Tournament' : 'Battle'}
      </Typography>
      <Typography variant="h2">
        {isTournament
          ? 'Welcome to the thunder dome!'
          : 'Welcome to the battle!'}
      </Typography>
      <BattleCarousel battle={battle as BattleType} />
    </Stack>
  );
};

export default Battle;
