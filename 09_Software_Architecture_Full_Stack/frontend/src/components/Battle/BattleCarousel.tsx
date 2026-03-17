import { useState } from 'react';
import { Battle } from '../../types';
import BattleView from './BattleView';
import BattleSummary from './BattleSummary';
import Stack from '@mui/material/Stack';
import ArrowLeftIcon from '@mui/icons-material/ArrowLeft';
import ArrowRightIcon from '@mui/icons-material/ArrowRight';
import Button from '@mui/material/Button';

const BattleCarousel = ({ battle }: { battle: Battle }) => {
  const [currBattleIndex, setCurrBattleIndex] = useState(0);
  const { background, isTournament, pokemon, battles } = battle;
  const { comments, loser, winner } = battles[currBattleIndex];

  return (
    <Stack direction="row" spacing={1} justifyContent="space-around">
      {isTournament && (
        <Button
          onClick={() =>
            setCurrBattleIndex(
              (currBattleIndex - 1 + battles.length) % battles.length
            )
          }
          variant="outlined"
        >
          <ArrowLeftIcon />
        </Button>
      )}
      <Stack direction="column" width="80%" key={currBattleIndex}>
        <BattleView
          background={background}
          comments={comments}
          loser={pokemon[loser]!}
          winner={pokemon[winner]!}
        />
        <BattleSummary comments={comments} />
      </Stack>
      {isTournament && (
        <Button
          onClick={() =>
            setCurrBattleIndex((currBattleIndex + 1) % battles.length)
          }
          variant="outlined"
        >
          <ArrowRightIcon />
        </Button>
      )}
    </Stack>
  );
};

export default BattleCarousel;
