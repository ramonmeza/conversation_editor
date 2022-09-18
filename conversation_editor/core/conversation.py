from dataclasses import dataclass, field


@dataclass
class Conversation:
    """Contains all information related to a conversation.

    This class acts as a container for all objects related to a conversation,
    including meta fields used to hold data for the editor and developers'
    convenience.

    Attributes:
        name (str):         Name of the conversation.
        
        description (str): 	High-level description of the conversation.

        nodes (list):       Array of nodes within this conversation.

        connections (list): Defines the connections between nodes. Each element
                            of the array corresponds to the node at the same
                            index in the nodes property. Each element contains
                            a list of outgoing connections to indices within the
                            nodes array.
    """

    name: str = 'New Conversation'
    description: str = 'This is a conversation description.'
    nodes: list = field(default_factory=list)
    connections: list = field(default_factory=list)
