import vlc, os, keyboard
from copy import copy

dirs = {
	1: '1_Poems',
	2: '2_Interview',
	3: '3_Smithy',
	4: '4_Arts',
}

def play(player: vlc.MediaListPlayer, num: int):
	instance = player.get_instance()
	media_list = instance.media_list_new()
	path = dirs[num]
	files = os.listdir(path)
	for file_ in files:
		if file_ != '.gitignore':
			media_list.add_media(instance.media_new(os.path.join(path, file_)))

	player.set_media_list(media_list)
	player.play_item_at_index(0)

def main():
	instance = vlc.Instance('--fullscreen', '--no-xlib')
	player = instance.media_list_player_new()
	player.get_media_player().toggle_fullscreen()

	for k, _ in dirs.items():
		keyboard.add_hotkey(str(k), play, args=[player, k])
	keyboard.add_hotkey('F11', player.get_media_player().toggle_fullscreen)

	play(player, list(dirs.keys())[0])

	keyboard.wait('esc')
	player.stop()

if __name__ == '__main__':
    main()
