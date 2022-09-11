# PutFile

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commitSummary** | **String** |  |  [optional]
**commitMessage** | **String** |  | 
**commitChoice** | [**CommitChoiceEnum**](#CommitChoiceEnum) |  |  [optional]
**lastCommit** | **String** | if omitted only new files will be accepted |  [optional]
**newBranchName** | **String** |  |  [optional]
**versioning** | [**VersioningEnum**](#VersioningEnum) |  |  [optional]
**files** | **List&lt;Object&gt;** |  |  [optional]

<a name="CommitChoiceEnum"></a>
## Enum: CommitChoiceEnum
Name | Value
---- | -----
DIRECT | &quot;direct&quot;
COMMIT_TO_NEW_BRANCH | &quot;commit-to-new-branch&quot;

<a name="VersioningEnum"></a>
## Enum: VersioningEnum
Name | Value
---- | -----
DVC | &quot;dvc&quot;
GIT | &quot;git&quot;
