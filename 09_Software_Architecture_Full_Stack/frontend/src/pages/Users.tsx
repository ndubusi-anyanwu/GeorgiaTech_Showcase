import Container from '@mui/material/Container';
import { useUsersList } from '../components/Users/useUsersList';
import CircularProgress from '@mui/material/CircularProgress';
import Typography from '@mui/material/Typography';
import TableContainer from '@mui/material/TableContainer';
import Paper from '@mui/material/Paper';
import Table from '@mui/material/Table';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import TableCell from '@mui/material/TableCell';
import TableBody from '@mui/material/TableBody';
import Select from '@mui/material/Select';
import MenuItem from '@mui/material/MenuItem';
import Button from '@mui/material/Button';
import IconButton from '@mui/material/IconButton';
import { TablePagination } from '@mui/material';
import DeleteIcon from "@mui/icons-material/Delete";

const Users = () => {
  const { isLoading, onDelete, onRoleChange, roles, users, handleChangePage, page, totalElements, rowsPerPage
    , handleUpdate, successMessage, errorMessage
  } = useUsersList();

  if (isLoading) {
    return (
      <Container style={{ textAlign: 'center', marginTop: '50px' }}>
        <CircularProgress />
        <Typography variant="h6" style={{ marginTop: '10px' }}>
          Loading users...
        </Typography>
      </Container>
    );
  }

  return (
    <Container style={{ marginTop: '20px' }}>
      <Typography variant="h4" gutterBottom>
        Users Management
      </Typography>
      {successMessage && (
        <Typography variant="body1" color="success.main" align="center">
          {successMessage}
        </Typography>
      )}
      {errorMessage && (
        <Typography variant="body1" color="error.main" align="center">
          {errorMessage}
        </Typography>
      )}
      {users.length === 0 ? (
        <Typography
          variant="h6"
          align="center"
          style={{ padding: "20px", color: "gray" }}
        >
          No users available to manage
        </Typography>
      ) : (
        <TableContainer component={Paper}>
          <Table>
            <TableHead>
              <TableRow>
                <TableCell>
                  <strong>Name</strong>
                </TableCell>
                <TableCell>
                  <strong>Role</strong>
                </TableCell>
                <TableCell>
                  <strong>Actions</strong>
                </TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {users.map((user, i) => (
                <TableRow key={i}>
                  <TableCell>{user.firstName} {user.lastName}</TableCell>
                  <TableCell>
                    <Select value={user.role?.id ?? '1'}
                      onChange={(e) => onRoleChange(user.id, parseInt(e.target.value.toString(), 10))}>
                      {roles.map((role) => (
                        <MenuItem key={role.id} value={role.id}>
                          {role.name}
                        </MenuItem>
                      ))}
                    </Select>
                  </TableCell>
                  <TableCell>
                    <Button
                      variant="contained"
                      color="primary"
                      onClick={() => handleUpdate(user.id)}
                    >
                      Update
                    </Button>
                  </TableCell>
                  <TableCell>
                    <IconButton
                      color="error"
                      aria-label="delete"
                      onClick={() => onDelete(user.id)}>
                      <DeleteIcon />
                    </IconButton>
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      )}
      {users.length === 0 ? ("") : (
        <TablePagination
          component="div"
          rowsPerPageOptions={[]}
          count={totalElements}// Total number of rows
          rowsPerPage={rowsPerPage} // Rows per page
          page={page} // Current page
          onPageChange={handleChangePage} // Page change handler
        />
      )}
    </Container>
  );
};

export default Users;
