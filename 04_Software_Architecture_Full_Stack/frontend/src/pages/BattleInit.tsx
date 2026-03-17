import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Divider from '@mui/material/Divider';
import Stack from '@mui/material/Stack';
import Typography from '@mui/material/Typography';
import { useState } from 'react';
import BattleForm from '../components/BattleForm/BattleForm';

const battleBtnStyles = (selectedColor: string) => {
  const activeStyles = {
    backgroundColor: selectedColor,
    color: 'black',
    fontWeight: 700,
  };
  return {
    backgroundColor: 'grey',
    borderRadius: 0,
    width: '50%',
    height: '100%',
    fontSize: '2rem',
    '&.Mui-focusVisible': activeStyles,
    '&:hover': activeStyles,
  };
};

const BattleInit = () => {
  const [initType, setInitType] = useState<number | null>(null);

  return (
    <Box display="flex" flexDirection="column" height="100%">
      {initType === null ? (
        <>
          <Typography variant="h1">Battle</Typography>
          <Stack
            direction="row"
            divider={
              <Divider
                orientation="vertical"
                flexItem
                sx={{ width: '0.5rem' }}
              />
            }
            sx={{ width: '100%', height: '100%' }}
          >
            <Button
              disableFocusRipple
              onClick={() => setInitType(0)}
              sx={battleBtnStyles('red')}
              variant="contained"
            >
              Battle
            </Button>
            <Button
              disableFocusRipple
              onClick={() => setInitType(1)}
              sx={battleBtnStyles('yellow')}
              variant="contained"
            >
              Tournament
            </Button>
          </Stack>
        </>
      ) : (
        <BattleForm
          isTournament={initType === 1}
          onClose={() => setInitType(null)}
        />
      )}
    </Box>
  );
};

export default BattleInit;
