import Box from '@mui/material/Box';
import { Pokemon } from '../../types';
import { useEffect, useState } from 'react';
import Typography from '@mui/material/Typography';
import IconButton from '@mui/material/IconButton';
import ReplayIcon from '@mui/icons-material/Replay';
import FastForwardIcon from '@mui/icons-material/FastForward';
import PokeSprite from './PokeSprite';
import Stack from '@mui/material/Stack';
import backgrounds from '../backgrounds';

type BattleViewProps = {
  background: string;
  comments: string[];
  loser: Pokemon;
  winner: Pokemon;
};

const BattleView = ({
  background,
  comments,
  loser,
  winner,
}: BattleViewProps) => {
  const [cmtIndex, setCmtIndex] = useState(0);

  const lastCmt = comments.length - 1;

  useEffect(() => {
    const interval = setInterval(() => {
      setCmtIndex((prevIndex) => {
        if (prevIndex >= lastCmt) return lastCmt;
        return prevIndex + 1;
      });
    }, 3000);

    return () => clearInterval(interval);
  }, []);

  const actor = comments[cmtIndex].split(' ')[0];

  return (
    <Box
      sx={{
        backgroundImage: `url(${backgrounds[background]})`,
        backgroundSize: 'cover',
        backgroundPosition: 'center',
        height: '24rem',
        position: 'relative',
        alignContent: 'end',
      }}
    >
      <Box
        sx={{
          position: 'absolute',
          top: 16,
          left: 96,
          right: 96,
          width: 'auto',
          backgroundColor: '#0005',
          border: '2px solid darkgreen',
          borderRadius: '8px',
          paddingY: '1rem',
        }}
      >
        <Typography sx={{ color: 'primary.contrastText' }}>
          {comments[cmtIndex]}
        </Typography>
      </Box>
      <PokeSprite
        active={actor === winner.name}
        side="left"
        url={winner.spriteUrl}
      />
      <PokeSprite
        active={actor === loser.name}
        side="right"
        url={loser.spriteUrl}
      />
      <Stack sx={{ padding: '0.5rem' }} direction="row-reverse">
        {cmtIndex === lastCmt && (
          <IconButton onClick={() => setCmtIndex(0)} sx={{ color: '#777A' }}>
            <ReplayIcon />
          </IconButton>
        )}
        {cmtIndex > 2 && cmtIndex < lastCmt && (
          <IconButton
            onClick={() => setCmtIndex(lastCmt)}
            sx={{ color: '#777A' }}
          >
            <FastForwardIcon />
          </IconButton>
        )}
      </Stack>
    </Box>
  );
};

export default BattleView;
