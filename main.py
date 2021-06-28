#!/usr/bin/env python3

import praw;
import time;
import random;
from credentials import SarumanCredentials;
from credentials import GaladrielCredentials;
from credentials import FrodoCredentials;

class Bot():
	def previously_responded(filename: str, comment_id: str) -> bool :
		with open(filename, 'r') as history:
			csv = history.read().splitlines()
			data = list(csv)

		if comment_id in data:
			print("Comment previously responded to. Skipping")
			return True
		else:
			return False

	def save_comment_id(filename: str, comment_id: str) -> None:
		with open(filename, 'a') as old_history:
			old_history.write(comment_id + '\n')

	def bind(c_id: str, c_secret: str,pw: str,u_name: str) -> object:
		api_bind = praw.Reddit(client_id=c_id,
				client_secret=c_secret,
				password=pw,
				user_agent='chat by /u/AutoCommentor',
				username=u_name)
		return api_bind; 

class Saruman(Bot):
	history_file = 'saruman_history.csv'

	
	def search() -> None:
		reddit = Saruman.bind(SarumanCredentials.client_id.value,SarumanCredentials.client_secret.value,SarumanCredentials.password.value,SarumanCredentials.username.value)

		for results in reddit.subreddit('lotrmemes').comments():
			print(results)
			body = results.body
			body=body.lower()
			comment_id = results.id
		
			found_general=body.find('saruman')
			found_theoden=body.find('i will draw you, saruman, as poison is drawn from a wound')
			found_theoden_isengard=body.find('you need not follow him. you were not always as you are now. you were once a man of rohan. come down')
			found_caradhas=body.find('spies of saruman. the passage south is being watched we must take the pass of caradhras')
			found_orcs=body.find('orcs')
			found_uruk=body.find('uruk')
			found_mountain_pass=body.find('it\'s saruman!')

			if Saruman.previously_responded(Saruman.history_file, comment_id):
				return "Skipped"

			else:
				if found_general != -1:
					Saruman.save_comment_id(Saruman.history_file, comment_id)

					if found_orcs != -1:
						print("Saruman orcs detected: {0}".format(body))
						try:
							results.reply('Do you know how the Orcs first came into being {0}? They were elves once, taken by the dark powers, tortured and mutilated. A ruined and terrible form of life. Now... perfected. My fighting Uruk-Hai. Whom do you serve?'.format(results.author))
							pass
						except Exception as e:
							print(e)
							break

					elif found_theoden != -1:
						print("Theoden detected: {0}".format(body))
						try:
							results.reply('If I go, Theoden Dies!')
							pass
						except:
							break

					elif found_caradhas != -1 and results.author == 'gandalf-bot':
						print("Caradhas detected: {0}".format(body))
						try:
							results.reply('So Gandalf, you try to lead them over Caradhras. And if that fails, where then will you go? If the mountain defeats you, will you risk a more dangerous road?')
							pass
						except:
							break

					elif found_mountain_pass != -1 and results.author == 'gandalf-bot':
						print("Caradhas detected: {0}".format(body))
						try:
							results.reply('Cuiva nwalca Carnirasse; nai yarvaxea rasselya! Cuiva nwalca Carnirasse; Nai yarvaxea rasselya; taltuva notto-carinnar!')
							pass
						except:
							break
	
					elif found_theoden_isengard != -1 and results.author == 'Theoden-Bot':
						print("Isengard detected: {0}".format(body))
						try:
							results.reply('A Man of Rohan? What is the House of Rohan, but a thatched barn, where brigards drink in the reek, and their brats roll on the floor with the dogs?! The victory at Helm\'s Deep does not belong to you, Theoden Horse Master! You are a lesser son of greater sires!')
							pass
						except:
							break
					else:
						print("General Saruman detected: {0}".format(results.body))
						try:
							results.reply(Saruman.random_comment(results.author))
							pass
						except:
							break
				else:
					pass


	def random_comment(author: str) -> str:
		QUOTES = ['Always You Must Meddle, Looking For Trouble Where None Exists.',
'Go now! Leave sauron to me.',
'The hour is later than you think.',
'You have elected the way of... Pain!',
'So you have chosen ... Death.',
'Who now has the strength to stand against the armies of Isengard ... And Mordor?',
'Rip them all down.',
'Moria... You fear to go into those mines. The Dwarves delved too greedily and too deep. You know what they awoke in the darkness of Khazad-dum... shadow and flame. ',
'Are you in need of assistance, {0}?'.format(author),
'Radagast the Bird-tamer! Radagast the Simple! Radagast the Fool!',
'Time? What time do you think we have?',
'They will find the Ring… and kill the one who carries it.',
'Your love of the Halfling’s leaf has clearly slowed your mind.',
'Against the power of Mordor there can be no victory.',
'The hour is later than you think. Sauron’s forces are already moving. The Nine have left Minas Morgul.',
'You did not seriously think that a Hobbit could contend with the will of Sauron, there are none that can.',
'Concealed within his fortress, the lord of Mordor sees all. His gaze pierces cloud, shadow, earth, and flesh. You know of what I speak, Gandalf: a great Eye, lidless, wreathed in flame.',
'Hunt them down. Do not stop until they are found. You do not know pain, you do not know fear. You will taste man-flesh!',
'Shall we not take council as we once did? Shall we not have peace?',
'Together, my lord {0}, we shall rule this Middle-earth. The old world will burn in the fires of industry. Forests will fall. A new order will rise. We will drive the machine of war with the sword and the spear and the iron fist of the orc.'.format(author),
'Gandalf the White. Gandalf the Fool! Does he seek to humble me with his newfound piety?',
'The Ring of Barahir. So Gandalf Greyhame thinks he’s found Isildur’s heir? The lost king of Gondor? He is a fool. The line was broken years ago. It matters not. The World of Men shall fall. It will begin at Edoras.',
'If the wall is breached, Helm’s Deep will fall.',
'You are sure of this?',
'{0} has regained much of his former strength. He cannot yet take physical form, but his spirit has lost none of its potency.'.format(author),
'I have seen it',
'I gave you the chance of aiding me willingly {0}. But you have elected the way of... pain!'.format(author),
'You have grown, {0}. Yes, you have grown very much. You are wise, and cruel. you have robbed my revenge of sweetness, and now I must go hence in bitterness, in debt to your mercy. I hate it and you! Well, I go and I will trouble you no more. But do not expect me to wish you health and long life. You will have neither. But that is not my doing. I merely foretell.'.format(author),
'A new power is rising! It\'s victory is at hand. This night, the land will be stained with the blood of Rohan! March to Helms Deep! Leave none alive! TO WAR!',
'There will be no dawn for men',
'Why? Why should we fear to use them?',
'Save your pity and your mercy! I have no use for it!',
'Smoke rises from the mountain of Doom. The hour grows late, and {0} rides to Isengard seeking my council. For that is why you have come, is it not?'.format(author),
'The power of Isengard is at your command, {0}, Lord of the Earth'.format(author),
'Embrace the power of the ring, or embrace your own destruction!'
]
		return random.choice(QUOTES)

class Galadriel(Bot):
	history_file = 'galadriel_history.csv'

	
	def search() -> None:
		reddit = Galadriel.bind(GaladrielCredentials.client_id.value,GaladrielCredentials.client_secret.value,GaladrielCredentials.password.value,GaladrielCredentials.username.value)

		for results in reddit.subreddit('lotrmemes').comments():
			print(results)
			body = results.body
			body=body.lower()
			comment_id = results.id
			
			found_general=body.find('galadriel')
	
			if Galadriel.previously_responded(Galadriel.history_file, comment_id):
				return "Skipped"

			else:
				if found_general != -1 and results.author != 'galadriel_bot':
					Galadriel.save_comment_id(Galadriel.history_file, comment_id)
					print("Galadriel detected: {0}".format(results.body))
					try:
						results.reply(Galadriel.random_comment(results.author))
						pass
					except:
						break
				else:
					pass

	def random_comment(author: str) -> str:
		QUOTES = ['And now at last it comes. You will give me the Ring freely! In place of the Dark Lord you will set up a Queen. And I shall not be dark, but beautiful and terrible as the Morning and the Night! Fair as the Sea and the Sun and the Snow upon the Mountain! Dreadful as the Storm and the Lightning! Stronger than the foundations of the earth. All shall love me and despair!',
'And you, {0}, I come to you last who are not last in my thoughts. For you I have prepared this. In this phial, is caught the light of Eärendil\'s star, set amid the waters of my fountain. It will shine still brighter when night is about you. May it be a light to you in dark places, when all other lights go out.'.format(author),
'Remember Galadriel and her Mirror!',
'I will not give you counsel, saying do this, or do that. For not in doing or contriving, nor in choosing between this course and another, can I avail; but only in knowing what was and is, and in part also what shall be.',
'It is said that the skill of the Dwarves is in their hands rather than in their tongues, yet that is not true of Gimli. For none have ever made to me a request so bold and yet so courteous...I do not foretell, for all foretelling is now vain: on the one hand lies darkness, and on the other only hope. But if hope should not fail, then I say to you, Gimli son of Glóin, that your hands shall flow with gold, and yet over you gold shall have no dominion',
'Hear all ye Elves! Let none say again that Dwarves are grasping and ungracious! Yet surely, Gimli son of Glóin, you desire something that I could give? Name it, I bid you! You shall not be the only guest without a gift.',
'Maybe the paths that you each shall tread are already laid before your feet, though you do not see them',
'Even the smallest person can change the course of the future',
'Welcome {0} of the Shire... one who has seen the eye!',
'I know what it is you saw, for it is also in my mind.',
'For the time would soon come when Hobbits would shape the fortunes of all.',
'The world is changed. I feel it in the water. I feel it in the earth. I smell it in the air. Much that once was is lost, for none now live who remember it.',
'In the land of Mordor, in the fires of Mount Doom, the Dark Lord Sauron forged in secret a Master-Ring, to control all others. And into this Ring, he poured his cruelty, his malice, and his will to dominate all life.',
'The Ring came to the creature Gollum, who took it deep into the tunnels of the Misty Mountains…and there, it consumed him',
'{0}, your coming to us is as of the footsteps of doom. You bring great evil here, Ringbearer.'.format(author),
'The quest stands upon the edge of a knife. Stray but a little, and it will fail, to the ruin of all. Yet hope remains, while all the company is true.',
'It is what will come to pass, if you should fail. The Fellowship is breaking, it has already begun. He will try to take the Ring, you know of whom I speak. One by one, it will destroy them',
'I have passed the test. I will diminish, and go into the West, and remain Galadriel.',
'You are a Ring-bearer, {0}. To bear a Ring of Power is to be alone.'.format(author),
'We shall not meet again, {0}'.format(author),
'The world is indeed full of peril, and in it there are many dark places; but still there is much that is fair, and though in all lands love is now mingled with grief, it grows perhaps the greater.',
]
		return random.choice(QUOTES)

class Frodo(Bot):
	history_file = 'frodo_history.csv'

	
	def search() -> None:
		reddit = Frodo.bind(FrodoCredentials.client_id.value,FrodoCredentials.client_secret.value,FrodoCredentials.password.value,FrodoCredentials.username.value)

		for results in reddit.subreddit('lotrmemes').comments():
			print(results)
			body = results.body
			body=body.lower()
			comment_id = results.id
		
			found_general=body.find('frodo')

			if Frodo.previously_responded(Frodo.history_file, comment_id):
				return "Skipped"

			else:
				if found_general != -1 and results.author != 'frodo_bot':
					Frodo.save_comment_id(Frodo.history_file, comment_id)
					print("Frodo detected: {0}".format(results.body))
					try:
						results.reply(Frodo.random_comment(results.author))
						pass
					except:
						break
				else:
					pass
	def random_comment(author: str) -> str:
		QUOTES = [
"What a pity that Bilbo did not stab that vile creature, when he had a chance!",
"You are wise and powerful. Will you not take the Ring?",
"Do not kill him even now. For he has not hurt me. And in any case I do not wish him to be slain in this evil mood. He was great once, of a noble kind that we should not dare to raise our hands against. He is fallen, and his cure is beyond us; but I would still spare him, in the hope that he may find it.",
"I tried to save the Shire, and it has been saved, but not for me.",
"There is no real going back. Though I may come to the Shire, it will not seem the same; for I shall not be the same. I am wounded with knife, sting, and tooth, and a long burden. Where shall I find rest?",
"You're late!",
"Short cuts make delays, but inns make longer ones.",
"I wish it need not have happened in my time",
"I wish the ring had never come to me. I wish none of this had happened.",
"And it is also said, 'Go not to the Elves for counsel, for they will say both no and yes.'",
"It is useless to meet revenge with revenge: It will heal nothing.",
"I feel that as longa s the shite lies behind, safe and comfortable, I shall find wander more bearable.",
"Do not be too sad, {0}. You cannot always be torn in two".format(author),
"I am naked in the dark, {0}, and there is no veil between me and the wheel of fire.".format(author),
"I'm glad to be with you, {0}, here at the end of all things.".format(author),
"There is no real going back.",
"Frodo wouldn't have got far without {0}, would he?".format(author),
"I will take ring... though, I do not know the way",
"Who is she? This woman you sing of?",
"Would you destroy it?",
"Can you protect me from yourself?",
"I cannot go back",
"The ring is mine!",
"You swore! You swore on the precious! {0} promised!".format(author),
"Because we've been here before. We're going in circles!",
"If you ask it of me, I will give you the One Ring",
"Mordor, {0}, is it left, or right?"
"Come on, Sam. Remember what Bilbo used to say: \"It's a dangerous business, Frodo. Going out your door. You step onto the road, and if you don't keep your feet there's no knowing where you might be swept off to.\"",
"Nothing. There's nothing. Wait. There are markings. It's some form of Elvish. I can't read it.",
"Before you came along, we Bagginses were very well thought of. Never had any adventures or did anything unexpected.",
"Whatever you did, you've been officially labeled a disturber of the peace.",
"Alright then, keep your secrets!",
"Yes, you have seen a thing or two since you last peeped out of a looking-glass",
"I can manage it. I must.",
"It must often be so, Sam, when things are in danger: some one has to give them up, lose them, so that others may keep them.",
"I should like to leave the Shire, if I could – though there have been times when I thought the inhabitants too stupid and dull for words, and have felt that an earthquake or an invasion of dragons might be good for them. But I don’t feel like that now. I feel that as long as the Shire lies behind, safe and comfortable, I shall find wandering more bearable: I shall know that somewhere there is a firm foothold, even if my feet cannot stand there again.",
"Then I know what I must do. It's just... I'm afraid to do it",
"I miss the Shire. I spent all my childhood pretending I was off somewhere else. Off with you, on one of your adventures.",
]
		return random.choice(QUOTES)
while True:
	try:
		Saruman.search()
		Galadriel.search()
		Frodo.search()
		time.sleep(5)
	except KeyboardInterrupt:
		break
	except Exception as e:
		print(e)
