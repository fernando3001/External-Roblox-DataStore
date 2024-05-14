# External Database Connection for Roblox Games

This project consists of an API developed with Flask that allows connecting an external database to Roblox games. In this case we will use mongo but you can use any other database you want.

## 🚨 IMPORTANT

- **ATTENTION!**: THIS PROJECT IS FOR PURE LEARNING PURPOSES ONLY. DO NOT USE IN PRODUCTION. SECURITY IS LOW, AND ANYONE CAN MANIPULATE IT.

## Installation

1. Clone this repository to your local machine.
2. Ensure you have Python and pip installed on your system.
3. Install the necessary dependencies.
4. Configure your connection to MongoDB (or other database you use) in your file by modifying the `url` variable with your MongoDB URL.

## Usage

1. Run the Flask application.
2. The API will be available on your LocalHost.

## Endpoints

- `GET /users/?user_id={user_id}`: Retrieves information for a specific user.
- `POST /users/`: Creates a new user.
- `PUT /users/{user_id}`: Updates information for an existing user.

For more details on the parameters and responses of each endpoint, refer to the source code in `endpoints.py`.

## Integration with Roblox

To integrate this API with your Roblox game, you can use Roblox's networking functions to make HTTP requests to the endpoints provided by the API. You can use GET, POST, and PUT requests to interact with the database and manage user data for your game.

Check the ModuleScript that is attached in the repository and use it as is (ModuleScript)

```lua
local HttpService = game:GetService("HttpService")
local HttpMethodsService = require(script.HttpMethodsService)

-- GET: Retrieve user data from MongoDB
local UserId = 111
HttpMethodsService.GetUsersFromMongoDB(UserId)

-- POST: Add new user information to MongoDB
local PostInformationFromUser = {
	user_id = 123456789, 
}
HttpMethodsService.addUserToMongoDB(PostInformationFromUser)

-- PUT: Update user data in MongoDB
local UserIdToUpdate = 692194040
local newPutDataFromUser = {
	Money = 1000,
	Cars = 231123
}
HttpMethodsService.updateUserInMongoDB(UserIdToUpdate, newPutDataFromUser)
```

## Contribution

Contributions are welcome! If you wish to contribute send me! Discord Below.

## License

This project is licensed under the MIT License.

## Contact

If you have any questions or suggestions about this project, feel free to contact me through my discord: fkooo.
