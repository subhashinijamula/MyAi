from pygame import mixer as mix
mix.init()
def play_song(path):
    mix.music.load(path)
    mix.music.play()
    mix.music.set_volume(0.5)
def control(inp):
    if(inp=="stop"):
        mix.music.stop()
    elif(inp=="pause"):
        mix.music.pause()
    elif(inp=="play"):
        mix.music.play()
    elif(inp=="unpause"):
        mix.music.unpause()
# play_song(r"C:\Users\jamul\Downloads\song.mp3")
# while True:
#     inp=input("enter control:")
#     control(inp)
# if __name__=="__main__":
#     print("iam inside song.py")
if __name__=="song":
    print("sample is imported")