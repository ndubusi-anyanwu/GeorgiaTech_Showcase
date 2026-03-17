import { Role } from "./Role";

export class User {
    id: BigInt;
    firstName: string;
    lastName: string;
    role: Role;

    constructor(id: BigInt, firstName: string, lastName: string, role: Role) {
        this.id = id;
        this.firstName = firstName;
        this.lastName = lastName;
        this.role = role;
    }
}
