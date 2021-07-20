import os
def play_music():
     music_dir='D:\\Audio\\New Music\\party'
     songs=os.listdir(music_dir)
     random = os.startfile(os.path.join(music_dir, songs[1]))
     return 'playing music'


