import random

# version 0.4

# format #

# This monster is a monsterName1 monsterName2
# It has monsterEyes and monsterMouth
# monsterDescPref (it has/it's got) monsterDesc and monsterWeapon


print ('This monster is a', end=' ')

# generation starts

monsterName1 = [
'replilian', 
'kinda smelly',
'big n\' hairy',
'built Ford tough',
'very intimidating',
'rather pleasant',
'large and dangerous',
'Stephen King\'s',
'big nasty',
'kinda pathetic',
'cat-sized but dangerous',
'Costco-sized',
'quite poised',
'big n\' sweaty',
'refrigerator-sized',
'undersized', 
'bus-sized',
'skyscraper-sized',
'terrifyingly powerful',
'enormous']
print(random.choice(monsterName1), end=' ')

monsterName2 = [
'beast',
'kaiju',
'dragon',
'generic forest cryptid',
'generic praire cryptid',
'generic sea cryptid',  
'gorilla-esque beast',
'puma-esque beast',
'snake-like beast',  
'vole-like beast',  
'bear-like beast',  
'bigfoot',
'jackalope',
'squid type thing',
'yeti',
'sea goat',
'imp',
'ant-lion',
'wraith',
'cartoon mummy',
'ghoul',
'banshee',
'trickster spider',
'scorpion',
'moth man',
'half-puma-man',
'zombie gnome',
'harpy',
'slime',
'living ragdoll',
'anthropomorphic bison',
'anthropomorphic wolf',
'anthropomorphic squid',
'anthropomorphic great dane',
'anthropomorphic lion',
'demon']
print(random.choice(monsterName2))


print ('It has', end=' ')

monsterEyes = [
'enormous bloodshot eyes',
'one eye with an expertly applied smoky look',
'tiny beedy eyes, like a doll\'s eyes',
'big green anime eyes',
'big blue anime eyes',
'dark eyes that give a withering look',
'18 beady little eyes',
'small eyes but huge eyelids',
'long eyes but short eyelids',
'short eyes but long eyelids',
'2 eyes but only one eyelid',
'a single eye with many pupils',
'very small eyes sprinkled all over its face',
'big round blue eyes with pupils shaped like hearts',
'a single eye with no pupil a single eye with a swirling galaxy of pupils',
'eyes where its ears should be and vice versa',
'white squares for eyes',
'one big eye and one small eye',
'no eyes but long lashes',
'yellow eyes with 💢-shaped pupils',
'grey eyes with spikes for eyelashes',
'yellow cat-like eyes',
'big watery eyes',
'pinhole-sized eyes eyes with projectile tears',
'three cat-like eyes',
'6 little black eyes in a grid',
'a square panel of many eyes that blink in unison',
'a redundant array of independent eyes', 
'blue eyes like limpid pools of tears',
'little yellow reptilian eyes']
print(random.choice(monsterEyes), end=' ')
               
print ('and', end=' ')

monsterMouth = [
'5 tiny mouths',
'a jaw that unhinges to reveal another, even scarier mouth',
'big pouty lips',
'a redundant array of independent mouths',   
'a Glasgow smile',
'a big gross mouth',
'a rather unscary mouth with a few cavities',
'teeth that are so straight and white it\'s scary',
'a regular mouth',
'a proboscus like a mosquito', 
'a big be-fanged mouth',
'tiny pathetic fangs',
'long shiny fangs',
'thin dehydrated lips',
'a big mouth with a jawbreaker in it',
'a giant foaming maw',
'no mouth at all',
'a mouth like a binder clip',
'a long sharp beak',
'a long snoot',
'a be-fanged snout',
'a horrid snout',
'a wry smile',
'a smirking mouth',
'a lipless hole of a mouth',
'a tongue but no mouth (uses ears)',
'a sideways mouth with crooked teeth',
'a wide sharp beak',
'a big ole\' chomper',
'a fairly normal mouth but rancid breath']
print(random.choice(monsterMouth))

# more or just print?
monsterDescPref = [
'It has',
'It\'s got']
print(random.choice(monsterDescPref), end=' ')

# limbs or fur
monsterDesc = [
# head stuff
'radioactive antlers',
'an lure on its head that looks like a limited edition Funko Pop',
'an lure on its head that looks like a Spiderman comic',
'an lure on its head that looks like a Twix bar',
'an lure on its head that looks like a pack of smokes',
'an lure on its head that looks like a 2TB SSD',
'an lure on its head that looks like a chocolate muffin',  
'a great many tentacles',
'a body like a linebacker (sweaty and overworked)',
'an anime sweatdrop',  
# hair or fur
'centipedes for hair',  
'a thick wintery pelt',
'long red fur',
'long blond hair like a Pantene commercial',
'a single tentacle that looks unwashed',
'huge feet with steel-toed boots',
'big flappers',
'big fins',
'centipedes for feet',
'centipedes for arms',
'huge swollen knees',
'huge hands',  
'giant claws',
'hook-like claws',  
'knife-like claws',
'huge weird feet',  
'glowing florescent bones',
'a long tail like a whip',
'glowing purple cheeks',
'cinematicly blood-dripping fangs',
'prehensile braids',
'a few prehensile tails',
'ill-fitting pants.',  
'muddy knee-high boots.',  
'an intimidating huge red rear']                
print(random.choice(monsterDesc), end=' ')

print ('and', end=' ')
                
monsterWeapon = [
# more traditional weapons 
'a nerf gun',
'a super soaker full of',
'a cast iron skillet',
'a whip',
'a gun??',
'a big stick',  
'a mace',
'a ford f250',  
'a letter opener',  
'a mall katana',
'a curtain rod',
'a paddle with "no! bad!" printed on it in comic sans',
'a broken bottle.',
'an Toyota RAV4',
'a boat oar',  
'bear spray',
'expired fish sticks',  
'a book of riddles',  
'a big rolled up newspaper.',  
'a big splintery stick',  
# health-adjacent
'very bad breath.',
'fleas',
'ticks.',
'rabies.',  
# bad stuff to have
'70,000 reddit karma',
'100,000 reddit karma',
'a disney fastpass',
'autoplay enabled',
# character traits
'a nasty temper',
'a bad attitide.',
'a passive-agressive attitude.',
'a penchant for gaslighting.',
'toxic traits out the wazoo.',
'bad jokes.',
'stans JKR.',
'a sour demeanor',
'main character syndrome',
'an excuse',
'unexamined cognitive biases',
'heavy, spooky, rattling chains',
'bad taste in youtubers',
'bad takes about women in video games']                
print(random.choice(monsterWeapon), end=' ')
               







