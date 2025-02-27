'''
Python module for Mopidy Pummeluff tags.
'''

__all__ = (
    'PlayPause',
    'Stop',
    'PreviousTrack',
    'NextTrack',
    'Shutdown',
    'Tracklist',
    'ToggleShuffle',
    'Volume',
)

from .playback import PlayPause, Stop, PreviousTrack, NextTrack
from .shutdown import Shutdown
from .tracklist import Tracklist, ToggleShuffle
from .volume import Volume

ACTIONS = {}
for action in __all__:
    ACTIONS[action] = globals()[action].__doc__.strip()
