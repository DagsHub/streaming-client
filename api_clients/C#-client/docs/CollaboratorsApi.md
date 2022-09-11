# IO.Swagger.Api.CollaboratorsApi

All URIs are relative to *http://localhost:3000/api/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**AddCollaborator**](CollaboratorsApi.md#addcollaborator) | **PUT** /repos/{username}/{repo}/collaborators/{collaborator} | Add user as a collaborator
[**GetCollaborators**](CollaboratorsApi.md#getcollaborators) | **GET** /repos/{username}/{repo}/collaborators | Get collaborators
[**RemoveCollaborator**](CollaboratorsApi.md#removecollaborator) | **DELETE** /repos/{username}/{repo}/collaborators/{collaborator} | Delete collaborator

<a name="addcollaborator"></a>
# **AddCollaborator**
> void AddCollaborator (string username, string repo, string collaborator, CollaboratorsCollaboratorBody body = null)

Add user as a collaborator

### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class AddCollaboratorExample
    {
        public void main()
        {
            // Configure HTTP basic authorization: basicAuth
            Configuration.Default.Username = "YOUR_USERNAME";
            Configuration.Default.Password = "YOUR_PASSWORD";
            // Configure API key authorization: tokenAuth
            Configuration.Default.AddApiKey("token", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("token", "Bearer");

            var apiInstance = new CollaboratorsApi();
            var username = username_example;  // string | A DagsHub username
            var repo = repo_example;  // string | name of the repository
            var collaborator = collaborator_example;  // string | collaborator username
            var body = new CollaboratorsCollaboratorBody(); // CollaboratorsCollaboratorBody |  (optional) 

            try
            {
                // Add user as a collaborator
                apiInstance.AddCollaborator(username, repo, collaborator, body);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling CollaboratorsApi.AddCollaborator: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **string**| A DagsHub username | 
 **repo** | **string**| name of the repository | 
 **collaborator** | **string**| collaborator username | 
 **body** | [**CollaboratorsCollaboratorBody**](CollaboratorsCollaboratorBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="getcollaborators"></a>
# **GetCollaborators**
> void GetCollaborators (string username, string repo)

Get collaborators

### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class GetCollaboratorsExample
    {
        public void main()
        {
            // Configure HTTP basic authorization: basicAuth
            Configuration.Default.Username = "YOUR_USERNAME";
            Configuration.Default.Password = "YOUR_PASSWORD";
            // Configure API key authorization: tokenAuth
            Configuration.Default.AddApiKey("token", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("token", "Bearer");

            var apiInstance = new CollaboratorsApi();
            var username = username_example;  // string | A DagsHub username
            var repo = repo_example;  // string | name of the repository

            try
            {
                // Get collaborators
                apiInstance.GetCollaborators(username, repo);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling CollaboratorsApi.GetCollaborators: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **string**| A DagsHub username | 
 **repo** | **string**| name of the repository | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="removecollaborator"></a>
# **RemoveCollaborator**
> void RemoveCollaborator ()

Delete collaborator

### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class RemoveCollaboratorExample
    {
        public void main()
        {
            // Configure HTTP basic authorization: basicAuth
            Configuration.Default.Username = "YOUR_USERNAME";
            Configuration.Default.Password = "YOUR_PASSWORD";
            // Configure API key authorization: tokenAuth
            Configuration.Default.AddApiKey("token", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("token", "Bearer");

            var apiInstance = new CollaboratorsApi();

            try
            {
                // Delete collaborator
                apiInstance.RemoveCollaborator();
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling CollaboratorsApi.RemoveCollaborator: " + e.Message );
            }
        }
    }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
