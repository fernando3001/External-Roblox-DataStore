local HttpMethodsService = {}
local HttpService = game:GetService("HttpService")

function HttpMethodsService.GetUsersFromMongoDB(user_ID)
	local apiUrl = "http://localhost:5000/users/?user_id=" .. user_ID
	
	local response = HttpService:GetAsync(apiUrl, true)
	local data = HttpService:JSONDecode(response)
	
	return data
end

function HttpMethodsService.addUserToMongoDB(userData)
	local url = "http://localhost:5000/users/"

	local headers = {
		["Content-Type"] = "application/json"
	}

	local success, response = pcall(HttpService.RequestAsync, HttpService, {
		Url = url,
		Method = "POST",
		Headers = headers,
		Body = HttpService:JSONEncode(userData)
	})

	if success and response.Success then
		print("User Added.")
	else
		print(response.StatusCode, response.StatusMessage)
	end
end

function HttpMethodsService.updateUserInMongoDB(userId, newData)
	local url = "http://localhost:5000/users/" .. userId 

	local headers = {
		["Content-Type"] = "application/json"
	}

	local success, response = pcall(HttpService.RequestAsync, HttpService, {
		Url = url,
		Method = "PUT",
		Headers = headers,
		Body = HttpService:JSONEncode(newData)
	})

	if success and response.Success then
		print("User Updated.")
	else
		print(response.StatusCode, response.StatusMessage)
	end
end


return HttpMethodsService
