# Conversation Editor

*@todo: add a screenshot of the editor here.*

A node editor for creating and editing dialogue trees which can be exported in an easy-to-understand and easy-to-use JSON structure.

# Example Conversation JSON Structure

```json
{
    "name": "Conversation Name",
    "description": "Description of the conversation",
    "nodes": [{
        "speaker": "Doctor",
        "text": "Hey there, how can I help you?"
    }, {
        "speaker": "Player",
        "text": "I'm not feeling too great. Can you take a look at me?"
    }, {
        "operator": "==",
        "attribute": "Health",
        "value": 100
    }, {
        "speaker": "Doctor",
        "text": "Doesn't seem like you have any wounds on you. What are your symptoms?"
    }, {
        "speaker": "Doctor",
        "text": "Well here's your problem! You're missing a leg!"
    }],
    "connections": [
        [1],
        [2],
        [3, 4],
        [],
        []
    ]
}
```


# Description of Conversation JSON Structure

The `Conversation` object acts as a container for all objects related to a conversation, including meta fields used to hold data for the editor and developers' convenience.

## Conversation Properties
| **Property Name** | **Type** | **Description** |
|---|---|---|
| name | string | Name of the conversation. |
| description | string | High-level description of the conversation. |
| nodes | array | Array of nodes within this conversation. |
| connections | array | Defines the connections between nodes. Each element of the array corresponds to the node at the same index in the nodes property. Each element contains a list of outgoing connections to indices within the nodes array. |

## Talk Nodes
`Talk Node` objects are used to store dialogue data.

### Properties
| **Property Name** | **Type** | **Description** |
|---|---|---|
| speaker | string | Name of the speaker. |
| text | string | Dialogue to be spoken. |


## Attribute Comparison Node
Attribute Comparison Nodes facilitate holding data for comparison in other software. It assumes the consumer of this data will parse the `operator`, `attribute` name and `value` to determine which branch to take. 

The operation should be executed with the `attribute` as the left-hand operand and `value` is the right-hand operand.

Below is an example of an Attribute Comparison Node and it's interpretation.

```json
// Is Health Less than 100
// Health < 100
{
    "comparison": "<",
    "attribute": "Health",
    "value": 100
}
```

### Properties
| **Property Name** | **Type** | **Description** |
|---|---|---|
| operator | string | Comparison operator to be used. |
| attribute | string | Name of the attribute to compare the value against. |
| value | int, string | The value to compare the attribute against. |
