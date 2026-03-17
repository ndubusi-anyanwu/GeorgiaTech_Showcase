CS 6310 Group 036 - Architectural Decision Record

Title: Authentication/Authorization - Addition of Users with passwords and varying permissions 

Status: Proposed

Context: Provide security to the Pokemon Tournament application. This added security will allow for our clients to utilize the application only if given access and will only allow them to use the application in a way they are meant to, with permission adjustments made by the Admin.

Decision: We will add security to the Pokemon application by adding a sign-in functionality with corresponding permissions. For permissions, there will be a general User who cannot create Pokemon, but only battle them. Then there will be a user with access to create additional Pokemon. Finally there will be an Admin that can create Pokemon but also can update other users' permissions. For authentication there will be 4 initial users created, two with the general user permission, one with access to create additional Pokemon, and one Admin. Usernames and passwords will be created for all 4 accounts, with the Admin having the ability to update the other 3 users' permissions. 

Consequences: Consequences of adding User authentication and authorization is increasing project scope, resulting in additional time (and cost from a business perspective) required to implement correctly. This could further increase future work required to maintain these users if additional access needs to be granted for new users or if authorization for a client changes. 
