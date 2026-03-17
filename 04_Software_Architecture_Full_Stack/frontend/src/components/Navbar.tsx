import Stack from '@mui/material/Stack';
import { NavLink } from 'react-router-dom';

const userRole = sessionStorage.getItem("user-role");

const Navbar = () => {
  return (
    <Stack
      direction="column"
      sx={{
        flexDirection: 'column',
        height: '100%',
        borderRight: '2px solid gray',
      }}
      spacing="8rem"
      alignContent="center"
      justifyContent="center"
    >
      <NavLink to="/battle">Battle</NavLink>
      <NavLink to="/pokemon">Pokemon</NavLink>
      {userRole === "ADMIN" && <NavLink to="/users">Users</NavLink>}
    </Stack>
  );
};

export default Navbar;
