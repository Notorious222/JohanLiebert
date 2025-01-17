import random
import threading
from typing import Union

from LightYagami.modules.helper_funcs.msg_types import Types
from LightYagami.modules.sql import BASE, SESSION
from sqlalchemy import (BigInteger, Boolean, Column, Integer, String,
                        UnicodeText)

DEFAULT_WELCOME = '{first}, the monster inside of me is exploding.'
DEFAULT_GOODBYE = 'Why would you do this?I trusted you!'

DEFAULT_WELCOME_MESSAGES = [
    "Player to player, Whatup {first} !",  
    "Ready Player {first}",
    "{first},I'll play with your soul like ether.",
    "I prove you lost already,{first} .",
    "{first}, drop the heat on us!",
    "{first} may have stories to tell.",
    "{first} just joined. Can I get a Pat?",
    "{first} just joined the chat - asweedasdf!",
    "{first} PASS THAT.DON'T FORGET THE ROTATION!",
    "{first},how many times should I tell you?Its PUFF-PUFF-PASS!",
    "Welcome, {first}. We were expecting you ( ͡° ͜ʖ ͡°)",
    "Welcome, {first}. We hope you brought some Brain cells with ya!",
    "Hey Yo, {first}. This a no ammunition zone.",
    "Call the cops when you see {first}.",
    "Be ready for some shit. {first} is coming up to me.",
    "{first},You got games on your Phone????.",
    "{first} just arrived.What am gon' do now.",
    "{first},tell me.How do you want it??.",
    "{first}, Do you know what is One Piece?",
    "Lil {first} showed up!",
    "BIG {first} on a higher plane!",
    "No matter where I go,I see the same {first}!",
    "{first} just showed up. Hold my beer.",
    "Challenger approaching! {first} has appeared!",
    "It's a bird! It's a plane! Nevermind, it's just {first}.",
    "God give me a sign...NVM {first} will do too.",
    "Never gonna give {first} up. Never gonna let {first} down.",
    "Ha! {first} has joined! You activated my trap card!",
    "{first}.We all embrace you with napalm!",
    "We've been expecting you {first}",
    "It's dangerous to go alone, take {first}!",
    "{first} has joined the chat! It's super effective!",
    "Cheers, love! {first} is here!",
    "{first} is here, as the prophecy foretold.",
    "{first} has arrived. Party's over.",
    "{first} is here to kick butt and chew bubblegum. And {first} is all out of gum.",
    "Hello. Is it {first} you're looking for?",
    "{first} has joined. Stay awhile and listen!",
    "Roses are red, violets are blue, {first} joined this chat with you",
    "Welcome {first}, Avoid Punches if you can!",
    "It's a bird! It's a plane! - Nope, its {first}!",
    "{first},you shall maintain composure at ease.",  #Discord welcome messages end.
    "Bungee gum has the property of both rubber and gum.Don't tell me you ain't knowing that {first}",
    "Hi, {first}. Don't lurk, only Villans do that.",
    "{first} has joined the battle bus.",
    "Don't like this complicated. Only what you're making to be!",  #Tekken
    "{first},I am the controller of Planet X.You're here to discuss something very important!",
    "{first},why are you alive at this hour??",
    "Something just fell from the sky! - oh, its {first}.",
    "At last you're here {first}.You've been away longer than Sigmund The Sea Creature !",
    "Hi, {first}, show me your Hunter License!",  #Hunter Hunter
    "I'm looking for Garo, oh wait nvm it's {first}.",  #One Punch man s2
    "Welcome {first}, leaving is not an option!",
    "Run Forest! ..I mean...{first}.",
    "{first},its all about Romance!",  
    "{first},Only God can Judge You.",  
    "That would not kill you could only make you stronger {first}", 
    "{first} what's all this Villainy??.",
    "{first} is like, One more steps and you're all goners.",
    "Call the Avengers! - {first} just joined the chat.",
    "{first} joined. You must construct additional pylons.",
    "{first} is here to tell us what the plan is.The hour is upon us its bananas.",
    "Come for the Snail Racing, Stay for the Chimichangas!",
    "Who needs Google? You're everything we were searching for.",
    "Can anyone picture {first}'s specific plan.",
    "Lets keep its real {first}.",
    "I'm just a butter knife,{first}'s a machete.",
    "{first},the Renowned Warrior,you're him right?",
    "Hi {first}, welcome to the dark side.",
    "Hola {first}, beware of people with disaster levels",
    "Hey {first}, we ain't got nothing to do with the bank robbery.",
    "Hi {first}\nThis isn't a strange place, this is my home, it's the people who are strange.",
    "Oh, hey {first} stop setting your password to password",
    "Hey {first}, so what we doin' today?",
    "{first} just joined, be at alert they could be a NARC.Hide the dope",
    "{first} joined the group, read by Mark Zuckerberg, CIA and 35 others.",
    "Welcome {first}, watch out for falling lumps of shit.",
    "Everyone stop what you’re doing, We are now in the presence of {first}.",
    "Hey You {first},listen,it's all about the scars",
    "Welcome {first}, drop your weapons and proceed to the spy scanner.",
    "Stay safe {first}, Keep 3 meters social distances between your messages.",  #Corona memes lmao
    "Hey {first}, Do you know I once One-punched a meteorite(Why don't no one care.)?",
    "You’re here now {first}, Resistance is futile",
    "{first} just arrived, the force is strong with this one.",
    "{first} just joined on president’s orders.",
    "Hi {first}, is the glass half full or half empty?",
    "Yipee Kayaye {first} arrived.",
    "Welcome {first}, if you’re a secret agent press 1, otherwise start a conversation",
    "{first}, I have a feeling we’re not in Kansas anymore.",
    "They may take our lives, but they’ll never take our {first}.",
    "Coast is clear! You can come out guys, it’s just {first}.",
    "Welcome {first}, pay no attention to that guy lurking.",
    "{first} gon' give it to ya!",
    "May the {first} be with you.",
    "{first} just joined. Hey, where's he tho?",
    "{first} just joined. Oh, there he is.",
    "Ladies and gentlemen, I give you ...  {first}.",
    "Behold my new evil scheme, the {first}-Inator.",
    "Ah, {first} the Platypus, you're just in time... to be trapped.",
    "*snaps fingers and teleports {first} here*",
    "La Di Da Di {first} likes to party!",
    "{first} just arrived. Diable Jamble!",  #One Piece Sanji
    "{first} just arrived. Aschente!",  #No Game No Life
    "{first} say Aschente to swear by the pledges.",  #No Game No Life
    "{first} just joined. El Psy congroo!",  #Steins Gate
    "Irasshaimase {first}!",  #weeabo shit
    "Hi {first}, what is 1000-7?",  #tokyo ghoul
    "Come. I don't want to destroy this place",  #hunter x hunter
    "I... am... Whitebeard!...wait..wrong anime.",  #one Piece
    "Hey {first}...have you ever heard these words?",  #BNHA
    "Can't a guy get a little sleep around here?",  #Kamina Falls – Gurren Lagann
    "It's time someone put you in your place, {first}.",  #Hellsing
    "Unit-01's reactivated..",  #Neon Genesis: Evangelion
    "Prepare for trouble...And make it double",  #Pokemon
    "Hey {first}, are You Challenging Me?",  
    "Oh? You're Approaching Me?",  #jojo
    "{first} just warped into the group!",
    "The world's a cold place {first},don't forget your Sweater.",
    "Sugoi, Dekai. {first} Joined!",
    "{first}, do you know gods of death love apples?",  
    "{first} what's your favourite song?",  
    "Oshiete oshiete yo sono shikumi wo!",  
    "Kaizoku ou ni...nvm wrong anime.",  
    "{first} just joined! Gear.....second!",  
    "Omae wa mou....shindeiru",
    "Enough {first}, Grandma Tsunade is too old for you!", 
    "{first},Chunchunmaru!",
    "{first},you ain't high right??!, ",
    "{first}.I got 5 on it!",
    "All Eyez on {first}!",
    "Make these haters suffer, {first}!",
    "The sword of the Great {first} will always remain imperial!",
    "{first}, do not fear any man but god!",
    "{first},God's Son Across the belly!",
    "{first} joined!, Gate of Death...open!",
    "{first}! I, Madara! declare you the strongest",
    "{first}, Whatup Homes!?",  
    "{first}, welcome to the hidden leaf village!", 
    "In the jungle, you must wait...until the dice read five or eight.",  #Jumanji stuff
    "{first} got his mind in the right place.",
    "{first},blows up, no guts, left chest, face gone ", 
]
DEFAULT_GOODBYE_MESSAGES = [
    "{first}, Did you rob the bank!!.",
    "{first} is outta here.",
    "{first} has left the place.",
    "{first} has left the clan.",
    "{first} has left the game.",
    "{first} has fled the area.",
    "{first} is out of the running.",
    "Nice knowing ya, {first}!",
    "He wears a mask just to cover the raw flesh.",
    "We hope to see you again soon, {first}.",
    "I donut want to say goodbye, {first}.",
    "Goodbye {first}! Guess who's gonna miss you :')",
    "Goodbye {first}! It's gonna be lonely without ya.",
    "Please don't leave me alone in this place, {first}!",
    "Good luck finding better shit-posters than us, {first}!",
    "You know we're gonna miss you {first}. Right? Right? Right?",
    "Congratulations, {first}! You're officially free of this mess.",
    "Where my {first} go? Figaro Figaro.",
    "You're leaving, {first}? Yare Yare Daze.",
    "This is it make no mistakes.",
    "Get your butt out.",
    "*developed a hole in the head*",
    "Think for yourself",
    "Question authority",
    "Straight to the depths of hell.",
    "Don't leave the house today",
    "Give up!",
    "Marry and reproduce",
    "Stay asleep",
    "Hell on Earth",
    "Reminisce now",
    "I bestow upon you, The Capital Punishment!",
    "Damn, whaat is this behaviour?",
    "Pulled you in my world and evolved you to chaos.",
    "What do you want to do today?",
    "You are dark inside",
    "Have you seen the exit?",
    "Get a baby pet it will cheer you up.",
    "Your princess is in another castle.",
    "You are playing it wrong give me the controller",
    "You might have ran out of Brain Cells.",
    "Live to die.",
    "When life gives you lemons reroll!",
    "Well, that was worthless",
    "I fell asleep!",
    "Where are you off to?",
    "Your old life lies in ruin",
    "Always look on the bright side",
    "It is dangerous to go alone",
    "Hard to forget.",
    "You have nobody to blame but yourself",
    "Lord, Forgive him for his sins, cos' here he comes.",
    "What's seen cannot be un-seen.",
    "Tried to bring you life but you want death.",
    "Unnecessary softness induces gayness.",
    "Follow the zebra",
    "Why so blue?",
    "The devil in disguise",
    "Go outside",
    "What can I do, What can i say, Is there another way?",
]
# Line 111 to 152 are references from https://bindingofisaac.fandom.com/wiki/Fortune_Telling_Machine


class Welcome(BASE):
    __tablename__ = "welcome_pref"
    chat_id = Column(String(14), primary_key=True)
    should_welcome = Column(Boolean, default=True)
    should_goodbye = Column(Boolean, default=True)
    custom_content = Column(UnicodeText, default=None)

    custom_welcome = Column(
        UnicodeText, default=random.choice(DEFAULT_WELCOME_MESSAGES))
    welcome_type = Column(Integer, default=Types.TEXT.value)

    custom_leave = Column(
        UnicodeText, default=random.choice(DEFAULT_GOODBYE_MESSAGES))
    leave_type = Column(Integer, default=Types.TEXT.value)

    clean_welcome = Column(BigInteger)

    def __init__(self, chat_id, should_welcome=True, should_goodbye=True):
        self.chat_id = chat_id
        self.should_welcome = should_welcome
        self.should_goodbye = should_goodbye

    def __repr__(self):
        return "<Chat {} should Welcome new users: {}>".format(
            self.chat_id, self.should_welcome)


class WelcomeButtons(BASE):
    __tablename__ = "welcome_urls"
    id = Column(Integer, primary_key=True, autoincrement=True)
    chat_id = Column(String(14), primary_key=True)
    name = Column(UnicodeText, nullable=False)
    url = Column(UnicodeText, nullable=False)
    same_line = Column(Boolean, default=False)

    def __init__(self, chat_id, name, url, same_line=False):
        self.chat_id = str(chat_id)
        self.name = name
        self.url = url
        self.same_line = same_line


class GoodbyeButtons(BASE):
    __tablename__ = "leave_urls"
    id = Column(Integer, primary_key=True, autoincrement=True)
    chat_id = Column(String(14), primary_key=True)
    name = Column(UnicodeText, nullable=False)
    url = Column(UnicodeText, nullable=False)
    same_line = Column(Boolean, default=False)

    def __init__(self, chat_id, name, url, same_line=False):
        self.chat_id = str(chat_id)
        self.name = name
        self.url = url
        self.same_line = same_line


class WelcomeMute(BASE):
    __tablename__ = "welcome_mutes"
    chat_id = Column(String(14), primary_key=True)
    welcomemutes = Column(UnicodeText, default=False)

    def __init__(self, chat_id, welcomemutes):
        self.chat_id = str(chat_id)  # ensure string
        self.welcomemutes = welcomemutes


class WelcomeMuteUsers(BASE):
    __tablename__ = "human_checks"
    user_id = Column(Integer, primary_key=True)
    chat_id = Column(String(14), primary_key=True)
    human_check = Column(Boolean)

    def __init__(self, user_id, chat_id, human_check):
        self.user_id = (user_id)  # ensure string
        self.chat_id = str(chat_id)
        self.human_check = human_check


class CleanServiceSetting(BASE):
    __tablename__ = "clean_service"
    chat_id = Column(String(14), primary_key=True)
    clean_service = Column(Boolean, default=True)

    def __init__(self, chat_id):
        self.chat_id = str(chat_id)

    def __repr__(self):
        return "<Chat used clean service ({})>".format(self.chat_id)


Welcome.__table__.create(checkfirst=True)
WelcomeButtons.__table__.create(checkfirst=True)
GoodbyeButtons.__table__.create(checkfirst=True)
WelcomeMute.__table__.create(checkfirst=True)
WelcomeMuteUsers.__table__.create(checkfirst=True)
CleanServiceSetting.__table__.create(checkfirst=True)

INSERTION_LOCK = threading.RLock()
WELC_BTN_LOCK = threading.RLock()
LEAVE_BTN_LOCK = threading.RLock()
WM_LOCK = threading.RLock()
CS_LOCK = threading.RLock()


def welcome_mutes(chat_id):
    try:
        welcomemutes = SESSION.query(WelcomeMute).get(str(chat_id))
        if welcomemutes:
            return welcomemutes.welcomemutes
        return False
    finally:
        SESSION.close()


def set_welcome_mutes(chat_id, welcomemutes):
    with WM_LOCK:
        prev = SESSION.query(WelcomeMute).get((str(chat_id)))
        if prev:
            SESSION.delete(prev)
        welcome_m = WelcomeMute(str(chat_id), welcomemutes)
        SESSION.add(welcome_m)
        SESSION.commit()


def set_human_checks(user_id, chat_id):
    with INSERTION_LOCK:
        human_check = SESSION.query(WelcomeMuteUsers).get(
            (user_id, str(chat_id)))
        if not human_check:
            human_check = WelcomeMuteUsers(user_id, str(chat_id), True)

        else:
            human_check.human_check = True

        SESSION.add(human_check)
        SESSION.commit()

        return human_check


def get_human_checks(user_id, chat_id):
    try:
        human_check = SESSION.query(WelcomeMuteUsers).get(
            (user_id, str(chat_id)))
        if not human_check:
            return None
        human_check = human_check.human_check
        return human_check
    finally:
        SESSION.close()


def get_welc_mutes_pref(chat_id):
    welcomemutes = SESSION.query(WelcomeMute).get(str(chat_id))
    SESSION.close()

    if welcomemutes:
        return welcomemutes.welcomemutes

    return False


def get_welc_pref(chat_id):
    welc = SESSION.query(Welcome).get(str(chat_id))
    SESSION.close()
    if welc:
        return welc.should_welcome, welc.custom_welcome, welc.custom_content, welc.welcome_type

    else:
        # Welcome by default.
        return True, DEFAULT_WELCOME, None, Types.TEXT


def get_gdbye_pref(chat_id):
    welc = SESSION.query(Welcome).get(str(chat_id))
    SESSION.close()
    if welc:
        return welc.should_goodbye, welc.custom_leave, welc.leave_type
    else:
        # Welcome by default.
        return True, DEFAULT_GOODBYE, Types.TEXT


def set_clean_welcome(chat_id, clean_welcome):
    with INSERTION_LOCK:
        curr = SESSION.query(Welcome).get(str(chat_id))
        if not curr:
            curr = Welcome(str(chat_id))

        curr.clean_welcome = int(clean_welcome)

        SESSION.add(curr)
        SESSION.commit()


def get_clean_pref(chat_id):
    welc = SESSION.query(Welcome).get(str(chat_id))
    SESSION.close()

    if welc:
        return welc.clean_welcome

    return False


def set_welc_preference(chat_id, should_welcome):
    with INSERTION_LOCK:
        curr = SESSION.query(Welcome).get(str(chat_id))
        if not curr:
            curr = Welcome(str(chat_id), should_welcome=should_welcome)
        else:
            curr.should_welcome = should_welcome

        SESSION.add(curr)
        SESSION.commit()


def set_gdbye_preference(chat_id, should_goodbye):
    with INSERTION_LOCK:
        curr = SESSION.query(Welcome).get(str(chat_id))
        if not curr:
            curr = Welcome(str(chat_id), should_goodbye=should_goodbye)
        else:
            curr.should_goodbye = should_goodbye

        SESSION.add(curr)
        SESSION.commit()


def set_custom_welcome(chat_id,
                       custom_content,
                       custom_welcome,
                       welcome_type,
                       buttons=None):
    if buttons is None:
        buttons = []

    with INSERTION_LOCK:
        welcome_settings = SESSION.query(Welcome).get(str(chat_id))
        if not welcome_settings:
            welcome_settings = Welcome(str(chat_id), True)

        if custom_welcome or custom_content:
            welcome_settings.custom_content = custom_content
            welcome_settings.custom_welcome = custom_welcome
            welcome_settings.welcome_type = welcome_type.value

        else:
            welcome_settings.custom_welcome = DEFAULT_WELCOME
            welcome_settings.welcome_type = Types.TEXT.value

        SESSION.add(welcome_settings)

        with WELC_BTN_LOCK:
            prev_buttons = SESSION.query(WelcomeButtons).filter(
                WelcomeButtons.chat_id == str(chat_id)).all()
            for btn in prev_buttons:
                SESSION.delete(btn)

            for b_name, url, same_line in buttons:
                button = WelcomeButtons(chat_id, b_name, url, same_line)
                SESSION.add(button)

        SESSION.commit()


def get_custom_welcome(chat_id):
    welcome_settings = SESSION.query(Welcome).get(str(chat_id))
    ret = DEFAULT_WELCOME
    if welcome_settings and welcome_settings.custom_welcome:
        ret = welcome_settings.custom_welcome

    SESSION.close()
    return ret


def set_custom_gdbye(chat_id, custom_goodbye, goodbye_type, buttons=None):
    if buttons is None:
        buttons = []

    with INSERTION_LOCK:
        welcome_settings = SESSION.query(Welcome).get(str(chat_id))
        if not welcome_settings:
            welcome_settings = Welcome(str(chat_id), True)

        if custom_goodbye:
            welcome_settings.custom_leave = custom_goodbye
            welcome_settings.leave_type = goodbye_type.value

        else:
            welcome_settings.custom_leave = DEFAULT_GOODBYE
            welcome_settings.leave_type = Types.TEXT.value

        SESSION.add(welcome_settings)

        with LEAVE_BTN_LOCK:
            prev_buttons = SESSION.query(GoodbyeButtons).filter(
                GoodbyeButtons.chat_id == str(chat_id)).all()
            for btn in prev_buttons:
                SESSION.delete(btn)

            for b_name, url, same_line in buttons:
                button = GoodbyeButtons(chat_id, b_name, url, same_line)
                SESSION.add(button)

        SESSION.commit()


def get_custom_gdbye(chat_id):
    welcome_settings = SESSION.query(Welcome).get(str(chat_id))
    ret = DEFAULT_GOODBYE
    if welcome_settings and welcome_settings.custom_leave:
        ret = welcome_settings.custom_leave

    SESSION.close()
    return ret


def get_welc_buttons(chat_id):
    try:
        return SESSION.query(WelcomeButtons).filter(
            WelcomeButtons.chat_id == str(chat_id)).order_by(
                WelcomeButtons.id).all()
    finally:
        SESSION.close()


def get_gdbye_buttons(chat_id):
    try:
        return SESSION.query(GoodbyeButtons).filter(
            GoodbyeButtons.chat_id == str(chat_id)).order_by(
                GoodbyeButtons.id).all()
    finally:
        SESSION.close()


def clean_service(chat_id: Union[str, int]) -> bool:
    try:
        chat_setting = SESSION.query(CleanServiceSetting).get(str(chat_id))
        if chat_setting:
            return chat_setting.clean_service
        return False
    finally:
        SESSION.close()


def set_clean_service(chat_id: Union[int, str], setting: bool):
    with CS_LOCK:
        chat_setting = SESSION.query(CleanServiceSetting).get(str(chat_id))
        if not chat_setting:
            chat_setting = CleanServiceSetting(chat_id)

        chat_setting.clean_service = setting
        SESSION.add(chat_setting)
        SESSION.commit()


def migrate_chat(old_chat_id, new_chat_id):
    with INSERTION_LOCK:
        chat = SESSION.query(Welcome).get(str(old_chat_id))
        if chat:
            chat.chat_id = str(new_chat_id)

        with WELC_BTN_LOCK:
            chat_buttons = SESSION.query(WelcomeButtons).filter(
                WelcomeButtons.chat_id == str(old_chat_id)).all()
            for btn in chat_buttons:
                btn.chat_id = str(new_chat_id)

        with LEAVE_BTN_LOCK:
            chat_buttons = SESSION.query(GoodbyeButtons).filter(
                GoodbyeButtons.chat_id == str(old_chat_id)).all()
            for btn in chat_buttons:
                btn.chat_id = str(new_chat_id)

        SESSION.commit()
