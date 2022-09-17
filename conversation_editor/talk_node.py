from dataclasses import dataclass


@dataclass
class TalkNode:
    """Contains all data related to a single node of conversation.

    This class is used to store dialogue data.

    Attributes:
        speaker (str): Name of the speaker.
        text (str):    Dialogue to be spoken.
    """
    
    speaker: str = 'Default Name'
    text: str = 'Default dialogue text.'
