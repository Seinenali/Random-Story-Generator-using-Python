import random
when=['A few years ago','Yesterday','In the 17th AD','A long time ago','Last night','In the 16th AD']
who=['An Elf','An Orc','A wizard','A Princess','A knight','A boy']
name=['Dandolf','Uhuru','Diana','Arthur','Albwin','Robin']
residence=['Havenport','Devenshire','Maginia','Ravenheim','Heimdale','Fridonia']
went=['Thieves Guild','Tournament','Old Temple in the ruins','Forbidden Forest','Dragons Lair','soilder in the kings army.']
happened=['found alot of Gold.','defeated the dragon.','found the legendary sword Heimer.','became an merchant.','was granted land and riches.','saved an dame in distress.']
print(random.choice(when) + ', ' + random.choice(who) + ' named ' + random.choice(name) + ' that lived in ' + random.choice(residence) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happened))