import spacy as sa 

#create nlp object
nlp = sa.load('en_core_web_sm')

story = """The Promise of the Forest Friends

In the heart of the Great Green Forest, there lived three different animals. Leo was a big, golden lion. He was strong, brave, and the king of the forest. Rory was a small, brown rabbit. He was very fast, very smart, and always full of energy. Ellie was a huge, grey elephant. She was gentle, kind, and very strong. Other animals thought a lion, a rabbit, and an elephant could never be friends. But they were the best of friends. They played together every single day. Leo protected them from danger, Rory found the best hidden sweet fruits, and Ellie gave them fun rides on her broad back. They made a promise to always help each other, no matter what happened.

One hot summer, the sun became very angry. It did not rain for many months. The Great Green Forest became very dry. The beautiful river turned into dry, cracked mud. The green leaves turned brown and fell off the trees. All the animals were thirsty and hungry. Leo, Rory, and Ellie decided to walk far away to find a new water hole. They walked for days and days. The ground was hard and the air was hot. 

One afternoon, Leo was walking in front of his friends. He was looking far away and did not look at the ground. He did not see a deep, hidden hole covered by dry leaves. It was an old, deep well that had dried up a long time ago. Suddenly, the dry ground broke under his heavy paws. Leo fell down, down, down into the dark hole. He hit the bottom with a loud thud. 

The hole was deep and dark. The walls were made of hard, dry clay. Leo tried to jump out, but the hole was much too deep. He tried to dig the walls, but his sharp claws just slipped on the hard clay. He roared as loudly as he could. "Help! Help me!" His big voice echoed in the dark hole. Up above, Rory and Ellie heard the loud roar. They ran as fast as they could to the edge of the hole. They looked down and saw their poor friend. "Do not worry, Leo!" shouted Rory. "We will get you out!" Ellie trumpeted loudly. "We are here, my friend. We will not leave you."

Ellie tried to reach down with her long trunk. But the hole was too deep. Her trunk could not touch Leo. Rory tried to climb down, but the walls were too steep and slippery. He slid right back up. "We need a good plan," said Rory, twitching his little nose. He was small, but his brain was big. "Ellie, can you push that big dead tree over here?" Ellie looked at a huge, dry tree nearby. She pushed it with her strong head. The tree fell near the hole. But it was not long enough to reach the bottom. Time was passing quickly, and the sun was going down.

Suddenly, Rory smelled something bad. It was smoke. He looked toward the east. The dry forest had caught fire. A big, orange wall of fire was moving toward them. The wind was blowing the fire right at them. "Ellie! Leo! The forest is on fire!" cried Rory. The other animals in the forest were running away. Birds flew high in the sky. Monkeys swung quickly in the trees. Everyone was running to the safe, rocky mountains.

"You must go!" roared Leo from the bottom of the hole. "Save yourselves! The fire is coming fast. I am too heavy. You cannot save me. Run away and be safe!" 

But Rory and Ellie did not move. "We are your friends!" said Rory bravely. "Friends do not leave friends behind." Ellie stamped her big foot on the ground. "We made a promise. We stay together in good times and bad times."

The fire was getting closer. The heat was burning their skin. The thick smoke made them cough. Rory thought fast. "Ellie, we need vines! Long, strong vines from the big banyan tree. Go get them! I will dig the edge of the hole to make it wider so the tree can go deeper." Ellie ran to the banyan tree. She used her trunk to pull down long, thick vines. Rory used his sharp front paws to dig the dry dirt at the edge of the hole. He dug and dug until his little paws hurt.

Ellie came back with the strong vines. She tied the vines to the big dead tree. Then, she pushed the tree into the hole. Because Rory dug the edge, the tree went deeper. "Leo! Climb the tree!" shouted Rory. Leo jumped and grabbed the tree. But the wood was dry and slippery. He slipped down. The fire was very close now. The leaves on the bushes were turning black and burning. "Try again, Leo! We believe in you!" cheered Rory. Ellie held the top of the tree with her strong trunk so it would not fall over.

Leo took a deep breath. He used all his strong muscles. He dug his sharp claws into the wood. He climbed up, step by step. When Leo reached the top, Ellie pulled him out with her trunk. Just then, the fire reached the dry grass near the hole. "Run!" shouted Ellie. Rory jumped quickly on Ellie’s back. Leo ran right beside her. They ran as fast as they could. The fire was right behind them. They could feel the hot wind on their backs. They did not stop. They did not look back.

Finally, they reached the rocky mountains. There was no grass or trees there, so the fire could not burn. They were safe. They sat on the cool rocks. They were very tired, dirty, and covered in black ash. But they were alive. Leo looked at his two friends. He had happy tears in his eyes. "Thank you," said the big lion. "You saved my life. You could have run away, but you stayed."

Rory smiled and cleaned his dirty paws. "A true friend is a friend in need," said the little rabbit. 

Ellie wrapped her long trunk around both of them in a big, warm hug. "We are a team," said the gentle elephant. "Lion, rabbit, or elephant, it does not matter. Our hearts are tied together." 

From that day on, their friendship grew even stronger. They lived happily in the forest, knowing that true loyalty means never giving up on each other, no matter how hard the times are."""
#create doc object
doc = nlp(story)

#access tokens 
# for word in doc:
#     print(word.text, word.dep_, word.pos)

for entity in doc.ents:
    print(entity.text,entity.label_)
