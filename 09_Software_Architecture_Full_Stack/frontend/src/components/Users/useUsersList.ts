import { useEffect, useState } from 'react';
import { User } from './User';
import { useGet } from '../../api/useFetch';
import { Role } from './Role';

export const useUsersList = () => {
  const [users, setUsers] = useState<User[]>([]);
  const [roles, setRoles] = useState<Role[]>([]);
  const [page, setPage] = useState(0); // Current page
  const [totalElements, setTotalElements] = useState(0);
  const [rowsPerPage, setRowsPerPage] = useState(10);
  const [successMessage, setSuccessMessage] = useState('');
  const [errorMessage, setErrorMessage] = useState('');

  const {
    isError: isUsersError,
    isSuccess: isUsersSuccess,
    trigger: usersTrigger,
    result: usersResult,
  } = useGet('api/user/get');

  const {
    isError: isRolesError,
    isSuccess: isRolesSuccess,
    trigger: rolesTrigger,
    result: rolesResult,
  } = useGet('api/user/roles');

  const {
    isError: isUserUpdateError,
    isSuccess: isUserUpdateSuccess,
    trigger: userUpdateTrigger,
    result: userUpdateResult,
  } = useGet('api/user/updateRole');

  const {
    isError: isUserDeleteError,
    isSuccess: isUserDeleteSuccess,
    trigger: userDeleteTrigger,
    result: userDeleteResult,
  } = useGet('api/user/delete');

  const isLoading = !(
    (isUsersError || (isUsersSuccess && users.length >= 0)) &&
    (isRolesError || (isRolesSuccess && roles.length >= 0))
  );

  useEffect(() => {
    usersTrigger(`page=${page}`); // Pass the current page to usersTrigger
  }, [page, rowsPerPage]);

  useEffect(() => {
    rolesTrigger();
  }, []);

  useEffect(() => {
    if (usersResult && usersResult.totalCount > 0) {
      setUsers(
        usersResult.users.map(
          (user: any) =>
            new User(user.id, user.firstName, user.lastName, user.role)
        )
      );
      setTotalElements(usersResult.totalCount);
    } else {
      console.log('No users available.');
    }
  }, [usersResult]);

  useEffect(() => {
    if (rolesResult && rolesResult.length > 0) {
      setRoles(rolesResult.map((role: any) => new Role(role.id, role.name)));
    }
  }, [rolesResult]);

  const onRoleChange = (userId: BigInt, newRoleId: number) => {
    setUsers((prevUsers) =>
      prevUsers.map((user) =>
        user.id === userId
          ? {
              ...user,
              role: roles.find((role) => role.id === newRoleId) ?? roles[0],
            }
          : user
      )
    );
  };

  // Handle user deletion
  const onDelete = async (userId: BigInt) => {
    setUsers((prevUsers) => prevUsers.filter((user) => user.id !== userId));
    await userDeleteTrigger(`userId=${userId}`);
  };

  useEffect(() => {
    if (isUserDeleteSuccess) {
      if (userDeleteResult.isSuccess) {
        setSuccessMessage(userDeleteResult.message);
        setErrorMessage('');
      } else {
        setSuccessMessage('');
        setErrorMessage('Error deleting user role. Please try again Later.');
      }
    } else if (isUserDeleteError) {
      setSuccessMessage('');
      setErrorMessage('Error deleting user role. Please try again Later.');
    }
  }, [isUserDeleteSuccess, isUserDeleteError, userDeleteResult]);

  const handleChangePage = (_: any, newPage: number) => {
    setPage(newPage);
  };

  const handleChangeRowsPerPage = (event: any) => {
    setRowsPerPage(parseInt(event.target.value, 10));
    setPage(0); // Reset to the first page when rows per page changes
  };

  const handleUpdate = async (userId: BigInt) => {
    const user = users.find((x) => x.id == userId);
    if (user) {
      await userUpdateTrigger(`userId=${user.id}&&roleId=${user.role.id}`);
    }
  };

  useEffect(() => {
    if (isUserUpdateSuccess) {
      if (userUpdateResult.isSuccess) {
        setSuccessMessage(userUpdateResult.message);
        setErrorMessage('');
      } else {
        setSuccessMessage('');
        setErrorMessage('Error updating user role. Please try again Later.');
      }
    } else if (isUserUpdateError) {
      setSuccessMessage('');
      setErrorMessage('Error updating user role. Please try again Later.');
    }
  }, [isUserUpdateSuccess, isUserUpdateError, userUpdateResult]);

  return {
    isLoading,
    onDelete,
    onRoleChange,
    roles,
    users,
    handleChangePage,
    page,
    totalElements,
    handleChangeRowsPerPage,
    rowsPerPage,
    handleUpdate,
    successMessage,
    errorMessage,
  };
};
