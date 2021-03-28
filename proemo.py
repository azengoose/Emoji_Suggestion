"""
A program to predict what emojis are appropriate for a message inputted by the user. 
Personally, I love being able to search and find the perfect emoji to use, but I'm sure 
some people can't be bothered and suggested emojis could  remove some friction from text 
messaging, and make it easier for someone to find the emoji perfectly expressing how they 
feel. 
Example 1: The weather sure is fine today. Prediction: 😁 👍 🥰
Example 2: These doggos are way too friggin' cute!!!! Prediction: 😭 😊 ❤️ 😍 🥰 🥺
Example 3: Lovin' this new product. Prediction: ❤️ 💕 😁 🔥
Example 4: Man I hate the way this update screws up the menu bar! 😒 😔 😩
REFERENCES 
	print("\N{grinning face with smiling eyes}") #😁 
	print("\N{face with tears of joy}") #😂 
	print("\u2764\uFE0F") #❤️ 
	print("\N{Smiling Face with Smiling Eyes}") #😊 
	print("\N{rolling on the floor laughing}") #🤣 
	print("\N{Person with Folded Hands}") #🙏 
	print("\N{thumbs up sign}") #👍 
	print("\N{Loudly Crying Face}") #😭 
	print("\N{Smiling Face with Heart-Shaped Eyes}") #😍 
	print("\N{sparkles}") #✨ 
	print("\N{Smiling Face with Smiling Eyes and Three Hearts}") #🥰 
	print("\N{Face with Pleading Eyes}") #🥺 
	print("\N{unamused face}") #😒 
	print("\N{pensive face}") #😔 
	print("\N{weary face}") #😩
	print("\N{Smiling Face with Open Mouth and Cold Sweat}") #😅 
	print("\N{fire}") #🔥 
	print("\N{thinking face}") #🤔 
	print("\N{two hearts}") #💕
	print("\N{Clapping Hands Sign}") #👏
"""
from textblob import TextBlob
import emoji

heart_words = ['love', 'luv', 'glad', 'gay', 'happy'] #how to give all stems, or does this work?
grinning_words = ['awesome', 'cool', 'sick', 'fantastic', 'fabulous']
cry_words = ['sad', 'depress','fuck']
unamused_words = ['shit', 'damn']

def predict_emoji():

	blob = TextBlob(text)
	sentiment_score = blob.sentiment.polarity 
	subjectivity = blob.sentiment.subjectivity
	print("\nsentiment: ", sentiment_score, ", subjectivity: ", subjectivity)

	if sentiment_score > 0.0:
		for x in heart_words:
			if x in text:
				return ("\N{two hearts}", "\N{Smiling Face with Smiling Eyes and Three Hearts}") #💕#🥰
		for x in grinning_words:
			if x in text:
				return ("\N{grinning face with smiling eyes}") #😁
		return ("\N{Smiling Face with Smiling Eyes}") #😊

	elif 0.2 > sentiment_score >= -.4:
		for x in heart_words:
			if x in text:
				return ("\u2764\uFE0F") #❤️ 
		return ("\N{thumbs up sign}") #👍

	else:
		for x in unamused_words:
			if x in text:
				return ("\N{unamused face}") #😒
		return ("\N{pensive face}") #😔

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

print(emoji.emojize("\nGreetings! :waving_hand:"))
print(emoji.emojize("\nI am an emoji suggestion program :robot:. My purpose is to help you find the perfect emoji for the occasion – no promises though... :upside-down_face:"))
print("If you want to know more about this program, please type in: 'info'")

text = input("\nEnter your message: ")
if text == 'info':
	print("\nThis program is based on a Python library called TextBlob, that provides a simple API that can perform basic NLP tasks. Due to the nature of the library, a more precise sentiment score will be given if you provide a longer message.")
	print("\nThe range for sentiment polarity is [-1.0:1.0], subjectivity is [0.0:1.0], where a lower subjectivity score signifies a more objective message.")
	text = input("\nEnter your message: ")

prediction = predict_emoji() 

print("Suggestion: {}".format(prediction))
print("Full message: ", text, prediction, "\n")

"""
EXAMPLES - CONTROLS
	What a great movie! 
			sentiment:  1.0 , subjectivity:  0.75

	This is great! Fantastic! Actually, I hate this. 
			sentiment:  0.2333333333333333 , subjectivity:  0.85
	
	What a terrible movie!
			sentiment: -1.0, subjectivity: 1.0
"""
