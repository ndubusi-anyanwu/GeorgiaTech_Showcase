import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Tooltip from '@mui/material/Tooltip';
import { PropsWithChildren } from 'react';

const SubmitButton = ({
  children,
  disabled,
}: { disabled: boolean } & PropsWithChildren) => (
  <Tooltip
    title="Only an even number of pokemon can be drafted!"
    followCursor
    disableFocusListener={!disabled}
    disableHoverListener={!disabled}
    disableInteractive={!disabled}
    disableTouchListener={!disabled}
  >
    <Box>
      <Button
        disabled={disabled}
        sx={{ height: '6rem', fontSize: '2rem' }}
        variant="contained"
        type="submit"
      >
        {children}
      </Button>
    </Box>
  </Tooltip>
);

export default SubmitButton;
