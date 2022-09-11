# DagsHubApi.PutFile

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commitSummary** | **String** |  | [optional] 
**commitMessage** | **String** |  | 
**commitChoice** | **String** |  | [optional] 
**lastCommit** | **String** | if omitted only new files will be accepted | [optional] 
**newBranchName** | **String** |  | [optional] 
**versioning** | **String** |  | [optional] 
**files** | **[Object]** |  | [optional] 

<a name="CommitChoiceEnum"></a>
## Enum: CommitChoiceEnum

* `direct` (value: `"direct"`)
* `commitToNewBranch` (value: `"commit-to-new-branch"`)


<a name="VersioningEnum"></a>
## Enum: VersioningEnum

* `dvc` (value: `"dvc"`)
* `git` (value: `"git"`)

