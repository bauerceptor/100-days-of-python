#	Challenge 1: Count the length of each word in the sentence

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

word_length = {word:len(word) for word in sentence.split()}
print(word_length)

#	Challenge 2: Convert the given temperatures from Centigrade to Fahrenheit

weather_c = {
	"Monday": 12,
	"Tuesday": 14,
	"Wednesday": 15,
	"Thursday": 14,
	"Friday": 21,
	"Saturday": 22,
	"Sunday": 24,
}

weather_f = {day:((temp_c * 9/5) + 32) for (day, temp_c) in weather_c.items()}

print(weather_f)
