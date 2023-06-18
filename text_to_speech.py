from gtts import gTTS
import os
import sys
import shutil 


gdrive_dir = "/Users/yusukeomura/yusuke-omura@ours-blanc.art - Google Drive/My Drive/Share/English"
args = sys.argv
arg1 = args[1]
file_name = os.path.basename(arg1)
print(file_name)
file_title = arg1.split('.')[0]

with open(arg1, "r") as file:
    file_text = file.read()

print(file_text)

tts = gTTS(file_text)

# save file to gdrive
shutil.copy(arg1, f"{gdrive_dir}/{file_name}")
tts.save(f"{gdrive_dir}/{file_title}.mp3")