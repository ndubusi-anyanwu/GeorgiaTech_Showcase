import Accordion from '@mui/material/Accordion';
import AccordionDetails from '@mui/material/AccordionDetails';
import AccordionSummary from '@mui/material/AccordionSummary';
import Typography from '@mui/material/Typography';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';

type BattleSummaryProps = {
  comments: string[];
};

const BattleSummary = ({ comments }: BattleSummaryProps) => (
  <Accordion sx={{ marginTop: '1rem' }}>
    <AccordionSummary expandIcon={<ExpandMoreIcon />}>Summary</AccordionSummary>
    <AccordionDetails sx={{ textAlign: 'left' }}>
      {comments.map((comment, i) => (
        <Typography
          key={i}
          fontWeight={600}
          lineHeight={1.5}
          sx={{ backgroundColor: i % 2 ? 'lightgrey' : '' }}
        >
          {comment}
        </Typography>
      ))}
    </AccordionDetails>
  </Accordion>
);

export default BattleSummary;
