import main

penalties = {"easy":-10, "medium":-20,"hard":-30}
plist = list(penalties.keys())
dlist = list(main.skills.keys())
twodie = ['adv','disadv']
keywords = dlist + twodie + plist
display = ' '.join(dlist)