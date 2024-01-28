from gtts import gTTS
import vlc
import os
import time

text = 'Features having a discrete set of possible values. For example, consider a categorical feature named house style, which has a discrete set of three possible values: Tudor, ranch, colonial. By representing house style as categorical data, the model can learn the separate impacts of Tudor, ranch, and colonial on house price. Sometimes, values in the discrete set are mutually exclusive, and only one value can be applied to a given example. For example, a car maker categorical feature would probably permit only a single value (Toyota) per example. Other times, more than one value may be applicable. A single car could be painted more than one different color, so a car color categorical feature would likely permit a single example to have multiple values (for example, red and white).Categorical features are sometimes called discrete features. Contrast with numerical data'

lang = 'en'

# gets current path
print('current path - ', os.getcwd())

# create gTTS object that takes in text, language and set slow speech to false
my_obj = gTTS(text=text, lang=lang, slow=False)
my_obj.save('what_is_categorical_data.mp3')

# setup vlc media player to play saved file
player = vlc.MediaPlayer('what_is_categorical_data.mp3')

# use created file, to get duration to feed into time.sleep()
media = vlc.Media('what_is_categorical_data.mp3')
media.parse()
duration = media.get_duration() / 1000 # get time in seconds

# plays the media for the duration that it would take to read it out , then stops the player
player.play()
time.sleep(duration)
player.stop()

