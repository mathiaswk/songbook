"""Utility functions for Songbook.

A one line summary of the module or program, terminated by a period.
"""

import os

def get_song_list(songs_dir):
    """
    Todo
    """
    songs = []
    for root, dirs, files in os.walk(songs_dir):
        for file in files:
            if os.path.splitext(file) == '.cho':
                songs.append(os.join(root, file))
    return files
