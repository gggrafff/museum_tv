# Museum TV

There is a famous man in Yekaterinburg, Alexander Andreevich Lysyakov: a blacksmith, an artist, and a writer. He's a great guy. He's making his own museum and really wants interactive TV there. He asked for help.

We put on a TV, a set-top box or a computer with a program. And there are videos in several folders on the computer.

Example:
1. Poems and fairy tales
2. The interview
3. The Forge
4. The Arts

It is necessary to mount several buttons (for example, these may be pins from a PC keyboard). So that when you press one, playback starts from folder (1), and when you press 3, playback starts from folder (3).

**This script monitors keystrokes and controls the vlc player to switch playlists.**

## How to run

1) You need python 3.12 or greater and poetry tool
2) Execute `poetry install` to install dependencies
3) If you use linux, add necessary rights:
```
sudo usermod -a -G input USERNAME
sudo usermod -a -G tty USERNAME
sudo reboot
```
4) Put video files to directories. If you use your own directory names, then fix the config in the `show.py` file.
5) Execute `poetry run python show.py`
6) Press 1, 2, 3, 4 to switch playlists or esc to exit.

## TODO
 * Pack this program by pyinstaller to one executable file
 * Add some default screen or subtitles with instructions
 * Add next video and previous video hotkeys
