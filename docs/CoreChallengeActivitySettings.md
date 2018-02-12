# CoreChallengeActivitySettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**boot_in_play** | **bool** | Whether the host can boot a user while the status is PLAYING. Null to inherit from activity | [optional] 
**custom_launch_address** | **str** | A custom address (url, ip or whatever is needed in your game) that users should connect to to play in this challenge rather than the usual game server. Max length: 255 | [optional] 
**custom_launch_address_allowed** | **bool** | Restriction for whether the host creating an occurrence can specify a custom launch address (such as their own ip address). Will override the challenge&#39;s custom_launch_address if they do. Null to inherit from activity | [optional] 
**host_option** | **str** | Restriction for who can host an occurrence. admin disallows regular users, player means the user must also be a player in the occurrence if not admin, non-player means the user has the option to host without being a player. Null to inherit | [optional] 
**host_status_control** | **bool** | Restriction for whether the host has control of the status once the game launches. If false they can only manage the game before (when setup and open). Max length: 255. Null to inherit from activity | [optional] 
**join_in_play** | **bool** | Whether users can join while the status is PLAYING. Null to inherit from activity | [optional] 
**leave_in_play** | **bool** | Whether users can leave while the status is PLAYING. Null to inherit from activity | [optional] 
**max_players** | **int** | The maximum number of players the game can hold. Null to inherit from activity | [optional] 
**min_players** | **int** | The minimum number of players the game can hold. Null to inherit from activity | [optional] 
**results_trust** | **str** | Restriction for who is able to report game end and results. Admin is always able to send results as well. Null to inherit from activity | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


