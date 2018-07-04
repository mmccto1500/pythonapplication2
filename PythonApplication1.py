
favorite_languages = {
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python',
	}

for name in sorted(favorite_languages.keys()) :
    print(name.title() + ",thank you for taking the poll.")

for name in favorite_languages.keys() :
    print(name.title() + ",check the origin keys")

friends = ['phil','sarah']
for name in favorite_languages.keys():
	print(name.title())

	if name in friends:
		print(" Hi " + name.title() + ", I see your favorite language is " + favorite_languages[name].title()
		+ "!")

alien_0={'color':'green','points':5}
alien_1={'color':'yellow','points':10}
alien_2={'color':'green','points':5,'health':100}

aliens = [alien_0,alien_1,alien_2]

for alien in aliens:
    print(alien)



