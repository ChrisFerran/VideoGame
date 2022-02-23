# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define d = Character("Dolus")
define r = Character("Robber")
define s = Character("Mrs Striker")
define m = Character("Mom")
define da = Character("Darius")
define w = Character("Winrey")
define y = Character("Yuuki")
define j = Character("Jerry")
define n = Character("[name]")
define em = Character("Emilia")
define tv = Character("TV")
define e = Character("Employee")
define dad = Character("Dad")
define p = Character("Police")
define doo = Character("DooDoo")
define win = Character("Winnifer")
define doc = Character("Doctor")
define no = Character("Note")
define c = Character("Credits")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.



    scene classroom
    with fade
    play music "classroom.mp3"
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    "Another day of school. I wonder what could possibly go wrong today. Nothing ever goes the way I want it too..."
    show striker


    # These display lines of dialogue.

    s "Alright class, settle down. Today we are going to have a pop quiz"

    show darius angry at right


    da "What? But that's not fair! You never told us we were gonna have a quiz!"

    show striker

    s "That's literally the point of a pop quiz Darius."

    show jerry at left

    j "A pop quiz is fine with me. As the smartest person in this school, I welcome any challenge that comes my way."
    da "Shut up Jerry! no one likes you or your elitist attitude!"
    j "At least I wear shoes to school you disgusting freak."
    da "How many times do I have to tell you? It's a..."
    show striker angry
    s "Alright both of you be quiet!"
    s "Since you seem to be pretty talkative today Darius, why don't you hand out the quiz to everybody?"

    da "Fine..."
    hide striker
    hide darius angry
    hide jerry
    "Jerry walks around the class, begrudgingly handing every student the quiz."
    "He finally walks up to me and puts the quiz on my table."
    show darius happy

    da "Good luck bro."
    hide darius happy

    "I look down at the quiz and discover that it is mercifully short. It is only 10 questions long and they all appear to be multiple choice."
    "Before I start answering the questions, I should put my name on it."
    $ name = renpy.input("Whats's your name?")
    $ name = name.strip()
    default name = "Pat"
    if not name:
        $ name = "Pat"

    "Alright now time to start the quiz"
    "Question number 1: What is the capital of Argentina?"
    "Oh crap I never read the chapter on capitals. It's ok I'll just skip to question 2 and come back to that one later."
    "Question number 2: What is the capital of Germany?"
    "..."
    "This whole quiz is over capitals isn't it?"
    "Question 3: What is the capital of the United States of America?"
    "Ok, finally, one I actually know the answer to. Maybe I won't do so bad on this test after all!"
    "Question 4: What is the capital of Ireland?"
    "Never mind I'm completely screwed. Alright, time to choose C on every question!"
    "I then proceeded to hastily mark C for every answer. After I finished I put my pencil down and let out a big sigh of obvious misery."
    "I looked around the class to see how everyone else was doing"
    show jerry
    "Of course Jerry was already done. But unlike me he actually looked quite satisfied with himself."
    hide jerry
    show darius angry
    "Darius had a look of utmost concentration on his face. He is by no means smart, but he has always worked hard and his grades reflect his perseverance."
    hide darius angry
    show winrey school
    "I looked to the girl who was seated directly behind Jerry. Her name was Winrey. I haven't really talked to her at all before but she is very popular and extremelly pretty."
    "And if that wasn't good enough she is also a grade A student and the star athlete on our school soccer team, AND she's the class president."
    "She's pretty much perfect in every way possible. And of course she was already finished with her test, and like Jerry, she looked satisfied with the results."
    "Unlike Jerry however, she isn't a total prick."
    hide winrey school
    show jerry angry
    "I've known Jerry since the first year of middle school and every year since then we have somehow managed to end up in the same class."
    "He's always made fun of me and Darius for being unpopular and dumb."
    "Jokes on him though as I've never seen him talk to anyone outside of class."
    hide jerry angry
    show striker happy
    s "Alright everyone put your pencils down. Time is up!"
    s "I will grade these tests immediately and have your scores calculated by the end of the period."
    s "In the mean time, you are free to talk amongst yourselves. Quietly I should add. There are still plenty of other classes who are working."
    hide striker happy
    show darius
    da "Hey [name], how do you think you did?"
    menu:

        "Well I knew the answer to 1 question...":
            jump choice1_yes

        "I knew the answer to every single question!":
            jump choice1_no


    label choice1_yes:
            #$ menu_flag = True

            da "Well at least you got a 1/10 at the very least. hehe..."

            jump choice1_done

    label choice1_no:

            #$ menu_flag = False

            da "Seriously?! Did you actually study for once?"
            da "Wait... You're being sarcastic, aren't you? Well there are always more tests in the future that you can do well on. You just need to study!"

            jump choice1_done

    label choice1_done:
label start1:

    da "I spent 3 hours last night studying everything we learned just in case we did end up having some quiz!"
    show jerry at left
    j "What are you two losers talking about over here?"
    show darius angry
    da "None of your business, you annoying prick."
    j "I assume you two are discussing how hard you failed that simplistic quiz made for 4 year olds."
    j "Seriously, anybody with half a brain cell could have aced that quiz."
    da "Have you ever thought about how no one, not even your parents love you?"
    j "I don't need to have people like me, you ignorant fool."
    j "With how brilliant and talented I am, I will end up becoming absurdly rich, and then everyone will want to be around me."
    j "Not that I'll let them of course. I genuinely hate most people. They're so annoying and ignorant."
    da "It's no wonder you don't have any friends..."
    hide jerry
    hide darius angry
    show striker
    s "Ok people, I finished grading the test. You all did well for the most part."
    s "I will now hand back the tests"
    hide striker
    "Mrs. Striker went around the class handing the papers to each student, one by one."
    "The first student who recieved their paper was Winrey. Once she reviewed her grade, she leaned back in her chair, put her feet on her desk, and grinned."
    "I guess she did well. No surprise there."
    "The next person to get their paper was Jerry."
    "He just glanced at the paper and smiled."
    "Darius was next in line at getting their grade at back."
    "I watched him nervously look at the score and let out a huge sigh of relief."
    "Finally, Striker slowly moved in my direction."
    "Without even looking in my general direction, she put my paper on my desk, face down."
    "Wait, why did she put my paper face down like that? Every other student received their paper face up."
    "I slowly turned the paper over and I knew immedietly why she singled me out like that."
    "On the top of the page was a big score written in red, menacing ink."
    "1/10. See me after class!"
    "Welp, I knew that was coming."
    "The rest of the class proceeded as it normaly would have. And by that I mean I completely zoned out and didn't hear a single thing that was taught."

    scene classroom evening
    with fade

    "Before I knew it, the final bell rang, signifying the end of the school day."
    show striker happy
    s "Alright class have a great day! Remember that tomorrow I will assign the groups for the project that you all will be working on for the remainder of the school year."
    s "I urge you all to take it seriously, as it is worth 50 percent of your entire grade."
    hide striker happy
    show darius happy
    da "You wanna walk home together [name]?"
    menu:

        "Mrs. Striker wanted to see me after class...":
            jump choice2_yes

        "Sorry, I'm busy today.":
            jump choice2_no

    label choice2_yes:
        #$ menu_flag = True

        show darius
        da "Oh dang you really did that bad huh? It's ok dude I'm sure you will do better next time"

        jump choice2_done

    label choice2_no:
        #$ menu_flag = False

        show darius
        da "Since when have you ever been busy with anything?"
        da "... Relax man, I'm just messing with you! Anyways, I'll see you tomorrow then."

        jump choice2_done

    label choice2_done:
label start2:
    hide darius
    "Darius walked out of the room by himself. Everyone else slowly cleared the room until it was just me and Mrs. Striker."
    "I reluctantly got out of my seat and slowly shuffled towards her desk."
    show striker
    s "Good evening [name], I assume that I don't need to tell you why I asked you to stay after class?"
    s "Your grades have been consistently slipping for quite awhile now."
    s "I know things have been really tough for you since the accident, which is why I'm not going to hold these recent bad grades against you."
    s "If you ever need to talk to anybody, just know that I am here for you. And I'm sure Darius is as well."
    s "If you feel like you might need professional counseling then I can arrange that as well."
    "I told her that I was fine, which was completely true."
    s "Ok, you are free to go for now."
    s "Be extra careful on the way home. It's about to get dark."
    "I left the room as quick as I could and was about to head to the bus stop in front of the school until I remembered that it was too late."
    "Could this day get any worse? Now I have to walk home and that takes over an hour."
    "To make things worse, my mom expects me to be home in about 30 minutes."
    "I could take the shortcut through the old abandoned park. No one will be around but I should be fine."
    "I reached into my pocket to feel if it was still there."
    "Sure enough, my pocket knife that my dad gave me for my 10th birthday was sitting snugly in my pocket like it always is."
    "I know that I'm technically not supposed to bring a pocket knife to school, but I feel naked without it and there isn't any security on campus to check that sort of thing."
    "As long as I have this for protection, I should be fine going in to the park."
    scene moon over field
    with fade
    play music "moon.mp3"
    "After about 20 minutes of fast-walking, I finally made it to the park."
    "Just as I expected, it was dark and there was no one in sight."
    "the moonlight radiated onto the ground and gave the entire place an eerie atmosphere."
    "The park has been abandoned for well over a decade due to a lack of fudning from the state, which led to all of the lightposts being taken down."
    "I walked for a little while longer until I heard a twig crack behind me."
    show robber1
    "I turned around and before me stood a pitch black silhouette of a man."
    "I couldn't make out a single detail besides his glowing eyes forming a scowl."
    r "Look kid, I don't want to hurt you but I am gonna need you to slowly hand over all the money you have."
    r "And don't even think of trying any funny business. I have a gun in my pocket and if you do anything suspicious I swear to God I'll kill you."
    "I started trembling all over my body and completely froze in place. I could tell from his tone of voice that he was serious."
    "The only question was whever he was lying or not about having a gun."
    "Is that really a risk that I'm willing to take? I should definitely just hand him over my wallet. No amount of money is worth dying for."
    "I reached in my pocket and to my surprise all I felt was my pocket knife."
    "Where the heck's my wallet?!?! I know I must have brought it to school with me! I always carry it in the same pocket as my pocket knife."
    "It doesn't really matter how I lost it now. The only thing I need to worry about now is how I'm going to get out of this situation."
    "What should I tell him?"
    menu:
        "I dont have any money. Please just let me go":
            jump choice3_yes

        "Piss off douchenozzle":
            jump choice3_no

    label choice3_yes:
        #$ menu_flag = True

        r "Listen kid, I'm just going to be brutally honest with you. I'm in really deep with some really bad people."
        r "They told me to get at least 100 bucks from you. They told me if I don't get the money, they...they told me they will kill my entire family..."
        r "And I know they're serious. They already did some terrible things. So please. I'm begging you. Just...just give me your money."
        "The man stuttered with every word he said, trying his best to hide back his tears. I could tell that every word he said was the honest brutal truth."
        "I also knew that I still didn't have any money. I knew that this man was desperate and if I didn't hand him any money he would kill me on the spot."
        r "Please kid... Just give me the money..."

        jump choice3_done

    label choice3_no:
        #$ menu_flag = False

        r "What did you just call me you annoying little punk?"
        r "I should kill you right now but I'll let that one slide since I'm so gracious."
        "Ok, so that probably wasn't a smart thing to say. I looked into his eyes and behind the brave front he put up, I could tell he was terrified of something."
        "I could tell that if I didn't hand him any money he would kill me on the spot."
        r "Ok kid, last chance before I blow your brains out all over this nice old park."

        jump choice3_done

    label choice3_done:
label start3:
    "Before I could even process what I was about to do, I swiftly grabbed the pocket knife and charged him at full speed."
    r "WHAT ARE YOU DOING KI..."
    play sound "gun.mp3"
    "{i} BANG!!!! {/i}"
    r "Oh my God... What have I done?!"
    r "I gotta get out of here!"
    scene black
    with fade
    play music "black.mp3"

    "..."
    "............"
    ".....Where....am I?"
    "I looked around but I couldn't see anything. It was pitch black."
    "How did I get here?"
    "I can't seem to remember anything."
    "Who am I?"
    "I sat there in the endless void for what felt like an eternity and a half."
    "At some point I lost all sense of myself."
    "I didn't think, or feel, or anything. I just was."
    "After some indiscriminate amount of time everything slowly started to come back."
    "Oh yeah. My name is [name]."
    "I live in the United States of America."
    "My best friends name is Darius."
    "My teachers name is Mrs. Striker."
    "I have a crush on a girl named Winrey."
    "I live with my mother."
    "My father and sister are dead."
    "They died in a..."
    "I couldn't bring myself to recount that time. Not yet."
    "But how did I get here?"
    "The last thing I remember is walking home from school after failing a test."
    "I was late, so I decided to take a shortcut. And then..."
    "Everything came back to me. The shadowy figure. The pocket knife. The gun shot..."
    "The gun shot! I was shot!"
    "But where am I now? Am I...dead?"
    show dolus
    d "yes you are, my child."
    "AHHHHHHHHHHHHHHHHHHHHHHHHHHHHH!!!!!"
    "Out of nowhere this person just appeared and it scared me so bad that I couldn't help but scream."
    "Who is this person? What do they want? I better ask her for more details."
    menu:
        "Who are you?":
            jump choice4_yes

        "Where am I?":
            jump choice4_no

    label choice4_yes:
        #$ menu_flag = True

        d "My name is Dolus and there is no need for alarm."
        d "I know that you are frightened, and that is very understandable."
        d "You wake up in a strange place without your memories, and are forced to stay here without any form of interaction for over a century."
        d "As for where you currently are, that is a hard question for me to answer."
        d "The name of this place can not be properly heard or understood by human ears. If I were to tell you the name of this place you would go insane and your body would be destroyed."
        d "The best name I can give you is what you might understand to be purgatory."
        d "A place that is between life and death, where people go after they die as they wait for their judgement from God."
        d "Usually people only stay here for a mere few moments, before they are teleported straight to the Lord himself."
        d "You are a special case however, as you were not supposed to die for another 57 years."

        jump choice4_done

    label choice4_no:
    #$ menu_flag = False

        d "The name of this place can not be properly heard or understood by human ears. If I were to tell you the name of this place you would go insane and your body would be destroyed."
        d "The best name I can give you is what you might understand to be purgatory."
        d "A place that is between life and death, where people go after they die as they wait for their judgement from God."
        d "Usually people only stay here for a mere few moments, before they are teleported straight to the Lord himself."
        d "You are a special case however, as you were not supposed to die for another 57 years."
        d "My name is Dolus and I deeply apologize, as that is the very first thing I should have told you."

        jump choice4_done
    label choice4_done:
label start4:
    "Purgatory? Dolus? 57 years? This was information overload."
    "Dolus must have noticed the confusion on my face as she continued to do her best to explain."
    d "I am an angel of God who was sent here to help you, and possibly offer you a gift."
    "A gift? What kind of gift? I asked her."
    d "The Lord has watched you struggle your entire life. And your pain and suffering has not gone unnoticed."
    d "You have truly had a hard life. God puts people through these trials as a test of sorts, and he was going to reward you for your diligence with a nice, easy life."
    d "That was, until, you were murdered."
    d "That was never supposed to happen, and God took quite a while with deciding what to do with you next. This is why you were here for so long. I apologize for the inconvenience."
    d "But the wait is finally over, and God has made up his mind. He has decided to offer you a choice."
    d "You can either choose to end your life right now, and ascend to Heaven."
    d "You will be reunited with your lost loved ones and you will live in peace and harmony for all eternity."
    d "The other option is truly unique. A one of a kind offer that God has never made before."
    d "You can choose to return to your life at the same time that you left it. It will be like you never died at all."
    d "But that is not all. God has decided to offer you a gift of sorts."
    d "If, at any time in the future you end up dying again, you will be sent back one minute in time. You will be able to redo that minute to make it so that you do not die."
    d "God has decided to offer you this gift as his way of saying sorry for all the trouble."
    d "So what will it be? Come with me to Heaven or go back to Earth with your newfound ability?"
    "This was so much information to take in."
    "I thought about my father and sister, and how much I missed them."
    "If I were to choose to go to Heaven, then I could see them again. We could be a family again."
    "I imagined us doing what we use to do before the accident. Playing cards, going to the swimming pool, my dad making his famous waffles that always somehow managed to get burnt to a crisp..."
    "I also wouldn't have to deal with Jerry ever again. Or tests, or anything else that I hated. Yeah, that would be nice."
    "I made up my mind, I would go to Heaven."
    "Right before I was about to tell Dolus about my decision, an image flashed in my mind. My mom."
    "If I left her, she would be all alone. She took my dads and sisters untimely death bad enough. If I were to go as well I don't know what she would do."
    "And then I thought of Darius. I was his only friend. Without me, Jerry might get the better of him and he might lose it."
    "And then another thought came to me."
    "I knew I had to ask her a certain question."
    '"What is the catch?" I asked her quizzically.'
    d "The catch?"
    "Come on, I wasn't born yesterday. I know there has to be some catch."
    d "Oh of course! It makes perfect sense for you to ask that question!"
    d "You have had a rough life, and then all of a sudden an angel comes down and offers you a great gift!"
    d "Well, I can tell you with complete confidence, there is no catch for you."
    "It is possible that she's lying, but she is an angel of God. Could she even lie if she wanted to?"
    "Well anyways, I guess I better choose an option."
    "Oh God, what do I do?"
    d "It is time to choose. Which will it be? Heaven or Earth?"
    menu:
        "I want to go to Heaven":
            jump choice5_Heaven

        "I want to return to Earth":
            jump choice5_Earth

    label choice5_Heaven:
        #$ menu_flag = True

        d "Very well, young one. I understand your choice. Why would you want to go back to Earth after such a hard life?"
        "Suddenly, before I knew it, Dolus grabbed my arm and we teleported to another place."
        scene heaven
        with fade
        play music "heaven.mp3"
        show dolus
        d "We have arrived. this is the entrance to Heaven."
        "I looked around. I was expecting something more... majestic?"
        "It was beautiful, but it looked like a beach."
        d "Not what you were expecting, is it?"
        d "That is understandable, most people expect clouds and harps and pearly gates, not a beach."
        d "That being said, it is Heaven, and it is perfect."
        d "here you shall feel no pain, no suffering, no hardships. Now go, be free. Be happy."
        hide dolus
        "Before my very eyes, Dolus vanished into thin air. She left no trace, as if she was never here to begin with."
        show emilia
        em "[name]... Is that really you?"
        "I couldn't believe my eyes. Before me stood my sister. Just as she looked before it happened."
        em "It really is you. I...I can't believe it!."
        em "I'm so happy to see you. Come on, let's go see dad!"
        "My sister grabbed my arm and together we ran off into the sunset. A family reunited."
        "After that day I never felt any pain or suffering. I was happy."
        scene black
        with fade
        c "Developed by Chris Ferran"
        c "Story by Chris Ferran"
        c "Characters designed by Chris Ferran"
        c "Characters created in Mannequin, developed by ar14"
        c "Supervised by Michael C. Murphy"
        c "Game Developed in Ren'py"
        c 'Music from https://filmmusic.io
          "Ancient Rite" by Kevin MacLeod (https://incompetech.com)
          License: CC BY (http://creativecommons.org/licenses/by/4.0/)'
        c 'Music from https://filmmusic.io
          "A Very Brady Special" by Kevin MacLeod (https://incompetech.com)
          License: CC BY (http://creativecommons.org/licenses/by/4.0/)'
        c 'Music from https://filmmusic.io
          "Exhilarate" by Kevin MacLeod (https://incompetech.com)
          License: CC BY (http://creativecommons.org/licenses/by/4.0/)'
        c 'Music from https://filmmusic.io
          "Wholesome" by Kevin MacLeod (https://incompetech.com)
          License: CC BY (http://creativecommons.org/licenses/by/4.0/)'
        c 'Music from https://filmmusic.io
          "Easy Lemon" by Kevin MacLeod (https://incompetech.com)
          License: CC BY (http://creativecommons.org/licenses/by/4.0/)'
        c 'Music from https://filmmusic.io
          "Modern Jazz Samba" by Kevin MacLeod (https://incompetech.com)
          License: CC BY (http://creativecommons.org/licenses/by/4.0/)'
        c 'Music from https://filmmusic.io
          "String Impromptu Number 1" by Kevin MacLeod (https://incompetech.com)
          License: CC BY (http://creativecommons.org/licenses/by/4.0/)'
        c 'Music from https://filmmusic.io
          "Redletter" by Kevin MacLeod (https://incompetech.com)
          License: CC BY (http://creativecommons.org/licenses/by/4.0/)'
        c 'Music from https://filmmusic.io
          "Comfortable Mystery 2" by Kevin MacLeod (https://incompetech.com)
          License: CC BY (http://creativecommons.org/licenses/by/4.0/)'
        c 'Music from https://filmmusic.io
          "Unseen Horrors" by Kevin MacLeod (https://incompetech.com)
          License: CC BY (http://creativecommons.org/licenses/by/4.0/)'
        c 'Music from https://filmmusic.io
          "Ishikari Lore" by Kevin MacLeod (https://incompetech.com)
          License: CC BY (http://creativecommons.org/licenses/by/4.0/)'
        c 'Music from https://filmmusic.io
          "Stay The Course" by Kevin MacLeod (https://incompetech.com)
          License: CC BY (http://creativecommons.org/licenses/by/4.0/)'
        c 'Gun sound effect from https://www.freesoundeffects.com/'
        c 'Explosion sound effect from https://freesound.org/people/tommccann/sounds/235968/'
        c 'Alarm sound effect from https://freesound.org/people/ZyryTSounds/sounds/219244/'
        c 'Doorbell sound effect from https://freesound.org/people/kwahmah_02/sounds/275072/'
        c 'Knock sound effect from https://freesound.org/people/Philip_Daniels/sounds/244325/'
        c 'Dropping luggage sound effect from https://freesound.org/people/stephenbist/sounds/434781/'
        c 'Heart monitor sound effect from https://freesound.org/people/samfk360/sounds/148897/'
        c "Special thanks to Michael C. Murphy and the MTSU Honors College"

        return

    label choice5_Earth:
        #$ menu_flag = False

        d "I understand. Why would you want to go to Heaven when you have so much more life left to live?"
        d "Before we go, it is imperative that I give you the gift."
        d "Stand still, this might hurt just a bit."
        "Dolus reached her hand towards me and placed her fingertips against my heart."
        d "{i}Da huic donum Dei! {/i}"
        "Suddenly a spark of electricity jolted out of her fingertips and radiated throughout my entire body."
        "Dolus was right on with her diagnosis. It did hurt just a bit. It felt like someone shocked me after sliding their feet across the carpet."
        "Painful, but definitely not as bad as I was expecting."
        d "It is done. You now have the gift of re-death."
        d "Every time you die in the real world, you will be sent back in time one minute and you will be able to make preventative measures to make sure that death never occurs in the first place."
        d "I will now send you back to Earth. I am afraid that this is goodbye, as I can not accompany you there."
        "Dolus grabbed my arm and I was sent back to Earth."
        scene bedroom
        with fade
        play music "bedroom.mp3"
        "..."
        "......."
        "What happened?"
        "My head was killing me and my entire body felt like it was run over by a dump truck."
        "How did I get to my room?"
        "Last thing I remember was failing that test, and now I'm somehow back in my bedroom."
        "I looked over at my clock. 7:30. Class starts in an hour. I can try to remember what happened on my way their."
        "I grabbed a fresh pair of clothers from my drawer and walked to the shower."
        "I usually shower at night but my entire body was glossed over with a layer of cold sweats."
        "Whatever happened yesterday, it must have been pretty wild."
        scene bathroom home
        with fade
        "I walked into the shower and turned on the faucet."
        "I felt the cool water rush against my hand as I tested the temperature before hopping in."
        "Just as cold as always. My shower hasn't been able to run warm water for a few months now. Only cold showers for me."
        "I asked my mom to call someone to fix it but she says that we just don't have the money right now."
        "I even tried fixing in myself but that just made matters worse."
        "I did eventually start to get used to it. And at this point I even sort of enjoy it. It's refreshing."
        "As I lathered my hair with shampoo, I tried my hardest to remember what happened last night."
        "Let's see. I left the school after it got dark."
        "Why did I leave so late?"
        "Oh yeah, Mrs. Striker wanted to see me after class since I failed that stupid pop quiz so hard."
        "At least she said she wouldn't hold the grade against me. She can be pretty nice when she wants to be."
        "I'm getting sidetracked. Ok so I left the school at night and headed home. But how did I get to my bed? I can't remeber."
        "After finishing my shower, I turned the water off and dried my self off with a cool brown towel that was hanging from the bathroom door."
        "I then put on my outfit for the day, stood in front of the sink, and brushed my teeth."
        "After I finished getting ready, I headed downstairs and into the kitchen."
        scene kitchen
        with fade
        "What should I eat for breakfast?"
        "I was running kind of late so I should just get some cereal."
        show mom happy
        m "Good morning sweety, did you sleep well?"
        "I hate when she calls me that."
        show mom
        m "I made breakfast for you! Eggs, bacon, toast, more eggs, sausage, more bacon."
        "Well my mom certainly knows the way to me heart. With food!"
        "I thanked her, grabbed a clean plate, and filled it to the brim with items that were sure to give me a heart attack at some point in my life."
        "Before I started to dig in, I picked up the remote off the kitchen counter and turned the T.V. on in the living room."
        "I switched the channel over to the local news station to see what was going on in our town today."
        tv "After a 6 month long search, a family is happy to be reunited with their dog that they lost due to a leash malfunction."
        m "It's so nice to hear some good news for a change! It seems like you only hear about tragedy after tragedy nowadays."
        "I finally started to dig in to my gigantic breakfast. It was delicious as always. The bacon was crispy and juicy."
        "The eggs were succulent. The sausage was to die for."
        "As I was eating, I had a thought that it might be a good idea to ask my mom about last night."
        "I looked up from my half-eaten plate and asked her what time I got home last night."
        show mom
        m "Last night? Oh yeah you did get home a little later than usual. You told me that you had to stay after school to talk to your teacher."
        m "Why? Is everything all right?"
        "I nodded my head and went back to chowing down."
        "Weird. I don't remember telling my mom anything last night. What's going on with me?"
        tv "The weather today should be bright and sunny, with a high of 72 degrees."
        m "Sounds like another beautiful day!"
        tv "Early this morning, a family of four was found brutally murdered in their home."
        tv "They were found by their neighbors with their heads decapitated and their arms and legs tied behind their back."
        show mom angry
        m "Oh my God... That's so horrible..."
        m "I can't believe someone could be evil enough to commit such a disgusting act."
        tv "The family included a father, mother, and two young girls."
        tv "The father was 32 years old and had been happily married to his wife, age 30, for 7 years now."
        tv "Their two young daughters were twins, and they were about to celebrate their fifth birthday next week."
        tv "Investigators do not think that this was a random act of violence. Evidence shows that the father might have been involved with a local gang."
        tv "No matter the circumstances, I think we can all agree that this was a terible tragedy that will shake the lives of this town for some time to come."
        "That is horrible, I thought to myself."
        "I looked down and realized that I had finished eating breakfast."
        show mom
        m "There is still some eggs left if you're still hungry [name]"
        "I was stuffed and it was time for me to leave so I politely declined and headed to school."
        scene school entrance
        with fade
        play music "classroom.mp3"
        "I arrived to school a little earlier than I anticipated."
        "My first class wouldn't start for another 15 minutes."
        "Yo, [name]!"
        "I looked behind me to see my friend Darius"
        show darius happy
        da "You ready for another great day of school?"
        "It always amazed me how positive he could be."
        show darius
        da "I'm gonna head on in, I want to talk to Mrs. Striker about our homework that was due last night."
        "Aw geez. I knew I forgot to do something."
        da "See ya in class!"
        "As he headed on in I thought that I might as well go to my locker to get my books for the day."
        scene hallway school
        with fade
        "I walked up to my locker and opened the lock."
        "Suddenly, as I was grabbing my books, I felt a sharp pain in the back of my head."
        show jerry
        j "Oh I'm soooo sorry [name]. It seems that I accidently dropped my heavy math book on your head. My bad."
        "If he wasn't a foot taller than me I would punch the crap out of him, but as it stands I just scowled at him and walked to class."
        scene classroom
        with fade
        show striker
        s "Alright class, settle down."
        s "I know I said yesterday that we would assign groups for the project today but we are actullay going to postpone that till tomorrow."
        s "The reason for this is that I noticed how subjugated this class is."
        s "You all have your little click and you don't talk to anybody outside your immediate friend group."
        s "Frankly, I find this fact to be rather sad. Back in my day the entire class talked and hung out with each other."
        s "Nowadays you're all so preoccupied with your little devices that you can't be bothered to interact with people."
        s "Well, that's going to change today. We are going to play a little break the ice game."
        s "I am going to put on a timer that is set for 5 minutes. During this time you are going to get up and talk to someone else."
        s "We are going to do this for the entire class period, and don't worry, you will all have time to talk to everybody."
        "This sounded like the polar opposite of fun and a complete waste of time."
        "I mean, what's the point of getting to know all these people when I won't even see most of them again in 9 months."
        s "Ok, I'm setting the timer for the first round. There aren't any requirements, but you do need to keep talking for the entire time."
        s "Ok! 3...2...1...GO!!!"
        hide striker
        "Mrs. Striker started the timer and all the students in the class got up and ran to someone else."
        "I decided to sit at my desk and let people come to me."
        "The first kid that came up to me was some guy named Zacharay. He talked about sharks for the entire duration of the round and I couldn't get a single word out."
        "Not that I wanted to of course. I didn't even bother to remember what he looked like, as he and most of the people in the class are just abunch of extras who don't matter at all to the story."
        "Next up was a girl who's name I didn't even bother remembering. She was pretty quiet, as after we introduced each other we both unanimously decided to sit together in awkward silence."
        "After time was up a familiar annoyance strolled up to my desk with a scowl on his face."
        show jerry
        j "Hello again, loser."
        j "How do we keep managing to run into each other like this."
        "I really didn't have the energy to deal with this clown today."
        "What should I tell him?"
        menu:
            "Piss off":
                jump choice6_yes

            "Piss off":
                jump choice6_no

        label choice6_yes:
            j "Oh wow, that was real rude of you."
            j "And here I was trying to come over here and be friendly."
            j "Oh well, I guess I'll just leave you over here in your lonesome."

            jump choice6_done

        label choice6_no:
            j "Oh wow, that was real rude of you."
            j "And here I was trying to come over here and be friendly."
            j "Oh well, I guess I'll just leave you over here in your lonesome."

            jump choice6_done
        label choice6_done:
    hide jerry
    "A few more people came up who aren't even worth mentioning"
    "Near the end of the game, Darius finally approached my desk."
    show darius
    da "Fancy meeting your here."
    da "Have you met any cool people?"
    menu:
        "I met a guy who wouldn't shut up about sharks":
            jump choice7_yes

        "Nope":
            jump choice7_no

    label choice7_yes:
        show darius happy
        da "Oh you mean Zacharay?"
        da "Yeah I talked to him too."
        da "He was telling me about his favorite movie. Can you guess what it is?"
        "I shook my head to indicate that I didn't care enought to even guess."
        show darius
        da "Jaws. His favorite movie is Jaws."

        jump choice7_done

    label choice7_no:
        da "That sucks. Did you even try to interact with anybody?"
        "I shook my head to indicate that I have not in fact tried to talk to anybody."
        da "You know if you talked to more people you would make more friends."
        da "Anyways I met a girl named Stephanie."
        da "She seems pretty cool. We talked about books the whole time."
        da "It turns out that she's a total bookworm!"

        jump choice7_done
    label choice7_done:
        da "Are you ok? You seem kind of down."
        "I decided that it would be a good idea to tell him about my memory loss."
        da "Dang, so you can't remember anything that happened last night? And your mom says that you talked to her but you don't remember having that conversation at all?"
        da "That's kinda freaky, not gonna lie."
        da "I'm sure you'll remember it eventually. You're probably just exhausted from all the homework we have been assigned recently."
        "Considering that I didn't do any of the homework, I knew that couldn't be it."
        show darius happy
        da "Alright, well it's time to introduce myself to the next person."
        da "I guess I'll see you at lunch [name]!"
        hide darius happy
        "Darius walked away and went to talk to some goth guy in the back of the class."
        "I looked around the room and realzied there was only one person who hasn't come up to my desk yet."
        "As soon as I realzied this, that same person made eye contact with me, smiled, and headed my way."
        show winrey school
        w "Hey, I don't think I've formally introduced myself to you yet."
        w "My names Winrey! And your name is [name], isn't it?"
        "Y..yes... I stammered."
        w "Well it's very nice to meet you!"
        w "So, what do you like to do in your free time?"
        "What do I say? My heart was beating out of my chest and I could feel sweat beging to drip from my brow."
        "Why am I so nervous all of a sudden? I mean, I know I really like her but it's not like me to completely shut down like this."
        "I gotta say something or else I'll look like a total freak!"
        w "I guess you're kind of shy, huh?"
        w "That's fine, I have a little sister who never talks at all!"
        w "You don't have to say a word! I'll do all the talking!"
        w "Well, anyways, as I was saying, My names Winrey."
        w "I'm a member of our school's soccer team as well as the class president, but you probably knew that last part already!"
        play sound "alarm.wav"
        "{i} BEEP! BEEP! BEEP! {/i}"
        "The timer went off indicating that the 5 minutes were up."
        w "Well anyways, I'll see you later [name]!"
        hide winrey
        "I can't believe it. I just made myself look like a total loser."
        "I couldn't even bring myself to say a single word during the entire time."
        "I bet she's gonna go tell all of her friends about how weird I am."
        "No, she's way too nice to do that. She will probably just forget about our encounter all together. And if she does remember, I'm sure she won't tell anybody."
        "Either way, there goes any chance of us ever becoming friends."
        "I guess I can't blame her. Who would want to be friends with a loser like me? Especially one who is constantly negative about everything."
        "If I ever want to gain more friends, I need to get a complete attitude adjustment."
        "During that entire game I went out of my way to talk to as few people as possible."
        "I'm sure then entire class hates me at this point."
        "Before I could wallow in my own self-pity for a second longer, Mrs. Striker got up in front of the class to say something."
        show striker happy
        "You all did a wonderful job with this exercise today!"
        "Didn't it feel great to talk to your fellow classmates instead of staring down at your phones like you normally do?"
        "I'm very proud of all of you, and now that you are all familiar with each other, we will be ready to choose teams for the project tomorrow."
        "I'll go over the details about how that will work tomorrow, but we are out of time for today."
        "You all go have a great, nutritious lunch!"
        scene school cafeteria
        with fade
        "I walked up to the lunch line to get my food."
        "I am in a special program that allows me to get free lunches every day at school."
        "Darius and most of the other people bring their lunches from home, and for good reason. The school lunches are terrible."
        "The portions are pathetically small and it all tastes like rubber."
        "There were only four people in front of me to get the school-made lunch"
        "I peered over the guys head in front of me to see what sorry excuse for food they would be dishing out today."
        "It looks like... some sort of unidentifiable pasta. For the sides they had greenish beans and half-mashed potatos."
        "For dessert they had...well, I couldn't really tell what it was supposed to be."
        "It was a greenish-brown color and I could smell it from where I was standing."
        "I decided right then and there that I would not partake in dessert."
        "It's probably a good thing it looks so gross. That way I'm not tempted to eat it, which will save me a lot of unneeded calories."
        "And after the gigantic breakfast I annihilated this morning, the last thing I need is a big dessert."
        "I scooped out a bowl full of the pasta and got a small helping of each of the sides. For the drink I decided to just get a water."
        "I grabbed my tray and walked over to the tables to find Darius."
        "I saw him sitting by himself at a table outside, eating a delicious looking homemade meal."
        "I sat my tray down across from him."
        show darius
        da "What's up [name]?"
        "I said hi and looked at his meal to see what his mom packed him."
        "Steak? His mom seriously packed him an entire freaking steak?!?!"
        "He must have noticed me eyeing his food because he laughed."
        da "Yeah, I was surprised too when I saw what my mom made for me."
        da "Evidently she wanted to do something special for me today. I don't really understand why. It's not my birthday or anything."
        da "Do you want some of it? I wont be able to eat the entire thing by myself. It's at least a 20oz steak."
        "I would definitely rather eat that than the slop the school provided for me."
        "Should I accept his offer?"
        menu:
            "I'll take some of it, thanks.":
                jump choice8_yes

            "No thanks, my meal looks good enough":
                jump choice8_no

        label choice8_yes:
            show darius happy
            da "Cool! pass me your plate and I'll cut you off a slice"
            "I handed over my tray to him and he cut of around half of his entire steak."
            "I thanked him and began devouring it like a dog."
            da "Wow! you must have been really hungry! Thanks for helping me eat it. My mom would be upset if I brought some of it home. She would have thought that I didn't like it."

            jump choice8_done

        label choice8_no:
            da "Ok, that's cool. I'll try my best to eat it all myself. If I don't my mom will think I didn't like it."
            "I looked down at my own food in misery and slowly chewed it up."
            "I don't know how, but it somehow tastes even worse than it looks."
            "I could have made a better meal, and that's the biggest insult I can give, as I'm a truly terrible cook."

            jump choice8_done
        label choice8_done:
            show darius
            da "Did you see the new episode of BroBro's Crazy Journey last night?!?!"
            da "Oh wait, I forgot you can't remember anything from last night."
            da "Dang that sucks... I really wanted to talk about what happened..."
            "Darius always likes to discuss BroBro with me."
            "It's been a tradition for us to watch the show and then come together at lunch and discuss what happened on the latest episode."
            "All the cool fight scenes, character developments, and of course Darius likes to talk about his theories about what he thinks might happen in the next episode."
            "I have already read all of the source material, so I probably know what's gonna happen."
            "There is always the chance that they deviate from the original books, but it's unlikely."
            "If they did end up changing the story, I would hate to have it spoiled for me."
            "Should I let Darius talk about last night's episode?"
            menu:
                "You can tell me what happens":
                    jump choice9_yes

                "No spoilers please":
                    jump choice9_no

            label choice9_yes:
                show darius happy
                da "Whoa, seriously? You don't mind at all if I spoil it?"
                da "Well, don't mind if I do!"
                da "Ok, so the episode starts with BroBro and his bro Goto going to Italy to stop Lolo from destroying the world with his Sit power."
                da "They finid out that his sit power is called {i} Za Eartho! {/i} and whenever he uses it, trees come out of Brobro's mouth!"
                da "So Lolo uses his power to incapacitate Brobro! And then it's all up to Goto to stop Lolo from destroying the entire world!"
                da "But at the end of the episode, we find out that Brobro's old ally, Zetzuo, is still alive! And he's gonna help Goto beat Lolo!"
                "I couldn't believe it! In the original story, Zetzuo never came back from the dead!"
                "Dang it! I knew I shouldn't have let Darius spoil it for me..."

                jump choice9_done

            label choice9_no:
                show darius
                da "Oh... Ok. I guess it's understandable that you wouldn't want it spoiled for you."
                da "I gotta say though, it was totally awesome!"
                da "Anyways, you should watch it ASAP so you don't have it spoiled for you."

                jump choice9_done

        label choice9_done:
            show darius
            "I told him that I would make sure to watch it when I get the free time"
            "I then opened my mouth wide and took a gigantic bite out of my food"
            da "Hey [name], wanna hear a joke that my mom told me?"
            "I nodded my head as I couldn't really talk with my mouth filled to the brim"
            show darius happy
            da "Ok, what did the dish soap say to the washing machine?"
            "I shrugged my shoulders to indicate that I had no idea, as my mouth was still full of food."
            da "Nothing! They're both inanimate objects and thus incapable of human speech."
            "The sheer terribleness of the joke threw me off so hard that I couldn't help but burst out laughing."
            "HAHAHAHAHHAHAHA!!!"
            "I realized in that moment that I had just made a huge, irreversible mistake."
            "My mom always told me not to talk or laugh with my mouth full, and in that split second I finally realized why."
            "I gasped for air but nothing came out."
            "I was choking on my food, and I coudln't get a single drop of oxygen into my body!"
            "I took a big gulp of water but I just spit it back out immediately."
            show darius angry
            da "Holy crap are you ok!?!?"
            "I was most certainly not ok, and he must have realized that."
            da "HELP! SOMEBODY HELP! HE'S CHOKING!!!"
            "Before anybody could get to me to help, I took one desperate gasp to try and get some air out."
            "Nothing."
            "I hit the ground and everything went dark."
            scene black
            with fade
            play music "black.mp3"
            "....."
            "So that's how I die huh."
            "I choked on some food after hearing a terrible joke."
            "People are gonna laugh at my funeral."
            scene school cafeteria
            with fade
            play music "classroom.mp3"
            show darius
            da "Hey [name], wanna hear a joke that my mom told me?"
            "......."
            "Wait, what the heck just happened?"
            "I was choking... I... I was dead..."
            "...And then, I...I somehow got back here?"
            "I realized that I still had the food in my mouth so I spit it all out onto my tray."
            da "Dang was it that bad?"
            da "So you don't wanna hear my joke then?"
            "I asked him if his joke was going to be about dish soap."
            show darius angry
            da "Hey! How did you know that?"
            da "I told that joke to Winrey earlier during the 5 minutes we had together."
            da "Did she tell you that joke during your two 5 minutes together?"
            "I didn't have time for this. What just happened."
            "Without even acknowledging Darius's question, I flew out of my seat and ran home as quick as I could."
            "I was gonna skip out on half the school day, and I was sure to get into trouble for doing so, but I can't be bothered to worry about that now."
            "I need to think about what happened."
            scene bedroom night
            with fade
            play music "bedroom-night.mp3"
            "It was a few hours after I got home."
            "Of course my mom was worried when she saw that I skipped out on class, but I just told her I wasn't feeling well and I ran up to my bedroom to think."
            "I still couldn't remember anything."
            "I looked over at my clock and saw that it was approaching midnight."
            "It wasn't until that exact moment that I realized how exhausted I was."
            "Dying will do that to you I guess."
            "I decided to go to bed and worry about it all in the morning."
            "I put on my pajamas, and hopped into bed."
            scene moon over field
            with fade
            play music "black.mp3"
            show robber1
            r "WHAT ARE YOU DOING KI..."
            play sound "gun.mp3"
            "{i} BANG!!!! {/i}"
            r "Oh my God... What have I done?!"
            r "I gotta get out of here!"
            scene black
            with fade
            show dolus
            d "I understand. Why would you want to go to Heaven when you have so much more life left to live?"
            d "Before we go, it is imperative that I give you the gift."
            d "Stand still, this might hurt just a bit."
            d "{i}Da huic donum Dei! {/i}"
            d "It is done. You now have the gift of re-death."
            d "Every time you die in the real world, you will be sent back in time one minute and you will be able to make preventative measures to make sure that death never occurs in the first place."
            d "I will now send you back to Earth. I am afraid that this is goodbye, as I can not accompany you there."
            scene bedroom
            with fade
            play music "bedroom.mp3"
            "Those dreams that I had last night. They felt so...real"
            "That was when I realized the cold hard truth."
            "Those dreams that I had, they weren't dreams. They were memories. Memories that I forgot. Memories of the first time I died. Memories of how I ended up back here in the first place."
            "A few other images flashed in my head all at once. Images of a man demanding that I give him money. Images of me realizing I don't have my wallet."
            "Images of me floating in a dark abyss all by myself for a long time."
            "I remember it all."
            "I remember that angel, Dolus was her name I think, I remember her explaining the situation to me."
            "How I was dead and how it was a huge accident. How God never intended for me to die that night."
            "How I was offered a choice, go to Heaven and live in eternal joy, or go back to Earth."
            "I remember how I chose to come back here, not because I really wanted to, but because I knew my mom would miss me. And Darius, and everybody else in my life."
            "I also remember Dolus giving me a gift."
            "What did she call it? Oh yeah, thats right, re-death."
            "She said that if I ever die again in the future, I will be sent back one minute in time and will be given another chance to live."
            "That's it! That's the mystery I've been trying to solve! That's where I was that night! That's why I couldn't watch the new episode of BroBro!"
            "And that's why I came back to life after I died. It's because I have a power, the power of re-death!"
            "This feels like something you would read in a crappy visual novel made by some guy for a school project! It's not something that would ever happen in real life!"
            "But yet, here I am. A real person who has been given a gift."
            "What should I do with this gift?"
            "My mind immediately went back to a quote I remember hearing in an old movie that I watched when I was just a young boy."
            "When ya got a power that no one else has, you should use it responsibly."
            "You should use it to help other people, not to help your life be better, but to help other people's lives be better."
            "....."
            "Why shouldn't I use it for myself though?"
            "Dolus herself said that I've had a rough life. I could use this power to improve everything about it."
            "I could use it to win the lottery, get perfect scores on every test, get a girlfriend!"
            "I then thought back to a particular memory that happened yesterday."
            scene classroom
            with fade

            show winrey school
            w "Hey, I don't think I've formally introduced myself to you yet."
            w "My names Winrey! And your name is [name], isn't it?"
            "Y..yes... I stammered."
            w "Well it's very nice to meet you!"
            w "So, what do you like to do in your free time?"
            "What do I say? My heart was beating out of my chest and I could feel sweat beging to drip from my brow."
            "Why am I so nervous all of a sudden? I mean, I know I really like her but it's not like me to completely shut down like this."
            "I gotta say something or else I'll look like a total freak!"
            w "I guess you're kind of shy, huh?"
            scene bedroom
            with fade

            "If I would have used my power in that very moment, I could have went back in time to redo that conversation so I wouldn't have looked like a total moron."
            "Wait, but to use my power I have to die, so that's out of the question."
            "I mean, to die whenever I wanted to I would have to kill myself, and I certainly don't have any way of doing that."
            "That's when I remembered something. Before my dad died, he used to take me out to a local shooting range and show me how to use a gun."
            "If I could just find that gun, I could kill myslef with ease!"
            "In that moment I realized just how absurd this entire situation was."
            "If anybody heard me say that part out loud, they would think I'm suicidal."
            "But I only want to do this to help myslef, and it's not like I'm hurting anybody by doing this."
            "So what if i reverse time to do better on a little quiz here and there. I'm not gonna use it to get away with murder or anything sinister like that."
            "I made up my mind. I will get my dad's gun and use to to go back in time at any point that something doesn't go the way that I desire."
            "If I'm gonna do this I should first set up a couple of ground rules."
            "Rule number 1. I won't use the power to commit crimes."
            "No robbing banks and evading the police with my rewind power."
            "I also shouldn't use it to win the lottery, as someone else might have been destined to win it."
            "Rule number 2. No betting on sport's games."
            "Using my power to gamble would make it so that other people would lose money, and I don't wanna hurt anybody."
            "I'm only using this power for my own good, if I use it in anyway to hurt someone else, then I would never be able to forgive myself."
            "Rule number 3... I can't think of anything else."
            "Oh well, I'll just use my own discretion to keep myself in check."
            "When it comes down to it, the only thing I want to do is make sure that my power doesn't end up hurting anybody."
            "I just want to use it to help myself."
            "Next up, I need to figure out where the heck my dad left the gun at."
            "I know we still have it, as my Mom refuses to give anything up that belonged to my dad or sister."
            "In fact, she has done her best to keep everything exactly how it was before it all happened."
            "My sisters old room looks exactly the same as it used to."
            "...Or at least I think it does. I haven't been able to bring myself to go in there since it happened..."
            "Anyways, my dad used to keep the gun locked up in a safe that he kept in the living room."
            "As far as I know, it should still be there."
            "I know for a fact that my mom wouldn't have touched it at all, as she has always hated guns."
            "The only other person that could get near it would be me, and while I have had a bad case of memory loss recently, I doubt I would have touched it at all."
            "Well, only one way to know for sure, I gotta go check my parents bedroom."
            scene living room
            with fade

            "I walked up to the safe to open it, but I realized that I was going to have to deal with a little problem."
            "The safe has a number pad on it, and to get in you had to enter in the correct 4-number code."
            "whenever we used the gun before, my dad would always be the one to open the safe, so I never knew what the code was."
            "At least my mom isn't home right now, so I don't have to deal with her asking me about what I'm doing."
            "I'm pretty sure she wouldn't be thrilled to learn that I am using the gun to try and kill myself."
            "Even if it isn't permanent, she still probably wouldn't like it. And I know I shouldn't tell her about my power just yet. I don't want to worry her."
            "I tried my hardest to think about what the code could possibly be."
            "I tried entering his birth year."
            "Nothing."
            "Ok, how about my mom's birthday?"
            "Nope."
            "My sister's?"
            "Nada."
            "Maybe it's mine..."
            "I entered in the year I was born in a desperate attempt to enter the vault."
            "Still not it..."
            "What could it possible be?"
            "Maybe there is some clues around the room..."
            "Where should I check first?"
            menu:
                "Check around the couch":
                    jump choice10_couch

                "Check around the tv":
                    jump choice10_tv

                "Check the coffee table":
                    jump choice10_coffeetable

            label choice10_couch:
                "I walked over to our ugly green couch and bent down to look under the couch."
                "All I saw were a few dust bunnies, a pen, and a quarter."
                "Nothing worth picking up down there."
                "Next I looked around at our piss-colored pillows."
                "I opened them up to see if there were any secrets hiding inside the materials."
                "Out of luck, once again. The only thing that was there was the fluffy materials that are supposed to be there."
                "I then decided to check under the actual cusions themselves."
                "I found a couple more quarters, a dime, and a penny, but no clues for what the code could possible be."
                "Where should I check next?"


                menu:
                    "Check around the tv":
                        jump choice102_tv

                    "Check the coffee table":
                        jump choice102_coffeetable

                label choice102_tv:
                    "I looked over to our tv."
                    "There is nowhere to hide anything in the actual tv so I can rule that out."
                    "The tv is on a stand that has a couple of drawers. Maybe there is something in one of them?"
                    "I opened the drawer on the far left all the way."
                    "Inside there were a few old dvd's that my dad and I used to watch when I was a kid."
                    "Mission Possible, Sherlock Holmes, The Fighters... So many good memories."
                    "I opened each dvd case on by one and checked every nook and cranny."
                    "Nothing besides the actual disks themselves."
                    "I moved on to opening the middle drawer."
                    "It was completely empty."
                    "I then opened the final drawer on the far right."
                    "Sitting inside was an old video game console that I had as a kid."
                    "I should plug this in and play it sometimes, it was really fun."
                    "Not now though. I'm on an important mission."
                    "Next I decided to check a row of books that were located directly above the left drawer."
                    "I flipped through each one carefully, hoping to find a little slip of paper or some extra writing on one of the pages."
                    "No such luck, I looked through every book and came up empty."
                    "Where else could it possible be!"
                    "In a last ditch effort, I looked around the room for anywhere a clue could possible be hiding."
                    "I looked under the carpet, I digged through the dirt of the plant, and I looked around the lamp but I always managed to come up completely empty handed."
                    "I looked back over near the tv and noticed a small, framed photograph sitting below it."
                    "I scooted up next to it and picked it up."
                    "It was a picture of my parents wedding day."
                    "I opened it up and a little slip of paper fell out from behind the bare photo."
                    "I picked it up, with my hands shaking so hard it could have started an earthquake. I flipped the paper over and on the back was 4 numbers scribbled in my dad's handwriting."
                    "2417"
                    "Could this possibly be it?"
                    jump choice10_done


                label choice102_coffeetable:
                    "I walked up to our coffee table and looked around it."
                    "The top part is made out of glass so it is see-through."
                    "Under that part is a little compartment that you can open to store whatever you want."
                    "I opened that, desperate for any clues, and inside I found nothing. It was completely empty."
                    "This is a dead end."
                    "Where should I check next?"
                    menu:
                        "Check around the tv":
                            jump choice103_tv

                    label choice103_tv:
                        "I looked over to our tv."
                        "There is nowhere to hide anything in the actual tv so I can rule that out."
                        "The tv is on a stand that has a couple of drawers. Maybe there is something in one of them?"
                        "I opened the drawer on the far left all the way."
                        "Inside there were a few old dvd's that my dad and I used to watch when I was a kid."
                        "Mission Possible, Sherlock Holmes, The Fighters... So many good memories."
                        "I opened each dvd case on by one and checked every nook and cranny."
                        "Nothing besides the actual disks themselves."
                        "I moved on to opening the middle drawer."
                        "It was completely empty."
                        "I then opened the final drawer on the far right."
                        "Sitting inside was an old video game console that I had as a kid."
                        "I should plug this in and play it sometimes, it was really fun."
                        "Not now though. I'm on an important mission."
                        "Next I decided to check a row of books that were located directly above the left drawer."
                        "I flipped through each one carefully, hoping to find a little slip of paper or some extra writing on one of the pages."
                        "No such luck, I looked through every book and came up empty."
                        "Where else could it possible be!"
                        "In a last ditch effort, I looked around the room for anywhere a clue could possible be hiding."
                        "I looked under the carpet, I digged through the dirt of the plant, and I looked around the lamp but I always managed to come up completely empty handed."
                        "I looked back over near the tv and noticed a small, framed photograph sitting below it."
                        "I scooted up next to it and picked it up."
                        "It was a picture of my parents wedding day."
                        "I opened it up and a little slip of paper fell out from behind the bare photo."
                        "I picked it up, with my hands shaking so hard it could have started an earthquake. I flipped the paper over and on the back was 4 numbers scribbled in my dad's handwriting."
                        "2417"
                        "Could this possibly be it?"
                        jump choice10_done

            label choice10_coffeetable:
                "I walked up to our coffee table and looked around it."
                "The top part is made out of glass so it is see-through."
                "Under that part is a little compartment that you can open to store whatever you want."
                "I opened that, desperate for any clues, and inside I found nothing. It was completely empty."
                "This is a dead end."
                "Where should I check next?"
                menu:
                    "Check around the tv":
                        jump choice104_tv

                    "Check around the couch":
                        jump choice102_couch

                label choice104_tv:
                    "I looked over to our tv."
                    "There is nowhere to hide anything in the actual tv so I can rule that out."
                    "The tv is on a stand that has a couple of drawers. Maybe there is something in one of them?"
                    "I opened the drawer on the far left all the way."
                    "Inside there were a few old dvd's that my dad and I used to watch when I was a kid."
                    "Mission Possible, Sherlock Holmes, The Fighters... So many good memories."
                    "I opened each dvd case on by one and checked every nook and cranny."
                    "Nothing besides the actual disks themselves."
                    "I moved on to opening the middle drawer."
                    "It was completely empty."
                    "I then opened the final drawer on the far right."
                    "Sitting inside was an old video game console that I had as a kid."
                    "I should plug this in and play it sometimes, it was really fun."
                    "Not now though. I'm on an important mission."
                    "Next I decided to check a row of books that were located directly above the left drawer."
                    "I flipped through each one carefully, hoping to find a little slip of paper or some extra writing on one of the pages."
                    "No such luck, I looked through every book and came up empty."
                    "Where else could it possible be!"
                    "In a last ditch effort, I looked around the room for anywhere a clue could possible be hiding."
                    "I looked under the carpet, I digged through the dirt of the plant, and I looked around the lamp but I always managed to come up completely empty handed."
                    "I looked back over near the tv and noticed a small, framed photograph sitting below it."
                    "I scooted up next to it and picked it up."
                    "It was a picture of my parents wedding day."
                    "I opened it up and a little slip of paper fell out from behind the bare photo."
                    "I picked it up, with my hands shaking so hard it could have started an earthquake. I flipped the paper over and on the back was 4 numbers scribbled in my dad's handwriting."
                    "2417"
                    "Could this possibly be it?"
                    jump choice10_done

                label choice102_couch:
                        "I walked over to our ugly green couch and bent down to look under the couch."
                        "All I saw were a few dust bunnies, a pen, and a quarter."
                        "Nothing worth picking up down there."
                        "Next I looked around at our piss-colored pillows."
                        "I opened them up to see if there were any secrets hiding inside the materials."
                        "Out of luck, once again. The only thing that was there was the fluffy materials that are supposed to be there."
                        "I then decided to check under the actual cusions themselves."
                        "I found a couple more quarters, a dime, and a penny, but no clues for what the code could possible be."
                        "Where should I check next?"
                        "I realized the only place I haven't looked at that point was the tv, so I decided to walked over to that section and look around for clues."
                        "I looked over to our tv."
                        "There is nowhere to hide anything in the actual tv so I can rule that out."
                        "The tv is on a stand that has a couple of drawers. Maybe there is something in one of them?"
                        "I opened the drawer on the far left all the way."
                        "Inside there were a few old dvd's that my dad and I used to watch when I was a kid."
                        "Mission Possible, Sherlock Holmes, The Fighters... So many good memories."
                        "I opened each dvd case on by one and checked every nook and cranny."
                        "Nothing besides the actual disks themselves."
                        "I moved on to opening the middle drawer."
                        "It was completely empty."
                        "I then opened the final drawer on the far right."
                        "Sitting inside was an old video game console that I had as a kid."
                        "I should plug this in and play it sometimes, it was really fun."
                        "Not now though. I'm on an important mission."
                        "Next I decided to check a row of books that were located directly above the left drawer."
                        "I flipped through each one carefully, hoping to find a little slip of paper or some extra writing on one of the pages."
                        "No such luck, I looked through every book and came up empty."
                        "Where else could it possible be!"
                        "In a last ditch effort, I looked around the room for anywhere a clue could possible be hiding."
                        "I looked under the carpet, I digged through the dirt of the plant, and I looked around the lamp but I always managed to come up completely empty handed."
                        "I looked back over near the tv and noticed a small, framed photograph sitting below it."
                        "I scooted up next to it and picked it up."
                        "It was a picture of my parents wedding day."
                        "I opened it up and a little slip of paper fell out from behind the bare photo."
                        "I picked it up, with my hands shaking so hard it could have started an earthquake. I flipped the paper over and on the back was 4 numbers scribbled in my dad's handwriting."
                        "2417"
                        "Could this possibly be it?"
                        jump choice10_done

            label choice10_tv:
            "I looked over to our tv."
            "There is nowhere to hide anything in the actual tv so I can rule that out."
            "The tv is on a stand that has a couple of drawers. Maybe there is something in one of them?"
            "I opened the drawer on the far left all the way."
            "Inside there were a few old dvd's that my dad and I used to watch when I was a kid."
            "Mission Possible, Sherlock Holmes, The Fighters... So many good memories."
            "I opened each dvd case on by one and checked every nook and cranny."
            "Nothing besides the actual disks themselves."
            "I moved on to opening the middle drawer."
            "It was completely empty."
            "I then opened the final drawer on the far right."
            "Sitting inside was an old video game console that I had as a kid."
            "I should plug this in and play it sometimes, it was really fun."
            "Not now though. I'm on an important mission."
            "Next I decided to check a row of books that were located directly above the left drawer."
            "I flipped through each one carefully, hoping to find a little slip of paper or some extra writing on one of the pages."
            "No such luck, I looked through every book and came up empty."
            "Where else could it possible be!"
            "In a last ditch effort, I looked around the room for anywhere a clue could possible be hiding."
            "I looked under the carpet, I digged through the dirt of the plant, and I looked around the lamp but I always managed to come up completely empty handed."
            "I looked back over near the tv and noticed a small, framed photograph sitting below it."
            "I scooted up next to it and picked it up."
            "It was a picture of my parents wedding day."
            "I opened it up and a little slip of paper fell out from behind the bare photo."
            "I picked it up, with my hands shaking so hard it could have started an earthquake. I flipped the paper over and on the back was 4 numbers scribbled in my dad's handwriting."
            "2417"
            "Could this possibly be it?"
            jump choice10_done
    label choice10_done:
        "I walked over to the safe and typed the code in."
        "I pressed the green enter key and prayed to the God that gave me this gift in the first place."
        play sound "safe.wav"
        "{i} Ding! Ding! Ding!{/i}"
        "An all too familiar sound penetrated my ears. The sound of success! I remember hearing that sound whenever my dad got the gun out of the safe!"
        "I pulled the lever open, and inside was exactly what I was hoping to find."
        "A small handgun, that was slightly larger than my hand."
        "I wasn't sure what the actual name of the gun was, but I knew from experience that it was powerful enough to penetrate straight through plenty of objects, as my dad and I would shoot various objects whenever we went to shoot together."
        "I was completely sure that it would be strong enough to kill me whenever I needed to go back in time."
        "Once again, it struck me just how weird this entire situation was."
        "I looked over at my clock and realized it was almost time for school. I would have to skip breakfast today in order to make it to class on time."
        "I ran upstairs to get ready as quick as humanly possible and bursted out of my front door."
        scene city1
        with fade
        "I ran down all the streets and side roads that made up my daily journey to my school."
        "No time to stop and smell the roses today! If I'm late I might get in trouble."
        "I then remembered what Mrs. Striker said the other day."
        "She told us that we would be put in groups today for our big project for the semester."
        "I hope I get in a group with cool people. Especially someone like Darius."
        "Honestly, as long as I dont end up in a group with that a-hole Jerry, I think I'll manage."
        "I wonder how she's gonna choose who to put in what group?"
        "I guess I'll find out all the juicy details soon enough."
        scene classroom
        with fade
        play music "classroom.mp3"
        "After running all the way through the town to get to school as soon as possible, I finally made it."
        "I walked into Mrs. Striker's classroom and sat down in my desk near the back of the class."
        "As I expected, I was the last one there, as everyone else was already sitting down and chatting with the people closest to them."
        "Darius sits on the other side of the classroom from me, so I never get to talk with him."
        "He sits close to Winrey, lucky..."
        "I do have the displeasure of sitting within earshot of Jerry. He never really talks to anybody besides me and Darius."
        "It's honestly kind of sad. In all the movies I've seen, the bullies are usually really popular, or at least have a couple of cronies to do their bidding."
        "Not Jerry, he was a bigger loser than I am, and that's saying something."
        "If he wasn't a total jerk I wouldn't mind being his friend, but for some reason all he ever wants to do is make fun of me and Darius."
        "Oh well, not my problem. If he wants to ruin his life and have no friends, thats on him."
        show striker
        s "Ok class, as we discussed yesterday, today we are going to pick the groups for the big project."
        s "I will be sure to let you know what we will be doing for the project tomorrow, but for today it will be enough to just find out who will be working with who."
        s "Now there are 23 students in this class, so unfortunately the groups will not be even."
        s "I have decided that the class will be split up into 5 groups of 4, and one extra group of 3."
        s "The way we will decide the groups is quite simple. I have not directly chosen who will be in what group, and instead it will be entirely random."
        s "I will call you up to the front of the class one by one, and you will pick up a small slip of paper from this cup."
        s "The paper will have a number on it. That number will be the group that you will be a part of."
        s "Does everyone understand?"
        "The class nodded their heads in unison."
        s "Ok, good. First up is Zachary."
        "Zachary walked up to the front of the class and shoved his hand into the cup."
        "He announced to the class that he was in group 1."
        s "Next up will be Winrey."
        show winrey school at right
        "Winrey walked up with confidence in every step she took and gently placed her hand into the cup."
        w "I'm in group 3!"
        "God, I hope I'm lucky enough to get in group 3."
        hide winrey school
        s "Come up here Jerry, it's your turn."
        show jerry at left
        "Jerry got out of his seat with an equal amount of confidence as Winrey, and stuck his hand into the cup."
        j "Group 4. If anybody else gets put in my group and is anything less than a complete genius like I am, they will be verry sorry."
        show striker angry
        s "Ok Jerry, no need to be rude. Sit down please."
        "Jerry scowled at Mrs. Striker and sat down."
        hide jerry
        show striker
        "A few more people went up and picked a number out of the cup."
        "One other person got put in a group with Jerry, but so far no one else was in Winrey's group."
        s "Darius, you're up next."
        show darius happy at left
        da "Cool!"
        "Darius walked up happily and picked his number."
        da "Mine says the number 3. I'm in group 3!"
        show winrey school at right
        w "That means you're with me! I hope we become good friends."
        da "I know we will! With the two of us together, we are sure to ace this project!"
        hide darius happy
        hide winrey
        "Ok. I REALLY need to get into group 3 now."
        "A few more people went up front and I realized I was one of the few people left to go."
        "Darius and Winrey still didn't have another teammate yet, which meant there were still two more papers with group 3 left."
        "Jerry had 2 teammates, which meant I could still end up in his group as well."
        "There was also a couple of other groups with an empty slot."
        s "[name], It's your turn. Come up to the front and choose your fate!"
        "Finally, I can figure out my fate for this project."
        "Will I end up with Darius and Winrey? That would be the best possible outcome."
        "Or maybe I'll get screwed over and end up with Jerry. That would suck big time."
        "I guess the most likely outcome is that I end up with a group of randoms."
        "I guess I could en..."
        show striker angry
        s "Can you hurry it up already!!! We don't have all day!"
        "Everyone in the class giggled and looked back at me."
        "I slowly stood up as my seat creaked behind me."
        "I walked up to the front of the classroom and put my hand into the cup."
        "I felt around in their for a couple of seconds, before nervously picking up a single sheet of paper."
        "I looked down at it and saw that it was blank."
        "Whats wrong with it! Why isn't there anything written on it? Is this some sort of cruel joke that the class is playing on me?"
        "I told Mrs. Striker that my paper was blank and that there must be some mistake."
        s "Flip it over, genius."
        "The class once again started laughing at my expense as I realized my idiotic mistake."
        "I flipped it over, and sure enought there was a number sitting inconspicuously on the other side."
        "4... Wait, that's..."
        show jerry angry at left
        j "Ugh... Are you serious? I actually have to work with [name]?"
        s "Those are the rules Jerry."
        show striker happy
        s "Ok [name], you have your number so you can sit down."
        "I couldn't believe my bad luck. Out of everybody in the class, out of every possible group, out of every possible combination, I end up with him!"
        "I have to spend the rest of the semester working with that d-bag while Darius gets to spend all his free time with the coolest girl in class?"
        "This sucks! I can't do this! No! I {i} won't {/i} do this!"
        "I have to ask Mrs. Striker if there is any way that I can be grouped with someone else."
        '"Umm... Mrs. Striker?" I asked nervously.'
        show striker
        s "What is it?"
        '"Well, is there any way that I can be grouped with someone else. I mean, no offense to Jerry, but we do not really get along and I think it would be best for the both of us if we were seperated."'
        j "I can't belive I'm saying this, but I agree with the idiot."
        show striker angry
        s "Absolutely not! The both of you will work together and you will get along!"
        s "I've watched you two call each other names and be hatefull all semester and frankly, I'm sick of you both!"
        s "You two seriously need an attitude adjustment!"
        s "You Jerry, you have a serious superiority complex! You think you're better than everybody else just because you make good grade!"
        s "well guess what mister, life isn't all about grades! You might be gifted at testing, but with you're attitude, you are gonna fail hard once you go out into the real world."
        s "Do you honestly believe that any company is going to want to hire an arrogant little prick like you?"
        s "You might be gifted, but that doesn't give you an excuse to be rude to everyone all the time!"
        s "it's no wonder that I always see you sitting by yourself. You have no friends because you're so unlikable."
        j "You say I have a superiority complex? That would imply that I'm not superior to everyone else, which is false."
        j "My IQ is leagues above everyone's in this room, including you teacher."
        s "That's it! You will have detention after school every day for the next week!"
        j "Whatever, like I care."
        s "I'm done talking to you."
        "I went to sit down, as I never meant to start this whole scene."
        s "Oh where do you think you're going? You're just as bad as Jerry and I think it's time that you know it!"
        s "You are always so negative! Always talking about how nothing ever goes your way and how your life sucks."
        s "I know you have been through some terrible things, but that's no excuse for your terrible behavior."
        s "So yeah, I am going to make you two work together. Maybe if you two are forced to spend time with one another you will see just how similar you two are."
        s "Maybe you will even become friends."
        "Friends? Me and Jerry? No way! After everything he's done to me, I would never even amuse the idea of us becoming friends."
        "I can't even stand to look at the guy. With his stupid girlish haircut and his annoying holier-than-thou attitude, I hope he dies."
        "Wait, dies."
        "I can't kill Jerry, but I think I just might have found a way out of this terrible situation."
        "I felt into my pocket and, sure enough, the gun was there."
        "Luckily, I always wear cargo shorts, which give me plenty of room to smuggle in a gun without any suspicion."
        "At that moment I knew what I must do."
        "It was time to test out my newly gift."
        "Before I could even think about the situation for a second longer I pulled the gun out of my pocket."
        s "Oh my God!"
        j "What the heck are you doing!"
        show darius angry at right
        da "No [name]! Stop!"
        "I opened my mouth, put the muzzle in my mouth so that it was facing my brain, and pulled the trigger."
        play sound "gun.mp3"
        "{i} BANG!!!!! {/i}"
        scene black
        with fade
        play music "black.mp3"
        "..."
        "......"
        "... Where... am I?"
        "...What... happened?"
        "How did I... How did I get here?"
        play sound "gun.mp3"
        "{i} BANG!!!!! {/i}"
        "That wretched sound burst back into my ear drums like I was hearing it all over again and all of my memories suddenly came back to me."
        scene classroom
        with fade
        play music "classroom.mp3"
        show striker
        s "[name], It's your turn. Come up to the front and choose your fate!"
        "..."
        "It... It worked."
        "I couldn't believe it."
        "I mean, I knew it would work, I pulled the trigger and everything, but still... it feels so surreal... Like I'm cheating."
        show striker angry
        s "Can you hurry it up already!!! We don't have all day!"
        "I looked around as everyone in the class started giggling."
        "It's all happening exactly as it did before."
        "I have travelled back in time!"
        "I got out of my seat with an extra spring in my step and skipped towards the front of the class."
        show striker happy
        s "Well well well, what's happened to you?"
        s "I don't think I've ever seen you looked this pumped up before!"
        s "You must be really excited to start this project!"
        "I just grinned at her and picked up a sheet of paper."
        "I can now game the system. Even if this paper does end up putting me in the same group as Jerry, I can just go back again! There aren't even any consequences!"
        "I looked down at the sheet of paper and saw that it was blank."
        "How's that old saying go? Fool me once, shame on you, fool me twice, shame on me."
        "Can't embarrass me this time you stupid slip of paper!"
        "I flipped the paper over and read the number sitting on the other side."
        "3. The paper said 3. Wait, I remember that name from earlier..."
        show darius happy at right
        da "Group 3! You got group 3! You're with me and Winrey!"
        show winrey school at left
        w "That's awesome! I know the three of us will get along greatly!"
        s "Ok you two... Settle down."
        s "Ok [name], you somehow lucked out and ended up with your best friend."
        s "I can't lie, I was hoping you would end up in another group, but this should work out just fine."
        "I couldn't believe my luck! Well, actually I could. I did game the system after all."
        "With this power, I don't ever have to worry about anything again! I can use this to go back and fix any problem that might arise!"
        s "Sit down [name] so that we can finish up selecting the groups."
        hide darius happy
        hide winrey
        "I sat back down in my seat and grinned to myself."
        "The last few people went and chose their groups, and I realized something. Our group only had 3 people!"
        "All the other had 4, but we were short a person."
        s "So it looks like the group of 3 ended up being Winrey, Darius, and [name]!"
        s "That works out quite well. The three of you are pretty smart so I can't see any problems arising."
        "She said the three of us were pretty smart but I knew she just meant Darius and Winrey."
        "Still, she was right though. With those two, we won't even notice how we are one person short."
        s "Alright, that should be enough for today. Remember that tomorrow I will let you all know what you will be doing for these projects."
        s "Have a good rest of the day!"
        "I got up to leave when a certain someone approached me."
        hide striker
        show winrey school
        w "Hey [name]!"
        w "I am looking foward to working with you and Darius on this project."
        w "I'm already pretty busy with all of my other activities, but don't you worry! I am making this my number one priority! I won't let you guys down!"
        "I already knew that there was no possible way for her to let us down. She is perfect after all."
        w "Ok, well I gotta go to soccer practice, see you guys tomorrow!"
        hide winrey
        "I got up once again to leave and another person came up to me."
        show darius happy
        da "What's up dude?"
        da "Isn't it great how we ended up in the same group!"
        da "I wonder what Mrs. Striker is gonna make us do for the project."
        da "Maybe we will make a volcano or something. What do you think?"
        menu:
            "A volcano sounds likely.":
                jump volcano

            "Do we live in a sterotypical highschool comedy?":
                jump rude

        label volcano:
                da "Yeah a volcano does sound like it could be what we end up doing."
                da "I mean, I've seen it done is so many movies but I've never actually done it. Sounds like it could be fun!"
                jump choice11_done

        label rude:
                show darius angry
                da "Alright man no need to be a dick about it."
                da "Since your so wise and smart, what do you think we will do?"
                jump question

        label question:
                menu:
                        "I... I dunno":
                            jump dunno

                        "Probably something stupid":
                            jump negative

                label dunno:
                            da "Yeah that's what I thought."
                            da "You are always the first guy to try and prove people wrong but you never have any ideas of your own."
                            da "I mean, I'm your best friend so I'm telling you this out of a place of love, but you have a serious attitude problem."
                            da "You need to work on that."
                            "I have been told that plenty of times already but that didn't make his words hurt any less."
                            "He is completely right. I do have an attitude problem."
                            jump choice11_done

                label negative:
                            da "Hey you never know it could be really fun."
                            da "You can be so negative sometimes. You should work on being more positive."
                            "He was right. I do need to work on being more positive."
                            "Especially now that I have this power, I could do whatever I want, surely that's something to be excited about."
                            jump choice11_done
label choice11_done:
    show darius
    da "Well anyways, I need to get home and do some homework, I'll see you tomorrow [name]!"
    hide darius
    "Darius bolted out of the room and I was finally able to leave my seat."
    "I walked towards the door and then yet another person started talking to me."
    show jerry
    j "Hey loser, I just thought I should tell you how happy I am that we aren't in the same group."
    j "I mean, I'm not gonna lie to you. I was REAL nervous that we would end up having to work together."
    j "And then what would I have done? I would have had to carry around abunch of dead weight with me."
    j "So thanks for not screwing that up for me."
    "This guy really knows how to get under my skin."
    "I do have the power to go back in time and reverse any actions that I take."
    "Maybe I could use that to my advantage?"
    menu:
        "(Punch his stupid little face in)":
            jump punch

        "(Kick him in the balls)":
            jump kick

        "(Be a responsible person and walk away)":
            jump boring

    label punch:
        '"Hey Jerry, you want to see something funny?" I asked him'
        j "Sure."
        "I cupped my hand into a fist, and punched him square in the face."
        hide jerry
        "He hit the ground with a loud thud and was completely knocked out."
        "That's what you derserve you annoying little prick."
        "I pulled my gun out and did what needed to be done to go back."
        scene black
        with fade
        play music "black.mp3"
        "In all the past times that I went back, it took a little while for me to remember what was happening."
        "This time, however, I knew where I was immedietly."
        "I must be getting used to time travel, which is nice as I will probably be using it quite often in the future."
        "I guess this empty darkness is a sort of waiting room for me to stay in until time gets reset."
        scene classroom
        with fade
        play music "classroom.mp3"
        show jerry
        j "Hey loser, I just thought I should tell you how happy I am that we aren't in the same group."
        "I just smiled at him, knowing that I had already recieved my sweet revenge."
        '"Whatever you say buddy." I told him smuggly.'
        "Before he could get another word out, I simply left the room without saying anything else."
        jump choice12_done

    label kick:
        '"Hey Jerry, do you ever plan on having kids?" I asked him mischievously'
        j "What, why would you even want to know that?"
        j "Well to answer your stupid question, I do in fact plan on having kids at some point."
        j "Of course I would have to find a women who truly deserves to be with someone as wonderful as me."
        j "They would have to be beautiful, funny, smart, and many other things."
        j "We would have one boy and one girl and I would raise them to be smart enough to take over this entire world if they so desired."
        j "I would name the girl Penny, as that is the name of my Grandmother who was also a genius."
        j "I would teach her everything there is to know about running a business."
        j "Her goal in life would be to make a company that is big enough to take out the heavy hitters in every industry!"
        j "The boy would be named Jerry, obviously, as that is the only male name that is acceptable for someone of his caliber."
        j "I would teach him how to be a star athlete in every sport imaginable."
        j "He will be the first person to ever win the highest award in every sport."
        j "On top of that, he will also be a thespian. The greatest one of all time."
        j "He would win the Oscar for Best Actor every single year of his career."
        j "Later on, he will also become a famous director who will make beautiful Art House films."
        j "So yes, I will have kids, and they will be perfect."
        "I wasn't expecting such an in depth answer, but it didn't really matter."
        "I reached my right leg back, and kicked him as hard as I could in the old babymaker."
        hide jerry
        "He clenched his privates and got down on the floor."

        j "Owwwww!!! You're gonna pay for that you little prick!"
        "Before he could retaliate, I whipped my gun out and killed myself, only temporarily of course."
        scene black
        with fade
        play music "black.mp3"
        "In all the past times that I went back, it took a little while for me to remember what was happening."
        "This time, however, I knew where I was immedietly."
        "I must be getting used to time travel, which is nice as I will probably be using it quite often in the future."
        "I guess this empty darkness is a sort of waiting room for me to stay in until time gets reset."
        scene classroom
        with fade
        play music "classroom.mp3"
        show jerry
        j "Hey loser, I just thought I should tell you how happy I am that we aren't in the same group."
        "I just smiled at him, knowing that I had already recieved my sweet revenge."
        '"Whatever you say buddy." I told him smuggly.'
        "Before he could get another word out, I simply left the room without saying anything else."
        jump choice12_done

    label boring:
        "As much as I wanted to stand up to him and give him what he truly deserves, I knew I should be the better man and walk away."
        "Before he could say another single demeaning word to me, I simply bid him a good evening and left."
        jump choice12_done
label choice12_done:
    scene houses evening
    with fade
    play music "bedroom.mp3"
    "I headed home the regular way this time, as I wasn't in a hurry and didn't feel like pushing my luck and going through the park again."
    "I could have taken a bus to get home quicker, but I decided to walk, as I wasn't in a hurry and I could use the exercise."
    "After a while of walking I finally made it home."
    "I strolled up to my front door, inserted my keys into the lock, turned the doorknob, and walked into my living room where my mom was standing."
    scene living room
    with fade
    show mom happy
    m "Hey there [name]! Did you have a good day at school?"
    "I knodded my head because I did in fact have a good day."
    "I ended up in a group with my best friend and my crush after all! Everything went perfectly, after a little bit of time travel anyways..."
    m "That's great sweety!"
    show mom
    m "I'm so proud of you, after the accident... well... I know I wasn't always there for you for awhile."
    m "And for that I'm sorry. But you seem to be doing pretty great anyways. You have a great friend in Darius and I think he has helped you deal with this whole ordeal in a way I never could."
    m "Anyways, I thought that it might be a good idea if the two of us went out for dinner tonight. We never get to talk much because we are both so busy."
    "I honestly couldn't even remember the last time I ate out at a restaurant. It did sound like fun."
    "I told her that I would love to eat out with her."
    show mom happy
    m "Yayyy! This will be fun! We can go to that cafe we used to love!"
    "The cafe. It's been so long since I've been there. I'm pretty sure the last time I went was with my sister..."
    m "Let me get ready real quick and we can head out!"
    scene cafe
    with fade
    play music "cafe.mp3"

    "We made it to the cafe while the sun was still shining high in the sky."
    "My stomach was growling like a zombie by the time we got there."
    "This cafe is a little different than any other restaurant that I've ever been to."
    "Instead of ordering up at the counter or having a waiter take your order, you take a menu to your table and circle the meal that you want."
    "After that, you bring the circled menu up to the front counter, where an employee takes it and makes your order as soon as possible."
    "It's the perfect restaurant for introverts, there is barely any human interaction and you don't even have to talk to the employee up front if you don't want to."
    "That's the main reason I used to go to this place so much."
    "I did go here with my family a lot, but mainly I would come here by myself and study or read a book."
    "Anyways, we walked through the front door and sat at a table by a big open window."
    "There wasn't any other customers in the entire cafe which was actually pretty typical."
    "Ever since I was young and started coming here, the place barely ever had many customers."
    "At most there might be a couple of other customers sitting by themselves at the bar up front, but there was rarely ever anybody sitting at the actual tables."
    "This was another reason I loved it so much. It was a great place to get some peace and quiet."
    "I never understood how the place was able to keep it's doors open after so many years of so little business."
    "My only thought was that it might be owned by a rich person who just keeps it open as a hobby."
    "My family used to joke that it was owned by the Mafia, and that is was only used as a money laundering scheme."
    "As funny as that would be, I always doubted the validity of that claim, as nothing interesting ever happens in this town."
    "I then remembered how just a few short days ago I was murdered by a guy and ended up getting super powers from God."
    "Maybe this cafe is actually ran by the Mafia, stranger things have happened, especially in this town, and especially to me."
    "My mom went up to the front and grabbed a couple of menus to bring back to our table."
    show mom
    m "Here you go sweety!"
    "I took the menu without saying a word, trying my hardest to indicate that I didn't want her calling me that anymore."
    "I opened it up and browsed through all of the different options that were avaliable at the time."
    "I was the exact same menu that they had when I was here last time. No surprise there, for the entire time that I've been going here, I have never seen the menu change at all."
    "This place serves a variety of different foods, but it specializes in breakfast foods, like a lot of diners and cafes do."
    "The first page listed all of the different breakfast items they had to choose from."
    "Eggs, bacon, sausage, hame, hashbrowns, pancakes, waffles, etc."
    "The middle pages had lunch and dinner options."
    "All different kinds of hamburgers, from a basic hamburger with no toppings, to an ultra-heart-attack-triple-burger-deluxe-edition, which was over 6,000 calories and a surefire way to an early death."
    "They also housed a few different kinds of steaks, though they were admittedly pretty terrible."
    "I remember how my dad was always a huge snob when it came to steaks. He would only order the most expensive option at any restaurant and would always get it cooked medium-rare."
    "If he didn't like any part of it, he would send it back at once and ask for either a new one, or a full refund."
    "He sort of became infamous for this at a few restaurants around town and some would even refuse to serve him after awhile."
    "This cafe was one of those places. He constantly harassed the chef about the quality of his meat, to the point where they just told him to go away."
    "He eventually begged them to let him come back, and they agreed on the sole condition that he didn't order any more steak."
    "This whole fiasco always embarrassed my family to the point where it became a big fighting point between my father and us."
    '"If they can not cook a good steak, then I should get a full refund!" He would always say.'
    "I would always just shake my head and my mom would start arguing with him about how childish he was being."
    "This eventually led to my dad learning how to cook steaks himself, and he would always cook them at home for us for dinner sometimes."
    "If I'm being honest, those were always some of the best steaks I ever had."
    "Eventually, I even became a steak snob myself, which led to me not ordering steaks here, as like I said before, were pretty bad."
    "They were always really chewy and tasteless, and the wouldn't even let you choose how you wanted it cooked."
    "I'm pretty sure they were always cooked well-done, which is why they were so chewy in the first place."
    "They probably did this to avoid any health problems, as the chef probably didn't know how to safely and properly cook a rare steak."
    "I guess that gives more credibility to the theory that this place is run by the Mafia. If it was run by them, they probably wouldn't worry about hiring an actual chef."
    "They would probably just get some jailbird they knew who they could trust to keep their secret."
    "I realized pretty quickly how that probably wasn't the case, as the rest of the food here was actually pretty good, it was just the steaks that were the issue."
    "Anyways, after the steaks they listed some other options, like salads, tacos, and chicken."
    "On the last page was the dessert options, and this is where the good stuff was."
    "This little cafe has some of the best desserts I have ever had the pleasure of tasting in my entire life."
    "They had this chocolate cake that oozed out chocolate sauce and whipped cream. It was so tasty and mouth watering."
    "They also has a cheesecake that was as big as my head."
    "Finally, they had a ice cream sundae that had at least 15 different scoops of ice cream."
    "My family would sometimes order this, and it was big enough for us all to split and we barely even put a dent in it."
    m "What are you going to order [name]?"
    m "I think I'm going to go with the Southwestern Salad. I ate a big lunch so I'm trying to cut back a little bit for dinner."
    "I browsed through the menu and narrowed my choices down to three options: The Bacon Cheeseburger, The Spicy Chicken Sandwich, and The Famous Triple Dunked Chicken Wings."
    "Those wings were dunked in the sauce of your choice three times and fried each time in between dunks."
    "Which choice should I get?"
    menu:
        "The Bacon Cheeseburger":
            jump burger

        "The Spicy Chicken Sandwich":
            jump chicken

        "The Famous Triple Dunked Chicken Wings":
            jump wings

    label burger:
        "I decided to go with the cheeseburger, as I wasn't really feeling chicken all that much, and that is what the other two options were made of."
        "I circled the burger and handed the menu to my mom."
        m "Oohhh The Bacon Cheeseburger. That seems like a good choice!"
        "My mom took both of our menus up to the front and handed them to the employee with a smile on her face."
        "She then came back down to our table and handed me an empty cup."
        show mom happy
        m "Here you go! I'm only getting water but you can get whatever drink you want!"
        show mom
        "I went up to the soda machine and decided to get a good old cola."
        "I usually try to only drink water, as I am deathly scared of getting a kidney stone, but I figured that one little soda couldn't hurt me all that much."
        "I filled the cup of to the brim and realized that I screwed up a little."
        "I forgot how the fizzy part overlaps the actual drink that you put in by quite a lot, and that fizz overflowed from my cup onto my hand."
        "I'm such an idiot. Oh well, no big deal."
        "I grabbed a couple of napkins and dried my hands off, as welll as the counter which also got drenched."
        "After that, I grabbed a lid, straw, and a few more napkins for my mom and I and headed back to our table."

        m "So how's your school year going so far [name]?"
        "I thought back to how I sort of hated most of my year for the most part."
        "I had to constantly deal with Jerry tormenting me, as well as pop quizzes that I always failed."
        "I then thought about how I was lucky to end up in a class with my best friend Darius, as well as a girl who's as awsome as Winrey."
        "To top it all off, I even ended up with super powers that I could use to get rid of any mistakes that I made."
        "My hand still felt sticky, and I realized I could have gone back in time to stop myself from making a mess out of myself."
        "Oh well, it's already been over a minute since it happened, and it's not that big of a deal anyways."
        "No use killing yourself over spilled soda."
        "I ended up telling my mom that my year was going pretty good so far and she seemed pleased to hear it."
        show mom happy
        "Oh thank God! I've been so worried that you were having a bad time. It's a relief to hear that you are doing well."
        "Right when I was about to comment I head a gruff voice come from the other side of the restaurant."
        e "Orda numbah 14! Ya orda's ready!"
        m "Oh that's us! That was really quick!"
        "I told my mom that I would get the food and I got up and went to the front to pick up our food."
        "One Bacon Cheeseburger and one Salad, yep that's our order all right!"
        "I brought the food back to our table and digged in."
        "The burger was so big that I could barely fit it in my mouth, but I tried my harderst."
        "I squished it down so that it was edible, and chomped down on a big bight of food."
        "I had a quick flash back to the other day to where I choked on my lunch and ended up dying."
        "Sure, I lived, but that feeling was terrible, and I definitely don't want to feel it again, so I better slow down my eating and take small, manageable bights."
        "I continued like this until I ate the entire burger and all of my fries."
        "I was planning on ordering a dessert, but I was stuffed to the brim."
        "Maybe I can come here with Darius at some point and we can just order desserts."
        m "Did you enjoy it? My salad was pretty tasty!"
        "I agreed and I put my empty dish on top of my mothers and brought the empty plates over to the top of the trash can, where they had a little basket to put your plates in."
        jump choice13_done

    label chicken:
        "I decided to go with the Spicy Chicken Sandwich, as I thought it might be a little different and I've never had one from here."
        "I'm a big fan of spicy foods, so if this isn't spicy enough I will definitely be disappointed."
        "I remember back a couple of years ago my class took a field trip to Nashville."
        "I honestly don't remember the point of the field trip, or why we decided to go there in particular as it is very far from where our town is located, but I do remember the hot chicken."
        "Nashville is famous for there hot chicken, and I can totally see why."
        "The one I ate was very spicy, and had a great taste on top of that."
        "One of my biggest pet peeves is food that is spicy for the sake of being spicy, and doesn't have any flavor of it's own."
        "I've had my fair share of spicy food that tasted like candle wax due to them focusing entirely on the amount of scoville units the food has."
        "This chicken didn't have that problem, it was delicious and spicy, which is a rarer combo than I would like."
        "Darius was there on that trip as well, and I remember how he decided to get the same hot chicken as me."
        "I warned him about how that was a bad idea, as I was a seasoned veteran of spicy foods and he was a mere novice."
        "He said he would be fine and ate it despite my warning."
        "Sure enough, it was way too spicy for him."
        "He started shaking all over his body and tears came running down his face."
        "That is when he made the worst decision possible."
        "He wiped his tears from his eyes using his bare hands that were still covered in spices."
        "He immdietly knew he screwed up, as he bolted out of his chair and ran to the restroom."
        "He was in there for a good 20 minutes or so, and during that time everyone was laughing at his mistake, and the teachers started to worry."
        "Eventually he came out of the bathroom and his eyes were all red and he claimed that he couldn't see anything."
        "The teachers called his mom and she drove all the way to Tennessee to pick him up."
        "I decided to go with him since I didn't have any other friends there at the time."
        "As it turned out he actually did permanent damage to his eyes, as he had to get glasses to see as well as he used to."
        "I sometimes make fun of him for it but I can tell he doesn't really find the humor in it."
        "After reminiscing about that for a little bit, I realized that I still needed to circle my selection and hand the menu to my mom."
        "I did exactly that and my mom grabbed my menu from me before I could get hers to bring them up front."
        m "I can bring the menus up front, don't you worry about it!"
        m "A Spicy Chicken Sandwich huh? Can't say I'm surpirsed, you always have been a big fan of spicy food!"
        "My mom took both of our menus up to the front and handed them to the employee with a smile on her face."
        "She then came back down to our table and handed me an empty cup."
        show mom happy
        m "Here you go! I'm only getting water but you can get whatever drink you want!"
        show mom
        "I went up to the soda machine and decided to get a good old cola."
        "I usually try to only drink water, as I am deathly scared of getting a kidney stone, but I figured that one little soda couldn't hurt me all that much."
        "I filled the cup of to the brim and realized that I screwed up a little."
        "I forgot how the fizzy part overlaps the actual drink that you put in by quite a lot, and that fizz overflowed from my cup onto my hand."
        "I'm such an idiot. Oh well, no big deal."
        "I grabbed a couple of napkins and dried my hands off, as welll as the counter which also got drenched."
        "After that, I grabbed a lid, straw, and a few more napkins for my mom and I and headed back to our table."

        m "So how's your school year going so far [name]?"
        "I thought back to how I sort of hated most of my year for the most part."
        "I had to constantly deal with Jerry tormenting me, as well as pop quizzes that I always failed."
        "I then thought about how I was lucky to end up in a class with my best friend Darius, as well as a girl who's as awsome as Winrey."
        "To top it all off, I even ended up with super powers that I could use to get rid of any mistakes that I made."
        "My hand still felt sticky, and I realized I could have gone back in time to stop myself from making a mess out of myself."
        "Oh well, it's already been over a minute since it happened, and it's not that big of a deal anyways."
        "No use killing yourself over spilled soda."
        "I ended up telling my mom that my year was going pretty good so far and she seemed pleased to hear it."
        show mom happy
        "Oh thank God! I've been so worried that you were having a bad time. It's a relief to hear that you are doing well."
        "Right when I was about to comment I head a gruff voice come from the other side of the restaurant."
        e "Orda numbah 14! Ya orda's ready!"
        m "Oh that's us! That was really quick!"
        "I told my mom that I would get the food and I got up and went to the front to pick up our food."
        "One Spicy Chicken Sandwich and one Salad, yep that's our order all right!"
        "I brought the food back to our table and digged in."
        "I took a bite out if the sandwich and realized I had made the right call."
        "It had a definite kick to it, but its was actually tasty!"
        "The perfect spicy food! I gobbled the rest of it down as well as eat all of my fries."
        "I was planning on ordering a dessert, but I was stuffed to the brim."
        "Maybe I can come here with Darius at some point and we can just order desserts."
        m "Did you enjoy it? My salad was pretty tasty!"
        "I agreed and I put my empty dish on top of my mothers and brought the empty plates over to the top of the trash can, where they had a little basket to put your plates in."
        jump choice13_done

    label wings:
        "I decided to go with The Famous Triple Dunked Chicken Wings, as I thought it might be something different."
        "And to top it all off, chicken wings are my favorite food."
        "The problem with chicken wings is that they are really easy to screw up in my opinion."
        "There are some food, pizza for example, that are impossible to screw up."
        "Sure, there are definitely some pizzas that are better than others, but I've never had a bad pizza."
        "Everything, from the ones you can get in the frozen section of the supermarket, to the authentic Italian ones, are all tasty in my opinion."
        "Chicken wings aren't like that. I have had some terrible chicken wings in my life."
        "The problem is that always have something wrong about them."
        "Either theres too much breading, or too little breading, or the sauce isn't good, or theres too much sauce, or a thousand other possible problems."
        "I love chicken wings, but I don't think I have actually ever had the perfect chicken wing."
        "I circled the menu option for chicken wings and handed it to my mother, who went up to the front counter to hand them the menu."
        m "I see you got chicken wings huh? That's no surprise! They are your favorite after all!"
        "My mother handed me an empty cup."
        show mom happy
        m "Here you go! I'm only getting water but you can get whatever drink you want!"
        show mom
        "I went up to the soda machine and decided to get a good old cola."
        "I usually try to only drink water, as I am deathly scared of getting a kidney stone, but I figured that one little soda couldn't hurt me all that much."
        "I filled the cup of to the brim and realized that I screwed up a little."
        "I forgot how the fizzy part overlaps the actual drink that you put in by quite a lot, and that fizz overflowed from my cup onto my hand."
        "I'm such an idiot. Oh well, no big deal."
        "I grabbed a couple of napkins and dried my hands off, as welll as the counter which also got drenched."
        "After that, I grabbed a lid, straw, and a few more napkins for my mom and I and headed back to our table."
        "I decided it would be a pretty good idea to grab a load of extra napkins, as chicken wings are usually pretty messy."
        m "So how's your school year going so far [name]?"
        "I thought back to how I sort of hated most of my year for the most part."
        "I had to constantly deal with Jerry tormenting me, as well as pop quizzes that I always failed."
        "I then thought about how I was lucky to end up in a class with my best friend Darius, as well as a girl who's as awsome as Winrey."
        "To top it all off, I even ended up with super powers that I could use to get rid of any mistakes that I made."
        "My hand still felt sticky, and I realized I could have gone back in time to stop myself from making a mess out of myself."
        "Oh well, it's already been over a minute since it happened, and it's not that big of a deal anyways."
        "No use killing yourself over spilled soda."
        "I ended up telling my mom that my year was going pretty good so far and she seemed pleased to hear it."
        show mom happy
        "Oh thank God! I've been so worried that you were having a bad time. It's a relief to hear that you are doing well."
        "Right when I was about to comment I head a gruff voice come from the other side of the restaurant."
        e "Orda numbah 14! Ya orda's ready!"
        m "Oh that's us! That was really quick!"
        "I told my mom that I would get the food and I got up and went to the front to pick up our food."
        "One order of The Famous Triple Dunked Chicken Wings and one Salad, yep that's our order all right!"
        "I brought the food back to our table and digged in."
        "I was glad that I got extra napkins, as they were drenched in sauce, a little more than I would have liked them to be, but the looked pretty good anyways."
        "I picked the first one up, a drumstick, dipped it in the ranch, and took a bite."
        "It was glorious."
        "I know I said that there was too much sauce, but after taking a bite I realized that wasn't true."
        "The sauce was spicy, yet flavorful. It was a standard buffalo sauce but done much better than I have ever seen it done before."
        "The meat was tender and juicy, It was packed to the brim with flavor."
        "And the breading...Oh my God the breading..."
        "You could tell it was triple dunked, as it was crunchier than your average wing, but it was perfect."
        "After all these years I've finally found it! The perfect chicken wing!"
        "At that moment, I knew exactly what I must do."
        "I had to become a famous journalist and report on serious stories all over the world so that people would trust me."
        "After a long time and after I gained enough credibility, I would publish an article about this place. No, about this chicken wing."
        "I would preach the gospel of it to the world! I would shout it's good name from the rooftop!"
        "Everyone must know of this glorious creation!"
        "In the article, I would urge everyone to come here, so that it could stay open forever."
        "I would then buy the restaurant so that I could discover the secret of the wing."
        "I would open up a location in every city across the globe!"
        "Everyone will eat this chicken wings and fall in love with it!"
        "Yeah, that's what I'm gonna do."
        "I then took the next chicken wing, a flat, and took a bite out of it."
        "Most people probably prefer the drumstick over the flat, but real chicken wing aficionados know that the flat rains supreme!"
        "The meat is more tender, and once you know the secrets of the flat, it becomes easier to eat."
        "I took another bite of it, this time dipping it in ranch, and ate it."
        "As expected, the ranch completed the whole experience."
        "I could feel the ranch and the buffalo sauce doing a tango of love in between my taste buds!"
        "This is it! This is Nirvana! This is Heaven! This is Valhalla! This is perfection!"
        "There is a huge debate between ranch lovers and blue cheese lovers and I am a member of the former."
        "I understand those who prefer blue cheese, as it is definitely more flavorful, the problem is that I don't like the flavor."
        "It tastes too moldy to me, and that's why I prefer ranch."
        "I ate all the rest of the chicken wings, savouring ever moment, until they were sadly all gone."
        "I licked all of the sauce off my hands and wiped them off with the napkins I grabbed earlier."
        "They didn't come with fries, which was fine with me as the wings were plenty on their own."
        "I was planning on ordering a dessert, but I was stuffed to the brim."
        "Maybe I can come here with Darius at some point and we can just order desserts."
        m "Did you enjoy it? My salad was pretty tasty!"
        "I agreed and I put my empty dish on top of my mothers and brought the empty plates over to the top of the trash can, where they had a little basket to put your plates in."
        jump choice13_done

label choice13_done:
    show mom happy
    m "I'm glad we came here! That was a really good meal!"
    "I agreed completely, and knew that I would be returning."
    "We got up to leave and headed for the front door, when I bumped into a familiar face."
    show jerry angry at left
    j "Watch where you're going you patheti..."
    j "Oh, it's you."
    "I couldn't believe my bad luck."
    "Out of all the people in the city to decide to go to this empty diner at this exact time, why did it have to be him?"
    "I thought about going back in time, but I realized one minute wouldn't matter."
    "If we stayed at the table he would have still come in and he would have still seen me."
    "I didn't want my mom to know that I had someone who was giving me trouble, so I decided to try and act friendly."
    '"Hey Jerry, what are you doing here, {i}friend?{/i}"'
    "I tried my best to emphasize the word friend to let him know that I was begging for him to go along with it."
    "I don't know why I even bothered, Jerry is a prick, why would he stop being a prick just because I was with my mom?"
    show jerry at left
    j "..."
    j "Hey... buddy..."
    "To my surprise, it actually worked!"
    "I could tell he was seriously struggling, but for some reason he decided to go along with it."
    m "Oh is this one of your friends [name]?"
    j "Yes I am m'am. Me and [name] go way back."
    m "Oh how wonderful! You never told me about him [name]!"
    m "What's your name?"
    j "Jerrimier, but you can call me Jerry."
    m "Oh what a great name! and what pretty hair! Your such a pretty girl!"
    "I couldn't believe what I just hear."
    "Not only was Jerry's full name freaking Jerrimier, but my mom somehow managed to mistake him for a girl."
    "My mom was never the smartest, but this might be a new low for her."
    "Jerry might have long hair, but he has male features and a very deep voice, not to mention his name is Jerry."
    show jerry angry at left
    j "Actually miss, I'm a guy!"
    show mom
    m "Oh my! I'm so sorry! Please forgive me!"
    j "It's... it's fine... I guess."
    j "Well anyways, I'll see you at school [name]!"
    m "Yes I'm sure we will meet again! Goodbye!"
    "My mom walked through the front door and I tried my best to follow but Jerry grabbed my arm and whispered something into my ear."
    hide mom
    j "You are so dead! You better watch your tracks for now on loser!"
    "Crap... I knew it was bad when my mom called him a girl but this might actually be a new low for me."
    "Jerry gave me one last menacing glare and stormed on into the restaurant."
    hide jerry angry at left
    "I walked out of the restaurant at a snail's pace, feeling completely defeated. What could he possible be planning to do to me?"
    "Will he actually want to fight or something physical like that? Jerry has always been a dick but he's never gotten violent."
    "He has always been the one to play at psychological warfare. He will just call you names and torment you mentally, but I might have pushed him a little too far this time."
    "He was actually nice enough to play along with my mom like that, and then she had to call him a girl... Just great..."
    "I guess there's no point in worrying about that now, whatever happens, happens. I guess at worst I can reset time if he tries to hurt me too badly."
    show mom
    m "What were you two talking about back there?"
    '"Oh, nothing much, just about school and stuff." I lied to her with a fake smile on my face.'
    show mom happy
    m "I think it's just wonderful that you are making so many new friends!"
    m "I thought Darius was your only friend... Not that there was anything wrong with that. Having one real friend is better than having 10 fake ones."
    m "But your friend there, what was her...I mean his name again? Jerry? He seems like a good guy."
    "My mom couldn't be farther from the truth but I was just glad that she actually bought my lie."
    "At least some good came out of that whole interaction. Jerry might hate me even more now but at least my mom doesn't think I'm a total loser."
    m "Since you are actually making new friends... Is there any girls that your talking to?"
    m "Maybe you even have a girlfriend that you're hiding from me!"
    "I hated when my mom brought this type of stuff up. It's not like I don't want a girlfriend, I mean I would kill to go out with Winrey, It's just that no one like me in that way."
    "And who can really blame them? I wouldn't want to date me neither."
    "I just rolled my eyes at my mom and got in our car."
    show mom
    m "Why are you upset? Is it something I said? I was only joking about the girl thing, I know you're way too focused on school to worry about love!"
    "If I was focused on school then maybe my grades wouldn't be so horrendous. No, I just don't have a girlfriend because I'm a total loser."
    "My mom got in the front seat and she drove us both home."
    scene bedroom night
    with fade
    play music "bedroom-night.mp3"
    "It was later that night, a few hours after I got home from the restaurant, that I was laying in my bedroom by myself."
    "Tomorrow's the big day. The day we find out what we are going to be doing on that project."
    "I thought back to the conversation I had with my mom earlier today about a girlfriend."
    "Now that I'm in a group with Winrey I can actually talk with her and maybe we will become friends, and eventually... No. I shouldn't get my hopes up too much."
    "Nothing has ever worked for me in that way before, why would that change now? Plus Darius is in our group, and he is way more charismatic than I am. He is actually a borderline extrovert."
    "If anybody is getting with Winrey, it's him."
    "I looked over at my clock and realized how late it was."
    "I better get to sleep so I can wake up tomorrow with plenty of energy."
    "I got under the covers and slowly drifted to sleep."
    scene black
    with fade
    play music "black.mp3"
    m "Are you ready to leave [name]?"
    '"Just a second!" I yelled'
    "I put on my shirt and walked downstairs."
    em "I'll see you tomorrow big brother!"
    "I looked over at my sister and waved her goodbye."
    m "See you tomorrow Emilia! And you too Henry!"
    "My mom went over and gave my sister a hug. She then walked over to my dad and gave him a kiss on the cheek."
    m "Alright [name], Let's go!"
    "Me and my mom headed out the front door and closed it shut behind us."
    scene bedroom
    with fade
    play music "bedroom.mp3"
    "..."
    "That dream..."
    "...That...Moment"
    "I haven't thought about that time for so long now..."
    "I wish I could just forget it all."
    "I looked down and realized I had cold sweats running down my entire body."
    "Ugh, I feel so gross and tired."
    "Even though I went to bed at a reasonable time last night I still felt dead on the inside."
    "I blame that dream. Why now? Why was I remembering that now? I thought I was finally over it all and now the memories have to start returning?"
    "No, I can't think about that anymore. I need to live my life normally. I can't let the past ruin everything for me."
    "I got out of bed and headed towards the bathroom to get ready."
    scene kitchen
    with fade
    "It was about 30 minutes later that I was finished getting ready and headed down to the kitchen to eat some breakfast."
    show mom
    m "Good morning! Did you sleep well?"
    "I lied and told her that I did sleep well."
    m "That's good to hear. I slept pretty well too."
    m "I just want to tell you that I'm so glad that we went out yesterday!"
    m "That meal was so good and it was nice to get some quality time with you!"
    m "We should do it more often, it seems like we barely see each other anymore."
    m "Well anyways, I didn't have time to make an extravagant breakfast this morning, so you can just grab some cereal."
    "That was fine, after the gigantic feast yesterday I was barely in the mood for another huge meal."
    "I went to the cabinet and grabbed a box of generic cereal."
    "My mom always bought the store brand version of everything as it was a little cheaper."
    "I didn't really mind all that much, as they tasted pretty much the same."
    "I've heard that with medicine, the name brand stuff is exactly the same as the store brand one."
    "They would be made at the same factory and everything. The only difference was the labels they put on it and the price they charged."
    "People would be willing to pay way more for the same exact product, just because it had a recognizable label attached to it."
    "I imagine that cereal is the same. They were all made in the same place but just given different names and prices."
    "I poured me a bowl of Deerios and poured milk in afterwards."
    "I heard that some people poured milk in first and would then add cereal after the fact, but those people should be locked up in prison."
    "Same as with people who stand up to wipe, some things should just be done in a certain way."
    "I turned on the tv and started eating my breakfast."
    tv "A local millionare has donated 50,000 dollars to a homeless shelter. He stated that everyone deserves a place to stay, and that it was his duty to provide that service if the government wouldn't."
    tv "Scientists have discovered a new species of fish located deep down in the Atlantic Ocean."
    tv "The person who discovered it was a young man who had decided to name the species Gorongosomo."
    tv "When asked why he decided to go with that name the man just said that he thought it sounded funny."
    tv "A women in Nigeria was found dead this morning, and the condition that she was found in has perplexed local officials."
    tv "Evidently, she was found with her facial features completely missing."
    tv "Police claim that she wasn't beaten or had any body parts removed, they were simply gone."
    tv "The place where her eyes and mouth should have been were completely blank, as if she never had any eyes before."
    tv "The Nigerian Government states that they are looking into this matter, and hope to solve the case quickly."
    show mom angry
    m "That's so strange... I wonder if there is some weird disease that did that to her."
    "I agreed that that was probably the case and finished up my bowl of cereal and cleaned my dishes."
    "That was certainly a weird story, but this is a weird world."
    "Unexplainable things like that happen every day, no use thinking about it too much."
    "I said goodbye to my mother and headed out to school."
    scene classroom
    with fade
    play music "classroom.mp3"
    show striker happy
    s "Ok class, you all know what we have planned for today."
    "I looked around to everyone in the class to see how they were all feeling."
    "I looked over to Darius, who was nervously tapping his naked feet on the ground."
    "Winrey looked perfectly happy. She had a huge smile on her face and I could tell she was just excited to see what we would be doing for the rest of the semester."
    "I then passed my gaze over to Jerry and my heart completely stopped in it's tracks."
    show jerry angry at left
    "He was staring straight into my soul, with a huge scowl on his face. When he noticed that I caught him staring at me he just scowled even harder."
    "He then put his right index finger against the edge of the left of his throat, and slowly dragged it across, probably indicating that he was planning on murdering me."
    "I guess he really is upset at me for yesterday. Luckily, if he is actually planning on killing me, it wouldn't be a big deal, because, ya'know, my gift."
    hide jerry angry at left
    "I then turned back around, trying my best to ignore Jerry, and listened to what Mrs. Striker had to say."
    s "Well, enough with all the mysteries and suspense, it's time to finally reveal what the project is."
    s "You are all going to put on individual plays!"
    "My heart dropped and shrank at least three sizes."
    "I have severe anxiety when it comes to public speaking, and a play is basically public speaking on steroids."
    show darius angry at right
    da "A play?!?!"
    da "Seriously? What does a play have anything to do with this class? I know that you're our only teacher, and you teach us all types of subjects, from math, to science, to writing, but what does a play have to do with anything?"
    show striker angry
    s "A play has everything to do with all of those things Darius."
    da "HOW!?!?"
    s "If you would have let me finish instead of rudely interrupting then I would have been able to tell you!"
    show darius at right
    da "...You're right... I'm sorry."
    s "You should be!"
    hide darius at right
    s "Anyways, to answer your question, I have noticed how nervous you all are to answer questions or do anything that involves public speaking."
    s "This simply will not do. Once you get out into the real world, you will have to speak in front of people constantly."
    s "And while it is important for me to teach you about math and science, a lot of those topics won't really be all that useful in the real world."
    s "Now that you all have smart phones, you can do basic math with that. You can look up any science fact you can think of on the internet."
    s "You know what you're phones can't help you with? Human interactions. That is why I have decided to make this my number one priority as a teacher."
    s "I would be doing you all a huge disservice if I threw you out into the real world with no speaking skills."
    s "You would fail at life horribly. How do you expect to impress at a job interview if you can't even get your words across clearly?"
    s "What if you want to apply for a loan? You think they give you money if you can't communicate effectively?"
    s "That's why we are going to put on a play. To help you all get out of your shells and be who you need to be to do well in this world."
    s "And if you are wondering why I have decided to make you all put on a play, instead of something more traditional like a speech, well, I just thought it would be more fun."
    s "Do you want to spend months researching a topic that you have no interest in, and creating a powerpoint to give a monotone speech, or would you rather flex your creative muscles by writing and performing a moving and emotional story."
    "I could tell from looking around that the opinions were mixed, and I can understand why."
    "On one hand, she's totally right. I'm not prepared for the real world."
    "I get anxiety from ordering a meal at a fast food restaurant."
    "And it would be kind of fun to write a story."
    "The problem is that this sounds like way more work."
    "A speech would take our group a few hours to make and prepare for, but a play could take months."
    "You have to spend a lot of time writing, and re-writing, and re-re-writing the story just to get it right."
    "You also have to memorize it all, and make sure that you are giving an emotional performance, which is definitely not my strong suit."
    "I'm pretty bad at showing my emotions to other people. I would much rather just keep it all to myself."
    "Overall, I'm not sure how I feel about this project, but it will surely be interesting at the very least..."
    show winrey school at right
    w "Mrs. Striker? I have a question."
    show striker happy
    s "What is it Winrey?"
    w "What are the details and requirements of the play?"
    w "Like, I'm totally down, but is there a certain topic we have to do the play over?"
    s "Nope! You can do the play over whatever strikes your fancy!"
    s "the only requirement is that every person in you group has to have a speaking role, and the play has to be in between 5 and 10 minutes in length."
    s "Everything else is completely up to you!"
    s "And I do expect you all to get very creative with this. No laziness will be tolerated."
    w "Ok, that sounds great! Thanks!"
    hide winrey school at right
    s "Ok, does everybody understand the requirements."
    "No one said a word."
    s "Great! These will be due during the last week of the semester!"
    "That gives us plenty of time to think of an idea."
    s "That's all the time we have for today! I hope you all have a great weekend and I'll see everyone here on Monday!"
    hide striker
    "I guess I should speak with Darius and Winrey so that we can come up with a plan."
    "Before I could even leave my desk both of them approached mine rather quickly."
    show darius
    show winrey school at left
    da "Hey [name], me and Winrey thought that it might be a good idea if we could meet up at some point tomorrow and make some initial plans for the play."
    w "Yeah, what would be a good time for you?"
    "I knew that I was completely free all day tomorrow, so I just told them whenever works for them is good for me."
    da "Ok, I'm free all day so I guess it's up to Winrey's schedule."
    w "I have soccer practice in the morning so that won't work. How about we meet up after lunch?"
    w "That way we all have time to get ready and eat seperately, and then we can come together to really work hard on this thing."
    da "That works fine for me."
    da "But where should we meet."
    w "Doesn't matter to me. Where do you think we should meet, [name]?"
    "I thought about it long and hard. My initial thoughts was the diner, but Winrey made it clear that she wanted us all to eat alone and then meet up after lunch so I guess that idea is out."
    "The only places that leaves us is our three houses."
    "Which one should I choose though?"
    "We could go to my house, but my mom might be home and if she sees Winrey and me together, I know I'll never hear the end of it."
    "I can just imagine what she would say..."
    m "Oh [name], YOu DiDN't TElL mE YOu HaD a giRlFRieNd. WhEN's THE weDdINg?"
    "That would be awkward and annoying. Maybe we should go to one of their houses."
    "I have been frineds with Darius for a few years now, but i've never actually been to his house before, it could be cool to see where he lives."
    "On second thought though, he never wears any shoes so he might be poor..."
    "It would be bad if I suggested his house and he had to make some excuse to not embarrass himself in front of us."
    "He always says he can't wear shoes because of a medical condition, but I'm pretty sure he's lying about that."
    "Whenever I even try and mention shoes he gets all squirmy and weird, like I just asked him some forbidden question."
    "What about Winreys house? I would really like to see where she live and maybe even meet her family."
    "If I can make a good first impression with her family then I might be able to get closer to her... and then..."
    "No I shouldn't get my hopes up."
    "Plus it might be rude of me to invite ourselves over to her place."
    "I barely even know her, how can I suggest that we meet up at her house?"
    "Well, it's time for me to choose."
    menu:
        "Let's meet at my house":
            jump choice14_me

        "Let's meet at Darius's house":
            jump choice14_Darius

        "Let's meet and Winrey's house":
            jump choice14_Winrey

    label choice14_me:
        "I decided that it would be best if we just met at my house."
        "Sure, it would be annoying for my mom to constantly bug me about my nonexistent girlfriend, but maybe she will be mature about it."
        "Plus, it could be cool for Winrey to meet my mom so that my mom knows that I have friends that are girls."
        "Also, I felt weird about suggesting that we meet up at one of their places. That seemed a little rude to me."
        w "Ok! That works perfectly for me! Can I have your address?"
        "I gave them both my address and told them to come around 2pm."
        "That would give me plenty of time to get ready and eat lunch. Maybe I can even have some snack prepared."
        da "Well I guess I'll see you two tomorrow then."
        w "Yep, see ya!"
        hide winrey school
        hide darius
        "The both of them left and headed of in seperate directions and I got out of my seat and made my way home."
        scene living room
        with fade
        play music "bedroom.mp3"
        "I got home pretty quickly and decided to watch some tv before I went to bed."
        "To my surprise, my mom was already in the living room watching some old black and white film."
        show mom
        m "Hey [name], how was school."
        "I told her it was good and explained how I had a couple of friends coming over tomorrow to work on a project."
        m "That works for me! I'll be home all day tomorrow so I'll try my best to stay out of your way."
        m "Do you want me to make any snacks or something?"
        "I told her that I didn't need her to make any snacks."
        m "Ok."
        "My mom actually does make pretty good snacks, but I don't want to force her to work on her day off and make me and my friends snacks."
        "I can just grab a bag of chips out of the pantry."
        "I asked my mom what movie she was watching as I didn't recognize it."
        m "Oh it's an old film from the 1930's. It's called 'The First Dog'"
        m "It's a touching story about a man who went out of his way to tame and befriend a wolf."
        m "He eventually domesticates it and they become best pals."
        "I thought that sounded really lame so I just went up to my room."
        scene bedroom
        with fade
        "It was the next day and my friends were due to arrive at any minute now."
        "I barely got any sleep last night, as I was so nervous about them coming over."
        "I also was afraid of having another nightmare like the one I had the previous night..."
        "I can't think about that now, I have to get in the right mindset."
        "My mom shouldn't be a problem, as she seemed pretty chill about people coming over yesterday."
        "I didn't mention to her that one of those people would be a cute girl, but hopefully she's able to keep a level head during the whole scenario."
        "I had already thought about exactly how I'll havr today go."
        "When they ring the doorbell, I will run downstairs and open the door to greet them."
        "I will give a very brief introduction to my mom, and then we will swiftly head upstairs and do everything else in my room."
        "I'll ask them if they want any snacks, and if they say yes then I will go back downstairs by myself to get them."
        "After that, we can just do whatever we need to do for the project."
        "Once it's all said and done, I will escort them to the door, have us each say our brief goodbyes, and send them on their merry ways."
        "Yes, this should go perfectly."
        play sound "doorbell.wav"
        "{i}Ding Dong!{/i}"
        "Oh crap! That's the doorbell."
        "I ran to my bedroom door but before I could open it, I looked down and realized I didn't have any pants on."
        "Crap! Crap! MEGACRAP!"
        "I ran to my dresser, picked up the first clean pair of pants I could grab, put them on, and ran downstairs to open the door and greet my friends."
        scene living room
        with fade
        "To my utter dismay however, my mom already beat me to it."
        show mom happy
        show winrey casual at left
        show darius happy at right
        m "Welcome! I'm [name]'s mom!"
        m "Please, come on in and make yourself comfortable!"
        "Ok, this is fine, my mom seems to be acting normal."
        w "Thank you so much!"
        da "It's nice to see you again Ms.!"
        m "Oh please Darius, you can just call me mom."
        da "Haha, no thanks that would be pretty weird."
        da "I'll just call you Ms."
        m "Whatever floats your boat, Darius."
        w "I would like to thank you for allowing us to intrude and work on our project."
        "Winrey is as nice and polite as ever."
        "I decided it was time to walk up and greet my guests."
        da "Oh there you are [name]. I was beginning to think that you were still asleep."
        w "Wow! Do you normally sleep that late?"
        menu:
            "Nope, never.":
                jump early

            "Sometimes...":
                jump sometimes

        label early:
            w "Me neither! I have always been an early bird!"
            show darius at right
            da "You liar! You were just telling me last week about how you love to sleep in late."
            "I told him that while I do like to sleep in, I would never sleep in this late."
            da "Oh ok, my bad."
            jump choice14_me2
        label sometimes:
            w "Oh that's cool."
            w "Personally I have always been an early bird, but theres nothing wrong with wanting to sleep in either."
            "As always, Winrey was completely cool and accepting of other people."
            jump choice14_me2

    label choice14_me2:
        m "So, I guess you three are going to want to get to work right?"
        w "Yes, where would be the best place for us to work so that we won't get in your way?"
        m "Anywhere is fine with me!"
        "I told them that we could go to my room and they agreed."
        m "You three behave yourselves now, no funny business!"
        "I know she was joking but I could tell that Winrey wasn't so sure."
        da "We'll try our best!"
        "And with that, the three of us headed upstairs."
        scene bedroom
        with fade
        show winrey casual
        show darius at right
        "We got into my room and Darius immedietly hopped onto my bed."
        show darius happy
        da "Man, it feels like I haven't been here in forever!"
        show darius at right
        "It was true, Darius hasn't been to my house in a long time."
        w "Where should I sit?"
        "I grabbed my chair that I kept at my desk and told her that she could sit on that."
        "It might not look like much, but that chair is the most comfortable seat in the house."
        "Winrey sat down in it and I could tell that she was pleasantly surprised by the comfort level of the chair."
        w "Wow! this things really comfy!"
        da "Dang [name], why didn't you offer me the best chair in the house?"
        "He was joking, but Winrey must have not caught on to that fact."
        w "Oh, you can have it Darius, I can just stand."
        da "Oh no no no! I was only kidding, the bed's perfectly fine for me!"
        w "Are you sure?"
        da "Yes, I'm completely sure."
        w "Ok then..."
        "Things were already getting a little awkward, so I decided to cut to the chase and ask them for ideas about what we could do for the play."
        "I personally had no interest about the topic, so I had already decided that I was going to let them choose what we should perform."
        w "I was thinking that we could put on Romeo and Juliet! I know it's a little cliche, but it's always a real crowdpleaser and I've always wanted to be Juliet."
        da "That sounds super lame. I mean, I bet everyones gonna do Romeo and Juliet, we should do something that no one could predict."
        show winrey angry casual
        w "Ok then, what's your great idea Darius?"
        da "I'm glad you asked."
        da "I was thinking we put on a play about BroBro's Crazy Journey."
        w "What the heck is that?"
        show darius angry at right
        da "Wait, are you serious? You mean to tell me that you have never heard about BroBro's Crazy Journey!?!?!"
        w "No, I haven't. Please enlighten me."
        show darius at right
        da "Well, BroBro's Crazy Journey, or just BroBro for short, is only the best tv show of all time!"
        da "It started off as a comic book that came out in the late 80's. [name] has actually read the entire thing."
        "Winrey looked over to me with a unidentifiable look on her face and I just shrugged with a nervous smile."
        da "The comic is actually still being released to this very day, but that's not the important part."
        da "The thing that really matters is the tv show."
        da "See, in 2009, a really rich guy who was a fan of the comic decided to purchase the rights for a television adaptation of the entire thing!"
        da "It's really great as well. [name] says that it does deviate from the source material occasionally, but it's pretty freaking awsome nonetheless!"
        w "Ok... That's fine and all, but how are we going to turn that into a play? What's the story like?"
        da "Well, BroBro isn't set up like your traditional show."
        da "Most shows follow one set of characters and tell abunch of different stories using those characters."
        da "BroBro works more as an anthology, with each chapter having a different main character and a completely different story."
        da "For example, the first part follows Brother Broseph, a priest with the power to detect vampires."
        da "One day, a little boy comes up to Brother Broseph, or BroBro for short, and tells him that his dad's a vampire and the kid asks BroBro to kill his dad for him, as he has hurt many innocent people."
        da "BroBro agrees to help, and the rest of the story follows his on a dark and serious tale full of horror and violence."
        da "The next chapter follows Broke Broseph, Brother Broseph's son. Unlike Brother Broseph, Broke Broseph is just a simple bartended working in Chicago."
        da "One day, Broke Broseph, or BroBro, finds himself in the middle of a gang war. He has to choose a side and fight for the good of the people!"
        da "This chapter is way more comical than the last, and every chapter after that follows suit."
        da "Eventually they all get super powers and it just gets crazier and crazier with each episode."
        w "So how are we supposed to put on a play with crazy stuff like superpowers? We don't have the time or budget for that."
        da "I've already thought of that! We can just do the first chapter, as it is pretty simple and stright foward."
        da "Theres no super powers or anything crazy like that! The entire story only has 4 characters as well!"
        da "Theres BroBro of course, as well as the little kid and his dad, who is the main antagonist."
        w "And who's the fourth character?"
        da "BroBro's girlfriend, Lolo!"
        w "..."
        show winrey casual
        w "I hate to admit it, but that does sound a lot more interesting than Romeo and Juliet."
        show darius happy at right
        da "Yay! I knew you would come around to the idea once I explained it more!"
        da "Well, since we are all in agreement, we can get to work on righting the first draft."
        da "We are going to have to cut out quite a lot to fit all of the material into a short play, but the story is so simple that it shouldn't be all that difficult."
        da "Before we go any further, I'm gonna run to the bathroom real quick, be right back."
        "Darius got off of my bed and sprinted towards the door."
        hide darius happy at right
        w "So [name], you're a big fan of this BroBro thing, right?"
        "I told her that I was, and that she won't regret us performing it."
        w "I'm sure it will all work out."
        "We sat around in an uncomfortable silence for a couple of minutes."
        w "Hey, can I ask you a question about Darius?"
        "About Darius? What could she possible want to know about him?"
        "Wait, maybe she has a crush on him, and she wants my advice about what the best way to ask him out would be!"
        w "Well, this is kind of awkward... but... why doesn't Darius ever wear any shoes?"
        "Thank God that was the only thing she wanted to know."
        "The only problem is I don't know what the right thing to tell her is."
        "I do know exactly why Darius doesn't wear any shoes but I'm not sure if I should be the one to tell her"
        "Wouldn't it make more sense for Darius to be the one to tell her instead of me? I get why she's asking me, it's definitely a sensitive topic."
        "I know that the reason is that Darius just has an irrational fear of shoes. I don't know exactly why, I just know he's never worn any before."
        "That goes for socks as well, he can't have anything touching his feet."
        "It is pretty strange, but I have always thought it was a pretty harmless fear to have, so I've never bothered with trying to help him get over his phobia."
        "But what do I tell Winrey?"
        "Since I don't have the details, I can just tell him he doesn't like shoes and leave it at that."
        "But would I be a bad friend to Darius if I go into details about it without his explicit permission?"
        "I could just tell her that it's not my place to discuss such matters, as it should really be Darius who tells her about that."
        "Also, I wouldn't mind hearing about why he has his fear. Maybe if we both confront him about it he will spill the beans."
        "It might be pretty rude to drop all of that on him though, what if he doesn't want to talk about it?"
        "What if the reason is super embarrassing or tragic?"
        "What should I tell her?"
        menu:
            "He's just scared of shoes for some reason":
                jump shoes

            "I think you should just as Darius":
                jump AskDarius

        label shoes:
            "I decided it would be best if I just told her everything I knew, which wasn't much."
            "I can't imagine Darius would mind all that much if I told her, I mean it's no secret that he never wears any shoes."
            "He had to get special permission from the principal to make sure it was ok and everything."
            "The entire class knows that something's up, we just don't know the details."
            show winrey angry casual
            w "Oh."
            w "So you don't know the exact reason? He's just scared of shoes and no one knows why?"
            "I told her that I didn't know any of the details, just that he was scared of them for some reason"
            w "That's such a strange quirk to have."
            w "And pretty dangerous I should add."
            w "I mean, what's he supposed to do in the winter?"
            w "Aren't his feet completely frozen? Wouldn't he get hypothermia or something?"
            "She had a good point, it would be pretty dangerous, but ever since I've known him, no such problems have arrived."
            w "Well, I think I'm gonna ask him about it."
            show winrey wink casual
            w "Oooohhh, hey [name], I've got a great idea."
            w "We should get him to confess about his little issue."
            w "If we find out the underlying reason for his fear, then I bet we can cure it!"
            w "We can treat him like a doctor would treat a patient! I just know that the two of us can fix him."
            "I wasn't all too sure about this."
            "I mean, it's nice of her to want to help Darius out and all that, but is it really our problem to try and fix?"
            "Shouldn't he go see a doctor about it or something?"
            "I'm afraid that the two of us might only make it worse. We are by no means professionals when it comes to mental illness."
            "Before I could tell her about my concerns, Darius strolled back into my room."
            jump choice14_me3
        label AskDarius:
            "I decided to tell Winrey to just ask Darius about it."
            "I think that it would make me a bad friend if I was to talk about his problems behind his back."
            "Besides, it's really not my place to tell her anything about him anyways. Darius should be the one to do that."
            w "Ok, I understand."
            w "I guess I should just ask him directly instead of trying to get information about him behind his back."
            w "I'll ask him when he comes back into the room."
            "Wait, what? She's really going to just straight up ask him about something so personal as soon as he comes back in here?"
            "I mean, she barely even knows the guy. This is the first time that the three of us have even hung out."
            "Shouldn't she wait until she gets to know him a little better before she asks him something so personal?"
            "Before I could tell her how bad of an idea that was, Darius came back from the bathroom and strolled on in."
            jump choice14_me3
    label choice14_me3:
            show darius at right
            show winrey casual
            da "What's up guys? You two seem like you were talking about something."
            w "Oh, me and [name] were just talking, and we were wondering if you could fill us in on something."
            da "Sure! What is it?"
            w "Well, why don't you ever wear any shoes?"
            show darius angry at right
            da "Wha... What!?"
            da "Why don't I... Why don't I... Why don't I ever wear any shoes?"
            da "Well uhhhh.... you see... uhhhhh....."
            show darius happy at right
            da "Hahahahahaaaaaaaa...."
            show darius at right
            da "Ummmmm...."
            show darius angry at right
            "It's a serious medical conditional alright!"
            "I can't wear shoes or else I'll die or something!"
            show winrey angry casual
            w "Or something?"
            da "Yeah! Or something!"
            da "I don't know! Just shut up ok!"
            da "You don't think I know how weird I must look?"
            da "Going to school without any shoes like some homeless person?"
            "That particular line seemed to strike some kind of cord with Winrey."
            w "What's that supposed to mean! What do you have against homeless people?"
            da "What?"
            da "I don't have anything against them, I was just giving an example!"
            da "Anyways, it's neither of your guys' problem anyways, so don't worry about it ok?"
            w "Ok, I'm sorry for asking, I just wanted to help you."
            da "Help me? Like I'm some weak pathetic little dog who can't fend for himself?"
            da "I don't need help! Theres nothing wrong with me ok!"
            da "I just choose not to wear shoes because I think their dumb."
            da "oH lOoK aT ME, I'M weAriNG SHoEs! Hurdy dur de dur."
            "Darius said that last line in a way that made it sound like he was mocking people for wearing shoes."
            da "People act like I'm the crazy one, were you born wearing shoes? No, because it's unnatural."
            w "You weren't born wearing clothes either but you're rocking that shirt and pants combo as we speak."
            da "Th...That's different ok! Anyways, we made enough progress on the project for today, so I'm going home."
            w "Ok, that's fine with me!"
            w "I'll see you to in class tomorrow!"
            da "Yeah, see you two later! I hope you both have a great day!"
            w "Yeah, have a great day!"
            hide winrey angry casual
            hide darius angry at right
            "Well, that could have gone better."
            "If I would have thought of it sooner, I could have gone back to prevent that conversation from ever going down, but it's been way longer than a minute, so I guess I just have to live with it."
            "It's ok, I'm sure the two of them will cool down soon. Luckily it seems like they are just mad at each other, instead of me, so I should be good."
            play sound "knock.wav"
            "{i} Knock knock knock. {/i}"
            "Someone was knocking on my door."
            "Could it be Darius and Winrey coming back to apologize?"
            '"Come in!" I yelled.'
            show mom
            m "Did everything go alright in here?"
            m "I thought I heard some yelling, and then the two of them left the house before I could do anything."
            '"Yeah, everything is fine. We were rehearsing for the project and they both remembered that they had to leave." I told her dishonestly.'
            "I didn't like lying to my mom, but I didn't fell like explaining what just happened."
            m "Oh ok, that's good to hear. I was worried there was some kind of argument."
            "I'll leave you alone then."
            jump choice14_done

    label choice14_Darius:
        "I decided that we should all meet at Darius's house."
        "It might be rude of me to invite us over, but they did give me the final say in the matter."
        "Plus I really didn't want to deal with my mom."
        "And this way I can finally see where Darius lives."
        da "Ok, that works for me! My house it is!"
        w "I'll see you guys there!"
        da "My address is 2586 LaneWood Avenue. Come around 2pm on Sunday."
        w "Will do!"
        "The three of us said our goodbyes and promised that we would meet on Sunday at 2pm at Darius's house."
        scene mansion day1
        with fade
        play music "bedroom.mp3"
        "It was Sunday, and I got to Darius's house at around 1:50 PM."
        "I like to be a little early to things whenever possible, as I hate being late."
        "I walked up to a gigantic mansion and realized that I must have made a mistake."
        "This must be the wrong address, how did I screw up so badly that I didn't even go to the right neighborhood?"
        w "Wow! This place is huge!"
        "I turned around and saw that Winrey also arrived early."
        show winrey casual
        w "I had no idea that Darius was so rich, did you?"
        "Wait, so I didn't go to the wrong house? Darius actually lived here?"
        show darius at right
        da "Hey guys, did you make it here ok?"
        w "Darius, I didn't realize your house was so big! If anything, I thought you were poor."
        show darius angry at right
        da "And why would you think that?"
        w "Uhhh... No reason, I was just kidding."
        da "Oh ok. Well, you guys wanna come on in?"
        show darius happy at right
        da "My parents aren't due to be home for a few more days so we have the whole place to ourselves!"
        w "Where did they go?"
        da "They both went on a business trip to Egypt."
        "I had no idea that Darius was so rich, or that his parents were so successfull."
        "I was like Winrey, I thought he was poor, due to the fact that he never were any shoes."
        "I guess that just proves why you should never judge a book by it's cover."
        "But that just makes me wonder even more about why he never wears any shoes..."
        da "Ok, come on in! I'll give you guys the full tour!"
        "Darius led us inside and showed us around his entire house."
        "He had a room for anything you could think of."
        "A workout room, a swimming pool, a movie theater, bowling alley, huge kitchen, the man had it all."
        "Finally he led us to his room."
        scene droom afternoon
        with fade
        show winrey casual
        show darius at right
        da "So, this is my bedroom."
        "Compared to the rest of the house, it was pretty normal. It was only slightly bigger than my own room."
        da "I requested the smallest room in the house, as I kind of hate big, open spaces."
        w "It's perfect! Even though I must admit that I'm a little surprised that you have a pink bed."
        show darius angry at right
        da "Uhhh, well... It was like that when I got here, and I didn't feel like changing it, ok!"
        w "Relax, I was just messing with you!"
        show darius happy at right
        da "Haha, yeah sorry, I can get a little defensive sometimes."
        "Things were getting a little awkward, so I decided to jump to the chase and ask them about ideas for the play."
        "I personally had no interest about the topic, so I had already decided that I was going to let them choose what we should perform."
        w "I was thinking that we could put on Romeo and Juliet! I know it's a little cliche, but it's always a real crowdpleaser and I've always wanted to be Juliet."
        da "That sounds super lame. I mean, I bet everyones gonna do Romeo and Juliet, we should do something that no one could predict."
        show winrey angry casual
        w "Ok then, what's your great idea Darius?"
        da "I'm glad you asked."
        da "I was thinking we put on a play about BroBro's Crazy Journey."
        w "What the heck is that?"
        show darius angry at right
        da "Wait, are you serious? You mean to tell me that you have never heard about BroBro's Crazy Journey!?!?!"
        w "No, I haven't. Please enlighten me."
        show darius at right
        da "Well, BroBro's Crazy Journey, or just BroBro for short, is only the best tv show of all time!"
        da "It started off as a comic book that came out in the late 80's. [name] has actually read the entire thing."
        "Winrey looked over to me with a unidentifiable look on her face and I just shrugged with a nervous smile."
        da "The comic is actually still being released to this very day, but that's not the important part."
        da "The thing that really matters is the tv show."
        da "See, in 2009, a really rich guy who was a fan of the comic decided to purchase the rights for a television adaptation of the entire thing!"
        da "It's really great as well. [name] says that it does deviate from the source material occasionally, but it's pretty freaking awsome nonetheless!"
        w "Ok... That's fine and all, but how are we going to turn that into a play? What's the story like?"
        da "Well, BroBro isn't set up like your traditional show."
        da "Most shows follow one set of characters and tell abunch of different stories using those characters."
        da "BroBro works more as an anthology, with each chapter having a different main character and a completely different story."
        da "For example, the first part follows Brother Broseph, a priest with the power to detect vampires."
        da "One day, a little boy comes up to Brother Broseph, or BroBro for short, and tells him that his dad's a vampire and the kid asks BroBro to kill his dad for him, as he has hurt many innocent people."
        da "BroBro agrees to help, and the rest of the story follows his on a dark and serious tale full of horror and violence."
        da "The next chapter follows Broke Broseph, Brother Broseph's son. Unlike Brother Broseph, Broke Broseph is just a simple bartended working in Chicago."
        da "One day, Broke Broseph, or BroBro, finds himself in the middle of a gang war. He has to choose a side and fight for the good of the people!"
        da "This chapter is way more comical than the last, and every chapter after that follows suit."
        da "Eventually they all get super powers and it just gets crazier and crazier with each episode."
        w "So how are we supposed to put on a play with crazy stuff like superpowers? We don't have the time or budget for that."
        da "I've already thought of that! We can just do the first chapter, as it is pretty simple and stright foward."
        da "Theres no super powers or anything crazy like that! The entire story only has 4 characters as well!"
        da "Theres BroBro of course, as well as the little kid and his dad, who is the main antagonist."
        w "And who's the fourth character?"
        da "BroBro's girlfriend, Lolo!"
        w "..."
        show winrey casual
        w "I hate to admit it, but that does sound a lot more interesting than Romeo and Juliet."
        show darius happy at right
        da "Yay! I knew you would come around to the idea once I explained it more!"
        da "Well, since we are all in agreement, we can get to work on righting the first draft."
        da "We are going to have to cut out quite a lot to fit all of the material into a short play, but the story is so simple that it shouldn't be all that difficult."
        da "Before we go any further, I'm gonna run to the bathroom real quick, be right back."
        "Darius got off of his bed and sprinted towards the door."
        hide darius happy at right
        w "So [name], you're a big fan of this BroBro thing, right?"
        "I told her that I was, and that she won't regret us performing it."
        w "I'm sure it will all work out."
        "We sat around in an uncomfortable silence for a couple of minutes."
        w "Hey, can I ask you a question about Darius?"
        "About Darius? What could she possible want to know about him?"
        "Wait, maybe she has a crush on him, and she wants my advice about what the best way to ask him out would be!"
        w "Well, this is kind of awkward... but... why doesn't Darius ever wear any shoes?"
        "Thank God that was the only thing she wanted to know."
        "The only problem is I don't know what the right thing to tell her is."
        "I do know exactly why Darius doesn't wear any shoes but I'm not sure if I should be the one to tell her"
        "Wouldn't it make more sense for Darius to be the one to tell her instead of me? I get why she's asking me, it's definitely a sensitive topic."
        "I know that the reason is that Darius just has an irrational fear of shoes. I don't know exactly why, I just know he's never worn any before."
        "That goes for socks as well, he can't have anything touching his feet."
        "It is pretty strange, but I have always thought it was a pretty harmless fear to have, so I've never bothered with trying to help him get over his phobia."
        "But what do I tell Winrey?"
        "Since I don't have the details, I can just tell him he doesn't like shoes and leave it at that."
        "But would I be a bad friend to Darius if I go into details about it without his explicit permission?"
        "I could just tell her that it's not my place to discuss such matters, as it should really be Darius who tells her about that."
        "Also, I wouldn't mind hearing about why he has his fear. Maybe if we both confront him about it he will spill the beans."
        "It might be pretty rude to drop all of that on him though, what if he doesn't want to talk about it?"
        "What if the reason is super embarrassing or tragic?"
        "What should I tell her?"
        menu:
            "He's just scared of shoes for some reason":
                jump shoe

            "I think you should just as Darius":
                jump AskDariu

        label shoe:
            "I decided it would be best if I just told her everything I knew, which wasn't much."
            "I can't imagine Darius would mind all that much if I told her, I mean it's no secret that he never wears any shoes."
            "He had to get special permission from the principal to make sure it was ok and everything."
            "The entire class knows that something's up, we just don't know the details."
            show winrey angry casual
            w "Oh."
            w "So you don't know the exact reason? He's just scared of shoes and no one knows why?"
            "I told her that I didn't know any of the details, just that he was scared of them for some reason"
            w "That's such a strange quirk to have."
            w "And pretty dangerous I should add."
            w "I mean, what's he supposed to do in the winter?"
            w "Aren't his feet completely frozen? Wouldn't he get hypothermia or something?"
            "She had a good point, it would be pretty dangerous, but ever since I've known him, no such problems have arrived."
            w "Well, I think I'm gonna ask him about it."
            show winrey wink casual
            w "Oooohhh, hey [name], I've got a great idea."
            w "We should get him to confess about his little issue."
            w "If we find out the underlying reason for his fear, then I bet we can cure it!"
            w "We can treat him like a doctor would treat a patient! I just know that the two of us can fix him."
            "I wasn't all too sure about this."
            "I mean, it's nice of her to want to help Darius out and all that, but is it really our problem to try and fix?"
            "Shouldn't he go see a doctor about it or something?"
            "I'm afraid that the two of us might only make it worse. We are by no means professionals when it comes to mental illness."
            "Before I could tell her about my concerns, Darius strolled back into my room."
            jump choice14_me3
        label AskDariu:
            "I decided to tell Winrey to just ask Darius about it."
            "I think that it would make me a bad friend if I was to talk about his problems behind his back."
            "Besides, it's really not my place to tell her anything about him anyways. Darius should be the one to do that."
            w "Ok, I understand."
            w "I guess I should just ask him directly instead of trying to get information about him behind his back."
            w "I'll ask him when he comes back into the room."
            "Wait, what? She's really going to just straight up ask him about something so personal as soon as he comes back in here?"
            "I mean, she barely even knows the guy. This is the first time that the three of us have even hung out."
            "Shouldn't she wait until she gets to know him a little better before she asks him something so personal?"
            "Before I could tell her how bad of an idea that was, Darius came back from the bathroom and strolled on in."
            jump choice14_me4
    label choice14_me4:
            show darius at right
            show winrey casual
            da "What's up guys? You two seem like you were talking about something."
            w "Oh, me and [name] were just talking, and we were wondering if you could fill us in on something."
            da "Sure! What is it?"
            w "Well, why don't you ever wear any shoes?"
            show darius angry at right
            da "Wha... What!?"
            da "Why don't I... Why don't I... Why don't I ever wear any shoes?"
            da "Well uhhhh.... you see... uhhhhh....."
            show darius happy at right
            da "Hahahahahaaaaaaaa...."
            show darius at right
            da "Ummmmm...."
            show darius angry at right
            "It's a serious medical conditional alright!"
            "I can't wear shoes or else I'll die or something!"
            show winrey angry casual
            w "Or something?"
            da "Yeah! Or something!"
            da "I don't know! Just shut up ok!"
            da "You don't think I know how weird I must look?"
            da "Going to school without any shoes like some homeless person?"
            "That particular line seemed to strike some kind of cord with Winrey."
            w "What's that supposed to mean! What do you have against homeless people?"
            da "What?"
            da "I don't have anything against them, I was just giving an example!"
            da "Anyways, it's neither of your guys' problem anyways, so don't worry about it ok?"
            w "Ok, I'm sorry for asking, I just wanted to help you."
            da "Help me? Like I'm some weak pathetic little dog who can't fend for himself?"
            da "I don't need help! Theres nothing wrong with me ok!"
            da "I just choose not to wear shoes because I think their dumb."
            da "oH lOoK aT ME, I'M weAriNG SHoEs! Hurdy dur de dur."
            "Darius said that last line in a way that made it sound like he was mocking people for wearing shoes."
            da "People act like I'm the crazy one, were you born wearing shoes? No, because it's unnatural."
            w "You weren't born wearing clothes either but you're rocking that shirt and pants combo as we speak."
            da "Th...That's different ok! Anyways, we made enough progress on the project for today, so I'm going home."
            w "We're already at your home you moron!"
            da "Oh yeah... Well... I think it's time for you two to go home!"
            w "That's fine with me!"
            w "I hope you two have a great day and a great weekend! I'll see you two at school!"
            da "Yeah! I'll see you two at school! I hope you all have an amazing weekend!"
            "Winrey stormed out of the room at a great haste and left me alone with Darius."
            hide winrey angry casual
            da "I'm sorry... That got a little out of hand."
            "He was right about that, I never expected the two of them to have an argument during our first meeting."
            da "I'll apologize to her tomorrow at school, you should go home and get some rest [name]."
            "I agreed and left his house."
            scene mansion day1
            with fade
            "I walked out of Darius's front door and saw Winrey standing at the same place where we met Darius earlier."
            show winrey angry casual
            w "Hey [name]..."
            w "That definitely got out of hand, huh?"
            "I agreed with her"
            w "I'm going to apologize to him tomorrow, it wasn't my place to ask him something so personal, especially right after he was kind enough to host this whole thing at his own house."
            "I was happy to realize that they both agreed that the argument was a mistake."
            "I'm sure things will get back to normal really quickly at this pace."
            "The two of them will probably make up tomorrow at school and we can just forget this ever happened."
            show winrey casual
            w "Well, I'll see you tomorrow at school, see ya!"
            hide winrey casual
            "Winrey ran off in the opposite direction of my home so I decided just to go on back to my house and call it a day."

            jump choice14_done

    label choice14_Winrey:
        "I decided that we should go to Winrey's house, as I was very curious to see what her house was like."
        show winrey angry school
        w "Ummm, actually, that's not a good idea... You see... well..."
        w "..."
        w "You just can't ok! My mom is...uh...cleaning!"
        show winrey school
        w "Yeah! She's cleaning! So you guys can't come."
        "Crap, I knew I shouldn't have chosen her house."
        "I mean, how rude of me was it to invite myself over like that? Especially since we are not even that good of friends."
        "Ok, which other place should I choose?"
    menu:
        "Let's meet at my house":
            jump choice14_me

        "Let's meet at Darius's house":
            jump choice14_Darius

    label choice14_done:
        scene bedroom night
        with fade
        play music "bedroom-night.mp3"
        "It was a couple hours after the argument had occured when I decided to go to bed."
        "I can't believe things got out of hand so quickly, one second we were doing our project and the next the two of them were at each others throats."
        "Oh well, after talking to the both of them, it sounds like they will make up pretty quickly, and even if they don't, it's not my problem to deal with."
        "I could feel my eyelids trying their hardest to close on their own, as if they were connected to a heavy 10 pound weight, so I decided it was time to hit the sack."
        "Hopefully tomorrow goes well."
        "I put on my pajamas and hopped under the covers."
        scene black
        with fade
        play music "black.mp3"
        m "That was a really fun weekend getaway [name]! The two of us should spend more time together!"
        "I agreed with her as we pulled into our driveway after a weekend trip away from the house."
        "I got out of the car, grabbed some of the luggage out of the car, and opened our front door."
        "Blech! What is that stench!?"
        "As soon as I walked through the door I could smell some kind of unidentifiable smell, but I knew it smelled horrible."
        "Did my sister try and cook again?"
        "I looked into the kitchen and saw nothing out of the ordinary."
        "All of the different foods and drinks were left exactly how they were when we left a couple of days ago."
        "I guess my dad and sister went out to eat all weekend. I don't blame them, if I was left alone, I wouldn't want to cook either."
        play sound "drop.wav"
        "{i} THUMP! {/i}"
        "I heard a loud sound coming from the living room, as if someone had dropped something heavy."
        "I walked into the living room to investigate, and sure enough I saw my mom standing by the living room entrance with the bag of luggage she was carrying strewn across the floor as if she didn't even care where they ended up."
        '"Come on mom, you need to be more careful." I told her.'
        "I looked over to her and realized that something was wrong."
        "My mom was standing there, completely pale, frozen in place."
        "She was looking towards the other side of the room, near the window."
        "I followed her gaze to see what she was looking at"
        "I caught a brief glance of blood...and some guts... and..."
        play sound "alarm.wav"
        "{i} BEEP! BEEP! BEEP {/i}"
        scene bedroom
        with fade
        play music "bedroom.mp3"
        play sound "alarm.wav"
        "{i} BEEP! BEEP! BEEP! {/i}"
        "I opened my eyes to see that my alarm clock was going off."
        "I got out of bed and turned it off so I wouldn't have to hear that ungodly noice for a second longer than I needed to."
        "..."
        "The dream... why am I remembering it all again."
        "I don't want to think about that stuff anymore, I want to move on, but I keep on having that dream."
        "I realized that it was Monday, and that I had to go to school today."
        "I grabbed a clean outfit out of my closet and took a quick shower to get rid of the cold sweats I woke up with."
        "I wasn't hungry at all, so I decided to skip breakfast and head over to school a little early."
        scene hallway school
        with fade
        play music "classroom.mp3"
        "I got to school about 10 minutes before class started."
        "I was about to walk into the classroom when I heard a couple of familiar voices from inside."
        "I stood against our classroom doorway so that I could eavesdrop in on the conversation without being seen."
        "I looked around to make sure that no one could see what I was doing, as I suspected, the hallway was completely empty."
        "For some reason, barely anybody gets to our school early at all, everyone just sort of arrives at the last possible moment."
        "The only people who do get here early are teachers and a couple of clubs, but they all have offices or rooms that they meet in, so the hallways are pretty much deserted right until class is about to start for the day."
        "I put my ear against the wall that was right next to the open door that lead into the classroom."
        "From where I was, I couldn't see anybody, and they wouldn't be able to see me, so I just listened to the voices."
        w "Listen, I'm real sorry about yesterday."
        da "No no no, you shouldn't have to apologize, it was me who was in the wrong."
        w "What? How? I was the one who brought up yout shoe problem, it was completely not ok for me to ask about that."
        da "Yeah, but I shouldn't have gone off on you, I mean it's only natural that you wanted to ask questions, I know how weird it is."
        w "Yeah it is weird, but that's ok, the little quirks that we all have is what makes us unique, and I think it's kind of cute..."
        da "Wha...? Cute?"
        w "I dunno, it's so weird that I think it's kind of charming, you know?"
        da "You got a foot fetish or something?"
        w "Oh piss off! That's not what I was getting at!"
        da "You sure? Cuz it sounds like you got a foot fetish."
        w "I swear to God I will deck you right here."
        w "I'll get my soccer cleats out of my bag and kick you so hard with them it will rewire your brain and make you want to wear shoes at all times! Even when you're in the shower or when you're sleeping!"
        da "That's a little hardcore."
        w "I am hardcore!"
        da "I can believe it."
        "What was happening in there? The two of them sound like an old married couple."
        "...Wait..."
        "Are they...flirting?"
        "I thought that the only thing they planned on doing was making up for yesterday, but this is taking it way too far!"
        "I swear I'm gonna kill Darius if he tries anything funny on her..."
        w "Well anyways, I guess I'll see you in class."
        da "We're already in class"
        w "Shut up!"
        "I had about enough of this, I walked into the classroom just so I could get the two of them to shut up."
        scene classroom
        with fade
        show winrey school
        show darius at right
        da "Oh hey [name], you're here awfully early aren't you?"
        '"I could say the same thing about you two." I told them coldly.'
        w "The two of us were just talking about yesterday and how stupid that argument was."
        da "Yeah but we made up, so you don't have to worry about anything [name]."
        "As if that's what I was worried about."
        "Before I could say anything else, the bell rang, indicating that class was about to start."
        "Just as I said, the hallways immedietly became flooded with students from all over."
        "Just a minute ago the place was completely empty, but now you could hardly find a place to stand if you tried."
        "A lot of people began flooding into class."
        "I caught a glimpse of Jerry, but I guess he didn't feel like doing anything today, as he just walked over to his seat and sat down without making eye contact with anybody."
        "Maybe he has forgot all about the other day."
        "Everybody took their seats right before the bell rang, but our teacher was nowhere to be seen."
        da "Where's Mrs. Striker?"
        w "I don't know, it's not normal for her to be late, she's usually the first person here."
        hide winrey school
        hide darius at right
        "I've always heard that if a teacher doesn't show up to class after 15 minutes, then everyone is legally allowed to leave."
        "I'm pretty sure that's just a rumor though, at least in highschool."
        "Maybe that's how that works in college, as you do have a lot more freedom there."
        "College."
        "It just hit me that I need to seriously think about college."
        "I had no eartly idea what I wanted to do with my life, so how am I supposed to choose a college or a major?"
        "With my bad grades, I won't be able to get a scholarship, or at least not a good one, so I should probably try to pick a cheaper college."
        "If I even do decided to go to college that is."
        "I could just learn a trade. I heard people can make good money from learning one particular skill and sticking with that their entire lives."
        "Maybe I could become a plumber, just like Dario from that game series."
        "Or an electrician, or something else."
        "No, I'm way too lazy to do any of that stuff. My dream job involves no physical labor at all, so pretty much every trade is out for me."
        "But what exactly is my dream job?"
        "Maybe something involving computers? No, I'm too dumb for that. All of that technical mumbo jumbo would go right over my head."
        "I could be an accountant. Balancing numbers and stuff. No, I failed my accounting class."
        "Finance? No, I'm bad with numbers."
        "Maybe I should think outside the box, and do something artistic."
        "I could be an artist, and make abstract paintings that sell for millions of dollars."
        "Or a filmaker. I could make the next billion dollar franchise."
        "No, all of that sounds way too risky and difficult."
        "Plus you probably need some connections to even enter those industries, and I barely have any friends besides Darius, who might not even be my friend for much longer if he keeps on flirting with Winrey like that..."
        "Anyways, college isn't for a couple more years, I have plenty of time to decide that."
        "I guess I could win the lottery using my powers..."
        "NO! I said I wouldn't use it for something like that."
        "Someone else could be destined to win the lottery, and If I take it from them, I could change the course of history for the worse."
        "I should only use my powers when I know it won't hurt anybody else."
        "Well except Jerry, screw that guy."
        show winrey school
        w "Class, can I have your attention!"
        "Everyone in the class immedietly became silent."
        "If anybody else told everyone to be quiet like that, no one would have listened, but Winrey seems to have a way of getting everyone to follow her orders."
        w "I'm not sure why, but Mrs. Striker seems to be late for some reason. As your class president, it is my job to step in in times like these."
        show jerry at left
        j "It has been 5 minutes since class started, in 10 more minutes we will all legally be aloud to leave."
        show winrey angry school
        w "Now Jerry, you and I both know that that is just a silly myth, you will stay here until class is over or I will have no choice but to write you up."
        "Oh crap, I was right! That is just a myth!"
        j "Whatever..."
        hide jerry at left
        show winrey school
        w "Until Mrs. Striker gets here, let us all behave ourselves. No funny business, ok everyone?"
        "The whole class agreed to be on their best behavoir, and everyone went back to doing their own thing."
        hide winrey angry school
        "Winrey went back to her seat, and whispered something to Darius."
        "Darius looked at her and started giggling."
        "What's going on between the two of them? When did they have time to become so chummy?"
        "Before I could give it any more thought, the classroom door opened and Mrs. Striker appeared."
        show striker
        s "Hello class, I apologize for my lateness, but I have some good news!"
        show striker happy
        s "We have a new classmate joining us today!"
        s "Come on in and introduce yourself, don't be shy!"
        "Suddenly a girl walked into the class and stood next to Mrs. Striker"
        show yuuki at left
        "The class stood in silence for about 10 seconds, and neither the girl nor Mrs. Striker said a word."
        "The girl was just staring at us all with a stupid grin on her face."
        "I didn't want to be rude, but she looked like a generic anime protagonist."
        "From the way she was dressed, to her hair color, to her eyes."
        "Isn't that a Japanese sailor uniform? I'm pretty sure girls wear that to school in Japan."
        "But that doesn't make any sense, she was as white as Winrey. Maybe she's a transfer student."
        show striker
        s "Ummm... Ok so this is Stephan..."
        y "Yuuki!"
        s "..."
        s "...What?"
        y "My name is not Stephanie as you were about to say! It is Yuuki! Yuuki Nasagori to be exact!"
        y "The name you were about to say was merely a fake name that was given to me by my parental units!"
        y "My real name is Yuuki! That name was given to my by the demon that is imbedded into my soul!"
        y "Me and him have a contract you see! I let him use my body as a vessel and he lends me his powers!"
        "Aw geez... This girl should be locked up..."
        "At least I probably won't have to deal with her that much."
        s "Umm.. Ok then, why don't you have a seat."
        s "It seems like there is an empty one right next to [name]."
        s "[name], why don't you raise your hand so Stepha... I mean so Yuuki can know where to sit."
        "I begrudgingly raised my hand, and Yuuki immedietly strolled to the empty seat right next to me."

        show yuuki
        y "Hello mortal! I will be your seatmate it seems!"
        y "I apologize if at any time you immedietly vaporize, as I sometimes forget to hold my powers back and end up killing people!"
        "Before I could say anything, she made a weird face and put her nose right against my neck."
        "She inhaled in real hard, as if she was trying to get high off of my aroma."
        y "Oh my Devil! You have it, don't you!"
        "I gave her a look that said that I didn't want to deal with her for a second longer."
        y "You have a power like me!"
        "That line caught my attention. Theres no way she could possibly detect my gift, could she?"
        "And if she can, does that mean that she also has some power? Was she not lying?"
        show striker happy
        s "Wow [name], I'm so pleased to see that the two of you are getting along so well!"
        s "Wait, I have an idea."
        s "Yuuki, we are doing this project in our class, why don't you join your new friends team?"
        y "I would be glad to assist him in any problems that might arise!"
        s "That's great! [name], you can give Yuuki the details, can't you?"
        hide striker

        "I didn't want to, but I agreed."
        show yuuki at center
        y "Many thanks are due to you for your assistance with my struggles, my dear compadre."
        "Now she's speaking spanish?"
        y "I must tell you right now, that you probably shouldn't get to close to me, as people who I get close to have a tendancy to perish in horrible, painful ways."
        y "For example, I befriended a talking washing machine named Carl. We were very close. He would wash all of my clothes every day."
        y "One day however, he stopped talking to me."
        y "On top of that, he also stopped washing my clothes."
        y "When I went into my magical dungeon to check on him, I found out that he was stranded all around the room in pieces."
        y "To this day I still don't know what happened to him, but I do know that I will never have a friend like him again."
        show yuuki happy
        y "Well, except for my friend Seperotosomes, she was a brave companion who helped me with many ceremonies."
        y "One time, we were conducting a ritual to bring back one of her dead relatives. Everything was going well until it wasn't."
        y "We had created a summoning circle, and we thought we had done everything correctly, but something went horrible wrong."
        show yuuki angry
        y "That idiot forgot to yell the special summoning spell, and it cost her her life."
        y "Well, kind of. I was able to move her soul into an old washing machine and..."
        y "...Wait..."
        "I don't know why this girl was going out of her way to tell these lies to me, as is I would believe them."
        "And now she's in our group? This sucks so hard."
        show yuuki
        y "Also I suppose that it would be best to warn you about my eyes."
        y "As you can see, they are different colors. I assure you that there is a good reason for this, and it is not just for looks."
        y "Using these eyes, I can do different special tasks."
        y "For example, if I focus in only on my left eye, I can read the thoughts of anybody who I make eye contact with."
        y "The best part is I don't even have to close my right eye to accomplish this miraculous task! I only need to focus on my left eye."
        "I wasn't sure what she meant by focusing in on one specific eye, but I did know that she was insane."
        show yuuki angry
        y "Hey! You don't believe me, do you? I can tell by the way you're looking at me! I don't even need to read your thought!"
        y "I can demonstrate my ability if you so wish, mortal."
        menu:
            "Ok, Prove it":
                jump Prove

            "I believe you":
                jump Believe

        label Prove:
            y "Ok then, I will!"
            y "Make eye contact with me, if you dare mortal!"
            "I did as she said and looked straight into her eyes."
            y "Ok, my amazing power takes a couple of seconds to work correctly, so just continue making eye contact. And don't you dare blink, as that would break the spell!"
            "I wasn't sure what the point of reading someones mind was if you had to make them make eye contact and they couldn't even blink at all."
            "If you are trying to read someone mind, wouldn't you want to do it discreetly?"
            "Her methods so far were as subtle as a dump truck running head first into an amusment park full of children."
            "I don't see how there could be any pratical use to this method."
            "How are you supposed to get someone to keep their eyes open without telling them the purpose?"
            "Were you just supposed to ask them to have a staring contest with them? What if they refuse? This is so dumb."
            y "Oh my..."
            "Wait, did she actually read my mind? Did she hear me calling her so-called power dumb?"
            y "Your thoughts...they are so...lewd!"
            y "How dare you think those things about me, you disgusting pig!"
            "What was she on about?"
            y "You were thinking about all the things you want to do to me!"
            y "You said that you thought I was hot!"
            y "Gross! As if I would ever be with a mortal in any physical sense! My mind and body belongs to Perongolomo, the demon in my body!"
            "This girl is completely off her rocker! As if I would ever think about her in that way!"
            "I would much prefer to be with someone who wasn't delusional."
            y "I'll forgive you for your insolence this one time mortal! But if I ever catch you thinking about me again, I swear I will put a spell on you!"
            "Man, whatever. As if I care what this weirdo thinks of me."
            jump choice15_done

        label Believe:
            show yuuki
            y "Wait, you do?"
            y "..."
            y "Uh... I mean, of course you do! HAHAHAHA! How could anybody see me and not believe that I am gifted with such powers!"
            y "You could have probably told how much power I possessed from the second I walked through that doorway!"
            "Of course I didn't actually believe that she had any powers, but I knew if I asked her to prove it I would have to interact with her for longer."
            "And I didn't want to talk to her for a second longer than was absolutely necessary."
            "Especially now that we are in a group together, I gotta do everything in my power to keep out interactions to a minimum, or else I might go insane myself."
            jump choice15_done

label choice15_done:
    y "I also have another power you know."
    y "If I focus in on only my right eye, I can shoot our laser beams!"
    y "Of course, I could never demonstrate this power to you, for obvious reasons, so you're just going to have to take my word on it."
    "I realized that we were having this insane conversation in front of the whole class, and I looked around to see that everybody was staring at us, including Mrs. Striker."

    show striker at right
    s "Umm. Ok. It's good that the two of you are getting along, but if you wouldn't mind..."
    show striker angry at right
    s "SHUT UP!!!"
    "Everyone in the class started laughing at us, and I realized how much of a pain in my behind this new girl was going to be."
    "I'm already pretty lame, I don't need this girl to lower my popularity anymore than it already is."
    show striker at right
    s "Sorry, I got a little too angry there."
    s "Well, moving on. Will everyone please take out your textbooks and turn it over to page 378?"
    s "Today we are going to be discussing the great wonders of the pythagorean theorem."
    hide yuuki
    hide striker
    "It was at that point that I completely checked out."
    "I have a bad habit of zoning out in class. Sometimes I wonder if I have ADHD or something."
    "It was a few minutes later when I felt something hit my head."
    "It didn't hurt at all but I turned around to see who the culprit was."
    "I looked around, and my I noticed Jerry was staring right at me."
    show jerry
    "He pointed at the ground and smiled"
    "I looked that and noticed that there was a crumpled up piece of paper resting right below my feet."
    "I bent down, picked it up, and began unraveling it to see what was inside."
    "To my dismay, there was a few words scribbled down quickly in Jerry's handwriting."
    j "You two look so cute together! Please make sure to invite me to the wedding!"
    "Those were the words that were written on the paper."
    "I hope Jerry was the only one who thought that."
    "The last thing I need is everyone thinking that I actually like that freak."
    "I crumpled the paper back up, turned around, and threw it at Jerry as hard as I could."
    show striker angry at left
    s "[name], what the heck do you think you're doing?"
    s "You know that it is strictly against class policy to throw things at other people!"
    s "If I catch you throwing things again, I will give you detention!"
    "I apologized to her and looked down at my desk."
    "If she had given me detention, then I could have used my power to go back in time and stop myself from throwing it."
    "Since she didn't though, it's not really worth it to use my power."
    "I did say I would use it only when it was completely necessary."
    "This is just a minor incident, I'm fine."
    "Or maybe I should go back? I mean, Jerry could retaliate in some way, and if I choose not to go back, he could try and fight me or something."
    "No, Jerry has never been the physical type, and I don't see that changing anytime soon."
    "Just in case though...maybe I shold go back..."
    "What should I do?"
    menu:
        "Go back":
            $ choice1 = "jump"
            jump back

        "Don't go back":
            $ choice1 = "stay"
            jump stay

    label back:
        "I decided it would be best to play it safe and go back."
        "I doubt Jerry would do anything serious, but I would rather go back now and be safe instead of waiting till later when I can't go back and regreting it"
        "I reached deep down into my pocket where I was hiding my gun, pulled it out, and quickly did the deed."
        scene black
        with fade
        play music "black.mp3"
        "..."
        "Ouch, guns hurt."
        scene classroom
        with fade
        play music "classroom.mp3"
        "..."
        "I was back in the classroom."
        "It worked."
        "I'm really glad that the side effects of this thing are wearing off."
        "I used to be disoriented whenever I went back, but now I know exactly what's going on and what I'm supposed to be doing."
        "In exactly 10 seconds, Jerry is going to throw that piece of paper at me."
        "And this time I'm not gonna throw it back at him. In fact, I'm not gonna do anything."
        "I'm not even going to pick the paper up off the ground and look at it."
        "And why should I? I already know what's written on it, theres no point in giving Jerry the satisfaction of me reading it."
        "In fact, I'm going to pretend like I didn't even notice him hitting me."
        "And I did exactly that. I felt the paper hit the back of my head and I completely ignored it."
        "I let out a small smirk of satisfaction as I knew Jerry must be pissed."
        "I could feel his harsh gaze piercing the back of my head in anger and confusion."
        "He genuinely doesn't know what to do now. He's confused as to why his stupid plan didn't work."
        "What a moron."
        jump choice16_done

    label stay:
        "I decided that it would be best to stay and accept my problems."
        "I can't be going back in time whenever I have the smallest issue arise."
        "What would I learn from my mistakes if I just think I can just erase them at a moments notice?"
        "Plus there could come a time when I don't have my gun for some reason, and if I come to rely on it this much then I could get into some serious trouble."
        "I should learn from these small mistakes and grow as a person. Save the gun for life and death situations."
        jump choice16_done

    label choice16_done:
        "The rest of the class went on as usual."
        "Mrs. Striker taught us the basics of calculus, which I didn't understand in the least bit."
        "She then finished up the session by reminding us to continue working on our projects, as we wouldn't want the presentation to sneak up on us."
        scene hallway school
        with fade
        "After class was over, I got out of my seat and walked into the hallway with the intention of heading home when I heard a voice call out my name behind me."

        da "[name]!"
        show darius
        "I turned around, and sure enough, Darius was standing there in his usual default pose."
        da "What's up man? I was wondering if you could work on our project today."
        "I didn't have any plans so I agreed."
        show darius happy
        da "Awsome! I'll go ask Winrey. Can you ask that new girl that's in our group?"
        "I had already forgot all about that creep and how she had intruded her way into our perfect trio."
        "Oh well, nothing I can do now. I told Darius that I would find her and tell her that we were meeting today."
        da "Good. I guess I'll see you there!"
        "Darius turned around to leave and go find Winrey, but before he could, I stopped him to ask where it is that we were meeting."
        da "Oh crap, I hadn't even thought of that! I'll let you choose."
        "I decided it would be best to meet at that diner that me and my mom ate at recently, as it would be pretty mean to force the programmer to create a bunch of different options for something that didn't even matter."
        da "That works for me! I'll see you there as soon as I get Winrey!"
        hide darius
        "And with that Darius went on his way to go and find Winrey. I still wasn't all that happy about how much time he was spending with her, but I didn't have time to worry about that now."
        "I need to find that girl, what was her name?"
        "Yuno? Yucho? Yatti?"
        "No, it was Yuuki! Yeah, I need to find Yuuki!"
        "Maybe she's still in the classroom?"
        scene classroom
        with fade
        "I walked back into the classroom, and to my dismay it was completely empty."
        "Where could she be?"
        scene hallway school
        with fade
        "I walked back into the hallway and started peering into each class, one by one."
        "The first class I looked into was the one immedietly to the right of ours."
        "I looked into the window, and saw that it too was empty."
        "I walked around the entire school, trying my best to find this girl that I didn't even like, and came out completely empty handed."
        "She must have went home for the day."
        "I don't have her number so there isn't really anything I can do about it now."
        "Oh well, I guess I'll just head over to the diner by myself and meet Darius and Winrey there."
        "I can tell them that I tried my hardest to find her, but she wasn't in the school. I'm sure they will understand."
        "I headed out to leave, but before I could make it out of the front doors of the school, I felt a slight pressure on my bladder."
        "Oh crap, I really need to pee!"
        "I fast walked over to the school bathroom and headed inside to relieve myself."
        scene bathroom
        with fade
        "I walked into the bathroom and went to the closest urinal I could find."
        "I unzipped my pants and let it rip."
        "Ahhhhh..... That feels nice."
        "I finished up, zipped my pants up, flushed the urinal and turned around to wash my hands."
        "AHHHHHHH!"
        "To my utter dismay and shock, a familar face was standing about a foot behind where I was just peeing."
        show yuuki
        y "Hello again, pervert!"
        "I couldn't believe it!"
        "Not only was this girl crazy enough to follow me into the mens restroom, but she also had the audacity to call me a pervert?!"
        "I was about a second from slapping her when I decided it would be best to play it calm."
        menu:
            "I'm sorry, but this is the mens room, you must have made a mistake.":
                jump niceboy

            "What the heck are you doing here you crazy witch!":
                jump meanboy

        label niceboy:
            "I did my best to say what I thought was the nicest response I could have to this scenario, as I think she must have some mental illness."
            y "Oh but I've made no mistake, human!"
            y "Yuuki goes where Yuuki wants!"
            y "I do not follow the same rules as a normal human! I, Yuuki, am above the law!"
            "So now she's referring to herself in the first person? Why am I not surprised."
            y "But if you must know, I came in here to find you, mortal!"
            "Me? What could this girl possibly want with me?"
            y "I came in here to ask you a question."
            "Could she not have waited until I was done using the bathroom?"
            y "I was wondering when the two of us would work on this project that the witch was speaking of."
            "Witch? Who's she talking about?"
            "Mrs. Striker? I guess that's the only person she could be talking about given the context of her sentence."
            "Well, no matter, I guess this works out since I was looking for her for the same reason."
            "I told her that we were meeting today at the diner, and that she could come with me if she wanted."
            y "Yes! That works perfectly mortal! I will wait right here as you be rid yourself of those malevolent miniscule molecules that you have contracted on your journey to the urine machine!"
            "What is she talking about? Germs?"
            "I shook my head and washed my hands and together, the two of us made our way to the diner."
            jump choice17_done

        label meanboy:
            "I tried my best to be nice, but I couldn't really contain my anger."
            "And who could blame me? This is a major invasion of my privacy! If the roles were reversed you bet this would end up on the local news!"
            show yuuki angry
            y "How dare you speak to me, Yuuki, in such an irreverent tone you dog!"
            y "Do you not know who I am?"
            y "I am the great Yuuki Rohaboochi!"
            "Didn't she use a different last name before?"
            y "I am a 1000 year old demon who has come here to take over the entire world!"
            y "I am inevitable!"
            "This girl has seen way to many movies, and she can't even keep her story straight."
            "She told me something entirely different today in class."
            show yuuki
            y "Anyways, I have come here today, to ask you a most important question that I need a most important answer to most importantly!"
            "..."
            y "When are we going to journey to the netherworlds to defeat that evil demon that we were assigned to do today in class."
            "I had no idea what she was talking about, but I did remember that I was supposed to tell her about us meeting at the diner, so I told her about it."
            y "Ah yes! That is the demon that I was discussing! We are working on defeating him today?"
            "I nodded my head and told her to wait outside and we could head over there together."
            y "This is indeed most excellent news! I shall wait here as you take care of the tiny lifeforms that have infected your hands!"
            "I washed my hands, and together, the two of us went on our way to meet Darius and Winrey at the diner."
            jump choice17_done

label choice17_done:
    scene cafe
    with fade
    play music "cafe.mp3"
    "Yuuki and I arrived at the cafe after about 30 minutes of walking."
    "Along the way, Yuuki talked non stop about her previous lives and all of the journeys she has been on."
    "I realized pretty quickly that her stories had no consistency, as she kept on contradicting herself."
    "The main way she would do this was by using a different last name for herself."
    "For some reason she liked to refer to herself in the third person, and whenever she did so she would use a different last name."
    y "I, Yuuki Trasobam, am an angel!"
    y "I, Yuuki, weqrestoom, killed JFK!"
    y "I, Yuuki ivsuriudhviuhdiudhvoiudhgoiudouyvbduovbodsouvbdtouvybdourbspufs8fhvouhiuosiususvbuyovbuodsy, am a total moron!"
    "She really got on my nerves, and for the entire walk, I elected to remain silent and let her do her thing."
    "Since we will have to work together frequently, I figured it would be best to not piss her off."
    "The worst part was her stupid grin."
    "No matter what, she always seemed to smile throughout all of her absurd stories."
    "No matter the tone of these adventures, she couldn't help but smile the entire time."
    "It didn't matter if she was talking about that time she raided a castle in Ancient Rome or how her entire family was tragically killed in a freak accident, she always smiled."
    "This was the entire opposite of myself, I barely ever smiled."
    "Sometimes people will bring this up to me and it will annoy the crap out of me."
    "[name], wHY dON't yoU EVeR SmilE?"
    "You know what the last thing anybody wants to do when someone tells them to smile?"
    "Smile."
    "They'll keep the grim look on their face out of spite, and that's what I started to do."
    "I still smile occasionally, but only when I feel like it, and I never fake it either."
    "If I feel the urge to smile, then I'll gladly smile. If I don't want to smile, I won't."
    "That's another thing that always annoys me."
    "Some people seem deadset on smiling at all times, no matter what."
    "These people always came off as fake and insincere to me."
    "If you don't feel like smiling than why are you? Because society tells you to?"
    show yuuki
    y "Hey mortal, are you alright? Has someone cast a spell of hatred on you?"
    "What was she talking about this time?"
    y "You've been standing at the front portal of this establishment for a full minute now, doing absolutely nothing."
    show yuuki happy
    y "You're a total freak!"
    "She's one to talk..."
    show yuuki
    y "So anyways... Where are your two mortal friends staying at?"
    y "There isn't anybody here yet. Didn't they get here before us?"
    "I looked around the cafe and realized that Yuuki, or whatever her name was, spoke the truth."
    "The place was completely empty, besides the workers."
    "That wouldn't actually be all that strange on its own, I mean this place has never been all that crowded, but Darius and Winrey should have made it here before us."
    y "You don't think they were kidnapped by a rival gang, do you?"
    y "Or maybe they were taken by wizards! Or Demons! Or an evil ancient God of Destruction!"
    y "Or maybe their making out somewhere..."
    '"Ok, shut up!" I screamed at her.'
    show yuuki angry
    "I couldn't even stand the thought of the two of them alone somewhere..."
    "I realized that I had accidently started a scene, as the person at the front counter was glaring at me."
    "I shot an awkward smile in her direction, trying to tell her sorry, and I gestured to Yuuki to choose a booth to sit at."
    y "Ok, fine. I'll find us a seat where we can't possible be overheard by any demons."
    show yuuki
    y "Luckily I can use my power of silence to make it so that no one else can hear out conversation."
    "Yuuki then stood up on one of the seats and started whispering some random gibberish."
    show yuuki angry
    y "{i}say nomoni say fretouti bo getsere fretsomonogetololol lolimono pedogreto saert{/i}"
    show yuuki
    y "It is done"
    show yuuki happy
    y "This place is now completely safe from any outside forces of evil!"
    show yuuki
    "I should make you pay me for my services, as it cost me quite a bit of mana to do these spells, but I'll let you off the hook just this once!"
    '"I am so grateful." I said sarcastically'
    "Before she could talk about anything else, I heard the front door open, and two familiar faces walked in."
    "Darius and Winrey walked into the restaurant together, and before long they spotted us and came to our table."
    "Before they had arrived, I decided to sit on the opposite side of the table from Yuuki, as I didn't want to be near her, but when the two of them arrived Yuuki got up and moved to my side of the table."
    show yuuki at left
    "She sat uncomfortably close to me, and I had zero personal space left."
    "Before I could tell her to scoot over, Darius and Winrey came over and sat on the opposite end of the two of us."
    show darius at right
    show winrey casual
    da "What's up guys!"
    w "Sorry we're late, I decided to change into a more comfortable outfit before we came, so I had to go get a pair of clothes out of my locker!"
    "So that's what happened. Thank God Yuuki wasn't right about them... well... I don't even want to imagine it."
    show darius happy at right
    da "The two of you look pretty close, don't they Winrey!"
    "I was painfully aware of how close Yuuki was to me at the moment, I felt like I couldn't breathe."
    w "Yeah they do!"
    w "Wait, where are my manners, I haven't even introduced myself yet!"
    w "My name is Winrey."
    da "And I'm Darius! I'm glad that we get to work with you on this project."
    w "Yeah, before you came it was just the three of us, and we were the only group to have less than 4 members."
    "The two of them might seem pretty happy might now, but once they get to spend 5 minutes with her they will realize just how good we used to have it."
    y "It is a pleasure to meet the both of you mortals! My name is Yuuki Daronga!"
    y "I am a level 75 mage who became trapped in this world after an evil demon trapped me here against my will."
    y "I hope that I won't have to stay too long, and I am currently resting so I can prepare for our great rematch!"
    w "..."
    da "....."
    w "...That's... pretty cool!"
    da "Yeah, I... I didn't know we hade a mage in the class!"
    "I was about to interject to end the painful conversation that we were trapped in, but before I could, Winrey handed us all some menus to look over."
    da "Oh cool! I'm starving!"
    y "I too am in a desperate need of energy. I'm afraid I, Yuuki Sereto, used it all up with casting spells before the two of you arrived."
    w "...Thanks, I guess?"
    da "Yeah, thanks for that..."
    y "You are quite welcome my friends, I was telling [name] over here that I will not charge for my service just this once."
    da "Wait, didn't you say that your last name was Daronga just a minute ago?"
    y "Yes. And?"
    da "Well... after that you said your name again, but this time you said Sereto as your last name."
    y "..."
    y "You must have misheard me, mortal! I, Yuuki Ferortop, have always had the last name of Quintepolocies!"
    da "Uhhhh...."
    "Things were starting to get out of hand, and I knew it would be best if we all got along, so I changed the subject by asking everybody what they were going to order."
    w "I'm gonna get a chocolate milkshake!"
    da "Oooohhh! Ice cream does sound good! Maybe I'll get that too!"
    show winrey angry casual
    w "Well don't get the same thing as me, copycat!"
    da "Oh, I'm sorry! I'll get something else!"
    show winrey wink casual
    w "Geez man I was just messing with you! get whatever you want!"
    show winrey casual
    da "Uhhh yeah, I knew that you were just messing with me!"
    show darius happy at right
    da "Ha..haha... I knew that..."
    show darius at right
    da "I guess I'll get the milkshake then..."
    "Did I imagine that, or did Winrey just wink at Darius?"
    "Is there something going on between the two of them?"
    "They were fighting so much the other day..."
    "Wait a second..."
    "I suddenly remembered how my mom would always tell me that sometimes people would get into arguents with each other when they liked each other."
    "She said that the reason they did this is because they didn't know what else to do with those feeling, so they were just mean to each other."
    "No, that's not it."
    "I mean, how could someone like Winrey fall for someone like Darius?"
    "She is wayyy out of his league."
    "And I'm not just saying that to be mean. Winrey was also way out of my league, it's not me being rude, I'm just being realistic."
    "And even if you take away looks, Darius has the personality of a dead wet blanket."
    "I know I'm his friend and all, but his only interesting trait is that he's scared of shoes!"
    "I'm way more interesting and mysterious."
    "Half my family's freaking dead! How metal is that? Shouldn't girls flock to me because they feel sorry for me?"
    "Plus I got superpowers!"
    "Maybe I should tell Winrey about my gift... I bet she would like me then..."
    w "Hey, Yuuki, what are you ordering?"
    y "I, Yuuki Verotop, shall order the Xtra Large Ice Cream Cake Extravaganza!"
    show darius happy at right
    da "Woooahh, that sounds awesome! What page is that on?"
    y "The page that, in your language, is pronounced 7."
    "Darius picked up his menu and quickly flipped to the seventh page."
    da "Holy crap! That's so much food! Do you see this thing Winrey?"
    w "A pound of chocolate cake with 8 scoops of ice cream of varying flavors, topped off with chocolate syrup, sprinkles, N&N's, Boreo's, and other smores!"
    da "7,680 calories! Surely you can't be serious Yuuki, that's way too much food for one person!"
    y "I am serious, and how did you know my last name was Shirley?"
    da "I thought it was...nevermind."
    w "Hey [name], what are you getting?"
    "I was originally planning on getting the wings, but after everyones chatter about sweets, I decided that I was going to get a milkshake as well."
    w "Oh so you're gonna copy off of my order to, huh?"
    y "You know mortal...if you would like to split with me...I...I wouldn't mind."
    "Why was she being nice to me all of a sudden?"
    "Ever since she started talking to me today, she has been rude and annoying, but now she's offering to split her meal?"
    "My mind immedietly went back to the thought I had just had a second ago about people being mean to someone when they had a crush on them."
    "No, that can't possible be it, can it?"
    "No no no! This weirdo can't like me like that! She probably likes guys who are goth or weird like she is!"
    "Unless, she knows about my power and she's attracted to it? She did tell me earlier that she knew I had powers."
    "What should I do?"
    menu:
        "Order your own food.":
            jump milkshake

        "Split with Yuuki":
            jump Cake

    label milkshake:
        "I told her that I was grateful for the offer, but I would rather order my own food."
        "Which was completely true. I was grateful that she was finally being nice to me instead of just being annoying, but I don't want to split a meal with her."
        "What would Darius and Winrey think if they saw us splitting a meal? What if they went around and told everybody in the school about it?"
        show yuuki angry at left
        y "Fine! I didn't want to split with you anyways! It was just a joke, ok!"
        y "As soon as you said yes, I was going to tell you that I was just kidding and how you should just get your own meal!"
        y "Thanks for ruining my plan, jerk!"
        "I could tell from her tone that everything she just said was a total lie."
        "I'm still not sure why she offered to split with me in the first place, but I do know that she wasn't lying about it."
        w "Well, anyways, I'll go place our orders in."
        da "Thanks Winrey!"
        show yuuki at left
        y "Yes, you have my deepest appreciation, mortal."
        "Winrey got out of her seat and told the person up front what our orders were."
        "She then came back to the table and sat down in the same place she was originally."
        w "So, I guess we should get started with out project."
        da "Yeah, we need to catch Yuuki up on our plan, and figure out what roll she shall have."
        y "Whatever role you have planned for me, I can gurantee that I will nail it!"
        "And with that Darius explained everything about our project."
        "From the origination of our plan, to the deep lore of the BroBro universe, to an in-depth plot summary of the first part, which we would be performing."
        y "Ah yes, BroBro. I am very familiar with him."
        y "In fact, me and him used to be partners in the midst of World War 1. The two of us would go around hunting vampires together, it was glorious."
        da "Yeah..."
        da "Well anyways the good news is that the first chapter has 4 characters."
        da "Before you came her Yuuki, one of us was going to have to double up on the roles, but luckily now we each only have to play one character."
        w "So just to be sure that I am remembering correctly, the story has 4 characters."
        w "They are Brobro, the little boy, the little boy's father, who is a vampire, and BroBro's girlfriend, Lolo."
        da "Yep, you got it!"
        w "Alright cool, so since there is 3 guys and one girl, either me or Yuuki is going to have to play one of the male characters."
        w "It would probably be best if one of us plays the little boy, as we could just make him a girl without changing the plot all that much."
        da "Yeah that's a great idea! It doesn't really matter what gender the kid is, so one of you two can play him and we can just make him a her!"
        w "Yeah! We can change her name or something. How about we call her Mary?"
        da "I like it! Now we just have to decide who is playing Mary and who is playing Lolo."
        w "I don't really care either way, Yuuki, which would you rather play?"
        y "Hmmm... Does this Lolo have any significance to the plot at all? Like, does she have any powers?"
        y "Because if she does, than I want to play Lolo, as I already have powers and I could play her without it seeming like it's fake."
        y "I could even shoot real lasers out of my eyes to make the play seem more real!"
        da "Yeah that's probably not a great idea. And to answer your question, Lolo does not have any powers."
        da "In fact, the first chapter of BroBro doesn't really have any powers at all, well, besides the vampire dad."
        y "Hmmmm... Can I be Lolo?"
        w "Sure, I don't have a preference!"
        y "This is most excellent! I will need to change some of the writing in the play around, so that I have superpowers of course."
        show darius angry at right
        da "Absolutely not! There will be no tampering with the script!"

        da "This is going to be a faithful reproduction of one of my favorite pieces of entertainment! And I'm not about to let you change it around!"
        show yuuki angry at left
        y "Fine! But I'm not playing Lolo then!"
        da "So you're gonna play the little girl?"
        y "Does she have superpowers?"
        da "..."
        da "No."
        y "Then I'm not gonna play her either!"
        da "Well you have to play somebody! Mrs. Striker clearly said that every person has to have a speaking role in the play!"
        y "You said that the vampire dad has superpowers, didn't you?"
        da "Well...Yeah. But you can't play him...You're a girl."
        y "So what? I can play a male character if I want!"
        da "Well what do you think Winrey?"
        w "I think that Yuuki can play the vampire dad if she wants to. I don't think it's a big deal."
        w "And then we can just make it so that the little girl is a boy, and you or [name] can play him."
        da "..."
        da "Fine. Yuuki, you can play the vampire dad."
        show yuuki happy at left
        y "Excellent! I am in your debt, young Darius. I promise that I will not fail you, for if I do, I shall jump off a bridge!"
        show darius at right
        da "Let's not jump to any extremes now."
        da "Well at least we have two of the four characters lined up now."
        da "Yuuki shall play the vampire dad, Bio, and Winrey will play Lolo."
        da "Now the only question is who is going to play the little boy, and who is going to play BroBro himself."
        "I had mixed feelings about this."
        "On one hand, I hate public speaking, so if I play the kid, I won't have nearly as much screentime, which would be nice."
        "On the other hand, if I let Darius play BroBro, he gets to play as Winrey's girlfriend."
        da "I know that both me and [name] really want to play BroBro, so I think I have a solution."
        da "[name], if it's alright with you, I would like to settle this by flipping a coin."
        da "If the coin lands on heads, you can play BroBro, if it lands on tails, I will play BroBro."
        da "Do you agree to these terms?"
        "I realized that there was no way that I was going to let Darius play BroBro."
        "Darius and Winrey were already getting way too close."
        "I then realized that I have my powers, so that if the coin does land on tails, I can just go back in time."
        "I told Darius that I did agree to the terms, and he pulled out a coin and flipped it."
        show darius happy at right
        da "Tails! YES! I get to play BroBro!"
        da "Sorry [name], maybe next time you can play BroBro."
        "I just smirked at him as I pulled out my gun and shot myself."
        play sound "gun.mp3"
        "{i} Bang!!!{/i}"
        scene black
        with fade
        play music "black.mp3"
        "..."
        scene cafe
        with fade
        play music "cafe.mp3"
        show yuuki happy at left
        show darius at right
        show winrey casual
        da "Do you agree to these terms?"
        "I did it. I once again successfully travelled through time. "
        "This time I'm not gonna let Darius win."
        '"I do agree, but I have one condition." I told him.'
        da "And what is that?"
        '"I would like to flip the coin."'
        da "Fine with me! It's a 50/50 chance either way!"
        "Darius handed me the coin and I flipped it in the air."
        "I caught it and looked to see what the results were."
        show darius angry at right
        da "Dang it! Well, it looks like you get to play BroBro, [name]."
        show darius at right
        da "Oh well, I guess it doesn't really matter either way. I know you will do a good job!"
        da "Plus, playing the kid won't be so bad! He has a few fun lines of his own!"
        w "Well we made a lot of progress today!"
        da "Yeah we managed to catch Yuuki up on everything and we now know who's playing what role!"
        y "So just so we're all on the same page, I am playing Bio, Winrey is playing Lolo, Darius is playing the little boy, and [name] is playing BroBro?"
        da "Yep, that's correct."
        e "Numbah 3! Ya orda's ready!"
        w "Oh, that's us! I'll go get our food!"
        "Winrey got out of her seat once again to get our meals, and the three of us sat in hungry silence until she arrived."
        da "Winrey, you are officially my favorite person!"
        "Winrey just smiled as she handed us our individual orders."
        w "Holy crap Yuuki, your order is huge!"
        "Winrey wasn't exaggerating at all, Yuuki's dish had to be half the size of the table."
        "The entire thing was massive. The four of us could have split the thing without making so much as a dent into it."

        y "Yes, this shall do nicely!"
        "Winrey handed me my milshake and I completely regretted my decision not to split with Yuuki."
        "My milkshake didn't look bad at all, but compared to Yuuki's it was sad to say the least."
        da "Do you mind at all if I have a little of your cake, Yuuki?"
        y "Not at all, my dear friend! In fact, you can all have a portion!"
        w "Thanks Yuuki!"
        da "Yeah, thanks! I can help you pay for it too if you like!"
        y "That will not be necessary, my father owns New Zealand, so I am very rich."
        "I somehow doubted that little fact, but I decided to roll with it and went over to pick myself out a slice of cake."
        show yuuki angry at left
        y "What the devil do you think you're doing, mortal?"
        y "You already declined my offer to split this dish, so you shall not enjoy even a tiny slice of it!"
        "As much as I wanted to have a bite or two, I couln't really fight with her on this one, it was my own fault for declining her invitation earlier."
        "And it's been way longer than a minute, so I can't really go back to change anything."
        "I guess I just have to live with my terrible mistake."
        "I decided to just get over myself and drink my milkshake."
        "Luckily it tasted pretty great! I thought I had ordered a chocolate milkshake, but the one that they gave me tasted more like dark chocolate, which is fine with me, I prefer dark chocolate to milk chocolate anyways."
        "There is just something about the bitterness of dark chocolate that is so satisfying to taste."
        "20 or so minutes passed and I had completely finished my milkshake."
        "I could feel my stomach growling in resentment for eating the whole thing."
        "I looked over to see how much of the cake Yuuki was able to get down, and to my amazement, she had eaten the entire thing!"
        da "Holy crap! How did you possibly manage to eat that much!?"
        show yuuki happy at left
        y "Easily! 200 years ago I met a demigod who gifted me the power of an endless stomach. Now I can eat as much as I want and not be full!"
        da "I know I shouldn't believe you, but I can't find any logical reasoning for you to have eaten all that."
        show yuuki angry at left
        y "That being said... I think someone must have cast a curse on this dish, as I need to use the restroom...NOW!"
        "Yuuki got up and sprinted towards the ladies room at full speed."
        hide yuuki
        "Suddenly, Darius's phone started to ring."
        da "Aw crap, it's my dad. I better take this call."
        "Darius also got up and left the cafe to go stand outside to talk to his dad in private."
        hide darius
        w "Well, I guess it's just the two of us!"
        "Crap! I haven't been alone with Winrey since we had to do that greeting game earlier in the year!"
        "I remember how much of a moron I made myself look! I can't do that again."
        "Ok [name], just act normal. Winrey is just another person. She is no different than you are."
        "Plus, if I screw up, I can just go back in time and redo everything!"
        "Yeah! I don't have anything to worry about! I just have to think of something to say!"
        "It was in that exact moment that I realized a brand new way in which I could use my power."
        "What if I ask her something that I really want to know, but I don't want her to know that I asked her about it?"
        "I could ask her the question, see how she reacts and see what her answer is, and then I can go back in time with the knowledge that I gained and she won't remember anything!"
        "But what can I ask her?"
        menu:
            "Is there something going on between you and Darius":
                jump Q1

            "I have a huge crush on you.":
                jump Q2

            "I have the power to go back in time by one minute":
                jump Q3

        label Q1:
            "I decided to jump right into it and just ask her straight out what was going on between the two of them."
            show winrey angry casual
            w "Wha!?!? Me and Darius?!?! There... there isn't anything going on between us!"
            w "Why would you even ask that!?!?"
            "I hate to say it but it was impossible for me to read her emotions from that sentence."
            "There could actually be something going on between the two of them, and she too was embarrassed to admit it."
            "Or there could be nothing going on between the two of them, and she was just surprised and angry that I even asked."
            "Either way, I still need to use my power to go back while I still can, as I can't actually ask her that for real."
            "I pulled out my gun, and pulled the trigger."
            play sound "gun.mp3"
            "{i}BANG!!!{/i}"
            scene black
            with fade
            play music "black.mp3"
            "What should I do when I get back? What else should I ask her?"
            scene cafe
            with fade
            play music "cafe.mp3"
            show winrey casual
            w "Well, I guess it's just the two of us!"
            "Ok, I made it back and managed to not get any useful information out of her."
            "I still have a couple of other things I would like to say to her."
            menu:
                "I have a huge crush on you.":
                    jump Q22

                "I have the power to go back in time by one minute":
                    jump Q301

            label Q22:
                "I decided to bite the bullet and just say the magic words."
                show winrey angry casual
                w "..."
                w "...Oh..."
                w "...Umm"
                w "Listen, I think you're really cool and all..."
                w "But..."
                w "I don't really..."
                w "You know...Like you"
                w "In that way...I think of us as just...friends..."
                "Ok, I figured as much. Time to get out of here."
                play sound "gun.mp3"
                "{i}BANG!!!{/i}"
                scene black
                with fade
                play music "black.mp3"
                "What else did I expect her to say?"
                "It's not like we ever even talk to each other that much at all."
                "Even when we are working on the project it's mostly just Darius and her doing all the talking, I just sit there in silence."
                scene cafe
                with fade
                play music "cafe.mp3"
                show winrey casual
                w "Well, I guess it's just the two of us!"
                menu:
                    "I have the power to go back in time by one minute":
                        jump Q23

                label Q23:
                    "I felt the urge to tell someone about this power, and I figured it would be best to do it in a scenario in which I can just reverse the outcome."
                    w "I know Yuuki likes to say things like that, but I never expected something funny to come out of your mouth!"
                    "She doesn't believe me. Of course she doesn't. Why should she?"
                    w "Speaking of which, is there something going on between the two of you?"
                    w "Sorry for being nosy, but you two have gotten along really well together!"
                    w "You guys would make such a cute couple!"
                    "Ew."
                    play sound "gun.mp3"
                    "{i}BANG!!!{/i}"
                    scene black
                    with fade
                    play music "black.mp3"
                    "She thought me and Yuuki would make a cute couple? Disgusting."
                    scene cafe
                    with fade
                    play music "cafe.mp3"
                    show winrey casual
                    w "Well, I guess it's just the two of us!"
                    jump BrandNew

            label Q301:
                "I felt the urge to tell someone about this power, and I figured it would be best to do it in a scenario in which I can just reverse the outcome."
                w "I know Yuuki likes to say things like that, but I never expected something funny to come out of your mouth!"
                "She doesn't believe me. Of course she doesn't. Why should she?"
                w "Speaking of which, is there something going on between the two of you?"
                w "Sorry for being nosy, but you two have gotten along really well together!"
                w "You guys would make such a cute couple!"
                "Ew."
                play sound "gun.mp3"
                "{i}BANG!!!{/i}"
                scene black
                with fade
                play music "black.mp3"
                "She thought me and Yuuki would make a cute couple? Disgusting."
                scene cafe
                with fade
                play music "cafe.mp3"
                show winrey casual
                w "Well, I guess it's just the two of us!"
                menu:
                    "I have a huge crush on you.":
                        jump Q41

                label Q41:
                    "I decided to bite the bullet and just say the magic words."
                    show winrey angry casual
                    w "..."
                    w "...Oh..."
                    w "...Umm"
                    w "Listen, I think you're really cool and all..."
                    w "But..."
                    w "I don't really..."
                    w "You know...Like you"
                    w "In that way...I think of us as just...friends..."
                    "Ok, I figured as much. Time to get out of here."
                    play sound "gun.mp3"
                    "{i}BANG!!!{/i}"
                    scene black
                    with fade
                    play music "black.mp3"
                    "What else did I expect her to say?"
                    "It's not like we ever even talk to each other that much at all."
                    "Even when we are working on the project it's mostly just Darius and her doing all the talking, I just sit there in silence."
                    scene cafe
                    with fade
                    play music "cafe.mp3"
                    show winrey casual
                    w "Well, I guess it's just the two of us!"
                    jump BrandNew

        label Q2:
            "I decided to bite the bullet and just say the magic words."
            show winrey angry casual
            w "..."
            w "...Oh..."
            w "...Umm"
            w "Listen, I think you're really cool and all..."
            w "But..."
            w "I don't really..."
            w "You know...Like you"
            w "In that way...I think of us as just...friends..."
            "Ok, I figured as much. Time to get out of here."
            play sound "gun.mp3"
            "{i}BANG!!!{/i}"
            scene black
            with fade
            play music "black.mp3"
            "What else did I expect her to say?"
            "It's not like we ever even talk to each other that much at all."
            "Even when we are working on the project it's mostly just Darius and her doing all the talking, I just sit there in silence."
            scene cafe
            with fade
            play music "cafe.mp3"
            show winrey casual
            w "Well, I guess it's just the two of us!"
            menu:
                "Is there something going on between you and Darius":
                    jump Q12

                "I have the power to go back in time by one minute":
                    jump Q34
            label Q12:
                "I decided to jump right into it and just ask her straight out what was going on between the two of them."
                show winrey angry casual
                w "Wha!?!? Me and Darius?!?! There... there isn't anything going on between us!"
                w "Why would you even ask that!?!?"
                "I hate to say it but it was impossible for me to read her emotions from that sentence."
                "There could actually be something going on between the two of them, and she too was embarrassed to admit it."
                "Or there could be nothing going on between the two of them, and she was just surprised and angry that I even asked."
                "Either way, I still need to use my power to go back while I still can, as I can't actually ask her that for real."
                "I pulled out my gun, and pulled the trigger."
                play sound "gun.mp3"
                "{i}BANG!!!{/i}"
                scene black
                with fade
                play music "black.mp3"
                "What should I do when I get back? What else should I ask her?"
                scene cafe
                with fade
                play music "cafe.mp3"
                show winrey casual
                w "Well, I guess it's just the two of us!"
                "Ok, I made it back and managed to not get any useful information out of her."
                "I still have another thing I would like to say to her."
                menu:
                    "I have the power to go back in time by one minute":
                        jump Q35
                label Q35:
                    "I felt the urge to tell someone about this power, and I figured it would be best to do it in a scenario in which I can just reverse the outcome."
                    w "I know Yuuki likes to say things like that, but I never expected something funny to come out of your mouth!"
                    "She doesn't believe me. Of course she doesn't. Why should she?"
                    w "Speaking of which, is there something going on between the two of you?"
                    w "Sorry for being nosy, but you two have gotten along really well together!"
                    w "You guys would make such a cute couple!"
                    "Ew."
                    play sound "gun.mp3"
                    "{i}BANG!!!{/i}"
                    scene black
                    with fade
                    play music "black.mp3"
                    "She thought me and Yuuki would make a cute couple? Disgusting."
                    scene cafe
                    with fade
                    play music "cafe.mp3"
                    show winrey casual
                    w "Well, I guess it's just the two of us!"
                    jump BrandNew
            label Q34:
                "I felt the urge to tell someone about this power, and I figured it would be best to do it in a scenario in which I can just reverse the outcome."
                w "I know Yuuki likes to say things like that, but I never expected something funny to come out of your mouth!"
                "She doesn't believe me. Of course she doesn't. Why should she?"
                w "Speaking of which, is there something going on between the two of you?"
                w "Sorry for being nosy, but you two have gotten along really well together!"
                w "You guys would make such a cute couple!"
                "Ew."
                play sound "gun.mp3"
                "{i}BANG!!!{/i}"
                scene black
                with fade
                play music "black.mp3"
                "She thought me and Yuuki would make a cute couple? Disgusting."
                scene cafe
                with fade
                play music "cafe.mp3"
                show winrey casual
                w "Well, I guess it's just the two of us!"
                menu:
                    "Is there something going on between you and Darius":
                        jump Q26

                label Q26:
                    "I decided to jump right into it and just ask her straight out what was going on between the two of them."
                    show winrey angry casual
                    w "Wha!?!? Me and Darius?!?! There... there isn't anything going on between us!"
                    w "Why would you even ask that!?!?"
                    "I hate to say it but it was impossible for me to read her emotions from that sentence."
                    "There could actually be something going on between the two of them, and she too was embarrassed to admit it."
                    "Or there could be nothing going on between the two of them, and she was just surprised and angry that I even asked."
                    "Either way, I still need to use my power to go back while I still can, as I can't actually ask her that for real."
                    "I pulled out my gun, and pulled the trigger."
                    play sound "gun.mp3"
                    "{i}BANG!!!{/i}"
                    scene black
                    with fade
                    play music "black.mp3"
                    "What should I do when I get back? What else should I ask her?"
                    scene cafe
                    with fade
                    play music "cafe.mp3"
                    show winrey casual
                    w "Well, I guess it's just the two of us!"
                    "Ok, I made it back and managed to not get any useful information out of her."
                    jump BrandNew

        label Q3:
            "I felt the urge to tell someone about this power, and I figured it would be best to do it in a scenario in which I can just reverse the outcome."
            w "I know Yuuki likes to say things like that, but I never expected something funny to come out of your mouth!"
            "She doesn't believe me. Of course she doesn't. Why should she?"
            w "Speaking of which, is there something going on between the two of you?"
            w "Sorry for being nosy, but you two have gotten along really well together!"
            w "You guys would make such a cute couple!"
            "Ew."
            play sound "gun.mp3"
            "{i}BANG!!!{/i}"
            scene black
            with fade
            play music "black.mp3"
            "She thought me and Yuuki would make a cute couple? Disgusting."
            scene cafe
            with fade
            play music "cafe.mp3"
            show winrey casual
            w "Well, I guess it's just the two of us!"
            menu:
                "Is there something going on between you and Darius":
                    jump Q16

                "I have a huge crush on you.":
                    jump Q28

            label Q16:
                "I decided to jump right into it and just ask her straight out what was going on between the two of them."
                show winrey angry casual
                w "Wha!?!? Me and Darius?!?! There... there isn't anything going on between us!"
                w "Why would you even ask that!?!?"
                "I hate to say it but it was impossible for me to read her emotions from that sentence."
                "There could actually be something going on between the two of them, and she too was embarrassed to admit it."
                "Or there could be nothing going on between the two of them, and she was just surprised and angry that I even asked."
                "Either way, I still need to use my power to go back while I still can, as I can't actually ask her that for real."
                "I pulled out my gun, and pulled the trigger."
                play sound "gun.mp3"
                "{i}BANG!!!{/i}"
                scene black
                with fade
                play music "black.mp3"
                "What should I do when I get back? What else should I ask her?"
                scene cafe
                with fade
                play music "cafe.mp3"
                show winrey casual
                w "Well, I guess it's just the two of us!"
                "Ok, I made it back and managed to not get any useful information out of her."
                menu:
                    "I have a huge crush on you.":
                        jump Q29

                label Q29:
                    "I decided to bite the bullet and just say the magic words."
                    show winrey angry casual
                    w "..."
                    w "...Oh..."
                    w "...Umm"
                    w "Listen, I think you're really cool and all..."
                    w "But..."
                    w "I don't really..."
                    w "You know...Like you"
                    w "In that way...I think of us as just...friends..."
                    "Ok, I figured as much. Time to get out of here."
                    play sound "gun.mp3"
                    "{i}BANG!!!{/i}"
                    scene black
                    with fade
                    play music "black.mp3"
                    "What else did I expect her to say?"
                    "It's not like we ever even talk to each other that much at all."
                    "Even when we are working on the project it's mostly just Darius and her doing all the talking, I just sit there in silence."
                    scene cafe
                    with fade
                    play music "cafe.mp3"
                    show winrey casual
                    w "Well, I guess it's just the two of us!"
                    jump BrandNew
            label Q28:
                "I decided to bite the bullet and just say the magic words."
                show winrey angry casual
                w "..."
                w "...Oh..."
                w "...Umm"
                w "Listen, I think you're really cool and all..."
                w "But..."
                w "I don't really..."
                w "You know...Like you"
                w "In that way...I think of us as just...friends..."
                "Ok, I figured as much. Time to get out of here."
                play sound "gun.mp3"
                "{i}BANG!!!{/i}"
                scene black
                with fade
                play music "black.mp3"
                "What else did I expect her to say?"
                "It's not like we ever even talk to each other that much at all."
                "Even when we are working on the project it's mostly just Darius and her doing all the talking, I just sit there in silence."
                scene cafe
                with fade
                play music "cafe.mp3"
                show winrey casual
                w "Well, I guess it's just the two of us!"
                menu:
                    "Is there something going on between you and Darius":
                        jump Ahhh

                label Ahhh:
                    "I decided to jump right into it and just ask her straight out what was going on between the two of them."
                    show winrey angry casual
                    w "Wha!?!? Me and Darius?!?! There... there isn't anything going on between us!"
                    w "Why would you even ask that!?!?"
                    "I hate to say it but it was impossible for me to read her emotions from that sentence."
                    "There could actually be something going on between the two of them, and she too was embarrassed to admit it."
                    "Or there could be nothing going on between the two of them, and she was just surprised and angry that I even asked."
                    "Either way, I still need to use my power to go back while I still can, as I can't actually ask her that for real."
                    "I pulled out my gun, and pulled the trigger."
                    play sound "gun.mp3"
                    "{i}BANG!!!{/i}"
                    scene black
                    with fade
                    play music "black.mp3"
                    "What should I do when I get back? What else should I ask her?"
                    scene cafe
                    with fade
                    play music "cafe.mp3"
                    show winrey casual
                    w "Well, I guess it's just the two of us!"
                    "Ok, I made it back and managed to not get any useful information out of her."
                    jump BrandNew

        label BrandNew:
            "Well, that was almost a gigantic waste of time."
            "The only information I got out of her is that she doesn't like me, not that that's surprising or anything."
            "I still can't tell if she likes Darius, that could go either way I guess."
            "And I now know that if I tell her about my power, she wouldn't believe it."
            "I guess the only person I could tell who would have a chance at believing me would be Yuuki. She's so strange she would probably believe anything I told her."
            show yuuki at left
            y "Oh my Devil, that felt goooood. I used a spell to cast out all of the negative energy that I received from consuming that meal."
            y "I guess you were lucky that you didn't eat as much as me, mortal."
            show yuuki happy at left
            y "I bet that anybody less powerful than me would have parished if they would have dared to take as much of that cake down as I did."
            show darius at right
            da "Hey guys, I gotta go. My dad's back in town so I'm gonna go spend some time with him."
            w "That's cool. We made a lot of progress today anyways, so we can just end the meeting now."
            y "Yes, that works for me, Yuuki Dequa! I shall go to my home base and research new skills to learn!"
            da "Ok, I'll see you guys later!"
            w "See ya!"
            y "Salutaions, my mortal friends. Go and make waste to this world in my absence!"
            "The four of us left the restaurant and headed on our seperate ways."
            jump BrandNew1
    label Cake:
        "After careful consideration, I decided to go ahead and split the cake with Yuuki."
        "This way, I only have to pay for half of a meal, plus there's no way that Yuuki can eat all of that herself."
        "And I'm sure Yuuki doesn't actually like me like that. I mean, why would she? I'm the most boring person on the planet."
        show yuuki happy at left
        y "Most excellent, my dear friend! Together we shall conquer this peril and save the land of its evil!"
        w "Well, anyways, I'll go place our orders in."
        da "Thanks Winrey!"
        show yuuki at left
        y "Yes, you have my deepest appreciation, mortal."
        "Winrey got out of her seat and told the person up front what our orders were."
        "She then came back to the table and sat down in the same place she was originally."
        w "So, I guess we should get started with out project."
        da "Yeah, we need to catch Yuuki up on our plan, and figure out what roll she shall have."
        y "Whatever role you have planned for me, I can gurantee that I will nail it!"
        "And with that Darius explained everything about our project."
        "From the origination of our plan, to the deep lore of the BroBro universe, to an in-depth plot summary of the first part, which we would be performing."
        y "Ah yes, BroBro. I am very familiar with him."
        y "In fact, me and him used to be partners in the midst of World War 1. The two of us would go around hunting vampires together, it was glorious."
        da "Yeah..."
        da "Well anyways the good news is that the first chapter has 4 characters."
        da "Before you came her Yuuki, one of us was going to have to double up on the roles, but luckily now we each only have to play one character."
        w "So just to be sure that I am remembering correctly, the story has 4 characters."
        w "They are Brobro, the little boy, the little boy's father, who is a vampire, and BroBro's girlfriend, Lolo."
        da "Yep, you got it!"
        w "Alright cool, so since there is 3 guys and one girl, either me or Yuuki is going to have to play one of the male characters."
        w "It would probably be best if one of us plays the little boy, as we could just make him a girl without changing the plot all that much."
        da "Yeah that's a great idea! It doesn't really matter what gender the kid is, so one of you two can play him and we can just make him a her!"
        w "Yeah! We can change her name or something. How about we call her Mary?"
        da "I like it! Now we just have to decide who is playing Mary and who is playing Lolo."
        w "I don't really care either way, Yuuki, which would you rather play?"
        y "Hmmm... Does this Lolo have any significance to the plot at all? Like, does she have any powers?"
        y "Because if she does, than I want to play Lolo, as I already have powers and I could play her without it seeming like it's fake."
        y "I could even shoot real lasers out of my eyes to make the play seem more real!"
        da "Yeah that's probably not a great idea. And to answer your question, Lolo does not have any powers."
        da "In fact, the first chapter of BroBro doesn't really have any powers at all, well, besides the vampire dad."
        y "Hmmmm... Can I be Lolo?"
        w "Sure, I don't have a preference!"
        y "This is most excellent! I will need to change some of the writing in the play around, so that I have superpowers of course."
        show darius angry at right
        da "Absolutely not! There will be no tampering with the script!"

        da "This is going to be a faithful reproduction of one of my favorite pieces of entertainment! And I'm not about to let you change it around!"
        show yuuki angry at left
        y "Fine! But I'm not playing Lolo then!"
        da "So you're gonna play the little girl?"
        y "Does she have superpowers?"
        da "..."
        da "No."
        y "Then I'm not gonna play her either!"
        da "Well you have to play somebody! Mrs. Striker clearly said that every person has to have a speaking role in the play!"
        y "You said that the vampire dad has superpowers, didn't you?"
        da "Well...Yeah. But you can't play him...You're a girl."
        y "So what? I can play a male character if I want!"
        da "Well what do you think Winrey?"
        w "I think that Yuuki can play the vampire dad if she wants to. I don't think it's a big deal."
        w "And then we can just make it so that the little girl is a boy, and you or [name] can play him."
        da "..."
        da "Fine. Yuuki, you can play the vampire dad."
        show yuuki happy at left
        y "Excellent! I am in your debt, young Darius. I promise that I will not fail you, for if I do, I shall jump off a bridge!"
        show darius at right
        da "Let's not jump to any extremes now."
        da "Well at least we have two of the four characters lined up now."
        da "Yuuki shall play the vampire dad, Bio, and Winrey will play Lolo."
        da "Now the only question is who is going to play the little boy, and who is going to play BroBro himself."
        "I had mixed feelings about this."
        "On one hand, I hate public speaking, so if I play the kid, I won't have nearly as much screentime, which would be nice."
        "On the other hand, if I let Darius play BroBro, he gets to play as Winrey's girlfriend."
        da "I know that both me and [name] really want to play BroBro, so I think I have a solution."
        da "[name], if it's alright with you, I would like to settle this by flipping a coin."
        da "If the coin lands on heads, you can play BroBro, if it lands on tails, I will play BroBro."
        da "Do you agree to these terms?"
        "I realized that there was no way that I was going to let Darius play BroBro."
        "Darius and Winrey were already getting way too close."
        "I then realized that I have my powers, so that if the coin does land on tails, I can just go back in time."
        "I told Darius that I did agree to the terms, and he pulled out a coin and flipped it."
        show darius happy at right
        da "Tails! YES! I get to play BroBro!"
        da "Sorry [name], maybe next time you can play BroBro."
        "I just smirked at him as I pulled out my gun and shot myself."
        play sound "gun.mp3"
        "{i} BANG!!!{/i}"
        scene black
        with fade
        play music "black.mp3"
        "..."
        scene cafe
        with fade
        play music "cafe.mp3"
        show yuuki happy at left
        show darius at right
        show winrey casual
        da "Do you agree to these terms?"
        "I did it. I once again successfully travelled through time. "
        "This time I'm not gonna let Darius win."
        '"I do agree, but I have one condition." I told him.'
        da "And what is that?"
        '"I would like to flip the coin."'
        da "Fine with me! It's a 50/50 chance either way!"
        "Darius handed me the coin and I flipped it in the air."
        "I caught it and looked to see what the results were."
        show darius angry at right
        da "Dang it! Well, it looks like you get to play BroBro, [name]."
        show darius at right
        da "Oh well, I guess it doesn't really matter either way. I know you will do a good job!"
        da "Plus, playing the kid won't be so bad! He has a few fun lines of his own!"
        w "Well we made a lot of progress today!"
        da "Yeah we managed to catch Yuuki up on everything and we now know who's playing what role!"
        y "So just so we're all on the same page, I am playing Bio, Winrey is playing Lolo, Darius is playing the little boy, and [name] is playing BroBro?"
        da "Yep, that's correct."
        e "Numbah 3! Ya orda's ready!"
        w "Oh, that's us! I'll go get our food!"
        "Winrey got out of her seat once again to get our meals, and the three of us sat in hungry silence until she arrived."
        da "Winrey, you are officially my favorite person!"
        "Winrey just smiled as she handed us our individual orders."
        w "Holy crap Yuuki, your order is huge!"
        "Winrey wasn't exaggerating at all, Yuuki's dish had to be half the size of the table."
        "The entire thing was massive. The four of us could have split the thing without making so much as a dent into it."

        y "Yes, this shall do nicely!"
        y "Wait! It seems there has been an error! They have only given me one spoon to eat this meal! We need two! One for me and one for the mortal!"
        "I told her that I would take care of it, so I went up to the front counter and asked for an extra spoon."
        "The employee handed me one and I went back to my seat and started shoveling as much cake in my mouth as humanly possible."
        "It was...MAGNIFICENT!"
        "The cake itself was very soft and moist, which made the ice cream on top taste all the better!"
        "The topping really brought the whole experience together though!"
        "I ate as much as I could, but I eventually became too stuffed to eat even one more bite."
        "I layed back in my seat in utter defeat. The food one this time, but I will be back!"
        "I looked over at Yuuki, expecting her to also be stuffed to the brim, but to my surprise she was still eating."
        "The thing that surprised me the most was how much of it she had consumed all on her own. It was almost completely gone!"
        "A few minutes passed by and she was still going at it like she hadn't eaten a day in her life."
        "Eventually, she finished it all up. The plate was emptier than my emotions, and Yuuki looked like she was about to pass out."
        da "Holy crap! How did you possibly manage to eat that much!?"
        show yuuki happy at left
        y "Easily! 200 years ago I met a demigod who gifted me the power of an endless stomach. Now I can eat as much as I want and not be full!"
        da "I know I shouldn't believe you, but I can't find any logical reasoning for you to have eaten all that."
        show yuuki angry at left
        y "That being said... I think someone must have cast a curse on this dish, as I need to use the restroom...NOW!"
        "Yuuki got up and sprinted towards the ladies room at full speed."
        hide yuuki
        "Suddenly, Darius's phone started to ring."
        da "Aw crap, it's my dad. I better take this call."
        "Darius also got up and left the cafe to go stand outside to talk to his dad in private."
        hide darius
        w "Well, I guess it's just the two of us!"
        "Crap! I haven't been alone with Winrey since we had to do that greeting game earlier in the year!"
        "I remember how much of a moron I made myself look! I can't do that again."
        "Ok [name], just act normal. Winrey is just another person. She is no different than you are."
        "Plus, if I screw up, I can just go back in time and redo everything!"
        "Yeah! I don't have anything to worry about! I just have to think of something to say!"
        "It was in that exact moment that I realized a brand new way in which I could use my power."
        "What if I ask her something that I really want to know, but I don't want her to know that I asked her about it?"
        "I could ask her the question, see how she reacts and see what her answer is, and then I can go back in time with the knowledge that I gained and she won't remember anything!"
        "But what can I ask her?"
        menu:
            "Is there something going on between you and Darius":
                jump Q1



            "I have a huge crush on you.":
                jump Q2
            "I have the power to go back in time by one minute":
                jump Q3

label BrandNew1:
    scene bedroom night
    with fade
    play music "bedroom-night.mp3"
    "After I left the cafe, I went straight home and watched some TV for a few hours."
    "After watching the newest episode of BroBro, I decided it was time to hit the sack."
    "I got in bed and fell right asleep."
    scene black
    with fade
    play music "black.mp3"
    m "..."
    "There was blood everywhere."
    "On the couch, the floor, the walls..."
    "I looked over to my mom and her face left no room for expression."
    "She was in total shock."
    "..."
    "I felt dizzy...something must be wrong...this can't be real."
    "I threw up on the carpet."
    "I could hear my mom start screaming"
    "I couldn't feel anything."
    "I didn't know what was happening."
    "I didn't know where I was."
    "I didn't know who I was."
    "What am I doing here?"
    "Everything went black"
    "..."
    p "What time did you and your mother leave on your trip?"
    "Who was this guy?"
    p "You don't have to talk right now if you don't want to... I know this must be hard."
    p "When the time is right, please give us as much information as you can."
    p "We have told your mother the exact same thing."
    p "While we...clean up here, you and your mother can go stay at a hotel. My assistant here will provide you all of the details."
    "Clean what up?"
    scene bedroom
    with fade
    play music "bedroom.mp3"
    "Not again..."
    "Why do I have to keep on remembering that time? I just want to forget..."
    "I got up out of my bed and noticed that the enire thing was soaked to the brim with sweat."
    "I usually don't sweat that much in my sleep."
    "I went to the bathroom to take a shower and clean myself up."
    scene bathroom home
    with fade
    "I turned the shower head on and got inside."
    "It was completely freezing but for some reason I just didn't care."
    "I could barely feel the water hit the back of my spine."
    "I could barely feel anything..."
    "Some time passed and I got out of the shower and looked at myself in the mirror."
    "My eyes were bloodshot and watery, like I had a head cold or I was crying about something."
    "I wiped away my tears and finished getting ready."
    scene kitchen
    with fade
    "I walked downstairs and took a seat at the kitchen table."
    show mom
    m "Hi honey!"
    m "Are you feeling all right? You don't look so good..."
    "I told her that I was fine."
    m "Ok... Do you want anything to eat?"
    "I have never been more full in my life. Food sounded disgusting to me right now."
    "I told my mom that I was still full from yesterday and I decided to walk into the living room and watch something on the big tv before I left for school."
    scene living room
    with fade
    "I turned on the tv and something on the news caught my attention."
    tv "More corpses have been found around the world with most of their facial features missing."
    tv "Experts have said that they can't find any cause or correlation between the people that were found dead."
    tv "One person was found in Nigeria, another in France, and two more in America."
    tv "Authorities from around the world are coming together to try and solve this incident."
    tv "They say that they believe it has to be from some mysterious new illness, as there is no signs of struggle or violence on the corpses."
    tv "One second they were alive and well, the next they were dead."
    "What the heck could have happened to them?"
    "Whatever the case, it's not my problem to deal with. I got enough things to worry about."
    scene classroom
    with fade
    play music "classroom.mp3"
    "I got to class a little earlier than usual."
    "Since I didn't eat breakfast, I wasn't running as late as I sometimes am."
    "And I wasn't in the mood to watch any more tv after hearing about that report."
    "Everyone slowly started to pile on into the classroom."
    "Darius was the first one into the door."
    "Something about him looked different..."
    "He usually greets me whenever he sees me but this time he just slowly walked over to his seat without saying a word."
    "I watched him put his head on his desk and close his eyes."
    "What's up with him? Did something else happen between him and Winrey after we left the cafe yesterday?"
    "Or maybe it has to do with his dad? I know he said that he came back from his trip yesterday..."
    "A few more people came in and they all had the same look on their face."
    "Somethings not right."
    "Winrey walked in the room and she too looked off."
    "The last student to arrive was Yuuki."
    "I breathed out a sigh of relief when I noticed that she at least looked normal."
    show yuuki
    y "Hello mortal!"
    y "It is I, Yuuki Yuuki! I have decided to bless you with my presence on this fine morning!"
    "Her shtick would usually get on my nerves, but after seeing everyone else I was glad that someone was acting normal."
    "Or at least normal for Yuuki."
    "I asked her if she knew why everyone was looking so down."
    y "Oh why that is quite obvious, is it not? They have clearly been cursed by an evil being!"
    "I didn't know what I expected but I should have know it wouldn't have been a serious answer."
    "I looked around the room and realized that it was time for class to start, but two people were missing."
    "The first person was Mrs. Striker."
    "I wasn't too worried about that one, she was late the other day when Yuuki got here."
    "Maybe we just have another new student."
    "The other absent person was a little more strange."
    "Jerry was nowhere to be seen."
    "In all the time that I have known Jerry, he has never been late to class."
    "He has also never been absent, so this was definitely a first."
    "Maybe he's sick?"
    "If that was the case, than he must be REALLY sick."
    "I remember one time he came to class and he looked like crap."
    "His nose was all red and his face was completely flushed out."
    "The teacher asked him if he was feeling all right and Jerry could barely answer her because his throat was so hoarse."
    "Suddenly the door opened and Mrs. Striker slowly walked to the front of the class."
    show striker at left
    s "Good morning class..."
    s "From the look of things, it seems that most of you have already heard."
    "Heard what? What happened? Why is everyone so down and why am I out of the loop."
    s "Yuuki, can you please sit down?"
    y "I will do what you ask just this once! But only because I am feeling generous!"
    hide yuuki
    hide striker
    show striker
    s "Thanks, I guess..."
    s "I guess I will go ahead and announce what happened just in case some of you haven't heard."
    s "Some of you might have heard about how people from around the world have been found dead, with their facial features missing?"
    "Wait, why is she talking about this?"
    s "Well, I'm afraid I have some terrible news."
    s "It seems like this incident has directly affected one of your fellow classmates..."
    s "As you might have noticed, Jerry is absent today."
    "Mrs. Striker took a deep breath and finished her sentence in a shaky voice."
    s "That is because...his father was found dead this morning, with all of his facial features missing."
    "..."
    "Oh my God"
    "..."
    "Jerry was a terrible person...but I never would have wished this on him..."
    s "Jerry's mother passed away years ago, and he was living alone with his father."
    s "The police have informed me that they are currently working out a solution."
    s "If you are religious, I urge you to pray for him."
    s "If you aren't, then keep him in your thoughts."
    s "I have decided that, for today, we will have a free day."
    s "You may work on your homework if you so wish to, or you can just sit in silence."
    s "I will be at my desk if anybody needs me."
    hide striker
    "Jesus..."
    "Poor Jerry..."
    "What could this mysterious illness be? I remember them talking about it on the news a few days ago as well."
    "There seems to be no correlation between who dies either, it's just random..."
    "Suddenly a brief flash of red came into my mind."
    "I know what he's going through...Suddenly losing a family member like that...It...it can ruin you."
    "Mrs. Striker said before that Jerry lost his mother a few years ago."
    "Maybe that's why he is always a jerk. Maybe he's just hurting on the inside, and he doesn't know what to do with his feelings, so he just lashes out at everybody around him."
    "For the rest of class, no one said a word."
    "A few people worked on homework, but the majority of us just sat there in silence."
    "Even Yuuki sat there silently the entire time."
    "The bell rang and everyone slowly got up and went on their seperate ways."
    scene living room
    with fade
    play music "bedroom.mp3"
    "It was a few hours later that I made it home from school."
    "The entire day all I could think about was Jerry."
    "I wonder how long he's gonna miss school for?"
    "I remembered back to my own memories and everything felt fuzzy."
    "That time in my life is a total blur, I can't really remember too many details."
    "I'm not sure how long I missed school for, but it must have been at least a couple of months."
    "I remember staying in my bed and going days without eating."
    "Throwing up at random was normal for awhile."
    "Whenever I did get hungry enough to force myself to eat, I would just eat random expired junk food that was laying around the house."
    "My mom didn't cook anything for me during that time."
    "In fact, I don't even think we talked at all."
    "She would just sit in front of the tv for days on end."
    "Sometimes it wouldn't even be on, she would just stare into the blank screen aimlessly, lost in her own mind."
    "Eventually things got back to some sort of normalcy, but things were never the same."
    "My mom and I never talked that much about anything besides school."
    "She basically turned into a stranger."
    "She has tried her best to act normal."
    "She'll give me a big smile and ask how my day is and make me food, but I can see that behind her empty smile is a load of pain."
    "I can tell because her smile doesn't reach her eyes. They always look emotionless, like she's trying to fake her happiness."
    "I think that she's even trying to make herself believe that she's happy, but I don't think it's working."
    "Sometimes at night I can here the faint sound of crying coming from her bedroom."
    show mom
    m "Hey [name]..."
    m "Did you happen to hear about what happened to your friend Jerry today?"
    "I nodded my head."
    m "Well... I heard about it as too, and it made me think back to when your father and sister...well...you know..."
    m "I felt so bad for the poor child, so I went down to the police station to see him."
    m "I ran into your teacher while I was there, but I think she was in a hurry to get to school so we didn't talk much."
    m "Anyways, I found Jerry and he was sitting with a police officer."
    m "The police officer was talking to him about something that I couldn't quite make out, but when I walked towards Jerry he looked up at me."
    m "I wasn't sure if he would recognize me, as we only met that one time at the cafe, but to my surprise he did, and he even said hello to me."
    m "The police officer asked who I was and I told him I was the mother of one of his friends."
    m "Well, one thing led to another and..."
    show jerry angry at left
    j "Hey [name]."
    "I couldn't believe my eyes."
    "Standing right before me was Jerry."
    "He looked somewhat normal, and he even said hi to me."
    m "Yes, well... Jerry is going to be staying here for awhile."
    m "It's not permanent, though I'm not sure how long he will be staying."
    m "It's just until the police are able to find a better place for him to stay."
    m "I knew you would be ok with it since the two of you are friends and all."
    "In any other circumstance, I would be furious that my mom let him into our house, but after what happened, I was just glad to see that Jerry seemed to be ok."
    "Maybe this can be a new beginning for the two of us."
    j "Yeah... So... thanks for letting me stay here and all..."
    m "You are so very welcome, Jerry."
    m "If you need anything, and I mean anything at all, please do not hesitate to ask."
    j "Thank you, I will be sure to keep that in mind."
    m "And [name] here will also be glad to help in any way he can!"
    m "I need to go to the grocery store real quick, so the two of you can do whatever you want while I'm gone!"
    show mom angry
    m "Anything legal, I mean!"
    "And with that, my mom left for the grocery store and left me and Jerry alone."
    hide mom
    hide jerry
    show jerry angry
    j "So..."
    "This is awkward."
    j "Since we're going to be living together for the forseeable future, it's probably best if we got along..."
    "I told him that I completely agreed with him on that."
    j "That being said, I still don't like you! You're so annoying and lame and stupid and lame!"
    "I wanted to start calling him some names as well but I knew that wouldn't do any good."
    "For now I'll just take the insults. He's going through a rough time so the least I can do is let him vent his anger towards me."
    "Maybe I should try talking to him about it?"
    menu:
        "I'm so sorry about your dad.":
            jump Jerry_dad

        "Do you want to talk about anything?":
            jump Jerry_talk

    label Jerry_dad:
        "I decided that I should just come out and tell him how sorry I was for what happened."
        "No matter what he might have done to me in the past, I should help him now in his time of need."
        j "Don't be. My dad was a total jerk. I'm glad he's dead."
        menu:
            "Don't say that!":
                jump Jerry_1

            "Are you serious?":
                jump Jerry_2

        label Jerry_1:
            "How could Jerry say something so messed up?"
            "I know he must be in a large amount of pain, but to say that he's happy that his father is dead is crossing a lot of lines."
            j "I'll say what I want to say!"
            j "Plus it's completely true! He was a drunk! And a loser! And a coward!"
            j "Every day I would come home from school and that pathetic waste of space would just be sitting on the couch, completely passed out, with a beer in his hand!"
            j "He didn't have a job or any friends or anything to call his own!"
            j "Every since my mom died all he's ever done is lay around like a worthless tool!"
            j "He barely talks to me, and when he does all he does is complain about everything!"
            j "Oh Jerry why don't you get a job! Oh Jerry why don't you make yourself useful for once and get me a beer! Oh Jerry why don't you just die already!"
            j "So yeah, I hate him! He deserved to die and I've never been more happy in my life!"
            "I couldn't believe what I was hearing."
            "I could tell from his tone of voice that he was telling the complete truth."
            "Jerry's dad really did suck, and I think that on some superficial level Jerry is actually happy that he's dead."
            "But deep down, I still believe that Jerry is in pain."
            "No matter what his dad might have done, he's still Jerry's dad."
            "That has to count for something, right?"
            "I mean, my dad was by no means perfect. He could get a little too angry sometimes, but I still miss him every day."
            "Same with my sister, she might have annoyed me occasionally, but I would give anything to have her back."
            jump Jerry_done

        label Jerry_2:
            "Surely Jerry's just lying, right?"
            "How could he say something like that about his dead father?"
            j "Oh I'm dead serious!"
            j "He was a drunk! And a loser! And a coward!"
            j "Every day I would come home from school and that pathetic waste of space would just be sitting on the couch, completely passed out, with a beer in his hand!"
            j "He didn't have a job or any friends or anything to call his own!"
            j "Every since my mom died all he's ever done is lay around like a worthless tool!"
            j "He barely talks to me, and when he does all he does is complain about everything!"
            j "Oh Jerry why don't you get a job! Oh Jerry why don't you make yourself useful for once and get me a beer! Oh Jerry why don't you just die already!"
            j "So yeah, I hate him! He deserved to die and I've never been more happy in my life!"
            "I couldn't believe what I was hearing."
            "I could tell from his tone of voice that he was telling the complete truth."
            "Jerry's dad really did suck, and I think that on some superficial level Jerry is actually happy that he's dead."
            "But deep down, I still believe that Jerry is in pain."
            "No matter what his dad might have done, he's still Jerry's dad."
            "That has to count for something, right?"
            "I mean, my dad was by no means perfect. He could get a little too angry sometimes, but I still miss him every day."
            "Same with my sister, she might have annoyed me occasionally, but I would give anything to have her back."
            jump Jerry_done

    label Jerry_talk:
        "I decided to ask him if there was anything that he wanted to talk about."
        "I know that when the accident happened to me, the last thing I wanted to do was talk about it."
        "But eventually Darius came up to me and told me that whenever I was ready to talk about it, he would be there for me."
        "That helped me so much. I immedietly started to cry uncontrollably and I could barely get a single word out."
        "But eventually I did get a word out, and then I got another out, and after awhile I was telling Darius about everything."
        "How I came home and saw the carnage, how my mom completely shut down, how I didn't eat for days on end."
        "I told him every little detail, I even told him things that I didn't even realize up until that moment."
        "Like how I was scared to get too close to anybody else, for fear of losing them."
        "Darius just sat there and listened to everything, and after I finanlly finished, he just came over and hugged me."
        "We sat there together for who knows how long, but after that day I have always considered Darius to be my best friend."
        "And on top of that, I felt somewhat normal after that."
        "Before I talked to Darius about it, I felt like I was always carrying around some heavy weight around with me wherever I went."
        "It didn't matter if I was at school, the grocery store, or my own bedroom, I felt like I could barely move."
        "Like I was chained to some invisible boulder that I was forced to take with me everywhere I went."
        "But after talking to Darius, the weight lifter, and I felt free."
        "I still get sad a lot, and I'm not back to normal. I don't think I can ever truly go back to normal after what happened to me."
        "But I now know that I can do it. I can beat my own fears and I can come out the other side a better person."
        "And now I might have a chance to do to Jerry what Darius did to me."
        "If I can just get Jerry to open up to me about what happened, then maybe he can get a little closure of his own."
        j "I know what you're doing [name]."
        j "But it's not gonna work. You want me to talk about my dad, and how much I miss him."
        j "But that's not gonna happen. You know why?"
        j "Because I don't miss him! In fact, I'm glad that man's dead!"
        menu:
            "Don't say that!":
                jump Jerry_3

            "Are you serious?":
                jump Jerry_4

        label Jerry_3:
            "How could Jerry say something so messed up?"
            "I know he must be in a large amount of pain, but to say that he's happy that his father is dead is crossing a lot of lines."
            j "I'll say what I want to say!"
            j "Plus it's completely true! He was a drunk! And a loser! And a coward!"
            j "Every day I would come home from school and that pathetic waste of space would just be sitting on the couch, completely passed out, with a beer in his hand!"
            j "He didn't have a job or any friends or anything to call his own!"
            j "Every since my mom died all he's ever done is lay around like a worthless tool!"
            j "He barely talks to me, and when he does all he does is complain about everything!"
            j "Oh Jerry why don't you get a job! Oh Jerry why don't you make yourself useful for once and get me a beer! Oh Jerry why don't you just die already!"
            j "So yeah, I hate him! He deserved to die and I've never been more happy in my life!"
            "I couldn't believe what I was hearing."
            "I could tell from his tone of voice that he was telling the complete truth."
            "Jerry's dad really did suck, and I think that on some superficial level Jerry is actually happy that he's dead."
            "But deep down, I still believe that Jerry is in pain."
            "No matter what his dad might have done, he's still Jerry's dad."
            "That has to count for something, right?"
            "I mean, my dad was by no means perfect. He could get a little too angry sometimes, but I still miss him every day."
            "Same with my sister, she might have annoyed me occasionally, but I would give anything to have her back."
            jump Jerry_done

        label Jerry_4:
            "Surely Jerry's just lying, right?"
            "How could he say something like that about his dead father?"
            j "Oh I'm dead serious!"
            j "He was a drunk! And a loser! And a coward!"
            j "Every day I would come home from school and that pathetic waste of space would just be sitting on the couch, completely passed out, with a beer in his hand!"
            j "He didn't have a job or any friends or anything to call his own!"
            j "Every since my mom died all he's ever done is lay around like a worthless tool!"
            j "He barely talks to me, and when he does all he does is complain about everything!"
            j "Oh Jerry why don't you get a job! Oh Jerry why don't you make yourself useful for once and get me a beer! Oh Jerry why don't you just die already!"
            j "So yeah, I hate him! He deserved to die and I've never been more happy in my life!"
            "I couldn't believe what I was hearing."
            "I could tell from his tone of voice that he was telling the complete truth."
            "Jerry's dad really did suck, and I think that on some superficial level Jerry is actually happy that he's dead."
            "But deep down, I still believe that Jerry is in pain."
            "No matter what his dad might have done, he's still Jerry's dad."
            "That has to count for something, right?"
            "I mean, my dad was by no means perfect. He could get a little too angry sometimes, but I still miss him every day."
            "Same with my sister, she might have annoyed me occasionally, but I would give anything to have her back."
            jump Jerry_done

label Jerry_done:
    "Whatever the case, I was so relieved to see that Jerry was at least willing to talk about what happened."
    "It shows that he is a braver person than I am. He's not gonna shut himself off from the world."
    "Jerry might be a prick, but he's a respectable prick."
    "He's a prick that, one day, I would be glad to call my friend."
    j "Anyways, I'm gonna go to sleep."
    "Sleep? But it's not even time for dinner. Why would he go to sleep so early?"
    j "I've had a long day, so I'm kind of exhausted. Good night."
    "Jerry left the living room and went upstairs to his makeshift bedroom to catch some z's."
    scene bedroom
    with fade
    "It was the day after Jerry moved in and I made a huge mistake."
    "Usually I set my alarm before I go to bed, but today I totally forgot to."
    "I looked at the clock and realized that school started in 10 minutes!"
    "I got out of bed and quickly put on some clothes and did my best to look at least a little presentable."
    "No time for a shower or breakfast, I just need to get to school, NOW!"
    "I ran downstaird and headed out my front door and ran all the way to school as quick as I could."
    scene classroom
    with fade
    play music "classroom.mp3"
    "I ran into the classroom, and to my surprise, it was completely empty."
    "Where is everybody? I should be 10 minutes late. Class should have already started."
    "I looked up at the clock on the wall, and to my surprise I was 50 minutes early."
    "How did that happen?"
    "I realized that the time had changed yesterday, so while I did forget to set my clock, it didn't matter and I made it here early anyways."
    "Well, I guess I can just stay here and wait for class to start."
    "After about 20 minutes Yuuki walked into the classroom."
    show yuuki
    y "Hello, mortal! What are you doing here so early?"
    menu:
        "I forgot about the time change.":
            jump timechange

        "I could ask you the same question.":
            jump same_question

    label timechange:
            show yuuki happy
            y "Hahahahaha!"
            y "What a silly mistake for someone of your caliber to make!"
            y "My internal clock is perfect, as it even changes on the same night as the time change!"
            y "I can thank the grand elder Mistelfomo for that! He granted me the power of time reading in exchange for his village's safety!"
            y "You see there was this grand dragon, and he asked me to slay the dragon."
            y "So of course I, Yuuki Jasequratop, obliged to help."
            y "I went to the dragons hidden lair and murdered not just him, but also his entire family as well!"
            y "The elder was so pleased that he gave me all the gold I could ever use on top of my time reading ability!"
            jump new_time

    label same_question:
            y "You could ask me the same question, but I am under no obligation to answer it, as I am your superior!"
            y "That being said, I guess I can tell you exactly what it is I am doing here so early, as you have been very useful to me these past few days."
            y "I, Yuuki Bevtold, am here looking for a hidden chamber that I have been told is here on this campus!"
            y "I have searched and scowered through every room in this establishment to no avail!"
            y "This is the last room that I have to search, so I am going to search it quickly before the other mortals arrive!"
            jump new_time

label new_time:
    "Before she could continue with whatever she was babbling on about, my stomach started growling loudly."
    "I realized that I never ate breakfast, or dinner last night for that matter."
    "The hunger pains hit me immedietly and Yuuki must have noticed this fact as well."
    y "Are you requiring some sustenance, mortal? Your stomach is screaming at you."
    "I told her the situation and she just laughed at me."
    y "Well mortal, you are in luck. For I, Yuuki Himigo, have just what you are requiring!"
    "Yuuki reached into her skirt pocket and picked out a brownie."
    y "Here! You may eat this to restore your lost mana!"
    "Should I take her brownie?"
    "On one hand, I am starving, and it would be rude of me to decline an offer."
    "On the other hand, this is Yuuki we're talking about."
    "Who knows what's in that thing! It could be poisoned or have some weird ingredients for all I know."
    menu:
        "Take the brownie.":
            jump high

        "Decline the brownie.":
            jump not_high

    label high:
        "I decided that it would be best to take her up on her offer and eat the brownie."
        "After all, Yuuki might be weird, but it's just a brownie, what's the worst that could happen?"
        "Yuuki handed me the brownie and I quickly stuffed the enire thing into my mouth and swallowed the brownie without even tasting it."
        "That hit the spot."
        "It wasn't too big, but it would be enough to tide me over until lunch."
        "A few more minutes passed, and during that time Yuuki was walking around the room and pressing her hands against every surface possible."
        hide yuuki
        "After awhile, people slowly started to pour into class."
        "Darius, Winrey, and a lot of others arrived."
        "A couple minutes before class, Jerry himself walked in."
        show jerry
        "I was shocked to see him. I thought he would stay home for at least a few more days."
        "Everyone else looked shocked as well, and Jerry must have noticed this, as he quietly walked over to his seat without sayinga word."
        "Everyone else in the class seemed like they were too scared to say anything, so I decided that I would at least greet him."
        "I said hello to him and he just nodded his head back at me."
        hide jerry
        "Mrs. Striker came in right before class started and she got in front of the class."
        show striker
        "I could tell that she to looked surprised to see Jerry, but she must have thought that it would be best to just continue with class as normal."
        s "Ok class, today I am going to let you all get in your groups for the project."
        s "You can work on whatever you want, as long as it's related to the project."
        "Everyone looked happy to find out that we weren't going to be learning anything new today."
        "Darius and Winrey came over to where me and Yuuki were sitting and I then realized that something seemed off."
        hide striker
        show darius
        show winrey school at left
        da "Hey [name], what's up?"
        "My stomach started rumbling, and I realized that something about that brownie was off."
        scene black
        with fade
        play music "black.mp3"
        "UUggghhhh..."
        scene classroom
        with fade
        play music "classroom.mp3"
        "..."
        "What happened?"
        "I was in the class, and then for a second everything went black."
        "Well, whatever it was, it seems to be over with now."
        "I looked up at Darius and something seemed a little off about him."
        show darius derp
        da "What's wrong [name]?"
        "I couldn't exactly pinpoint exactly what it was, but something about Darius looked a little different."
        menu:
            "Did you get a haircut?":
                jump haircut

            "Did you get new glasses?":
                jump glasses

            "Am I on drugs?":
                jump drugs

        label haircut:
            da "Wow! I didn't expect you to notice! Yeah, I got one from my father!"
            da "He gives really good haircuts!"
            "So that explains what's going on! He just got a haircut!"
            "For a second there I was really afraid that something else was up."
            jump high2

        label glasses:
            da "No, these glasses are the same ones I've had since I got that stuff in my eyes!"
            "Huh, if that's not it then I have no idea what's different."
            jump high2

        label drugs:
            "I decided to ask him if I was high on some sort of drug, as it's the only logical explanation."
            "Darius looked different for sure, but not in the way that someone would normally look different."
            "He looked a little more...flat?"
            "Like instead of using a program to create him, someone just drew him in Microhard Color."
            da "You? High? Of course you're not high!"
            "Well, if he says I'm not high, then I'm definitely not high!"
            "Darius wasn't the type of guy to lie to me, so I trust him on this."
            jump high2

    label high2:
        show winrey derp at right
        w "What's up guys?"
        da "Oh, hey Winnifer."
        "Winnifer? Since when has Darius called Winrey Winnifer?"
        win "Good morning to you DooDoo."
        doo "That's my name, don't wear it out!"
        "Now Darius is being called doodoo? What's going on?"
        show yuuki derp at left
        y "Bleeep! Blooop! Bleep! Bloop!"
        win "Oh, hey there Yuuki Duuki!"
        y "Brep! Brep! Brep!"
        doo "Heyyyy, get out of my way Yuuki!"
        doo "Your hairs in my way!"
        y "Groooooop!"
        doo "Ugghhh, forget it! I forgot that Yuuki doesn't speak any real languages!"
        "What?"
        win "Hey DooDoo, you wanna go out?"
        doo "You mean, like out on a date?"
        win "Yeah, I have a huge crush on you and you're naked feet so let's go out and get foot massages!"
        doo "Okey dokey artichokey!"
        win "There is one little problem about you though..."
        doo "And what could that possibly be?"
        win "You're 2-dimensional, I usually only date 3d guys."
        doo "Whaaaat! But you're 2d as well you hypocrite!"
        doo "In fact, we're all 2d!"
        win "Oh yeah I forgot!"
        y "I would say that you two are two dimensional in every since of the word!"
        y "For starters, yeah the both of you are literally two dimensional, as you both look like crappy drawings."
        y "But you guys are also 2 dimensional when it comes to your personality!"
        y "I mean holy crap DooDoo, you have the personality of a wet blanket!"
        y "You're only interesting factor is that you don't wear shoes."
        y "Ooooohhh how exciting! He doesn't wear shoes! That's not enough to base an entire character off of!"
        y "The only thing else you do is... actually I can't think of anything else! That's it!"
        y "In fact I think I wouldn't be going too far to say that you're actually a one dimensional character!"
        y "There's seriously not a single thing I find interesting about you in the slightest!"
        y "I think I speak for everyone when I say that you would be way more interesting if you ended up dead in the same way that Jerry's father died!"
        y "And don't think I forgot about you Winrey, err... I mean Winnifer!"
        y "At least DooDoo has the naked feet thing going on! It's not that much but at least it's something!"
        y "What do you have going on? That you're the leader of the soccer team? That you're the class representative? Booorriiinng!"
        y "Not a single line of dialogue that's come out of you're mouth for the entire story has been interesting!"
        y "You're just a love interest for [name], and you even fail at that!"
        y "You've barely talked to him at all, how could the two of you possibly end up together by the end of the game?"
        y "I ship you and DooDoo together so that hopefully the two of you can leave for good!"
        y "I have a hard time even calling you a 1-dimensional character!"
        y "That would imply that you have a character at all!"
        y "Seriously, if there was a competition between all of the Mary Sue's in fiction, you would win by a landslide!"
        y "The only problem is that you're so friggin forgetable that no one would even remember that you won in the first place!"
        y "I really hope that something interesting happens with you by the time this story ends, because if not then I'm gonna freak!"
        y "I mean, look at me, Yuuki Veronico!"
        y "As soon as I showed up things started to get really interesting."
        y "Unlike the two of you I have some interesting qualities."
        y "I'm a total chuunibyou for starters! And if you don't know what that word means then save and close the game real quick and go look it up!"
        y "I'm the only one in this game with a sense of humor. It might not be funny humor but at least I'm trying, so that has to count for something, right?"
        y "On top of all that, I have the most interesting character design as well! You guys look so boring and normal."
        y "If this was a tv show you two would be background characters for sure!"
        y "Me, on the other hand, look like a freaking anime protagonist!"
        y "I've got pink hair and different color eye's and I'm wearing a freaking sailor uniform!"
        y "I'm the total package baby!"
        doo "Did you say something, Yuuki?"
        win "Yeah it sounded like she actually used her words there for a second!"
        y "Blooooooooop!"
        doo "Nope, I guess I was just imagining it!"
        "Something freaky is definitely going on."
        "Darius is now DooDoo? Winrey is now Winnifer? Yuuki is breaking the fourth wall?"
        "Wait, what fourth wall? That only implies in stories, this is reality. There is no fourth wall to break."
        "Unless..."
        "We are all living in a simulation created by some evil aliens!"
        "Or this is actually just a huge game of The Nims!"
        "Or this is actually just some third-rate visual novel that was created by some random guy for an honor's thesis!"
        "No, that's crazy!"
        "This is reality! Nothing strange is going on here."
        doo "hey guys, you wanna see something funny?"
        win "Sure!"
        doo "Watch this! I can become invisible!"
        hide darius derp
        "Sure enough, DooDoo, I mean Darius, vanished into thin air."
        win "Woooaahhhh! Let me try!"
        hide winrey derp
        doo "You did it Winnifer! We're both invisible!"
        y "Blloooooooop!"
        "Ok, that's definitely not normal."
        "As far as I'm aware, I'm the only person with special powers here. Something is definitely up."
        "And that's when it hit me."
        "I suddenly remember earlier, when Yuuki gave me that brownie to eat."
        "Oh My God!"
        "She put something into those brownies to make me hallucinate!"
        "Yuuki fed me pot brownies!"
        "Oh God... How long is this gonna last?"
        "Knowing Yuuki, these could last all day! I can't be like this all day!"
        "What would my mom say?"
        "She always told me that if she caught me doing drugs, she would literally kill me!"
        "I know that she's serious too, as drugs have always been sort of a touchy subject in my house."
        "My dad used to battle with drug addiction all the time."
        "In fact he was a total drug addict when he met my mom."
        "Luckily, with her help, he was able to go into rehab where he eventually kicked the habit."
        "What if I become addicted too?"
        "I can't follow in my dads footsteps!"
        "I need to go back in time to make it so I never ate these stupid brownies!"
        "There was a problem with this plan though."
        "It's been way longer than a minute since I ate these brownies in the first place."
        "If I kill myself and go back in time, it wouldn't do me any good at all!"
        "I would still be high as a kite when I go back."
        "Wait just a second..."
        "In that moment I had a brilliant idea."
        "What if I can go back in time more than once?"
        "Dolus never told me the specifics of this power."
        "What if I kill myslef, go back in time by one minute, and then kill myself again?"
        "Would I travel back in time by two minutes?"
        "Well, whatever happens I have to try something."
        "I don't want to see the look on my mom's face when she sees that her only son was baked."
        "She's gone through enough hardships, I refuse to be the reason she goes through another."
        "So, with every bone in my body aching in anticipation, I pulled the gun out of my pocket, place it against my head, and pulled the trigger."
        play sound "gun.mp3"
        "{i}BANG!!!{/i}"
        scene black
        with fade
        play music "black.mp3"
        "..."
        "Here I am again, trapped in the total darkness."
        "Hey that would be a cool name for a heavy metal album..."
        "Trapped in the Total Darkness..."
        "I gotta remember that one..."
        "..."
        scene classroom
        with fade
        play music "classroom.mp3"
        show darius derp
        show yuuki derp at left
        show winrey derp at right
        doo "hey guys, you wanna see something funny?"
        win "Sure!"
        doo "Watch this! I can become invisible!"
        hide darius derp

        win "Woooaahhhh! Let me try!"
        hide winrey derp
        doo "You did it Winnifer! We're both invisible!"
        y "Blloooooooop!"
        "Ok, the first jump worked."
        "I'm exactly one minute into the past."
        "No point in delaying this anymore."
        "I pulled the gun out of my pocket and shot myself again, having no idea what would happen."
        play sound "gun.mp3"
        "{i}BANG!!!{/i}"
        scene black
        with fade
        play music "black.mp3"
        "..."
        "Everything seems to be working as normal so far."
        "Im back here in the black as I usually am."
        "But what if something goes wrong that I can't reverse?"
        "What if I'm only allowed to go back in time by one minute?"
        "What would happen then?"
        "Would I have just actually killed myself for real?"
        "Oh no..."
        "What if I'm actually dead!"
        "Ok, keep it together [name], everything is probably fine."
        "You're gonna stay in here for a couple of more seconds, and then you're gonna go back in time by another minute."
        "Everything is going to work out..."
        "..."
        scene classroom
        with fade
        play music "classroom.mp3"
        show darius derp
        show yuuki derp at left
        show winrey derp at right
        y "Unlike the two of you I have some interesting qualities."
        y "I'm a total chuunibyou for starters! And if you don't know what that word means then save and close the game real quick and go look it up!"
        y "I'm the only one in this game with a sense of humor. It might not be funny humor but at least I'm trying, so that has to count for something, right?"
        y "On top of all that, I have the most interesting character design as well! You guys look so boring and normal."
        y "If this was a tv show you two would be background characters for sure!"
        y "Me, on the other hand, look like a freaking anime protagonist!"
        y "I've got pink hair and different color eye's and I'm wearing a freaking sailor uniform!"
        y "I'm the total package baby!"
        doo "Did you say something, Yuuki?"
        win "Yeah it sounded like she actually used her words there for a second!"
        y "Blooooooooop!"
        doo "Nope, I guess I was just imagining it!"
        "..."
        "YES!"
        "IT ACTUALLY WORKED!"
        "I have travelled back in time by two minutes!"
        "This means that there probably isn't a limit to my powers!"
        "I can go back in time as far as my heart desires!"
        "Well, as far back as I was alive I guess."
        "I can't travel back in time to before I was born."
        "But I still need to go back further!"
        "I once again pulled the gun out and blew my own brains out onto the classroom floor and walls."
        play sound "gun.mp3"
        "{i}BANG!!!{/i}"
        scene black
        with fade
        play music "black.mp3"
        "..."
        "This part of time traveling sucks."
        "It's like being stuck at a loading screen in a video game..."
        "..."
        scene classroom
        with fade
        play music "classroom.mp3"
        show darius derp
        show yuuki derp at left
        show winrey derp at right
        doo "And what could that possibly be?"
        win "You're 2-dimensional, I usually only date 3d guys."
        doo "Whaaaat! But you're 2d as well you hypocrite!"
        doo "In fact, we're all 2d!"
        win "Oh yeah I forgot!"
        y "I would say that you two are two dimensional in every since of the word!"
        y "For starters, yeah the both of you are literally two dimensional, as you both look like crappy drawings."
        y "But you guys are also 2 dimensional when it comes to your personality!"
        y "I mean holy crap DooDoo, you have the personality of a wet blanket!"
        y "You're only interesting factor is that you don't wear shoes."
        y "Ooooohhh how exciting! He doesn't wear shoes! That's not enough to base an entire character off of!"
        "..."
        "It worked again!"
        "I have now travelled back in time by 3 whole minutes!"
        "It's still gonna take a couple of more times before I get to the point where I decided to eat the brownie."
        "I forgot just how long Yuuki went on her weird rant for."
        "She's got a point though, Darius does have the personality of a wet blanket."
        "I need to stop getting so sidetracked!"
        "I don't think I need to explain what I did next."
        play sound "gun.mp3"
        "{i}BANG!!!{/i}"
        scene black
        with fade
        play music "black.mp3"
        "Can we just skip over this part for now on?"
        "..."
        scene classroom
        with fade
        play music "classroom.mp3"
        show darius derp
        show yuuki derp at left

        w "What's up guys?"
        da "Oh, hey Winnifer."

        win "Good morning to you DooDoo."
        doo "That's my name, don't wear it out!"

        show yuuki derp at left
        y "Bleeep! Blooop! Bleep! Bloop!"
        win "Oh, hey there Yuuki Duuki!"
        y "Brep! Brep! Brep!"
        doo "Heyyyy, get out of my way Yuuki!"
        doo "Your hairs in my way!"
        "Still not far enough..."
        play sound "gun.mp3"
        "{i}BANG!!!{/i}"
        scene black
        with fade
        play music "black.mp3"
        "..."
        scene classroom
        with fade
        play music "classroom.mp3"
        show darius derp
        da "What's wrong [name]?"
        "Ok we are getting close."
        play sound "gun.mp3"
        "{i}BANG!!!{/i}"
        scene black
        with fade
        play music "black.mp3"
        "UGGGHHHH"
        "Let me skip this part already!"
        "What's the point of it anyway!"
        "What does this black emptiness accomplish?"
        "What's it's purpose?"
        "If I ever see Dolus again, I'll be sure to ask her about it..."
        scene classroom
        with fade
        play music "classroom.mp3"
        "I got back and this time no one was standing in front of me."
        "Did I make it far enough back in time?"
        "I could feel something funny rumbling around in my stomach, so the answer to that question was no."
        play sound "gun.mp3"
        "{i}BANG!!!{/i}"
        play sound "gun.mp3"
        "{i}BANG!!!!!!!{/i}"
        play sound "gun.mp3"
        "{i}BANG!!!!!!!!!!!{/i}"
        play sound "gun.mp3"
        "{i}BANG!!!!!!!!!!!!!{/i}"
        "I went back in time a few more times."
        "I stopped counting how many times after awhile, but it was probably around 10 in total before I finally got to the point where I was trying to go."
        show yuuki
        y "Are you requiring some sustenance, mortal? Your stomach is screaming at you."

        y "Well mortal, you are in luck. For I, Yuuki Himigo, have just what you are requiring!"

        y "Here! You may eat this to restore your lost mana!"
        "Oh thank God... I finally made it."
        "After my incredibly difficult journey, I have finally reached my destination."
        "Yuuki's face looked how it normally did, not like some fake knock-off that I saw when I was high."
        "She looked like how I imagine an oasis would look like in the middle of the desert to some lost wonderers."
        "It was beautiful!"
        "Her different color eyes gleemed in the sunlight that was radiating from the windows."
        "Her pink hair reminded me of the nostalgic sense that I would get when eating cheap bubblegum when I was just a kid."
        "Her Japanese sailor uniform reminded me of one of my favorite shows..."
        "..."
        "Wait...what am I saying?"
        "This whole thing was her fault to begin with!"
        "If she didn't offer me a freaking pot brownie than I never would have had to go back in time so much in the first place!"
        "Her different eye colors looked like a random mishmash of puke that a chile would throw up after eating too much ice cream."
        "Her pink hair looked like expired bubblegum that one would accidently touch when they put their hand underneath their seat at school."
        "Her Japanese sailor uniform reminded me of how we lived in America and how this girl was mentally insane!"
        "I took the brownie from her hand, but this time I took it not to eat it, but to throw it away so that no one else would fall into her trap!"
        "I would yell at her for tricking me into eating a pot brownie in the first place, but then I would have to tell her my secret and I didn't feel like doing that just yet."
        "I walked out of the classroom and threw the bronwnie into the closest garbage bin that I could find."
        "The rest of the class proceeded as normal."
        "We got into groups as Mrs. Striker had instructed and further discussed our project."
        "Winrey and Darius approached my desk and after a couple of minutes Yuuki came over as well."
        show yuuki at left
        show darius
        show winrey school at right
        da "What's up guys? You ready to work on this project?"
        w "You bet!"
        y "Whatever, I am of the upmost upset that I couldn't find what I was looking for before class, but I will do all I can to help us out in this project."
        da "Good to hear!"
        "We decided that it was time to start rehearsing the play itself, so we all prepared and tried our best to get into character."
        "It turns out that Darius had made a script of his own for the play so we didn't have to worry about that part."
        show darius happy
        da "I had to make some changes to the play to get it so that we could perform it in a timely manner."
        da "The stories the same for the most part, I just had to cut out a lot of the filler."
        da "In it's current state, it should take us anywhere from 5-10 minutes to perform."
        w "Wow! Great job Darius! I wish you would have told me that you were writing the script."
        w "That probably took quite a lot of time, didn't it?"
        da "Uhhh...no actually. I was able to write the whole thing in about an hour."
        w "What? How is that even possible?"
        da "Well I kind of know the story like the back of my hand, so it didn't take much effort or brain power to figure it all out."
        y "Like the back of your hand? Is it normal for mortals to have a vast understanding in their hand behinds?"
        da "It's just a figure of speech Yuuki..."
        y "Ohhhh..."
        "We each took a few minutes to read over our own parts and practice them individually before we came together to do the whole thing together."
        "I read over my part and realized that I had quite a few lines to say."
        "Well I guess that makes sense. I do have the lead role."
        "After we all had a firm grasp on our roles, we came together and practiced the parts for the rest of class."
        "Things went surprisingly smooth for the most part."
        "Sure, my acting was pretty stiff but I think I did a good job over all."
        "The only problem we had was keeping Yuuki under control."
        "She kept on trying her best to go off script."
        y "Hello, BroBro! I will use my powers of levitation to kill you!"
        show yuuki happy at left
        y "Bwahahahahahah!"
        show darius angry
        da "Yuuki! How many times do I have to tell you!"
        da "Your character doesn't have any levitation powers!"
        show yuuki angry at left
        y "Oh yeah? How do you know?"
        da "Because I've seen the freaking show!"
        da "And I even read the source material to prepare for this play!"
        y "Well why don't we just make it so that he does have levitation powers for the play?"
        da "Absolutely not! There will be no tampering with the script!"
        da "IT. IS. SACRED!!!"
        da "And how are you supposed to even do levitation powers anyways?"
        y "I'll just use my actual levitiaion powers, duh!"
        da "You don't have any... Never mind, just forget it"
        da "Please just stick to the script Yuuki, I'm begging you."
        y "..."
        y "fine..."
        show darius
        da "Thank you!"
        y "I do have one question though..."
        da "What is it?"
        show yuuki at left
        y "Well, I watched a little bit of the show to have a better grasp at my character, and I noticed something a little odd..."
        da "And what is that?"
        y "Well, I couldn't help but noticing that your character wears shoes in the show, yet here you are with bare feet!"
        show darius angry
        da "Uhhh... Well you see.... Uhhhh...."
        y "What's the matter? I thought you were the one who was trying to protect the integrity of the source material? Is something the matter?"
        da "No! It's just... Uhhh... my character is supposed to be poor, so I thought it would be good if he didn't wear any shoes! That's all!"
        "Darius was such full of crap but I didn't care enough to say anything."
        y "I see..."
        da "..."
        w "..."
        y "Ok then! That makes sense to me!"
        "Darius let out a huge sigh of relief and we spent the rest of the class period practicing over and over until we could get everything right."
        scene classroom evening
        with fade
        play music "classroom.mp3"
        show yuuki at left
        show darius
        show winrey school at right
        w "Oh BroBro, you did it, you saved me!"
        '"I could not have possible done it without the power of friendship and love that I had on my side!"'
        w "I love you!"
        da "And... Cut!"
        da "Great job everyone!"
        "I was a little upset that Darius decided to cut out the kiss between me and Winrey, but I know that doing that scene would have made Winrey uncomfortable, so it was probably for the best."
        da "We made a huge amount of progress today!"
        w "Yeah, great job guys! I think we're practically ready to perform this thing!"
        "I looked around the class and realized that it was just the four of us left."
        da "Dang, it seems that everyone left already."
        w "I guess that makes sense, class did end over an hour ago."
        y "Yes, nightfall is approaching as we speak. We better go home before demons eat our souls!"
        da "Yeah, good point Yuuki! I'll see you guys later!"
        w "See ya!"
        y "Farewell mortals!"
        "The four of us left the school and went on our seperate ways."

        "I went home that day, completely exhausted and ready to fall asleep."
        "As soon as I got home, I jumped into my bed and passed out as soon as my head hit the pillow."
        jump newish

    label not_high:
        "I decided that it would be best if I didn't take the brownie."
        "For as hungry as I was, this was a hard decision to make but I didn't really trust Yuuki all that much."
        "For all I know that brownie could be filled with drugs or poison or some other non-brownie item."
        "For now, I'll just starve."
        show yuuki angry
        y "Fine! Be that way! I didn't want to give you my beautiful brownie anyways!"
        "I could tell that my rejection upset her, but that was way better than eating her brownie."
        "Hopefully I can make it all the way to lunch."
        "Yuuki left my side and started walking around the room at random and pressing her hands up against every object possible."
        hide yuuki
        "After awhile, people slowly started to pour into class."
        "Darius, Winrey, and a lot of others arrived."
        "A couple minutes before class, Jerry himself walked in."
        show jerry
        "I was shocked to see him. I thought he would stay home for at least a few more days."
        "Everyone else looked shocked as well, and Jerry must have noticed this, as he quietly walked over to his seat without sayinga word."
        "Everyone else in the class seemed like they were too scared to say anything, so I decided that I would at least greet him."
        "I said hello to him and he just nodded his head back at me."
        hide jerry
        "Mrs. Striker came in right before class started and she got in front of the class."
        show striker
        "I could tell that she to looked surprised to see Jerry, but she must have thought that it would be best to just continue with class as normal."
        s "Ok class, today I am going to let you all get in your groups for the project."
        s "You can work on whatever you want, as long as it's related to the project."
        "Everyone looked happy to find out that we weren't going to be learning anything new today."
        hide striker
        "Winrey and Darius approached my desk and after a couple of minutes Yuuki came over as well."
        show yuuki at left
        show darius
        show winrey school at right
        da "What's up guys? You ready to work on this project?"
        w "You bet!"
        y "Whatever, I am of the upmost upset that I couldn't find what I was looking for before class, but I will do all I can to help us out in this project."
        da "Good to hear!"
        "We decided that it was time to start rehearsing the play itself, so we all prepared and tried our best to get into character."
        "It turns out that Darius had made a script of his own for the play so we didn't have to worry about that part."
        show darius happy
        da "I had to make some changes to the play to get it so that we could perform it in a timely manner."
        da "The stories the same for the most part, I just had to cut out a lot of the filler."
        da "In it's current state, it should take us anywhere from 5-10 minutes to perform."
        w "Wow! Great job Darius! I wish you would have told me that you were writing the script."
        w "That probably took quite a lot of time, didn't it?"
        da "Uhhh...no actually. I was able to write the whole thing in about an hour."
        w "What? How is that even possible?"
        da "Well I kind of know the story like the back of my hand, so it didn't take much effort or brain power to figure it all out."
        y "Like the back of your hand? Is it normal for mortals to have a vast understanding in their hand behinds?"
        da "It's just a figure of speech Yuuki..."
        y "Ohhhh..."
        "We each took a few minutes to read over our own parts and practice them individually before we came together to do the whole thing together."
        "I read over my part and realized that I had quite a few lines to say."
        "Well I guess that makes sense. I do have the lead role."
        "After we all had a firm grasp on our roles, we came together and practiced the parts for the rest of class."
        "Things went surprisingly smooth for the most part."
        "Sure, my acting was pretty stiff but I think I did a good job over all."
        "The only problem we had was keeping Yuuki under control."
        "She kept on trying her best to go off script."
        y "Hello, BroBro! I will use my powers of levitation to kill you!"
        show yuuki happy at left
        y "Bwahahahahahah!"
        show darius angry
        da "Yuuki! How many times do I have to tell you!"
        da "Your character doesn't have any levitation powers!"
        show yuuki angry at left
        y "Oh yeah? How do you know?"
        da "Because I've seen the freaking show!"
        da "And I even read the source material to prepare for this play!"
        y "Well why don't we just make it so that he does have levitation powers for the play?"
        da "Absolutely not! There will be no tampering with the script!"
        da "IT. IS. SACRED!!!"
        da "And how are you supposed to even do levitation powers anyways?"
        y "I'll just use my actual levitiaion powers, duh!"
        da "You don't have any... Never mind, just forget it"
        da "Please just stick to the script Yuuki, I'm begging you."
        y "..."
        y "fine..."
        show darius
        da "Thank you!"
        y "I do have one question though..."
        da "What is it?"
        show yuuki at left
        y "Well, I watched a little bit of the show to have a better grasp at my character, and I noticed something a little odd..."
        da "And what is that?"
        y "Well, I couldn't help but noticing that your character wears shoes in the show, yet here you are with bare feet!"
        show darius angry
        da "Uhhh... Well you see.... Uhhhh...."
        y "What's the matter? I thought you were the one who was trying to protect the integrity of the source material? Is something the matter?"
        da "No! It's just... Uhhh... my character is supposed to be poor, so I thought it would be good if he didn't wear any shoes! That's all!"
        "Darius was such full of crap but I didn't care enough to say anything."
        y "I see..."
        da "..."
        w "..."
        y "Ok then! That makes sense to me!"
        "Darius let out a huge sigh of relief and we spent the rest of the class period practicing over and over until we could get everything right."
        scene classroom evening
        with fade
        play music "classroom.mp3"
        show yuuki at left
        show darius
        show winrey school at right
        w "Oh BroBro, you did it, you saved me!"
        '"I could not have possible done it without the power of friendship and love that I had on my side!"'
        w "I love you!"
        da "And... Cut!"
        da "Great job everyone!"
        "I was a little upset that Darius decided to cut out the kiss between me and Winrey, but I know that doing that scene would have made Winrey uncomfortable, so it was probably for the best."
        da "We made a huge amount of progress today!"
        w "Yeah, great job guys! I think we're practically ready to perform this thing!"
        "I looked around the class and realized that it was just the four of us left."
        da "Dang, it seems that everyone left already."
        w "I guess that makes sense, class did end over an hour ago."
        y "Yes, nightfall is approaching as we speak. We better go home before demons eat our souls!"
        da "Yeah, good point Yuuki! I'll see you guys later!"
        w "See ya!"
        y "Farewell mortals!"
        "The four of us left the school and went on our seperate ways."
        "I realized it was getting pretty late so I decided to take the same short cut home that I did on the night that I got my powers."
        scene moon over field
        with fade
        play music "moon.mp3"
        "It was dark and gloomy in the park."
        "There wasn't a soul around and I was completely alone."
        "I wasn't scared though, If anything happens I can just use my power to go back in time."
        "I walked for a few minutes until I heard something behind me."
        "It sounded like leaves crunching against the concrete."
        "The only thing that could make that sound would be someone walking behind me."
        "But who would be walking behind me like that? Like they're trying to sneak up on me."
        "Maybe it's Yuuki pulling a prank on me?"
        "That seems right up her alley. I can just imagine what she would say."
        y "I decided to follow you home to make sure nothing happened to you!"
        y "Plus I decided to sneak up on you to see what your detection level was."
        "I turned around to tell Yuuki to piss off, but before I could I felt a painful thump against my head and everything went dark..."
        scene black
        with fade
        play music "black.mp3"
        "..."
        "......................"
        "...Where...am I?"
        "Am I dead?"
        "This is the same place where I am taken when I go back in time."
        "What's going on?"
        "I didn't kill myself..."
        "Maybe someone else killed me?"
        "I then remembered the thump that I took to the back of my head."
        "Owwww... I can still feel it..."
        "..."
        "Wait... I can...feel it?"
        "That can't be right, whenever I go back in time I can't feel anything."
        "Ewww..."
        "I noticed that there was a terrible smell as well, it almost smelt like a mixture of poop and sewer water."
        "Oh no... I'm not dead at all..."
        "I'm still alive, I'm just trapped in some pitch black place."
        show robber1
        r "I see you're finally awake."
        "Those eyes..."
        "I recognize them from somewhere...but from where?"
        "Suddenly, a brief memory flashed into my mind."
        scene moon over field
        with fade
        play music "moon.mp3"
        show robber1
        r "Look kid, I don't want to hurt you but I am gonna need you to slowly hand over all the money you have."
        r "And don't even think of trying any funny business. I have a gun in my pocket and if you do anything suspicious I swear to God I'll kill you."
        scene black
        with fade
        play music "black.mp3"
        show robber1
        "Oh my God..."
        "It's that guy from before..."
        "The guy who killed me..."
        "The guy who started it all..."
        r "I can tell from your face that you remember me kid."
        r "I guess I shouldn't be surprised, I did kill you after all."
        r "Or at least I though I did, I shot you straight in the head... How are you alive anyways?"
        menu:
            "I've got a good doctor.":
                jump sarcastic

            "God saved me.":
                jump truth

        label sarcastic:
            r "You must got one heck of a doctor to fix that injury kid."
            r "When I left you your brain was oozing out of you forehead."
            r "I wouldn't believe it myself unless I saw you, but here you are in the flesh."
            jump trapped

        label truth:
            r "Hmph... yeah right."
            r "As if God really exists..."
            r "That would be nice kid, but I'm positive that he's fake."
            r "Well, however it is that you survived, you're real lucky."
            r "When I left you your brain was oozing out of you forehead."
            r "I wouldn't believe it myself unless I saw you, but here you are in the flesh."
            jump trapped

        label trapped:
            r "Well you're probably wondering why I brought you down here anyways, aren't you?"
            "Honestly this whole thing was happening so quickly that I didn't have much time to think of anything."
            r "Well, it's cuz I've got a major bone to pick with you."
            r "You might have heard on the news the day after we met about how an entire family was murdered?"
            r "Or maybe you didn't since you did just get shot in the head..."
            r "Well, anyways, that was my family."
            r "My wife and my two little girls...They were all..."
            r "..."
            r "They were killed."
            r "They had there hands and feet tied behind there back and they were tortured for hours on end."
            r "Eventually the guy in charge cut their heads off."
            r "I was there..."
            r "I...I saw the whole thing go down..."
            r "I was a part of it too..."
            r "The boss of the gang that I was a part of came to my house with two of his underlings and tied us up while we were sleeping."
            r "They cut us all up and did unspeakable things to all four of us..."
            r "Don't ask me how, cuz even I'm not sure, but somehow I managed to escape."
            r "I got out of my ropes and killed one of the guys."
            r "The boss and the other guy ran away as they could see how furious I was."
            r "They knew that if they stayed, I woulda killed them."
            r "But it was too late."
            r "Right before I escaped, the torturer pulled a machete out of a bag and decapitated my beautiful wife and my precious little girls..."
            r "I don't remember much of what happened after that..."
            r "All I know is that I felt every emotion under the sun."
            r "I did things to that man that still haunt me to this day..."
            r "After I was finished with him he didn't even look human anymore."
            r "His entire body was unrecognizable."
            r "I finished him off by tying him up in the same way that he tied us up and took off his head with the same machete he used on my family."
            r "I then ran away and never came back to that house again."
            r "The police must have found them out pretty quickly, because I was staying in a hotel room the very next day and I saw the report on the television."
            r "I listened to the whole thing and I couldn't believe what they had to say."
            tv "Early this morning, a family of four was found brutally murdered in their home."
            tv "They were found by their neighbors with their heads decapitated and their arms and legs tied behind their back."
            tv "The family included a father, mother, and two young girls."
            tv "The father was 32 years old and had been happily married to his wife, age 30, for 7 years now."
            tv "Their two young daughters were twins, and they were about to celebrate their fifth birthday next week."
            tv "Investigators do not think that this was a random act of violence. Evidence shows that the father might have been involved with a local gang."
            tv "No matter the circumstances, I think we can all agree that this was a terible tragedy that will shake the lives of this town for some time to come."
            r "Can you believe that? They actually mistook that monster for me."
            r "They buried him right next to my family."
            r "I visited the gravestone and sure enough, my name was sitting on it right there in front of me."
            r "You ever see a gravestone with your own name on it, kid?"
            r "It's so freaking surreal..."
            r "I just sat there for hours, not moving an inch..."
            r "I didn't cry or anything, I just sat there and reflected on my current situation."
            r "How I was scared and broke after I lost my job, and decided to go to the local mafia for money."
            r '"We can give you a great life with a lot of benefits if you join us." They told me.'
            r "I fell for everything they said, hook, line, and sinker."
            r "I mean, it just sounded so perfect, you know?"
            r "I would make over double what I made at my last job for half the work."
            r "My family would be protected, everything would be perfect."
            r "Well, anyways, after I sat there at my own grave for a few minutes, I realized that those guys who killed my family got away."
            r "I realized that they could be doing the same exact thing to another family, and that's when I knew what I had to do."
            r "I spent the next few days hunting every single last one of them down."
            r "I killed all of them."
            r "From the lowliest grunt, to the big man himself, they all died."
            r "After I had finished gutting the big boss, I sat down at his desk."
            r "I put my feet up, and for the first time since that fateful night, I felt at ease."
            r "You know I always hear people say that getting revenge on the people who wronged you won't help you at all."
            r "They always say that you will still feel empty and broken and how nothing can fix you."
            r "You know what I say to that?"
            r "I say that it's a big steamin load of BS."
            r "I felt so great in that moment..."
            r "I just sat there in his office, laughing hysterically, realizing that I had won!"
            r "For the first time in my life I felt like the big man."
            r "In that moment I thought that I could take on the whole friggin world!"
            r "I went back to the hotel that day feeling perfect."
            r "I spent the next few days relaxing and feeling content."
            r "Then this morning, I wake up and I decide to go for a little stroll around town."
            r "I walked around all freaking day."
            r "I went to every shop in town and bought everything my heart desired."
            r "I stole all of the bosses money so I had plenty of cash to burn you see."
            r "After awhile it started getting dark, so I decided to take a shortcut through the park."
            r "And that's when I saw something that truly surprised me."
            r "I saw you."
            r "And I was so confused."
            r "I must be mistaken. That can't be him. I know I killed him."
            r "I decided to tail you to see where you were going, and to make sure that it actually was you."
            r "After I got close enough, I realized that it was in fact you, and that's when it hit me."
            r "See, the only reason I was out that night was because the boss told me that I needed to mug a few guys to get some cash."
            r "Well, my deadline was getting real close when you came along and I knew that you would be my last chance."
            r "And, well, you know the rest of the story."
            r "You don't have any money, things get out of hand, and then boom, I accidently kill you."
            r "Or so I thought."
            r "But as I was standing behind you earlier, I realized that you're partially to blame for what happened to my family."
            r "Ya see, if you just had the money I needed, everything would have went as planned and my family would have been ok."
            r "I knew that if I didn't get you, all my pain would come back."
            r "And I knew that I couldn't go and let that happen, could I?"
            r "I mean, I felt so good. I wasn't about to stop having that feeling."
            r "So here we are kid, just the two of us, and I'm about to kill you, for real this time."
            r "Just to be sure that I get the job done, I'm gonna shoot you in the head and the chest and a few more shots everywhere else just to be safe."
            r "I can't have you coming back to life again, can I?"
            "I realized that I was in a pretty bad scenario."
            "It didn't matter that he was going to kill me, I would just come back, but that's the problem."
            "I don't know how long I've been here, but it's definitely been way longer than a minute."
            "He's gonna kill me and I'm just going to go right back to right before he kills me."
            "I'm going to be stuck in an endless loop of death and reset..."
            r "Well kid, I guess this is goodbye."
            "I felt around and I realized something huge."
            "That moron didn't even tie me up!"
            "I felt around in my pocket, and my gun was still there!"
            r "Any last words kid?"
            "Is this guy the biggest idiot in the world or what?"
            "I could just shoot him right now, but as much as he might deserve it, I don't really want any blood on my hands."
            "Think [name], there has to be some way out of this scenario that doesn't include murder, right?"
            "And that's when I had a crazy idea."
            "Can I go back in time more than once?"
            "Like, could I shoot myself, go back in time by one minute, and immediately shoot myself again to travel back in time an additional minute?"
            "Dolus never said anything about it, so I don't see why not, but it was certainly risky."
            "What if the limit is only once, and I actually kill myself the second time?"
            "Well, I guess I would rather be dead for real than spend all of eternity getting shot by this dunce."
            "I felt the gun in my pocket and pulled it out, I was ready to shoot myself."
            r "Hey! What's that you got in your hand kid?"
            r "You better not try anything funny! I'll kill you!"
            r "In hindsight I probably should have checked his pockets for anything he could use to escape..."
            r "I am a thug after all. Checking peoples pockets should be second nature to me."
            "I've had just about enough of this guys shenanigans, so I went ahead and shot myself in the head."
            play sound "gun.mp3"
            "{i}BANG!!!{/i}"
            r "What the heck are you doing you psycho!"
            scene black
            with fade
            "..."
            "......"
            "...I...I think it worked."
            "This place looks exactly like the place that I was just trapped in, so it's hard to tell if I'm at the place where I usually go when I die or of I'm still with that guy."
            "I yelled out to see if anybody would answer but there was no sound to be heard."
            "I also tried to feel around but I couldn't feel anything."
            "Lastly, I took a big whiff to see if I could smell anything."
            "Nothing, there wasn't even a hint of any type of smell, both good or bad."
            "I remember that the place I was trapped in smelt horrible, so I guess this isn't it."
            "Unless I shot myself in such a way that I lost all of my senses but I was technically still alive."
            "No, that seems rather unlikely."
            "Ok, I guess it did work."
            "Now the only question is if I can go back multiple times."
            "Well, whatever the answer is, I'm about to find out."
            scene black
            with fade
            show robber1
            r "I knew that if I didn't get you, all my pain would come back."
            r "And I knew that I couldn't go and let that happen, could I?"
            r "I mean, I felt so good. I wasn't about to stop having that feeling."
            r "So here we are kid, just the two of us, and I'm about to kill you, for real this time."
            r "Just to be sure that I get the job done, I'm gonna shoot you in the head and the chest and a few more shots everywhere else just to be safe."
            r "I can't have you coming back to life again, can I?"
            "..."
            "Ok, it worked, I'm back in time by one minute."
            "No point in delaying the inevitable."
            "I pulled my gun out for who knows how many times and pulled the trigger."
            play sound "gun.mp3"
            "{i}BANG!!!{/i}"
            scene black
            with fade
            "..."
            "Ok, it seems that I'm back in the place I always go."
            "Now the only question is if it lets me go back or not."
            "What if it doesn't though, what will happen then?"
            "I quickly imagined all of the possible outcomes."
            "I guess I could just stay here for all eternity. It would become my purgatory."
            "That wouldn't be so bad. I'm sure after awhile I would lose all sense of myself and just cease to exist."
            "There's definitely worse fates that a person could come across."
            "I could end up in Hell for all I know."
            "I have done some pretty terrible stuff in my life. It wouldn't surprise me if I ended up there."
            "My family wasn't really religious at all, we never went to church or anything like that."
            "Due to that, I never really believed in Hell or anything like that."
            "I just assumed that after you died, you just vanished."
            "That obviously changed recently when I met Dolus."
            "Now I believe in heaven and Hell, for better or worse."
            "Before I could think about the end of my life any more, I felt something in my gut and I was pulled from that realm of existence."
            scene black
            with fade
            show robber1
            r "It's so freaking surreal..."
            r "I just sat there for hours, not moving an inch..."
            r "I didn't cry or anything, I just sat there and reflected on my current situation."
            r "How I was scared and broke after I lost my job, and decided to go to the local mafia for money."
            r '"We can give you a great life with a lot of benefits if you join us." They told me.'
            r "I fell for everything they said, hook, line, and sinker."
            r "I mean, it just sounded so perfect, you know?"
            "..."
            "................."
            "...Holy crap...It actually...It actually worked!"
            "I travelled back in time by another full minute!"
            "This opens up so many new possibilities with my time travel powers!"
            "There has been a couple of times before where I wanted to change the past by a little, but I waited longer then a minute so I thought I was just completely out of luck!"
            "But now that I know that I can travel back as much as I want, I'm no longer chained by those boundaries!"
            "I guess there is still a couple of limitations."
            "The big one is my own existence."
            "I can't travel back to a time before I was born, as I wouldn't have anyway to die if I don't even exist."
            "The other big limitation that I can think of in the moment is my own mental limitations."
            "Going back a few times isn't really that big of a deal, but what if I wanted to go back a few days, or maybe even a few years?"
            "I would surely go crazy, right?"

            "Oh well, it's not worth thinking about right now, I still have to go back quite a few more times to get out of this situation."
            play sound "gun.mp3"
            "{i}BANG!!!{/i}"
            scene black
            with fade
            "..."
            "I hope this works again."
            "I realized that there was still no gurantee that it was going to work a third time."
            "What if the limit is two, and I actually die this time?"
            "I know that seems unlikely, but Dolus never gave me any instructions about how exactly to use this power."
            "For all I know she might consider this an abusement of my gift."
            "She might even try and take it away."
            scene black
            with fade
            show robber1
            r "I got out of my ropes and killed one of the guys."
            r "The boss and the other guy ran away as they could see how furious I was."
            r "They knew that if they stayed, I woulda killed them."
            r "But it was too late."
            r "Right before I escaped, the torturer pulled a machete out of a bag and decapitated my beautiful wife and my precious little girls..."
            r "I don't remember much of what happened after that..."
            r "All I know is that I felt every emotion under the sun."
            r "I did things to that man that still haunt me to this day..."
            r "After I was finished with him he didn't even look human anymore."
            r "His entire body was unrecognizable."
            "..."
            "Alright, cool. Three times works just as well as two."
            "I think it's safe to say for now on that I can go back as many times as I want to."
            play sound "gun.mp3"
            "{i}BANG!!!{/i}"
            scene black
            with fade
            "You know the worse part of this power is having to wait every time I go back."
            "You would think it would be the actual shooting yourself in the head part, but nope, that parts pretty easy compared to this."
            "I'm a really impatient person, so waiting around like this sucks."
            "The worse part is tha I have no idea how long it's gonna take to go back."
            "There is no way to tell time in here, so for all I know it could take hours."
            "Sometimes it's pretty quick, but other times it takes what seems like forever."
            "This was one of those times."
            "I just sat there in silence for what felt like forever."
            "Maybe I was wrong, and three actually was the limit."
            "It would makes sense, with the rule of threes and all."
            "Nah, I'm sure I'm fine, it's just taking awhile to mess with me."
            "It's like a loading screen in a video game."
            "Sometimes those take a super long time, and sometimes they are almost instant."
            scene black
            with fade
            show robber1
            r "Well, it's cuz I've got a major bone to pick with you."
            r "You might have heard on the news the day after we met about how an entire family was murdered?"
            r "Or maybe you didn't since you did just get shot in the head..."
            r "Well, anyways, that was my family."
            r "My wife and my two little girls...They were all..."
            r "..."
            r "They were killed."
            r "They had there hands and feet tied behind there back and they were tortured for hours on end."
            r "Eventually the guy in charge cut their heads off."
            r "I was there..."
            r "I...I saw the whole thing go down..."
            "..."
            "Cool, we're back, but still not back far enough."
            play sound "gun.mp3"
            "{i}BANG!!!{/i}"
            scene black
            with fade
            "..."
            "UGGGHHHHH..."
            "Can we just skip this part already?"
            scene black
            with fade
            show robber1
            r "I see you're finally awake."
            r "I can tell from your face that you remember me kid."
            r "I guess I shouldn't be surprised, I did kill you after all."
            r "Or at least I though I did, I shot you straight in the head... How are you alive anyways?"
            "Ok, this was from the very beginning of our convesation."
            "This is right before he started monologuing about how much his life sucks and about how we live in a society and all that crap."
            "I'm not sure how this next time jump is going to go."
            "I was passed out just a minute ago, so how will that effect my time travel?"
            "Will I still be passed out when I come back, or will I be awake?"
            "It's gonna be a real problem if I'm still passed out, as I won't be able to travel back anymore after that."
            "If that's the case, than I'm gonna have to find another way out."
            "I'll have to kill him..."
            "No, I'm sure it's gonna work the same way it always has."
            play sound "gun.mp3"
            "{i}BANG!!!{/i}"
            scene black
            with fade
            "..."
            "If this doesn't work I'm gonna have to kill him."
            "I might hate the guy, but can I really do it if I have to?"
            "I'm not sure if I have the stomach for murder..."
            "Also, if this doesn't work than my previous hypothesis about time travel would be rendered incorrect."
            "I wouldn't be able to travel all the way back to my birth."
            "I would only be able to travel back as far as when I fell asleep."
            "Please work..."
            scene black
            with fade
            show robber1
            r "Man I sure hope this kid wakes up soon."
            r "I'm dying to monoluge to him about how much my life sucks and how we live in a society and all that crap."
            "..."
            "It worked!"
            "I'm conscious! A whole minute before I was before!"
            "Great! Now I know I can get out of here, it's just gonna take some time!"
            play sound "gun.mp3"
            "{i}BANG!!!{/i}"
            scene black
            with fade
            "SKIP THIS PART! IT'S SO BORING!!!"
            scene black
            with fade
            show robber1
            "Man I wonder how the football games going... Come on kid wake up already!"
            play sound "gun.mp3"
            "{i}BANG!!!{/i}"
            play sound "gun.mp3"
            "{i}BANG!!!!{/i}"
            play sound "gun.mp3"
            "{i}BANG!!!!!{/i}"
            play sound "gun.mp3"
            "{i}BANG!!!!!!!{/i}"
            play sound "gun.mp3"
            "{i}BANG!!!!!!!!!{/i}"
            play sound "gun.mp3"
            "{i}BANG!!!!!!!!!!!!!{/i}"
            play sound "gun.mp3"
            "{i}BANG!!!!!!!!!!!!!!!!{/i}"
            play sound "gun.mp3"
            "{i}BANG!!!!!!!!!!!!!!!!!!{/i}"
            "I killed myself countless of times."
            "Each time I slowly crept my way around the boundaries of time."
            "Everytime I went back, the guy was talking to himself about something random."
            r "Man I sure do like cake."
            r "I really wanna see that new movie that came out this week."
            r "We live in a society."
            r "Did I leave the stove on?"
            "The more I heard from his, the more pathetic he sounded."
            "I know his entire family died and all that, but that doesn't give him an excuse to be so lame."
            "After more jumps than I could possible even begin to count, the scenery finally changed."
            scene moon over field
            with fade
            play music "moon.mp3"
            show robber1
            r "Yes! I knocked him out without him struggling at all!"
            r "Now I can take him back to my secret lair and monologue to him and kill him!"
            r  "Today's a great day!"
            "Yes! I was close!"
            "I still need to go back a few more times to get back to a time where I didn't take this shortcut."

            "If I can just get back to when I was in front of my school, I should be able to just take the long way home and not worry about going through here."
            play sound "gun.mp3"
            "{i}BANG!!!{/i}"
            play sound "gun.mp3"
            "{i}BANG!!!!{/i}"
            play sound "gun.mp3"
            "{i}BANG!!!!!!!{/i}"
            play sound "gun.mp3"
            "{i}BANG!!!!!!!!{/i}"
            "I killed myself a few more times."
            "Each time I did, the place where I was standing moved by a little bit."
            hide robber1
            "I lost sight of the guy after a single more jump, and after a few more I slowly started going backwards through the park, minute by minute."
            "I went from the middle of the park, to near a bench, to next to a pond, to next to a red tent, to behind a light post, to the front entrance of the park."
            "After a few more jumps, I had officialy made it to my destination. I was standing in front of the school!"
            scene school entrance evening
            with fade
            play music "classroom.mp3"
            "I did it!"
            "I got myself out of the scariest situation of my life using my power!"
            "Before I celebrated any longer, I realized just how exhausted I was."
            "Time travelling really wears you down."
            "{i}Grrruuummmmblllleeee...{/i}"
            "I could feel my stomach start to growl out at me in anger."
            "I forgot that I never got a chance to eat today."
            "Our group worked on our project through the lunch period."
            "I tried to decided if I was more tired or hungry, and I realized that the answer was the former."
            "I was so tired that I could barely keep my eyes open."
            "I slowly stumbled my way home and passed out on my bed the second my head hit the pillow."
            jump newish

label newish:
    scene bedroom
    with fade
    play music "bedroom.mp3"
    play sound "alarm.wav"
    "{i}BEEP! BEEP! BEEP!{/i}"
    "..."
    "UUggghhh"
    "It's time for school already? How is that even theoretically possible?"
    "I literally just got into bed a couple of seconds ago, surely there must be some mistake?"
    "I fumbled my way out of bed to turn off the alarm. My eyes were so heavy that I couldn't even see."
    "I finally reached my destination and punched the off button as hard as I could manage."
    "Stupid alarm..."
    "I walked over to my bedroom window and opened up my blinds."
    "Ouch! Well my alarm was definitely correct about the time. The sun beated against my skin and blinded me completely."
    "Unlike the other day, I wasn't running late at all, so I took my time getting ready."
    "After I finished with the daily routine, I went downstairs to eat some breakfast."
    scene kitchen
    with fade
    "I groggily walked over to the kitchen table and let out a big yawn."
    show jerry
    j "Sleepy today, are we?"
    "Oh crap. I totally forgot Jerry lived with us now."
    "I told him good morning and noticed that my mom was slaving away at the oven, cooking us breakfast."
    show mom at left
    m "Good morning honey! Did you sleep well enough?"
    "I told her that I did, even though that wasn't true at all."
    show mom happy at left
    m "That's wonderful sweety! I decided to make the three of us a big breakfast since Jerry is staying over for the time being."
    j "Yes, thank you very much for this wonderful meal. I've had such a nice time since I came here."
    m "Well you've been an amazing guest to have over!"
    m "Hey [name], you got home pretty late last night, is everything ok."
    "I thought back to all of the shenanigans I got into yesterday, but I saw no real reason to tell my mom about it, so I just told her that me and my friends were working on our project."
    "That wasn't really a lie either, we were working on the project for quite a long time."
    "In fact, we are almost completely done with it. If we had to perform it today we would probably be ready."
    j "Oh yes, the play. What is your group performing?"
    "I told him about BroBro and how we were doing an adaptation of the first part of it."
    j "Hmph, I'm not surprised that someone like you would put on a play of some third rate comic book."
    "I forgot just how much of a massive dick Jerry was."
    "I know his father just died, so I would cut him a little slack, but I decided I wouldn't just bend over and let him have all the fun himself."
    '"And what is your group performing then?" I asked him.'
    j "My group? Oh we are putting on the all time classic Romeo and Juliet."
    "Jerry was really going to make fun of me when his group was doing something so basic and uninspired?"
    menu:
        "That's a good choice for a play.":
            jump Romeo

        "That's the most boring and uninspired idea I've ever heard. It fits you perfectly!":
            jump Juliet

    label Romeo:
        "I decided against being mean and just lied to him about how much I liked the idea."
        j "Why how right you are!"
        j "It's a classic for a reason you know!"
        j "shakespeare truly was a genius, wasn't he?"
        j "A play about love and tragedy, it's the perfect one to perform for our class!"
        j "I'm playing the role of Romeo of course."
        j "I just know that after we perform this play, I'm gonna hit it big!"
        j "A talent agency will probably be able to sniff out my performance from across the world and I will become a world class actor!"
        "I'm not sure why Jerry thought that a talent agent would be attending our play, but I just let him live in his fantasy."
        jump newish1

    label Juliet:
        "Jerry's dad might have died, but I wasn't about to let him walk all over me."
        "Especially with how lame his play was gonna be."
        "I wouldn't be surprised in the least if half of the groups put on Romeo and Juliet."
        "I mean we never had to tell Mrs. Striker what our play was going to be about."
        "I told Jerry that his play was a bad and boring idea and I could tell that he didn't appreciate it."
        show jerry angry
        j "Well who asked you anyways?"
        j "Plus I'm not boring or uninspired at all!"
        j "I'm beautiful! A masterpiece! A true one of a kind!"
        j "So of course I would put on the greatest play ever put to paper!"
        j "Anything less than that would be beneath me!"
        j "You ignorant child! You have to have an extremely high IQ to understand the intricacies of Romeo and Juliet!"
        j "It is a play that would fly over your head you stupid baby!"
        j "It's about love and society and everything inbetween!"
        show mom happy at left
        m "You two are such good friends, aren't you?"
        m "I can tell by the way that you two are arguing!"
        m "Fake friends would be too scared to be honest with each other but you two cut right to the chase and I like it!"
        "I think my mom was misunderstanding the situation by quite a lot."
        "We weren't arguing because we were good friends, we were arguing because we hated each others guts!"
        show jerry
        j "Yes, you do have a good point."
        j "Me and [name] are quite close, aren't we?"
        "Jerry looked at me and gave me a creepy smile."
        "I wasn't sure what he was thinking but I just nodded my head in agreement."
        m "I just knew it!"
        jump newish1

label newish1:
    show mom happy at left
    m "Breakfast is ready you two!"
    j "Let me get that for you."
    "Jerry went over and picked up a couple of the dishes and brought them over to the table."
    "I wasn't about to let him be a better person than I was, so I followed suit and brought over a couple more dishes."
    m "Thank you so much for the help you two!"
    "I looked down and realized that my mom had really outdone herself this time."
    "Bacon, eggs, pancakes, waffles, cereal, toast, biscuits, cinnamon roles, apples, coffee, sausage, ham, everything that one could eat at a breakfast was sitting right here in front of me."
    "I piled on a plate to the brim, full of everything that my mom had made."
    "I then turned on the tv to see what was going on in the world."
    tv "The weather today will be sunny with a high of 76 degrees."
    "Boring, I have a weather app on my phone so this segment is useless to me."
    tv "Yet another case of mysterious deaths happened this morining."
    show jerry angry
    tv "At least 10 people were found dead last night with their facial features completely missing."
    tv "Experts still have no idea what is causing these mysterious deaths, as there seems to be no correlation between any of them."
    tv "There have been confirmed cases of this disease in Cuba, Mexico, Canada, Greenland, Ireland, The U.S., The U.K., Japan, North Korea, and Russia."
    tv "And those are just the confirmed deaths."
    tv "Police have gone on record saying that there is a very good chance that more people have been killed as well, they just haven't been found yet."
    "This is so strange. What could be causing all of this?"
    show mom angry at left
    m "[name], turn that off this instant!"
    "I could tell that my mom was mad and I knew why."
    "I looked over at Jerry and he looked mad."
    "Understandably so. His dad did die to this thing, I would be pissed as well."
    m "I think it's time for the two of you to go to school."
    m "Jerry, are you feeling ok? Would you rather stay home?"
    show jerry
    j "I'm completely fine! In fact I've never felt better!"
    "Jerry's face changed as soon as my mom asked him how he was doing."
    "I think it's true that Jerry hated his father, but I could tell that he was hurting nonetheless."
    "Me and Jerry quickly finished eating and headed off to school together."
    show classroom evening
    with fade
    "I got to class on time and it proceeded as it normally would."
    "Mrs. Striker taught us some new math thingy and I didn't pay attention at all."
    "That wasn't out of the ordinary for me, as I never really pay attention."
    "The reason I was zoned out this time was different than normal though."
    "Usually I'm just daydreaming about some fantasy I come up with or some movie I saw or some video game I've been playing, but this time was different."
    "I couldn't get my mind off of these deaths that keep on happening around the world."
    "What could have possibly caused something like that?"
    "Could it be some new type of disease? I guess it's possible but something made me doubt that."
    "Usually scientists and doctors can figure out what disease casuses something but they all seem to be stumped by this one."
    "That wouldn't be too out of the ordinary if we lived in the 1500's, but we don't."
    "We live in the golden age of technology and medicine, if it was a disease I think that we would be able to figure it out."
    "I think that it may be caused be something else. Something more...Sinister."
    "I used to not believe in the supernatural, but after meeting Dolus and learning about God and everything, I now wonder if something like that could be the cause."
    "Whatever the case, there wasn't really anything I can do about it."
    "It's not like I could use my time travel powers to go back and see what caused it."
    "From my understanding, the people were completely fine one second and then dead the next."
    "I shouldn't worry about it. If you can't do anything about a problem then there is no reason to worry about it."
    show yuuki
    y "Hello mortal. Lost in though, are you?"
    y "Well anyways, Darius wanted to tell you that the four of us are meeting up after school at my place to do one last rehearsal of the play."
    '"Wait, at your house?" I asked her.'
    y "Yes, is that a problem?"
    '"No" I said in a matter of fact sort of tone.'
    "It wasn't a problem, I was just surprised."
    "For some reason I always imagined that Yuuki lived in some random trash can in an alley way."
    "She's so delusional that she could probably imagine that as a hidden lair of sorts."
    y "Good."
    y "Well come on now! Darius and Winrey have already left for their perilous journey to my headquarters!"
    y "I told them where to go but I forgot to tell you so I figured we could just travel together!"
    y "It's safer with two people you know! Going alone could be dangerous!"
    "I didn't really care what her reasoning was, but I was glad to have a travel buddy so I wouldn't have to walk alone."
    "Last time I walked alone when the sun was setting I met that one shadowy figure guy..."
    "Yuuki and I left the school and walked to her house together."
    scene japanese setting 2206x1080
    with fade
    play music "japan.mp3"
    "..."
    "Uhhhh...."
    "Is this...Is this the right place?"
    "I couldn't believe my eyes."
    "We live in America, but it looked like we traveled back in time to Feudal Japan."
    show yuuki happy
    y "Do you like it mortal?"
    "I wasn't sure if like was the right word for how I was feeling."
    "It was...different, that's for sure."
    y "I can tell by the facial expressions that you are producing that you do in fact enjoy the looks of my homestead."
    menu:
        "Why does your house look like this?":
            jump Japanese

        "It's awesome!":
            jump boring1

    label Japanese:
        show yuuki
        y "Ahh, well it's sort of a long story, but I suppose that we do have the time to tell it."
        y "The story begins 25 years ago when my father, Gorbis Fawklberry, came to America for the first time."
        y "You see, his parents were both from America, but they had to move to Japan in the 1950's due to the end of World War 2 due to business reasons."
        y "They lived there for a few years until they gave birth to my father, a lowly mortal with no special powers to call his own."
        y "He grew up in an old village that was lost to time, and all of the houses there looked exactly like this one."
        y "My father lived there for a few decades, where he worked many jobs of many different types and professions."
        y "He was a farmer, a mailman, a cook, and a gangster."
        y "How he ended up as a gangster I have no earthly idea, but it is at that job where our story begins."
        y "His group was at odds with the Yakuza, one of the scariest groups in all of Japan."
        y "They fought many of battles, none of which involved using magic or anything of the like."
        y "One night my father was stuck in a bloody battle with a couple of Yakuza members all by himself."
        y "Things weren't looking good for my father."
        y "He shot and punched and stabbed and kicked as much as he good, but as he was just a mortal, his body eventually gave out."
        y "His legs gave in and he hit the ground hard."
        y "There was still one Yakuza member standing, and he was pissed at my father."
        y "The Yakuza man rushed my father with a broken bottle, with the full intention of killing him, but right before he could land the killing blow, something amazing happened."
        y "The Yakuza member stopped right in his tracks, took the bottle to his own throat, and scliced it right open."
        y "That's right, the Yakuza member killed himself right in front of my father."
        y "He was confused, of course, but right before he could do anything else, he heard a voice."
        y "The voice was that of a woman, and it told my father to not be afraid."
        y "She said that she had used her super powers to force the man to kill himself."
        y "My father didn't believe her of course, so she demonstrated her powers on him."
        y "She made him get off the floor and start breakdancing."
        y "After that little exchange, my father had no other plan of action besides believing her."
        y "The next thing my father asked is why him? Why did she choose to save him in that moment."
        y "The mysterious woman said that it was because she used another one of her powers to read his mind and heart."
        y "She found out by doing so that he was a kind soul with a good history who just got caught up in a bad place."
        y "She also read all of the other peoples souls and found that they were bad people, who killed and raped and robbed without remorse."
        y "In that moment she decided to save him."
        y "The two started to see each other regurarly, and that's the story of how my father met her wife, my mother."
        y "They lived in a house that looked just like this for over 20 years."
        y "Well one day, my father screwed up big time, and both his own gang as well as the Yakuza were after him."
        y "My mother, for all of her power, was unable to stop them as she was getting old and fragile."
        y "My father had no choice but to flee the country with nothing on them besides the clothes on their back."
        y "Right before they left however, my mother used the last bit of her strength to make a mental copy of their home."
        y "Well, they eventually ended up here in this town."
        y "When they got here, my father realized that they had no money to buy a house, as they used all of their cash to get to America."
        y "My mother told him to not be afraid, and she guided him to an empty lot in an abandoned part of the town."
        y "She took the copy of the house that she had made, and placed it right here, onto this lot."
        y "A few years later I was born right here in this very house."
        y "The town started to grow up around me, and it became my home."
        y "Everything was great until that fateful day..."
        show yuuki angry
        y "One day, about a decade ago, my mother fell ill."
        y "She had none of her powers left so she couldn't heal herself, so she had no choice but to go to a special hospital across the country that specialized in her rare disease."
        y "I went there with my parents and we stayed there for over a year until my mother passed."
        y "It was hard on me, but it was much harder on my father."
        y "He didn't say a word to me for over 6 months."
        y "During that time we stayed with my grandparents, who had also moved back to America a few years ago."
        y "They took care of me until my father was somewhat back to normal."
        y "After they were sure that he was well enough to take care of me on his own again, we moved back here."
        y "Well, we were going to move back here, but right before we could something terrible happened."
        y "I woke up one night, right before we were about to move back, to a loud sound coming from my fathers makeshift bedroom."
        y "I ran to his side as quick as I could, but it was too late, my father was dead."
        y "He killed himself."
        y "I stayed with my grandparents for a couple of years, but my grandmother died two years ago from a heart attack."
        y "And then about a month ago, my grandpa died of old age."
        y "I had no more family to go to, but I was 18 so I was old enough to live on my own."
        y "My grandparent had also left me a few thousand dolllars, so I took that money and moved back here, and that is when I met you guys!"
        "..."
        "Yuuki always lies to me, so it's hard to know if she was telling the truth or not."
        "I figured that at the very least it was partially true."
        "I believed that her family was all dead and that she came back here alone."
        "I also believed the part about her dad living in Japan and meeting her mom there."
        "It was the only way to explain why her house looked like this."
        "What I had a hard time believing was the part about her mom having powers."
        "Yuuki has yet to show me any sign of her powers, so I was pretty sure she was lying about that."
        "Still though, I have powers, so I guess it's possible for other people to possess them as well."
        "Whatever the truth is, I was glad that Yuuki was nice enough to share her story with me."
        jump newish2

    label boring1:
        "I decided to tell her how awsome I found her house to be."
        y "Thanks, it is pretty cool, isn't it?"
        y "You wanna know how I got it?"
        y "Well, the truth is that I won it in a deathmatch."
        y "Yeah, you heard me right, a deathmatch."
        y "Me and 49 other people were brought to an abandoned island and forced to fight to the death."
        y "I obviously won in a landslide, as I have superpowers."
        y "My prize was this house, as well as 1 billion dollars."
        y "I'm so nice that I decided to donate the money to the local Wizard's for hope charity, but I did keep the house."
        y "My parents died when I was young so I lived by myself."
        y "I moved her and that's when I met you guys!"
        "I highly doubted that her story was true, but I decided not to question her further."
        "I was still curious about how she actually got the house, but I guess that will just have to remain a mystery."
        jump newish2

label newish2:
    show winrey casual at left
    show darius at right
    w "Hey guys, I hope it's ok that we got here before you did Yuuki."
    da "Yeah we didn't know what to do so we just stayed here at the door."
    show yuuki
    y "That is completely fine, mortals."
    y "But now that we are all here I, Yuuki Fawklberry, shall open the door!"
    "She made it sound a lot more epic than it actually was, but that's exactly what she did, she opened the door to her house."
    w "This house is so amazing Yuuki! How did you get it?"
    y "That is too long of a story for me to tell twice in one day!"
    y "you can ask [name] if you are so curious."
    "I told them the story that Yuuki had told me earlier."
    da "Dang, that's a pretty crazy story Yuuki."
    y "Yes, I know that it might sound strange to a non-magic user such as yourself, but I assure you it is the truth!"
    w "Well, I guess we should get started on our final rehearsal."
    y "Yes! Let us commence the play!"
    "We practiced the play for another hour or so until we had the thing down completely."
    "All of us knew our lines and where we were supposed to move and how we were supposed to act, it was pretty great if I do say so myself."
    "After we had practiced for awhile, I needed to use the bathroom, so I asked Yuuki where it was."
    y "This house moves all of the time, so there is no way to tell where the bathroom is located at!"
    y "Plus I never have to urinate, as my body has a spell put on it that negates the need for relief."
    y "But I'm sure if the two of us went together, we could find it!"
    y "Plus I need to get something out of the kitchen, so I will accompany you as well."
    hide winrey casual
    hide darius
    "Yuuki and I walked around the house for what seemed like forever."
    "Yuuki's house was much bigger than I originally thought."
    "There were rooms everywhere, and they had all sorts of weird items inside."
    "Wands, hats, torture devices, work out machines, video game consoles, her house had it all."
    "Wait, did I say torture devices?"
    "Yep her house had a bunch of those."
    "None of them had any blood on them so I decided not to call the police, but I did decide to never get on Yuuki's bad side."
    "After a few minutes, we eventually found the bathroom."
    y "It is here that I must leave you mortal, I will travel to the kitchen to get my things."
    y "You should probably head back to Winrey and Darius by yourself, as it will take me a few minutes to take care of business."
    hide yuuki
    "Yuuki left and I quickly did my business."
    "Ahhhh, sweet relief."
    "I pulled my pants up, flushed the toilet, washed my hands, and made my way back to Winrey and Darius."
    "I made it to the door of the room that we were practicing without any problems, and sure enough I made it back before Yuuki."
    "I was about to open the door, when I heard some whispering coming from inside."
    w "Don't you think we should tell them?"
    da "Tell them what?"
    w "You idiot!"
    da "Why am I an idiot?"
    w "You seriously don't know what you think we should tell them?"
    da "Oh, you mean how I like to dip my chicken wings in peanut butter?"
    w "No you moron!"
    da "Then what?"
    w "Shouldn't we tell them that we're dating?"
    "..."
    "I couldn't believe my ears."
    "Darius and Winrey are...dating?"
    "..."
    "......."
    "Wait..."
    "Why arent I upset?"
    "No seriously, I didn't seem to care at all that they were dating."
    "In fact, the only thing I felt was happiness for my friend Darius."
    "I have had a crush on her for awhile, but after we started to be in a group together, I don't know."
    "I guess I just stopped thinking about her in that way."
    "I think that I might have had a crush on the idea of Winrey."
    "The perfect girl."
    "The girl who was the class president and who was on the soccer team."
    "The girl with perfect test scores, the girl who everyone adored."
    "But I met her and started to talk to her, and I realized that just wasn't who she was."
    "She was a normal person just like anybody else."
    "And once I realized that, I think I stopped liker her so much."
    "Probably due to the fact that we had no chemistry."
    "We didn't talk outside of our group at all."
    "Darius, on the other hand, talked to her all the time."
    "The two of them were always together, so it makes sense that they ended up dating."
    "It also makes sense that they hid it from me."
    "Darius knew that I liked Winrey, so he probably didn't want to hurt my fellings."
    "I'm grateful that he cared about how I felt that much, but I did wish he was honest with me..."
    da "Not yet..."
    w "Why not?"
    da "It's just, I don't want to hurt his feelings..."
    w "You mean [name]?"
    da "Yeah..."
    w "..."
    da "..."
    w "Fine..."
    w "But you have to tell him at some point, you know that right?"
    da "Yeah I know, but just not right now, ok?"
    da "Anyways, there was something else I wanted to ask you about."
    w "Shoot me."
    da "Well, I was wondering when I was gonna get to go to your house and meet your family."
    w "......."
    da "Is something wrong?"
    w "..."
    da "Hey, why are you tearing up?"
    w "....."
    da "Is it something I said."
    w "...."
    da "Listen, I'm sorry. I didn't mean anything by it."
    w "......"
    w "...I guess I should probably tell you..."
    da "Tell me what?"
    w "Well, you remember back to when we were going to meet at someones house to work on the project?"
    da "Yeah?"
    w "Well, the truth is we couldn't go to my house for a reason..."
    da "Ok, what's the reason?"
    w "Before I tell you, I need to make sure you know that this is just a secret between the two of us."
    w "You can't tell [name] or Yuuki or anybody, got it?"
    da "Ok, sure."
    w "No, I need you to promise that you won't tell anyone."
    da "I promise."
    w "You swear to God that you won't tell?"
    da "I swear to God and my parents and everyone else!"
    w "Ok..."
    w "Well...The truth is..."
    w "I'm homeless."
    da "..."
    da "What?"
    w "I don't have a home, I live in a red tent in the old park,"
    da "No... that... that can't be."
    w "it's the truth."
    da "But how? You're always so clean and...and..."
    w "I use the shower at school every day. It's a perk of being class president."
    da "But how did you become homeless in the first place?"
    w "Long story short, my dad went through some hard times and lost the house."
    w "My mom died a long time ago and now my dad is way too weak to work."
    w "He is also too prideful to ask for help, so we live in a tent."
    w "Or, we did live in a tent."
    w "He's dead now."
    w "Died of natural causes, perks of living outside through the winter I supposed."
    da "Oh my God... I'm so sorry..."
    w "It's fine, I get by."
    da "Well, there's no reason for you to live in the tent, you know that right?"
    w "What do you mean?"
    da "Are you serious? I live in a freaking empty mansion!"
    da "There is plenty of rooms for you to stay in!"
    w "Darius, I can't ask that of you..."
    da "Are you serious? I'm your boyfriend! I'm supposed to help you out!"
    w "But..."
    da "No but's! You are living with me and that's final!"
    w "Darius..."
    w "Thank you... Thank you so much!"
    w "I could never begin to repay you!"
    da "You don't have to repay me, we are together now, we are supposed to help each other out when we need it."
    "I could hear Winrey start to cry uncontrollably, and I could hear Darius doing his best to comfort her."
    "Man, I couldn't believe it..."
    "Winrey is homeless?"
    "She's been living in a tent this whole time and I never knew..."
    "I'm a horrible friend."
    "I would have offered to let her live with me, but it's probably for the best that she lives with Darius."
    "I've got my hands full with Jerry, and the two of them are dating, so it makes sense that she would want to live with him."
    "Also, why do all of my friends, including myself, have sappy backstories and dead parents?"
    "These last few weeks have felt like a crappy soap opera."
    da "You know what...maybe we should tell them..."
    da "I mean, if we are going to be living under the same roof, they would probably find out eventually anyways."
    w "I agree completely. It's best if they hear it from us instead of finding out on there own."
    show yuuki at left
    y "Tell us what?"
    "Oh crap! Yuuki scared the living crap out of me."
    "I was listening in on there conversation so hard that I didn't even hear her approaching."
    "Yuuki walked into the room in front of me, and I followed suit."
    show darius
    show winrey casual at right
    da "Uhhh...Well, you see..."
    w "Me and Darius are..."
    y "Dating?"
    show darius happy
    da "Yeah! How did you know that?"
    y "I mean it was kind of obvious... You two have been acting all lovey dovey recently."
    y "Plus did you really expect you could hide anything from I, Yuuki Helpopit?"
    y "I do have the power to read minds you know. I could have figured it out on my own if I wanted to."
    y "But I supposed I respect you two mortals too much to go prying around in your personal lives."
    show darius happy
    da "Yeah, I guess we should have known you would find out Yuuki..."
    da "Hey [name], you're ok with it, aren't you."
    "I was ok with it actually."
    menu:
        "Yep, congratulations!":
            jump Congratulations

        "I already knew.":
            jump honesty

    label Congratulations:
        "I decided to just tell him that I was cool with it and congratulate him as well."
        "I was considering telling him that I already knew, but I figured there would be no point in that."
        "Why should I let him know I overheard their conversation?"
        "I'm sure Winrey wouldn't want me to know that she's homeless. If she did she would have told me."
        da "Great! I was hoping you would be cool with it!"
        da "Well I guess the next thing we have to do is perform the play, right?"
        w "Yep, it's next week."
        da "Alright then, I guess I will see you guys then."
        da "You coming Winrey? We need to go get your stuff and move it to my house."
        w "Yeah, let's go!"
        y "Wait, move what stuff to your house?"
        show darius angry
        show winrey angry casual at right
        da "..."
        w "..."
        "I couldn't believe that Darius had let something so big slip out of his mouth like that."
        "He had just accidently told Yuuki and I the truth."
        w "I guess it's ok for you guys to know the truth."
        y "What truth?"
        w "Well...The truth is...I'm homeless."
        w "Or, at least I was homless up until a couple of minutes ago."
        w "It's a long story, but to make it quick, my dad lost his job and we couldn't afford the house anymore."
        w "My mom has been dead for a while and I'm to busy to work, so we had no choice but to live in a tent."
        y "So what?"
        w "...Huh?"
        y "So what that you were homeless?"
        y "That doesn't make you any less of a person you know."
        w "I know that, but it's still embarrassing."
        y "So what? Who cares what other people think about you?"
        y "It's over now, isn't it? You are staying with Darius, end of story."
        w "Yeah, I guess so, but still..."
        y "Still what?"
        y "It's nothing to be embarassed about, you know I'm homeless right?"
        w "..."
        da "..."
        "..."
        "I know Yuuki has a lying problem, but I think she should know better than to tell people that she is homeless when we are in her own house."
        y "Well the point is that I don't think anybody will think less of you as a person, so don't worry about it!"
        w "Ok...you're right."
        show winrey casual at right
        w "Thanks for that Yuuki..."
        w "I consider you to be a good friend of mine."
        y "I do as well, though I'm not supposed to befriend mortals, we can just keep it our little secret."
        w "That sounds good."
        show darius
        da "Well I'm glad we got all that out of the way."
        w "Yeah I feel like a huge weight has been lifted from my shoulders."
        w "Thank you so much you guys. I really like all of you. I mean it."
        da "And we like you too."
        y "Yes, I like you, even if you don't have any hidden powers!"
        da "Alright, well we're heading out."
        y "Safe travels my friends! Do not get eaten by a Pixotacious on your way back!"
        da "We'll be sure to keep that in mind!"
        y "Well mortal, I guess I will see you later as well."
        "I told everybody goodbye and headed home for the day."



        jump newish3

    label honesty:
        "I decided to tell him that I already knew that they were dating."
        "I know that it's not ok to eavesdrop in on a conversation like I did, so I thought it would be best to just come clean."
        da "Wait, you did? How?"
        y "Isn't it obvious Darius? [name] has powers just like I do! Isn't that right [name]?"
        menu:
            "Yep, I've got powers.":
                jump truthbomb

            "No, I heard you guy's talking a second ago.":
                jump realtruth

        label truthbomb:
            show yuuki happy at left
            y "I just knew it! What powers do you possess, oh Great One?"
            menu:
                "Time-Travel powers.":
                    jump actualtruth

                "Flight.":
                    jump flight

                "Mind-Reading abilities.":
                    jump Mindreading

            label actualtruth:
                "I can't believe I did it but I actually told them the truth."
                y "Wow! That's so cool!"
                da "Haha, you usually don't joke around like that [name]!"
                "I knew they wouldn't actually believe me, which is why I was ok with telling them."
                "Yeah sure, Yuuki might believe me, but I'm sure she would forget what I said anyways."
                "Plus I'm sure she won't ask me to prove it, as she hasn't done a great job at proving her own powers herself."
                da "Well I guess the next thing we have to do is perform the play, right?"
                w "Yep, it's next week."
                da "Alright then, I guess I will see you guys then."
                da "You coming Winrey? We need to go get your stuff and move it to my house."
                w "Yeah, let's go!"
                y "Wait, move what stuff to your house?"
                show darius angry
                show winrey angry casual at right
                da "..."
                w "..."
                "I couldn't believe that Darius had let something so big slip out of his mouth like that."
                "He had just accidently told Yuuki and I the truth."
                w "I guess it's ok for you guys to know the truth."
                y "What truth?"
                w "Well...The truth is...I'm homeless."
                w "Or, at least I was homless up until a couple of minutes ago."
                w "It's a long story, but to make it quick, my dad lost his job and we couldn't afford the house anymore."
                w "My mom has been dead for a while and I'm to busy to work, so we had no choice but to live in a tent."
                y "So what?"
                w "...Huh?"
                y "So what that you were homeless?"
                y "That doesn't make you any less of a person you know."
                w "I know that, but it's still embarrassing."
                y "So what? Who cares what other people think about you?"
                y "It's over now, isn't it? You are staying with Darius, end of story."
                w "Yeah, I guess so, but still..."
                y "Still what?"
                y "It's nothing to be embarassed about, you know I'm homeless right?"
                w "..."
                da "..."
                "..."
                "I know Yuuki has a lying problem, but I think she should know better than to tell people that she is homeless when we are in her own house."
                y "Well the point is that I don't think anybody will think less of you as a person, so don't worry about it!"
                w "Ok...you're right."
                show winrey casual at right
                w "Thanks for that Yuuki..."
                w "I consider you to be a good friend of mine."
                y "I do as well, though I'm not supposed to befriend mortals, we can just keep it our little secret."
                w "That sounds good."
                show darius
                da "Well I'm glad we got all that out of the way."
                w "Yeah I feel like a huge weight has been lifted from my shoulders."
                w "Thank you so much you guys. I really like all of you. I mean it."
                da "And we like you too."
                y "Yes, I like you, even if you don't have any hidden powers!"
                da "Alright, well we're heading out."
                y "Safe travels my friends! Do not get eaten by a Pixotacious on your way back!"
                da "We'll be sure to keep that in mind!"
                y "Well mortal, I guess I will see you later as well."
                "I told everybody goodbye and headed home for the day."
                jump newish3

            label flight:
                "I decided to lie and just tell them I could fly as a joke."
                "I know that they wouldn't believe me no matter what I said, but to be safe I shouldn't reveal my actual power."
                y "Flight huh?"
                y "Prove it."
                "..."
                w "He is just kidding around Yuuki! He can't actually fly."
                y "How can you be so sure, huh?"
                w "Well...If he actually could fly, don't you think he would have used that to get to school every day?"
                y "Not if it was a secret."
                w "I guess so, but people don't have powers like that!"
                show yuuki angry at left
                y "I do!"
                w "..."
                y "I promise! I can't prove it right now because my mana is low, but one day I will show you guys my true power."
                da "I can't wait to see that!"
                da "Well I guess the next thing we have to do is perform the play, right?"
                w "Yep, it's next week."
                da "Alright then, I guess I will see you guys then."
                da "You coming Winrey? We need to go get your stuff and move it to my house."
                w "Yeah, let's go!"
                y "Wait, move what stuff to your house?"
                show darius angry
                show winrey angry casual at right
                da "..."
                w "..."
                "I couldn't believe that Darius had let something so big slip out of his mouth like that."
                "He had just accidently told Yuuki and I the truth."
                w "I guess it's ok for you guys to know the truth."
                y "What truth?"
                w "Well...The truth is...I'm homeless."
                w "Or, at least I was homless up until a couple of minutes ago."
                w "It's a long story, but to make it quick, my dad lost his job and we couldn't afford the house anymore."
                w "My mom has been dead for a while and I'm to busy to work, so we had no choice but to live in a tent."
                y "So what?"
                w "...Huh?"
                y "So what that you were homeless?"
                y "That doesn't make you any less of a person you know."
                w "I know that, but it's still embarrassing."
                y "So what? Who cares what other people think about you?"
                y "It's over now, isn't it? You are staying with Darius, end of story."
                w "Yeah, I guess so, but still..."
                y "Still what?"
                y "It's nothing to be embarassed about, you know I'm homeless right?"
                w "..."
                da "..."
                "..."
                "I know Yuuki has a lying problem, but I think she should know better than to tell people that she is homeless when we are in her own house."
                y "Well the point is that I don't think anybody will think less of you as a person, so don't worry about it!"
                w "Ok...you're right."
                show winrey casual at right
                w "Thanks for that Yuuki..."
                w "I consider you to be a good friend of mine."
                y "I do as well, though I'm not supposed to befriend mortals, we can just keep it our little secret."
                w "That sounds good."
                show darius
                da "Well I'm glad we got all that out of the way."
                w "Yeah I feel like a huge weight has been lifted from my shoulders."
                w "Thank you so much you guys. I really like all of you. I mean it."
                da "And we like you too."
                y "Yes, I like you, even if you don't have any hidden powers!"
                da "Alright, well we're heading out."
                y "Safe travels my friends! Do not get eaten by a Pixotacious on your way back!"
                da "We'll be sure to keep that in mind!"
                y "Well mortal, I guess I will see you later as well."
                "I told everybody goodbye and headed home for the day."
                jump newish3

            label Mindreading:
                "I decided to lie and just tell them I could fly as a joke."
                "I know that they wouldn't believe me no matter what I said, but to be safe I shouldn't reveal my actual power."
                y "Mindreading?"
                y "That's an awesome power!"
                y "I have that one as well!"
                y "I would ask you to read my mind to prove it, but everyone know that two mindreaders can't read each others minds."
                da "I've never know you to joke around like that [name]!"
                w "Yeah, you're usually so serious, it's not like you."
                "I'm not always serious..."
                da "Well I guess the next thing we have to do is perform the play, right?"
                w "Yep, it's next week."
                da "Alright then, I guess I will see you guys then."
                da "You coming Winrey? We need to go get your stuff and move it to my house."
                w "Yeah, let's go!"
                y "Wait, move what stuff to your house?"
                show darius angry
                show winrey angry casual at right
                da "..."
                w "..."
                "I couldn't believe that Darius had let something so big slip out of his mouth like that."
                "He had just accidently told Yuuki and I the truth."
                w "I guess it's ok for you guys to know the truth."
                y "What truth?"
                w "Well...The truth is...I'm homeless."
                w "Or, at least I was homless up until a couple of minutes ago."
                w "It's a long story, but to make it quick, my dad lost his job and we couldn't afford the house anymore."
                w "My mom has been dead for a while and I'm to busy to work, so we had no choice but to live in a tent."
                y "So what?"
                w "...Huh?"
                y "So what that you were homeless?"
                y "That doesn't make you any less of a person you know."
                w "I know that, but it's still embarrassing."
                y "So what? Who cares what other people think about you?"
                y "It's over now, isn't it? You are staying with Darius, end of story."
                w "Yeah, I guess so, but still..."
                y "Still what?"
                y "It's nothing to be embarassed about, you know I'm homeless right?"
                w "..."
                da "..."
                "..."
                "I know Yuuki has a lying problem, but I think she should know better than to tell people that she is homeless when we are in her own house."
                y "Well the point is that I don't think anybody will think less of you as a person, so don't worry about it!"
                w "Ok...you're right."
                show winrey casual at right
                w "Thanks for that Yuuki..."
                w "I consider you to be a good friend of mine."
                y "I do as well, though I'm not supposed to befriend mortals, we can just keep it our little secret."
                w "That sounds good."
                show darius
                da "Well I'm glad we got all that out of the way."
                w "Yeah I feel like a huge weight has been lifted from my shoulders."
                w "Thank you so much you guys. I really like all of you. I mean it."
                da "And we like you too."
                y "Yes, I like you, even if you don't have any hidden powers!"
                da "Alright, well we're heading out."
                y "Safe travels my friends! Do not get eaten by a Pixotacious on your way back!"
                da "We'll be sure to keep that in mind!"
                y "Well mortal, I guess I will see you later as well."
                "I told everybody goodbye and headed home for the day."
                jump newish3
        label realtruth:
            "I decided that it would be for the best to just come clean and let them know I heard their conversation."
            "They probably would be mad, but I didn't want to hold that secret against them."
            da "Wait...you heard all of that?"
            da "How much did you hear?"
            '"Everything, I told him."'
            da "..."
            w "Did you...did you hear about my living situation?"
            "I told them that I did."
            show darius angry
            show winrey angry casual at right
            da "..."
            w "..."
            w "That's fine."
            w "I guess it's ok for you guys to know the truth."
            y "What truth?"
            w "You can tell her [name], since you're an expert on the subject."
            "I could tell that Winrey was upset, and I couldn't really blame her."
            "I caught Yuuki up on the whole situation."
            "Yuuki just stood there for a second, without making a sound."
            y "So what?"
            w "...Huh?"
            y "So what that you were homeless?"
            y "That doesn't make you any less of a person you know."
            w "I know that, but it's still embarrassing."
            y "So what? Who cares what other people think about you?"
            y "It's over now, isn't it? You are staying with Darius, end of story."
            w "Yeah, I guess so, but still..."
            y "Still what?"
            y "It's nothing to be embarassed about, you know I'm homeless right?"
            w "..."
            da "..."
            "..."
            "I know Yuuki has a lying problem, but I think she should know better than to tell people that she is homeless when we are in her own house."
            y "Well the point is that I don't think anybody will think less of you as a person, so don't worry about it!"
            w "Ok...you're right."
            show winrey casual at right
            w "Thanks for that Yuuki..."
            w "I consider you to be a good friend of mine."
            y "I do as well, though I'm not supposed to befriend mortals, we can just keep it our little secret."
            w "That sounds good."
            show darius
            da "Well I'm glad we got all that out of the way."
            w "Yeah I feel like a huge weight has been lifted from my shoulders."
            w "Thank you so much you guys. I really like all of you. I mean it."
            da "And we like you too."
            y "Yes, I like you, even if you don't have any hidden powers!"
            da "Well I guess the next thing we have to do is perform the play, right?"
            w "Yep, it's next week."
            da "Alright then, I guess I will see you guys then."
            da "You coming Winrey? We need to go get your stuff and move it to my house."
            w "Yeah, let's go!"
            da "Ok, see you two later!"
            w "Yeah, bye guys!"
            y "Safe travels my friends! Do not get eaten by a Pixotacious on your way back!"
            da "We'll be sure to keep that in mind!"
            y "Well mortal, I guess I will see you later as well."
            "I told everybody goodbye and headed home for the day."
            jump newish3

label newish3:
    scene classroom
    with fade
    play music "classroom.mp3"
    "It was a few days after we had met at Yuuki's house, and today was the big day."
    "Today is when we give out performance!"
    "I got to class alittle earlier than usual, with the goal of getting in a last minute practice session."
    "I knew all of my lines perfectly, but I really didn't want to screw it up at all."
    "Of course I knew that wouldn't be a problem at all, as I can just go back in time if I do happen to screw up."
    "But I would rather save that for emergencies instead of using it for whenever I feel like it."
    "Yuuki, Darius, and Winrey all got to class early as well."
    "The four of us did a whole run through the entire play before anybody else got there."
    "After we all felt confident in our parts, we took our seats and waited for the class to start."
    "A few minutes passed by and everyone made it on time and took their seats."
    "Mrs. Striker walked into the room and got up in front of the class."
    show striker
    s "Alright class, today is a pretty big day. It's the day when you all show us what you have been working on all semester."
    s "Without further ado, do we have any volunteers to go first."
    "I shot my hand up in the air as soon as the final words of her sentence left her mouth."
    "I could tell that everybody in the class besides Darius was pretty shocked to see me volunteer to go first."
    "I understand why they would be so surprised. I am pretty introverted and shy so they wouldn't think that I would be the volunteer type."
    "But the truth is, my shyness is the reason that I volunteer to go first."
    "I get really bad anxiety from public speaking, and the days leading up to these sort of things always leave me a nervous wreck."
    "When I was younger I would always go last, and throughout the entire class, I would always be super anxious."
    "I would be sitting there thinking about all the terrible ways in which I could screw up, and how I was going to fail."
    "I would do this so much that I would never even listen to anybody elses speeches, and I would never enjoy myself."
    "And my anxiety always became a self-fulfilling prophecy. I would always to terribly in my speeches do to how nervous I was."
    "That's when I realized something. I have to present at some time, that's unavoidable."
    "But going later only serves to make my anxiety last longer."
    "If I go first, I can get my speech out of the way, and afterwards I won't be nervous at all."
    "After I finish presenting, I can just sit back and enjoy everyone else's presentation."
    "I've also learned that teachers seem to grade easier on the first couple of people."
    "They seem to appreciate the effort it takes to volunteer so they won't be as harsh on you."
    "Also, everyone else is also worried about their own speeches, so no one is really paying attention to you."
    "That means that if you do screw up, not as many people will notice."
    "I've told Darius about my reasoning before, and he seems to agree with me, as now he always tries and volunteer to go as early as possible."
    show striker happy
    s "Oh wow! Good for you [name]! I'm proud to see you show some initiative by going first."

    "Mrs. Striker left the front of the classroom and sat down at an empty desk at the back of the class."
    hide striker
    show yuuki
    show darius at right
    show winrey school at left
    "The four of us got up in front of the class, and did what we had rehearsed."
    "Before we actually started the play, Darius told the class what we would be performing, and gave some backstory about BroBro."
    "Though I could barely see her from where I was standing, As Jerry was sitting right in front of her, I could still hear Mrs. Striker's voice."
    s "What an interesting idea for a play!"
    show darius happy at right
    da "Thanks! I guess we will start now."
    "Darius stepped back and took his place in the line."
    "I knew that it was my time to get up in front of the class and give my first set of lines."
    '"Hello, little boy, may I help you with something?"'
    "Darius got up next to me, and with his best little kid voice, he said his lines."
    show darius at right
    da "Are...are you Brother Broseph?"
    '"Yes, but all of my friends like to call me BroBro for short."'
    da "Ok...is it true that you can detect and kill vampires?"
    '"Well why would a young boy such as yourself ask such questions?"'
    da "My...my dad is a vampire."
    '"Are you sure of this? Maybe he just prefers to stay up late at night and likes his meat a little on the bloody side."'
    da "That's the problem Brother...I mean BroBro! He likes his meat a little too bloody!"
    '"You mean like, rare?"'
    da "No I mean like raw! He prefers his meat to be attached to people while they are still alive!"
    '"Are you sure of this?"'
    da "Positive! In fact he...he killed my own mother! And many other innocent people!"
    da "Please BroBro, you have to save him!"
    '"I will come with you to see your father, and if what you have said is true, I will take care of him."'
    "So fare the play is going perfectly."
    "Everyone seemed to find Darius's kid voice rather funny, as you would hear giggling at every one of his lines."
    "That was completely expected, as his part is rather funny."
    "We started the next scene which involves me talking to my girlfriend Lolo."
    show winrey angry school at left
    w "Oh BroBro, please don't go!"
    "Winrey gave Lolo a hard southern accent, which was strange as this story doesn't take place anywhere near the south."
    "But everyone else seemed to like it, as they all laughed at her first line as well."
    '"I am deeply sorry Lolo, but I must go. This little boy needs my help."'
    w "Oh BroBro, please be careful! If you get killed I swear to God I'll kill you!"
    '"I promise you that everything will go fine, goodbye for now, my beloved."'
    show winrey school at left
    "I was surprised at just how small of a part Winrey had in this play."
    "In the original story, Lolo has a much bigger part that involves her getting kidnapped by the vampire dad."
    "Darius said that he had to cut all of that for time, and I was ok with that."
    "We moved on to the next scene, which involves me confronting the vampire."
    '"So, you must be the vampire that this young child was talking about."'
    y "Hahahahaha! Yes! I am a vampire! And I will use my vampire powers to kill you!"
    "I respect Darius and he is a lot of good things, but screenplay writer wasn't one of them."
    "The play had dialogue that sounded like it was made by a robot from the 90's."
    "I guess he did do a better job than I would have, but I can't help but find the whole thing rather cheesy."
    "Oh well, I guess I should be thankful that he was willing to do it at all."
    "I stopped my negative thinking and got back to the play at hand."
    '"Well than I, BroBro, shall defeat you where you stand!"'
    '"Get ready to die, evildoer!"'
    show yuuki happy
    y "HAHAHAHAHHAHAHHAHAHHAHAHHAHAH"
    y "Do you, a lowly human really think that you can defeat an actual vampire?"
    '"Maybe not, but I do have one thing that you do not have!"'
    y "And what is that?"
    '"The power of friendship!"'
    y "..."
    y "Are you serious?"
    '"Dead serious! I have this young boy, and my girlfriend Lolo. With them by my side, I know that I cannot lose!"'
    y "I guess we shall see about that! Well then, come at me BroBro!"
    "I rushed towards Yuuki and threw out a fake punch."
    y "Ouch! How dare you hit someone of my calibur!"
    y "You shall pay for that with your life BroBro!"
    "Yuuki then rushed me and threw out a couple of fake punches while screaming about how useless I was."
    "I hit the ground as hard as I could, and the final scene of the play began."
    y "Hahaha! I told you that you could not defeat me!"
    show darius angry at right
    da "Hey dad!"
    y "Wha..."
    "{i}Bonk!!!{/i}"
    "Darius hit Yuuki over the head with a rubber hammer that we found at a local store."
    show yuuki angry
    y "Ouch! How dare you strike your own father, you stupid brat!"
    da "This is for my mom, and all of the people you killed, you monster!"
    "Darius then got on the ground next to Yuuki and hit her over and over again with the fake hammer."
    y "Ouch! Ouch! OWWWWWWWCCCCHHHH!!!"
    "Yuuki then said her last lines of the play with a loud scream!"
    y "Curse you son! Curse you BroBro! If only I had the power of friendship on my side I would have never failed!"
    y "But mark my words. This isn't the end! I will come back! Maybe not in either of you two's life time, but I will return eventually!"
    y "And when I do I will exact my revenge on your bloodline!"
    "And with that, Yuuki keeled over, and pretended to die in typical Yuuki fashion."
    "And by that I mean she overexaggerated as much as she possibly could."
    show darius happy at right
    da "We did it BroBro! We have defeated my evil father!"
    da "Now we shall have true peace!"
    '"Than you young boy. For without you, I would not have been able to win."'
    '"It truly is wonderful that I have such good friends to help me out!"'
    "And with that, the play was over."
    "The four of us bowed, and everyone clapped in the nonchalant sort of way that everyone does during these types of things."
    "We went back to our seats and Mrs. Striker returned to the front of the room."
    hide darius
    hide yuuki
    hide winrey
    show striker
    s "Well that was unique to say the least!"
    s "Do we have any other volunteers, or do I have to start calling on people?"
    "For a couple of seconds there was complete silence. It looked like no one was going to volunteer."
    show jerry at left
    j "My group shall go next."
    s "Great!"
    "Mrs. Striker once again returned to her seat in the back of the class and Jerry's group performed next."
    hide striker
    "Jerry's group was performing Romeo and Juliet, and they certainly did that."
    "They did a super condensed version of the play, and they did as good of a job as you could expect."
    hide jerry
    "Once they finished, Striker had to start calling volunteers, and ony by one every group went and performed their play."
    "One other group did Romeo and Juliet, and all the other groups either made up a play, or did some other famous play like Macbeth."
    "After everyone finished Mrs. Striker got up in front of the class and started speaking."
    show striker happy
    s "You all did a wonderful job today! I am very proud of all of you!"
    s "I will grade this over the weekend, and until then, just relax and have a good time!"
    "Mrs. Striker then dismissed us and I went home."
    scene black
    with fade
    play music "black.mp3"
    p "Before we start, I would just like to thank the two of you for taking the time to come here today."
    p "I know these last couple of weeks have been very hard on both of you, and I would like to offer you both my deepest condolences."
    "Neither me nor my mother said a word."
    p "Well, I guess we can get started."
    p "The reason I have asked for the two of you to come here is because we have discovered the cause of the death of Henry and Emilia."
    p "I know that what I am about to say will be difficult to understand and accept, but just so you know we have double checked every fact to make sure we didn't miss anything."
    p "It seems that the night that the two of you left, Henry pulled out a shotgun that he kept hidden, and used it to kill Emilia."
    p "He then turned the shotgun on himself, and committed suicide."
    "..."
    "why..."
    "Why would my dad do something like that."
    "He didn't."
    "No, he {i}couldn't.{/i}"
    "I know he wasn't perfect, but he would never harm Emilia."
    "He loved her so much."
    "I don't know what happened, but I know something isn't right here."
    "Something has to be wrong."
    "There has to be some mistake."
    "They must have missed some key detail that would have changed the whole case."
    "My dad must have been framed."
    "Yeah that has to be it."
    "My dad must have pissed someone off and they framed his for the murder of his own daughter."
    "Or maybe there is some supernatural element at play."
    "No, I don't believe in that sort of nonsense."
    "I looked over at my mom to see her reaction."
    "Her eyes were glazed over like she didn't hear a single word that was said."
    "That didn't surprise me. She hasn't said a word since the whole thing went down."
    p "Please let me know if there is anything that the two of you need."
    p "Just know that everyone here has been thinking and praying for the both of you."
    p "But that's all we have to say for now."
    scene bedroom
    with fade
    play music "bedroom.mp3"
    "..."
    "That memory..."
    "I still don't believe what they said about my dad."
    "There is simply no way that he would do something like that."
    "Still though...I miss them so much..."
    "Especially my sister."
    "My dad and I were never all that close."
    "He just opperated on a completely different wave length than me."
    "My sister on the other hand..."
    "We spent time together every day."
    "Playing silly games, teasing each other in the way only siblings can, play fighting..."
    "Every day since her death has been filled with nothing besides misery and woe."
    "I am but a hollow shell of who I once was."
    "If only there was some way to get her back."
    "Some way to save her from her fate."
    "Some way to erase the past and make a new one in it's place."
    "..."
    "Wait!"
    "Suddenly I remembered my discovery of a few days ago."
    "I remember how I discovered an entire new aspect to my powers."
    "The power to go back in time was not limited by just one minute."
    "I can go back as many times as I want to."
    "I can save my sister!"
    "..."
    "...But...should I?"
    "I have always heard about this thing called the butterfly effect."
    "How going back in time and changing things, no matter how small, can have unforeseen consequences."
    "And saving a persons life is by no means a small change."
    "That could alter the very frabric of reality as we know it."
    "It could inexplicably be the spark that starts the fire of World War 3!"
    "Or it could change the world for the better."
    "My sister could grow up to cure cancer, she did always want to go into the medical field."
    "There is also the psychological impact to take into consideration."
    "Let's see, my sister was killed on March 8th, a couple of years ago."
    "And today is...March 8th!"
    "Today is the 2 year anniversary of my sisters death and I didn't even remember it..."
    "Well anyways, that means that there has been 365*2 days since she had died."
    "That would be...crap I'm terrible at math."
    "I reached over for my calculator that I kept in my desk and did some quick calulations."
    "365*2=730."
    "That's 730 days since it happened."
    "No wait it's 731 days, this year is a leap year."
    "Ok there are 24 hours in a day, 60 minutes in an hour, and 60 seconds in a minute."
    "So the amount of seconds in 731 days would be..."
    "60 seconds * 60 minutes * 24 hours * 731 days."
    "Which would equal..."
    "63,158,400..."
    "Over 63 million seconds..."
    "Divided by 60 would equal...1,052,640"
    "And that's just the lowest possible number."
    "It takes a couple of seconds to pull the gun out and actually shoot myself..."
    "Is this worth it?"
    "Is this really what I want to do?"
    "Won't I go crazy from all of that time?"
    "All of that stress?"
    "And what if there are consequences?"
    "What if the butterfly effect is real?"
    "What should I do?"
    menu:
        "Save Emilia.":
            jump SaveEmilia

        "Don't save Emilia.":
            jump StayPut

    label SaveEmilia:
        "..."
        "I have to do it."
        "Whatever it takes."
        "No matter the cost."
        "Whatever it takes."
        "No matter if I go crazy."
        "Whatever it takes."
        "No matter if it causes World War 3."
        "Whatever it takes."
        "It is my duty as a brother to protect my sister."
        "Whatever it takes."
        "I will save Emilia!"
        "Whatever it takes!"
        "No use in delaying it any longer!"
        "I have to do it!"
        "I must do it!"
        "I will do it!"
        "And with that, I pulled out my gun and shot myself for the first time in this long journey of death and resurrection."
        play sound "gun.mp3"
        "{i}BANG!!!{/i}"
        scene black
        with fade
        play music "dead.mp3"
        "..."
        "Am I doing the right thing?"
        "I am, right?"
        "I'm protecting my sister."
        "That has to be the right thing to do."
        scene bedroom
        with fade
        "So far, so good."
        "1 down, 1,052,639 or more to go..."
        play sound "gun.mp3"
        "{i}BANG!!!{/i}"
        scene black
        with fade
        "..."
        scene bedroom
        with fade
        "2 down, 1,052,638 to go..."
        play sound "gun.mp3"
        "{i}BANG!!!{/i}"
        "3 down, 1,052,637 to go..."
        play sound "gun.mp3"
        "{i}BANG!!!{/i}"
        "4 down, 1,052,636 to go..."
        play sound "gun.mp3"
        "{i}BANG!!!{/i}"
        "5 down, 1,052,635 to go..."
        play sound "gun.mp3"
        "{i}BANG!!!{/i}"
        "6 down, 1,052,634 to go..."
        play sound "gun.mp3"
        "{i}BANG!!!{/i}"
        "7 down, 1,052,633 to go..."
        play sound "gun.mp3"
        "{i}BANG!!!{/i}"
        "8 down, 1,052,632 to go..."
        play sound "gun.mp3"
        "{i}BANG!!!{/i}"
        play sound "gun.mp3"
        "{i}BANG!!!BANG!!!{/i}"
        play sound "gun.mp3"
        "{i}BANG!!!BANG!!!BANG!!!{/i}"
        play sound "gun.mp3"
        "{i}BANG!!!BANG!!!BANG!!!BANG!!!{/i}"
        "9 down..."
        "10 down..."
        "20 down..."
        "50 down..."
        "176 down..."
        scene black
        with fade
        "..."
        "This is going to be the hardest thing I, no anybody has ever done."
        "All the pain, the hardship..."
        "I realize now that I will be sacrificing everything to save her."
        "There is no way I come out of this the same way I started."
        "Something will be different."
        "I will be broken..."
        scene bedroom night
        with fade
        "I looked out the window for the first time in quite a few jumps and I realized that it has become night time."
        "At least I'm making a little progress."
        "I still have a long journey of pain and anguish ahead of me."
        "Well, back to it."
        play sound "gun.mp3"
        "{i}BANG!!!{/i}"
        play sound "gun.mp3"
        "{i}BANG!!!BANG!!!{/i}"
        play sound "gun.mp3"
        "{i}BANG!!!BANG!!!BANG!!!{/i}"
        play sound "gun.mp3"
        "{i}BANG!!!BANG!!!BANG!!!BANG!!!{/i}"
        "236 down..."
        "289 down..."
        "371 down..."
        "521 down..."
        "563 down..."
        scene black
        with fade
        "The more times I went back the less grasp I had on reality."
        "I lost count after a couple of hundred more jumps and I no longer knew when or where I was."
        "I would have stopped long ago, but every time I considered it I saw her."
        show emilia
        "I saw her face and her smile."
        "I could almost hear her voice encouraging me."
        em "You can do it [name]!"
        em "I believe in you!"
        "When I heard her, I became instantly more comfortable."
        "I knew that I could do it."
        "I knew that I had to do it."
        "I knew that I was strong enough to push through the pain and psychological trauma and save my sister!"
        scene classroom
        with fade
        show striker
        s "Well that was unique to say the least!"
        s "Do we have any other volunteers, or do I have to start calling on people?"
        "For a couple of seconds there was complete silence. It looked like no one was going to volunteer."
        show jerry at left
        j "My group shall go next."
        s "Great!"
        "After an uncountable number of jumps, I made it back to the day where we were doing the play."
        "I couldn't even remember when we performed these."
        "Was it yesterday?"
        "What does yesterday even mean anymore to me?"
        "Would yesterday be the day before the play, or the day before I started time jumping to save my sister?"
        "Does yesterday even exist anymore?"
        "These thoughts are nothing but a waste of time to me now."
        "I need to focus on what really matters!"
        play sound "gun.mp3"
        "{i}BANG!!!{/i}"
        scene black
        with fade
        "I've probably made well over a few thousand jumps by now..."
        "But that doesn't even scratch the surface of what I need to do."
        "My time so far is but a grain of sand to the desert that is the 2 years I need to go through..."
        scene japanese setting 2206x1080
        with fade
        "A few thousand more jumps went by...or maybe it was in the ten thousands?"
        "Anyways we were back at Yuuki's house."
        show winrey casual at left
        show darius at right
        w "Hey guys, I hope it's ok that we got here before you did Yuuki."
        da "Yeah we didn't know what to do so we just stayed here at the door."
        show yuuki
        y "That is completely fine, mortals."
        y "But now that we are all here I, Yuuki Fawklberry, shall open the door!"
        "How many days ago was this?"
        "Man if Yuuki knew I actually had powers she would freak."
        "She did say on her first day that she knew but she hasn't said anything about it since."
        "I guess she was just messing around and saying random stuff like she always does."
        "Oh well, here we go again."
        play sound "gun.mp3"
        "{i}BANG!!!{/i}"
        scene classroom
        with fade
        show yuuki
        "After a lot of more jumps, I ended up in the scene where Yuuki offered me a brownie."
        "Yuuki sure is a character."
        "She can definitely be annoying at times, but I would be lying if I haven't enjoyed having her around."
        "Heck, at this point I would probably rather hang out with her than I would anybody else."
        "She keeps things exciting and unique. You never know what you're gonna get when you talk to her."
        "Sure she has a serious lying problem, but I bet I could get her to tell the truth with time."
        "Maybe when I get back to my regular timeline, after this whole ordeal is done, I can really get to know her."
        "I was always so rude and mean to her...She didn't deserve that..."
        y "Are you requiring some sustenance, mortal? Your stomach is screaming at you."
        y "Well mortal, you are in luck. For I, Yuuki Himigo, have just what you are requiring!"
        y "Here! You may eat this to restore your lost mana!"
        play sound "gun.mp3"
        "{i}BANG!!!{/i}"
        scene black
        with fade
        "After a certain amount of jumps everything began to jumble together."
        "I slowly worked my way backwards through time, and I would always end up in different places."
        scene bedroom night
        with fade
        "I would spend a few thousand jumps in my bedroom at night."
        scene bedroom
        with fade
        "After a while, it would start to get brighter as evening approached."
        "The weirdest part of this whole thing was how the day cycle would be in reverse."
        "Usually you go from the night to the morning, but I would go from the night to the evening."
        "It made it much more difficult to get a feel for where and when I was."
        "Humans aren't supposed to go through this sort of thing."
        play sound "gun.mp3"
        "{i}BANG!!!{/i}"
        scene classroom
        with fade
        "Most days I would end up in the classroom at school, as that is where I would spend 8 hours a day for most of the week."
        show striker
        s "Thanks, I guess..."
        s "I guess I will go ahead and announce what happened just in case some of you haven't heard."
        s "Some of you might have heard about how people from around the world have been found dead, with their facial features missing?"
        s "Well, I'm afraid I have some terrible news."
        s "It seems like this incident has directly affected one of your fellow classmates..."
        s "As you might have noticed, Jerry is absent today."
        s "That is because...his father was found dead this morning, with all of his facial features missing."
        s "Jerry's mother passed away years ago, and he was living alone with his father."
        s "The police have informed me that they are currently working out a solution."
        s "If you are religious, I urge you to pray for him."
        s "If you aren't, then keep him in your thoughts."
        s "I have decided that, for today, we will have a free day."
        s "You may work on your homework if you so wish to, or you can just sit in silence."
        s "I will be at my desk if anybody needs me."
        "Oh yeah..."
        "My lifes been so crazy lately that I'm ashamed to admit that I've forgotten about Jerry."
        "He might live with me, but I don't really see him all that much."
        "He mostly keeps to himself and stays in his room when we aren't at school."
        "And we never walk to school together either, so I don't talk to him much either."
        "That's another thing I should fix when I get back."
        "He has always been mean to me, but maybe if I am nice to him we can become friends."
        "Nobody ever did figure out how these people are dying either..."
        "Their facial features missing? That is seriously freaky."
        "Hopefully they will figure out the cause at some point so that they can stop it from happening anymore."
        play sound "gun.mp3"
        "{i}BANG!!!{/i}"
        scene cafe
        with fade
        show yuuki at left
        show winrey casual
        show darius happy at right
        da "The two of you look pretty close, don't they Winrey!"
        w "Yeah they do!"
        w "Wait, where are my manners, I haven't even introduced myself yet!"
        w "My name is Winrey."
        da "And I'm Darius! I'm glad that we get to work with you on this project."
        w "Yeah, before you came it was just the three of us, and we were the only group to have less than 4 members."
        y "It is a pleasure to meet the both of you mortals! My name is Yuuki Daronga!"
        y "I am a level 75 mage who became trapped in this world after an evil demon trapped me here against my will."
        y "I hope that I won't have to stay too long, and I am currently resting so I can prepare for our great rematch!"
        w "..."
        da "....."
        w "...That's... pretty cool!"
        da "Yeah, I... I didn't know we hade a mage in the class!"
        "Oh yeah, this is where Yuuki first met Darius and Winrey."
        "Was this also the first day that I met Yuuki, or were these seperate days?"
        "Everything is closing in together. I can't remember many details."
        "Why did we come to the cafe again?"
        "Was it to work on our project? Or were we just all trying to get to know each other?"
        "Was this the time that I ordered those amazing hot wings?"
        "Did I ever order those hot wings?"
        "I can't even remember if I ever ordered them or if I decided to try something else."
        "Was this the time that Yuuki offered to split her meal with me?"
        "Or did we go to the cafe another time?"
        "I need to stop thinking about all this so much."
        "It really is just a complete and utter waste of time and energy."
        "Time that I could be using to save my sister."
        play sound "gun.mp3"
        "{i}BANG!!!{/i}"
        scene hallway school
        with fade
        w "Listen, I'm real sorry about yesterday."
        da "No no no, you shouldn't have to apologize, it was me who was in the wrong."
        w "What? How? I was the one who brought up yout shoe problem, it was completely not ok for me to ask about that."
        da "Yeah, but I shouldn't have gone off on you, I mean it's only natural that you wanted to ask questions, I know how weird it is."
        w "Yeah it is weird, but that's ok, the little quirks that we all have is what makes us unique, and I think it's kind of cute..."
        da "Wha...? Cute?"
        w "I dunno, it's so weird that I think it's kind of charming, you know?"
        da "You got a foot fetish or something?"
        w "Oh piss off! That's not what I was getting at!"
        da "You sure? Cuz it sounds like you got a foot fetish."
        w "I swear to God I will deck you right here."
        w "I'll get my soccer cleats out of my bag and kick you so hard with them it will rewire your brain and make you want to wear shoes at all times! Even when you're in the shower or when you're sleeping!"
        da "That's a little hardcore."
        w "I am hardcore!"
        da "I can believe it."
        w "Well anyways, I guess I'll see you in class."
        da "We're already in class"
        w "Shut up!"
        "Ok so this was the time that I was listening in on Winrey and Darius's conversation."
        "I'm assuming this is the first time the two of them got to spend any alone time together."
        "This might have been when the two of them developed feelings for each other."
        "It still surprises me how I'm not upset at all that the two of them got together."
        "I had a huge crush on Winrey and at some point it just went away."
        "How did that happen?"

        "Wasn't this also the day Yuuki arrived?"
        "And wasn't it the day we all went to the cafe?"
        "Who knows anymore."
        play sound "gun.mp3"
        "{i}BANG!!!{/i}"
        scene classroom
        show darius angry at right
        da "A play?!?!"
        da "Seriously? What does a play have anything to do with this class? I know that you're our only teacher, and you teach us all types of subjects, from math, to science, to writing, but what does a play have to do with anything?"
        show striker angry
        s "A play has everything to do with all of those things Darius."
        da "HOW!?!?"
        s "If you would have let me finish instead of rudely interrupting then I would have been able to tell you!"
        show darius at right
        da "...You're right... I'm sorry."
        s "You should be!"
        hide darius at right
        s "Anyways, to answer your question, I have noticed how nervous you all are to answer questions or do anything that involves public speaking."
        s "This simply will not do. Once you get out into the real world, you will have to speak in front of people constantly."
        s "And while it is important for me to teach you about math and science, a lot of those topics won't really be all that useful in the real world."
        s "Now that you all have smart phones, you can do basic math with that. You can look up any science fact you can think of on the internet."
        s "You know what you're phones can't help you with? Human interactions. That is why I have decided to make this my number one priority as a teacher."
        s "I would be doing you all a huge disservice if I threw you out into the real world with no speaking skills."
        s "You would fail at life horribly. How do you expect to impress at a job interview if you can't even get your words across clearly?"
        s "What if you want to apply for a loan? You think they give you money if you can't communicate effectively?"
        s "That's why we are going to put on a play. To help you all get out of your shells and be who you need to be to do well in this world."
        s "And if you are wondering why I have decided to make you all put on a play, instead of something more traditional like a speech, well, I just thought it would be more fun."
        s "Do you want to spend months researching a topic that you have no interest in, and creating a powerpoint to give a monotone speech, or would you rather flex your creative muscles by writing and performing a moving and emotional story."
        "And this was the day when we found out what we would be doing for our project."
        "I hate to admit it but I'm glad that we ended up doing a play."
        "I got to make a couple of new friends and I became even closer to the friends that I already had."
        "Without this play I probably wouldn't have met Yuuki either."
        "She only ended up talking to us because we had one less person on our team than everyone else."
        "And without the play, Darius and Winrey would have never gotten together."
        play sound "gun.mp3"
        "{i}BANG!!!{/i}"
        hide striker
        "I kept on shooting myself and I kept on going back."
        "For some reason I didn't seem to go to the black empty place as much either."
        "I did occasionally, but it was rare. And when I did it only seemed to last for a couple of quick seconds."
        "I remember that when I first started, the black place seemed to last forever."
        "I wonder what changed?"
        "Did I just become better and time travelling?"
        "Maybe time travel is like a muscle, and the more you use it the more strong you get."
        "And the stronger you get, the less you have to push yourself."
        "I guess I've just become a master time traveller."
        "Time to train my muscles even more."
        play sound "gun.mp3"
        "{i}BANG!!!{/i}"
        scene classroom
        show striker
        s "Ok class, as we discussed yesterday, today we are going to pick the groups for the big project."
        s "I will be sure to let you know what we will be doing for the project tomorrow, but for today it will be enough to just find out who will be working with who."
        s "Now there are 23 students in this class, so unfortunately the groups will not be even."
        s "I have decided that the class will be split up into 5 groups of 4, and one extra group of 3."
        s "The way we will decide the groups is quite simple. I have not directly chosen who will be in what group, and instead it will be entirely random."
        s "I will call you up to the front of the class one by one, and you will pick up a small slip of paper from this cup."
        s "The paper will have a number on it. That number will be the group that you will be a part of."
        s "Does everyone understand?"
        "And this was the day that I ended up on my team with Winrey and Darius."
        "I sure am glad I decided to go back in time after I initially got on a team with Jerry."
        "That would have been real rough, and I definitely wouldn't have met Yuuki."
        play sound "gun.mp3"
        "{i}BANG!!!{/i}"
        "A lot of more jumps occured where I stopped paying attention to where I was."
        "They were all blending together, and it was a waste of time to stop and reminisce about my past."
        "Eventually, I ended up in the living room, and I realized that I was about to have a serious problem on my hands."
        scene living room
        with fade
        "BANG!"
        "BANG?"
        "bang?"
        "..."
        "Oh no..."
        "How could I have forgotten such an important detail."
        "I looked ahead of me, and all I saw was a locked safe."
        "The safe that carried the gun that I used to time travel..."
        "I only started carrying around a gun a little after I got my power."
        "Before then, all I kept with me in the way of a weapon was my pocket knife..."
        "This is bad."
        "This is {i}really{/i} bad."
        "If I want to continue time travelling past this point in time I'm gonna have to use my pocket knife to go back."
        "The gun I use is completely painless. It's instantaneous."
        "But a knife? That's gonna hurt..."
        show emilia
        em "You can do it!"
        hide emilia
        "..."
        "She's right."
        "I don't have a choice in the matter."
        "I've made it this far. I can't let any obstacles get in the way now."
        "I pulled the pocket knife out of my back pocket, pulled it up to my throat, and slit my throat open as fast as I could."
        "{i}BLEGH!{/i}"
        "What followed next was the worst pain that I have ever experienced in my entire life."
        "I could feel every molecule around my neck screaming out in anguish."
        "I looked down and I could see the blood pouring out everywhere around the floor."
        "Things around me started to get hazy, and I lost all sense of vision."
        "My nostrils were inflamed with the toxic smell of blood."
        "Do it for Emilia. Do it for Emilia. Do it for Emilia!"
        "I said those words over and over again in my head, as it was the only thing that could possibly help me fight through the pain."
        "A couple of seconds went by, and everything went dark."
        scene black
        with fade
        "..."
        "I'm here again."
        "I felt against my throat to see if it was back to normal. It was."
        "I could feel myself shaking all over, with cold sweats dripping from every pore of my skin."
        "This is about to get a lot worse than it was before."
        "So much pain..."
        "And the worst part is now it's going to take a lot more jumps to get back to where I need to be."
        "Before, when I had the gun, killing myself took about a second of time."
        "That means that with every jump, I was going back about 59 seconds in time once you deduct the one second it took to pull the trigger."
        "But now..."
        "I don't know exactly how long it took to die, but it was at least a few seconds."
        "This is gonna suck..."
        scene living room
        with fade
        "I'm back."
        "This time I need to count to see how many seconds it takes to die."
        "I pulled out the pocket knife, took a deep breath, and sliced open my throat with my shaky hands."
        "Once again the pain seared throughout my entire body."
        "I don't know how I'm gonna get through this, but I need to count."
        "1"
        "Blood started to pour out everywhere like I was in a horror movie."
        "2"
        "I gasped for air but nothing came out."
        "3"
        "I lost my balance and fell onto the carpet."
        "4"
        "The blood started to be soaked up into the carpet like a sponge."
        "5"
        "The pain became almost unbearable."
        "6"
        "I looked at my blood-stained hand to see that it was shaking uncontrollably"
        "7"
        "My nose drowned in blood and I could no longer smell anything."
        "8"
        "I lost all sense of vision but I could still feel the pain."
        "9"
        "I couldn't think clearly anymore."
        "10"
        "11,12..."
        "20,21,22"
        "This is really bad. That's a lot of time..."
        "37...38..."
        "I'm gonna have to jump so many more times because of this..."
        "43...44...45..."
        "And these jumps are so much more painful."
        "48...49...50..."
        "56...57...58...59..."


        "I felt nothing, and I slipped into darkness..."
        scene black
        with fade
        "59 seconds."
        "It takes 59 seconds to die."
        "That means that from now on, I will only be going back in time by 1 second on average."
        "I originally had to jump a little over a million times, but now that number just increased by a lot."
        "I hate this so much..."
        scene living room
        with fade
        "..."
        "Well, time to get to work..."
        "I slit my throat once again, and it was just as painful as the last two times."
        "I hit the floor, and after 10 seconds, I died."
        scene black
        with fade
        "I continued slitting my throat for more times than I could possibly begin to count."
        "With each jump, the pain stayed about the same."
        "It never became easier, but I did start to think about it less."
        "The pain became second nature to me."
        "I was used to it now."
        "After awhile the pain was all I knew."
        "I forgot what it was like to not have blood pouring out of your body."
        "I forgot what it was like to breathe."
        "I forgot everything."
        "This was just my life now."

        scene classroom
        with fade
        show winrey school
        w "Hey, I don't think I've formally introduced myself to you yet."
        w "My names Winrey! And your name is [name], isn't it?"
        "Y..yes... I stammered."
        w "Well it's very nice to meet you!"
        w "So, what do you like to do in your free time?"
        w "I guess you're kind of shy, huh?"
        w "That's fine, I have a little sister who never talks at all!"
        w "You don't have to say a word! I'll do all the talking!"
        w "Well, anyways, as I was saying, My names Winrey."
        w "I'm a member of our school's soccer team as well as the class president, but you probably knew that last part already!"
        play sound "alarm.wav"
        "{i} BEEP! BEEP BEEP! {/i}"
        w "Well anyways, I'll see you later [name]!"
        hide winrey
        "I had gotten to the point where I could no longer notice that I was slitting my own throat."
        "My body just did it by itself at this point."
        "Just as how you don't have to think about breathing, I didn't need to think about the pain that I was about to inflict on myself."
        "It was second nature."
        "That being said, I did hesitate a second this time."
        "I think that it was because this moment stuck out in my mind a lot."
        "Oh gosh I really don't want to relive this moment."
        "It's so embarrassing. How is it possible for someone to be as lame as me?"
        "I realize now that I never even really talked to Winrey all that much, even when we were on a team together."
        "How did I ever even think we had a chance together if we never even talked?"
        "I'm so lame..."
        "..."
        "Wait a second..."
        "Did Winrey just mention that she had a little sister who never talks?"
        "That doesn't add up."
        "When we were at Yuuki's house she said she lived in a tent with just her dad."
        "Was she lying about having a little sister?"
        "Why would she lie about that?"
        "Oh, I get it now."
        "She must have been trying to make me feel better by telling me she has a sister who never talks."
        "That has to be it."
        "Before I could think about this any longer, I pulled the knife out and slit my own throat."
        "I could hear yelling across the classroom as people started to realize what I just did."
        "I guess it would be pretty startling to see someone run a knife across their own throat, but it didn't bother me anymore."
        "I could hear someone yelling to call 911."
        "I could here people screaming and crying and praying and throwing up..."
        "Before I could hear anything else, I passed out."
        scene black
        with fade
        "That's pretty annoying."
        "It's bad enought that I have to die so often, now I have to hear everyone elses reaction to my death on top of all that?"
        scene black
        with fade
        "After who knows how long, I sliced my throat and ended up staring face to face with someone that I never thought I would see again."
        show dolus
        d "It is done. You now have the gift of re-death."
        d "Every time you die in the real world, you will be sent back in time one minute and you will be able to make preventative measures to make sure that death never occurs in the first place."
        d "I will now send you back to Earth. I am afraid that this is goodbye, as I can not accompany you there."
        "I've made it back to when I initially got my powers."
        "And here I am face to face with Dolus."
        "Maybe I should tell her about the adventure I've been having."
        "...No."
        "She might think that this is a misuse of my power."
        "If she doesen't like what I'm doing, she migth take the power back and then I would be at square one."
        "I'll just keep what I'm doing a secret."
        "..."
        "But wait..."
        "Can I travel back to before I got my power?"
        "What if I try to and I just die for real, because I haven't recieved my power yet?"
        "I've come too far to let that stop me now."
        "Either I'm bringing Emilia back to Earth, or I'm gonna join her in heaven."
        "I took a deep breath, and sliced my throat, not knowing what the outcome was going to be for the first time in a long while."
        hide dolus
        scene black
        with fade
        show dolus
        d "Oh of course! It makes perfect sense for you to ask that question!"
        d "You have had a rough life, and then all of a sudden an angel comes down and offers you a great gift!"
        d "Well, I can tell you with complete confidence, there is no catch for you."
        "..."
        "It worked!"
        "Or did it?"
        "I then realized that by the time I jumped back previously, Dolus had already given me my powers, so of course it would have worked."
        "But now I have actually travelled back to a time when I didn't possess this gift."
        "Ok, I guess this time will be the real test."
        "I sliced my throat and waited to see what would happen."
        hide dolus
        scene black
        with fade
        show dolus
        d "The Lord has watched you struggle your entire life. And your pain and suffering has not gone unnoticed."
        d "You have truly had a hard life. God puts people through these trials as a test of sorts, and he was going to reward you for your diligence with a nice, easy life."
        d "That was, until, you were murdered."
        d "That was never supposed to happen, and God took quite a while with deciding what to do with you next. This is why you were here for so long. I apologize for the inconvenience."
        d "But the wait is finally over, and God has made up his mind. He has decided to offer you a choice."
        d "You can either choose to end your life right now, and ascend to Heaven."
        d "You will be reunited with your lost loved ones and you will live in peace and harmony for all eternity."
        d "The other option is truly unique. A one of a kind offer that God has never made before."
        d "You can choose to return to your life at the same time that you left it. It will be like you never died at all."
        d "But that is not all. God has decided to offer you a gift of sorts."
        d "If, at any time in the future you end up dying again, you will be sent back one minute in time. You will be able to redo that minute to make it so that you do not die."
        d "God has decided to offer you this gift as his way of saying sorry for all the trouble."
        d "So what will it be? Come with me to Heaven or go back to Earth with your newfound ability?"
        "Ok, this time it actually did work!"
        "I let out a huge sigh of relief, glad that all my effort and pain wasn't about to go to waste."
        "There shouldn't be anymore road blocks between me and Emilia now."
        "All it's gonna take now is a path paved of literal blood, sweat, and tears."
        scene moon over field
        with fade
        show robber1
        r "WHAT ARE YOU DOING KI..."
        play sound "gun.mp3"
        "{i} BANG!!!! {/i}"
        r "Oh my God... What have I done?!"
        r "I gotta get out of here!"
        hide robber1
        "I felt a terrible pain in my chest, knowing that I had just gotten shot by the man who set me on this path."
        "Well I guess I don't have to kill myself this time...He already did the job for me..."
        scene classroom
        with fade
        show striker


        # These display lines of dialogue.

        s "Alright class, settle down. Today we are going to have a pop quiz"

        show darius angry at right


        da "What? But that's not fair! You never told us we were gonna have a quiz!"

        show striker

        s "That's literally the point of a pop quiz Darius."

        show jerry at left

        j "A pop quiz is fine with me. As the smartest person in this school, I welcome any challenge that comes my way."
        da "Shut up Jerry! no one likes you or your elitist attitude!"
        j "At least I wear shoes to school you disgusting freak."
        da "How many times do I have to tell you? It's a..."
        show striker angry
        s "Alright both of you be quiet!"
        s "Since you seem to be pretty talkative today Darius, why don't you hand out the quiz to everybody?"

        da "Fine..."
        hide striker
        hide darius angry
        hide jerry
        "Man this really brings back memories."
        "This was the start of the day that I recieved my powers..."
        "I guess if Mrs. Striker never asked to see me after class then I never would have recieved my powers."
        "For the first time I realized how much of a group effor it was for me to get this gift."
        "Mrs. Striker had to call me in after class, The guy had to kill me, and God had to decide to gift me these powers."
        "It's almost like it's destiny for me to save Emilia."
        "No, it is destiny!"
        "God must have known that I would have done this!"
        "Maybe it's why he gave me these powers in the first place."
        "It's my job to save her."
        "I contined to kill myself over and over again."
        "Each time I remembered less than the last."
        "All the deaths, the screams, the pain, it all jumbled together."
        "After tens of millions of more jumps, I finally made it to my destination."
        scene bedroom
        with fade
        play music "bedroom.mp3"
        "I was in my bedroom, about an hour before my mom and I were supposed to leave."
        "I need to figure out a way to save my sister."
        "Luckily I've had plenty of time to think of a couple of different solutions."
        "I could pretend I'm sick and stay home with Emilia to protect her from my dad."
        "The only problem with that is there is still a chance that he does what he did in my timeline."
        "What if I try and take Emilia with us?"
        "If I remember correctly, the reason she stayed behind is because she needed to work on some homework."
        "Maybe I could convince her to bring the homework with her?"
        "It's worth a shot at least."
        "I left my bedroom and headed towards the kitchen where my mother and sister were at."
        scene kitchen
        with fade
        show mom at left
        m "Hey [name], are you almost ready to leave."
        "Before I could answer, my sister, the person who I leapt through time millions upon millions of times to see, walked into the kitchen."
        show emilia
        em "What's the matter [name], you look like you've seen a ghost."
        "I could barely control my emotions."
        "I've never been much of a crier, but I could feel that the tears were about to start flowing."
        "I was overwhelmed with emotion. I was so happy to see her."
        "But I also felt a since of dread and sadness."
        "I knew that in just a few short hours she would be dead if I didn't do anything to save her."
        "I knew that my dad would kill her..."
        "I didn't believe it at first when the police told me, but I certainly do now."
        "There was way too much evidence to support it."
        "I never knew he was capable of doing something like that. He usually seemed so happy and cheerful."
        "I guess on the inside he was harboring some deep, dark emotions."
        "Oh well, I can't save him now."
        "Whatever the reason for his actions, he made his choice."
        "He is simply too dangerous to be left to his own devices."
        "I need to focus on my sister now."
        em "Uhhh, are you alright [name]?"
        menu:
            "Come with us on the trip.":
                jump trip

            "I'm fine. Do you have homework?":
                jump homework

        label trip:
            em "How many times do I have to tell you? I have homework to do."
            menu:
                "Do it later.":
                    jump later

                "You can bring it on the trip.":
                    jump bringit

            label later:
                em "I have already procrastinated on it for a long time."
                em "It's due at the end of next week, I need to do it now."
                "I knew that wouldn't work."
                menu:
                    "You can bring it on the trip.":
                        jump bringit

            label bringit:
                em "I don't know if that's a good idea..."
                menu:
                    "Why not?":
                        jump whynot

                    "It's a great idea!":
                        jump greatidea

                label whynot:
                    em "Because I'll be distracted by you guys the entire time."
                    em "Look, I really need to focus on this, ok?"
                    "I told her that I would be glad to help her with the homework if she came on the trip."
                    em "Really?"
                    em "Well, if you're sure...I guess I'll come."
                    jump saved

                label greatidea:
                    em "And how is that a good idea?"
                    menu:
                        "Because I can help you.":
                            jump helpyou

                        "Because it will be more relaxing where we are going!":
                            jump relaxing

                    label helpyou:
                        em "Seriously?"
                        "I told her I was dead serious."
                        em "Since when have you been so helpful."
                        "I wanted to tell her all about my travels and what I've gone through, but I knew I couldn't."
                        "She would think I was crazy if I told her I had travelled back in time minute by bloody minute just to save her."
                        "Instead I just told her that I was in a helpful mood."
                        em "Well thanks! I guess I will come then."
                        jump saved

                    label relaxing:
                        em "As relaxing as that may be, I need to focus."
                        em "So sorry, but no, I'm not going."
                        menu:
                            "I can help you with your homework.":
                                jump helpyou

        label homework:
            em "I do have quite a bit of homework actually."
            em "I have to write a 5 page essay that I haven't even started on and it's due next week."
            em "I also have a lot of math problems I need to do for Algebra."
            em "And I need to study for a big Geography test I have on Wednesday."
            "I didn't know she had so much stuff that she needed to work on."
            "I'm not the smartest guy, but I have already taken all of those classes, and I did a decent enough job in them."
            "I could probably help her with all of the homework."
            menu:
                "I can help you if you come with us.":
                    jump comewith

                "Mom could probably help you.":
                    jump momhelp

            label comewith:
                em "Seriously?"
                "I told her I was dead serious."
                em "Since when have you been so helpful."
                "I wanted to tell her all about my travels and what I've gone through, but I knew I couldn't."
                "She would think I was crazy if I told her I had travelled back in time minute by bloody minute just to save her."
                "Instead I just told her that I was in a helpful mood."
                em "Well thanks! I guess I will come then."
                jump saved

            label momhelp:
                show mom angry at left
                m "Now hold on just a second mister!"
                m "I am completely fine with Emilia coming with us on this trip, in fact I encourage it."
                m "But if you think I'm gonna use my free time to do homework, well you got another thing coming!"
                m "If you want her to come, you better help her yourself!"
                m "I'm gonna be in the spa or the pool for the whole time. I don't have time or energy to use my brain!"
                em "It's fine mom, I'll just stay home."
                em "It's not like [name] is smart or helpful enough to help me anyways!"
                "Crap!"
                "I knew I screwed up when I pushed all of the effort off onto my mom!"
                "I should have volunteered to help her myself..."
                "I could use my knife and go back in time and redo this conversation."
                "But I just got use to not killing myself over and over again..."
                "I don't know if I want to go through that pain again unless it's completely necessary."
                "Plus I don't want to slit my own throat in front of my own mother and sister."
                "It would completely traumatize them!"
                "Not that it would be permanent or anything, as soon as I go back they would forget all about it."
                "But I wouldn't."
                "For the rest of my life I would hear their screams of agony and shock of seeing their own flesh and blood kill themselves right in front of them."
                "Their screams would haunt my nightmares..."
                "I already have enough screams from everyone else."
                "Every time I needed to go back in front of people I heard them cry and yell..."
                "It hurt me more than the knife ever could."
                "Whenever I needed to go back in time in front of my mother, I would get out of her sight and do it where she couldn't see me."
                "I couldn't bare to see her in pain."
                "Not again anyways..."
                "No, if I can avoid it, I would rather not go back in time."
                "Instead, I will just improvise and tell Emilia that I will help her."
                menu:
                    "Ok, I'll help you instead.":
                        jump mehelp

                label mehelp:
                    em "Wait...You are gonna help me with my homework?"
                    "I told her that I would."
                    em "Since when have you been so helpful."
                    "I wanted to tell her all about my travels and what I've gone through, but I knew I couldn't."
                    "She would think I was crazy if I told her I had travelled back in time minute by bloody minute just to save her."
                    "Instead I just told her that I was in a helpful mood."
                    em "Well thanks! I guess I will come then."
                    jump saved

label saved:
    "I couldn't belive what I was hearing!"
    "It worked! After all this time, after all the suffering and pain I went through, it was finally over!"
    "It was all worth it!"
    show mom happy at left
    m "Ok Emilia, you better hurry and go pack your bag if you want to come, we are leaving pretty soon."
    em "Ok, I'll hurry."
    em "And thanks for helping me [name], it means a lot."
    hide emilia
    show mom happy
    m "That was nice of you to offer."
    m "And so unlike you...are you feeling normal? Do you have a fever or something?"
    "I told her that I felt better than I have in a very long time."
    "For the first time in 2 years, I was truly happy."

    scene bedroom
    with fade
    "The three of us went on the trip and I helped my sister with her homework just as I had promised."
    "It took most of the weekend but that was completely fine with me."
    "After what I had been through to get to that point, homework was nothing."
    "When we got back home though, we found exactly what I was afraid we would find."
    "My dad, covered in blood, with the gun I had used so many times in his hand."
    "Everything went about the same as it did after I had initially found my dad and sister dead."
    "My mom became silent and didn't talk."
    "The police interviewed us constantly and did a full investigation."
    "This time I wasn't effected nearly as much as last time."
    "I had already greaved for him before, and after knowing what he would have done to my sister, I was just glad it was all over."
    "My sister took his death pretty hard."
    "She didn't go quiet like my mother, but she didn't smile at all."
    "I have always known my sister to smile at all times."
    "She always held the same face no matter what happened, but that wasn't the case this time."
    "Whenever we talked I could tell she was dead on the inside."
    "Her voice went monotone and she never joked about anything."
    "Just like me, her grades dropped a lot as well."
    "Eventually, after about a year, she started to get back to normal."
    "She still hurt, and every now and then I could hear her crying in her room late at night."
    "But she did get her smile back."
    "Though I could tell that she was hiding a lot of negative feelings behind that smile."
    "I knew this would be hard for her, but at least she was alive."
    "Throughout the two years that followed my dad's death, I tried my best to do everything exactly how I did it before."
    "I know that I changed time drastically by saving my sister, but I thought if I did everything the same in my own life, maybe there wouldn't be that much of a difference."
    "And there wasn't."
    "I still got grouped up with Winrey and Darius for our project. We still did a play over BroBro."
    "Yuuki still came into my life like a nuclear explosion and joined our group, Jerry's father still died a mysterious death and came to live with us."
    "This time though, he had to sleep on the couch, as my sister's bed was occupied."
    "Everything seemed to be going great, and eventually I made it back to the day that I went back to save my sister."
    "After along time, my journey was complete."
    "And I had accomplished exactly what I set out to do. I saved my sister."
    "Now I get to live my life free of pain and guilt."
    "Or at least as free as possible."
    "I woke up about an hour and a half before school began and got ready."
    "It was while I was brushing my teeth that I realized I had made a horrible mistake."
    "The time changed last night, and we moved foward an hour in time!"
    "Class begins in 15 minutes!"
    "I rushed out of my house and ran to school."
    scene classroom
    with fade
    play music "classroom.mp3"
    "I made it to class with exactly no time to spare."
    "I was the last person there, and Mrs. Striker glared at me and told me to take a seat."
    "I sat down and looked at the clock to see what time it was."
    "While looking at the clock, I realized something."
    "2 minutes from now is the exact time that I started to go back and save my sister!"
    "I am about to make it back to the exact second that I at when I left!"
    show striker
    s "Ok class, today we are going play a little game."
    s "I need two volunteers to come to the front of the room."
    "Yuuki shot her hand up as quick as she could."
    s "Ok Yuuki, you can come up. Anyone else volunteer?"
    w "I'll play too!"
    s "Ok, thanks you two for volunteering."
    "Yuuki and Winrey got up in front of the room and stood on either side of Mrs. Striker."
    show yuuki at left
    show winrey school at right
    "I looked at the clock again, 1 more minute!"
    s "Ok, so this game is going to be a memorization exercise."
    s "Everyone in the class is going to take turns saying a random word, and you two will have to repeat every word they say in order."
    s "The winner is whoever can remember the most amount of words."
    "30 seconds left!"
    show yuuki happy at left
    y "Ooooohhh! This sound like fun!"
    y "I'm totally gonna beat you Winrey!"
    "15 seconds!"
    w "Fat chance of that! I get an A on every test because of my amazing memory capacity!"
    "10 seconds!"
    y "Yes, but you are forgetting something big!"
    "5 seconds!"
    y "I Yuuki Havetoro, am a..."
    "And...That's it!"
    "This is exactly the time I left to save my sister!"
    "This means that I have officially made it back to wh..."
    "I looked up to the front of the class and screamed out in horror."
    show yuuki dead at left
    show winrey dead at right
    show striker dead
    play music "dead1.mp3"
    "All three people standing at the front of the class, Yuuki, Mrs. Striker, and Winrey, all froze completely."
    "They stood in the exact same position, but there was one major difference."
    "All of their facial features were missing..."
    j "Oh my God! No! Please God no! Not again!"
    "I could hear Jerry start wailing uncontrollably in agony, obviously remembering what happened to his father."
    da "Winrey?!?! Oh God Winrey! Are you ok?!"
    "Darius got up and stared to shake Winrey, desperately trying to get her back to normal."
    "I looked around to see that they weren't the only victims."
    "I counted four more students who had frozen up with their faces gone."
    "Dear God, what could have caused this!"
    "..."
    "...no..."
    "It can't be..."
    "This all happened the second that I would have gone back originally."
    "It has to be a coincidence, right?"
    "I pulled out my gun and shot myself out of pure desparation."
    play sound "gun.mp3"
    "{i}BANG!!!{/i}"
    scene black
    with fade
    "..."
    "I have to save them."
    "I don't know how, but I must."
    scene classroom
    with fade
    show striker
    show yuuki at left
    show winrey school at right
    w "Fat chance of that! I get an A on every test because of my amazing memory capacity!"
    "I've got 10 seconds to save them."
    "I stood up and screamed as loud as I could."
    "I don't know what I said, I don't even know what my plan is, all I know is I need to try something."
    "Everyone became silent and stared at me."
    "I looked Yuuki in the eyes, and next thing I knew the three of them froze."
    show yuuki dead at left
    show winrey dead at right
    show striker dead
    j "Oh my God! No! Please God no! Not again!"
    da "Winrey?!?! Oh God Winrey! Are you ok?!"
    "I can't lose them!"
    "I can't lose Yuuki!"
    play sound "gun.mp3"
    "{i}BANG!!!{/i}"
    scene black
    with fade
    "Come on..."
    "Think of something..."
    scene classroom
    with fade
    show striker
    show yuuki at left
    show winrey school at right
    w "Fat chance of that! I get an A on every test because of my amazing memory capacity!"
    "I ran up to Yuuki and did the only thing that I could think of."
    "I gave her a hug, refusing to let go when she pushed back on me."
    "I could hear laughter at my action slowly turn into screams of horror and I knew that I have failed once again."
    show yuuki dead at left
    show winrey dead at right
    show striker dead
    j "Oh my God! No! Please God no! Not again!"
    da "Winrey?!?! Oh God Winrey! Are you ok?!"
    play sound "gun.mp3"
    "{i}BANG!!!{/i}"
    scene black
    with fade
    "no..."
    "please..."
    "I can't go through this again..."
    scene classroom
    with fade
    show striker
    show yuuki at left
    show winrey school at right
    w "Fat chance of that! I get an A on every test because of my amazing memory capacity!"
    play sound "gun.mp3"
    "{i}BANG!!!{/i}"
    play sound "gun.mp3"
    "{i}BANG!!!!{/i}"
    play sound "gun.mp3"
    "{i}BANG!!!!!{/i}"
    "I kept on shooting myself to go back further in time."
    "I needed to warn Yuuki..."
    scene bedroom
    with fade
    "I was back in my bedroom, about an hour before school started."
    "I ran to Yuuki's house as quick as I could manage."
    scene japanese setting 2206x1080
    with fade
    play music "heaven.mp3"
    play sound "doorbell.wav"
    "{i}DING!DING!DING!{/i}"
    "I frantically rang her doorbell, praying to God that she would come out."
    show yuuki
    y "[name]?"
    y "What are you doing here?"
    "I hugged her for what felt like a lifetime and started crying uncontrollably"
    "Not just for Yuuki, but for everything that was happening."
    "For the two years of pain and suffering I went through, for all the deaths I experienced, for my failures to save everybody..."
    "I couldn't get out a word, but Yuuki must have known something was wrong, as she just hugged me back."
    menu:
        "I can't save you!":
            jump cantsave

        "You're going to die today...":
            jump dietoday

    label cantsave:
        y "I don't know what you're talking about, but you already have."
        "I didn't know what she meant."
        show yuuki angry
        y "Before I came here... I had no friends, for reasons that I'm sure you can imagine."
        y "Everyone thought I was a freak, a loser, a nobody."
        y "They made fun of me, called me names, hurt me..."
        "She pulled her hair back and showed me a scar on the back of her head."
        y "I didn't know how to make friends."
        y "Both of my parents were dead... I was broken."
        y "I made things up...I told people I had powers..."
        y "I transferred here, expecting everything to be the same."
        y "And at first it was."
        y "You were mean to me, called me names, just like everyone else."
        y "But eventually, you started to like me, think of me as a friend..."
        y "Even if you didn't really show it, I could tell just by the way you looked at me."
        show yuuki
        y "I could tell you thought of me as a friend."
        y "Thank you for that."
        y "Thank you for letting me join your group."
        y "Thank you for letting me perform the play with you guys."
        y "Thank you for not hurting me."
        y "Thank you for not talking about me behind my back."
        y "Thank you for listening to me."
        y "Thank you for putting up with my delusions."
        y "Thank you for loving me when no one else would."
        menu:
            "You're going to die today...":
                jump dietoday1

        label dietoday1:
            show yuuki angry
            y "..."
            y "I don't know how you know that...but I believe you."
            "I decided it was time to tell her everything."
            "I told her about how I died."
            "How I met Dolus and got this gift."
            "How I used it to save my sister."
            "How I saw her die in front of the class..."
            "How I thought it might be my own fault..."
            y "..."
            y "Ok."
            y "I believe you."
            y "I know you wouldn't lie to me about this."
            y "If today is my day, that's ok."
            y "I miss my parents so much..."
            y "At least this way...At least I get to see them again."
            y "Thank you for telling me this."
            "I hugged Yuuki again, while the both of us wept in silence."
            "We hugged for what felt like forever."
            "Eventually, I took a step back to say something, and I saw it again."
            show yuuki dead
            "I fell to the ground at her feet and wept some more."
            "I felt helpless."
            "I knew I couldn't save her."
            "I knew it was my fault."
            "I knew that somehow, my powers had done this to everyone."
            "I felt uselsss."
            "I felt sad."
            "I felt empty."
            "But one emotion stuck with me longer than the others."
            "When I stopped crying, I could still feel one thing pulsating throughout every bone in my body.."
            "Anger. Pure hatred for the one who started this whole mess in the first place."
            jump endgame
    label dietoday:
        show yuuki angry
        y "..."
        y "I don't know how you know that...but I believe you."
        "I decided it was time to tell her everything."
        "I told her about how I died."
        "How I met Dolus and got this gift."
        "How I used it to save my sister."
        "How I saw her die in front of the class..."
        "How I thought it might be my own fault..."
        y "..."
        y "Ok."
        y "I believe you."
        y "I know you wouldn't lie to me about this."
        y "If today is my day, that's ok."
        y "I miss my parents so much..."
        y "At least this way...At least I get to see them again."
        y "Thank you for telling me this."
        menu:
            "I can't save you!":
                jump cantsave1

        label cantsave1:
            y "But [name]...you already have!"
            "I didn't know what she meant."
            show yuuki angry
            y "Before I came here... I had no friends, for reasons that I'm sure you can imagine."
            y "Everyone thought I was a freak, a loser, a nobody."
            y "They made fun of me, called me names, hurt me..."
            "She pulled her hair back and showed me a scar on the back of her head."
            y "I didn't know how to make friends."
            y "Both of my parents were dead... I was broken."
            y "I made things up...I told people I had powers..."
            y "I transferred here, expecting everything to be the same."
            y "And at first it was."
            y "You were mean to me, called me names, just like everyone else."
            y "But eventually, you started to like me, think of me as a friend..."
            y "Even if you didn't really show it, I could tell just by the way you looked at me."
            show yuuki
            y "I could tell you thought of me as a friend."
            y "Thank you for that."
            y "Thank you for letting me join your group."
            y "Thank you for letting me perform the play with you guys."
            y "Thank you for not hurting me."
            y "Thank you for not talking about me behind my back."
            y "Thank you for listening to me."
            y "Thank you for putting up with my delusions."
            y "Thank you for loving me when no one else would."
            "I hugged Yuuki again, while the both of us wept in silence."
            show yuuki angry
            "We hugged for what felt like forever."
            "Eventually, I took a step back to say something, and I saw it again."
            show yuuki dead
            "I fell to the ground at her feet and wept some more."
            "I felt helpless."
            "I knew I couldn't save her."
            "I knew it was my fault."
            "I knew that somehow, my powers had done this to everyone."
            "I felt uselsss."
            "I felt sad."
            "I felt empty."
            "But one emotion stuck with me longer than the others."
            "When I stopped crying, I could still feel one thing pulsating throughout every bone in my body."
            "Anger. Pure hatred for the one who started this whole mess in the first place."
            jump endgame

label endgame:
    "DOLUS!"
    "I screamed her name out as loud as I could manage in my current state."
    "DOLUS! Come down here! Tell me what you did to me!"
    "I screamed her name over and over again for as long as I could."
    "I screamed for an eternity."
    "I screamed until I passed out right in front of Yuuki's motionless corpse."
    scene black
    with fade
    play music "black.mp3"
    "..."
    "Dolus..."
    "Why..."
    show dolus
    d "Is something the matter my child?"
    d "I have heard you call my name and I came as soon as I could."
    menu:
        "What did you do to me?":
            jump dotome

        "I know what you did.":
            jump knowwhat

    label dotome:
        d "I have no idea what you are talking about."
        "I could tell she was lying."
        "I knew exactly what she did."
        jump dolus1

    label knowwhat:
        d "What are you talking about?"
        jump dolus1

label dolus1:
    "I decided to just come out and accuse her of what I think she did."
    '"You made it so that every time I went back in time, someone died." I said.'
    d "..."
    d "Oh"
    d "So..."
    d "It seems you've figured it out then."

    show dolus evil
    "Suddenly Dolus opened her eyes for the first time and I knew I was dead on the money."
    "She had blood-colored eyes and an evil grin that showed she was happy with what she did."
    d "What tipped you off exactly?"
    d "Was it the first time you went back and heard about a mysterious death on the news."
    d "Or was it the second time? Third? No?"
    d "You just figured it out, didn't you?"
    d "It took almost everyone you know dying to make the connection."
    d "Or maybe deep down you already knew, but you just didn't want to believe it."
    d "Maybe you liked your power so much, that you were ok with a few deaths here and there."
    d "As long as you didn't know them, who cares?"
    d "No, I think you actually did just figure it out."
    d "You are pretty stupid, it would take almost 40 million jumps for you to have figured it out."
    d "40 million jumps, 40 millions deaths, what a big weight to carry around with you for the rest of your life."
    d "Jerry's dad, Yuuki, Winrey, your teacher, and a lot more. All dead because of you."
    "I couldn't believe what she was saying."
    "How could she possibly blame me for this?"
    "She was the one who tricked me in the first place!"
    "I suddenly remembered back to when I first met Dolus."
    "I asked her if there was a catch to my power, and she said that there was no catch!"

    '"You told me there was no catch!" I yelled at her in anger.'
    d "Actually, my exact words were there is no catch for you."
    d "That statement is completely true."
    d "Nothing bad happened to you when you went back in time, only other people."
    d "You got off scot-free."
    d "The people who died were chosen at random."
    d "Honestly I'm amazed that so many people you personally knew were among the victims of your latest adventure."
    d "40ish million people dead out of over 7 billion people on this Earth, and you knew 3 of the people who were killed?"
    d "Now that's funny!"
    '"What did you do to me exactly?" I asked her."'
    "I just wanted to know the details of all this."
    d "Well, I suppose there is no harm in telling you everything."
    d "It's not like you can change anything now!"
    d "My name is Dolus, and as you can probably imagine, I am no Angel."
    d "I am in fact a demon."
    d "I have been working under Lucifer for over 10,000 centuries."
    d "And I just have to say, I hate the guy."
    d "The way he runs Hell is so...boring!"
    d "We get new people in all the time, and he just wastes them!"
    d "All Lucifer does is the traditional torture."
    d "Pulling out people's nails, whippings, gouging out eyes, that sort of thing."
    d "And I would consider myself to be a sort of...visionary."
    d "I have so many great ideas for what we could do with Hell."
    d "So one night, I scheduled a meeting with the big man, and I tell him all of my brilliant ideas."
    d "You know what he did? He laughed in my face!"
    d "He told me to know my place and he sent me on my way."
    d "I felt so angry, so betrayed!"
    d "Growing up I was always told how great Lucifer was!"
    d "And when I go in to meet him I find out he's nothing but your average pencil-pusher!"
    d "He had no inspirations! He was content with the boring old Hell."
    d "So that's when I had a brilliant idea."
    d "If I couldn't get Lucifer to listen to my ideas, I would just become the new Lucifer!"
    d "I decided right then and there that I was going to overthrow Lucifer and become the new King of Hell!"
    d "But there was a slight problem with this plan."
    d "I am but a lowly demon, there was no way in Hell that I could possibly beat him."
    d "That's when I remembered an old tale about how demons can get more power by stealing human souls."
    d "See one human soul isn't that much, but every human soul on Earth?"
    d "That would be more than enough to make me the most powerful demon imaginable."
    d "But there was a slight problem."
    d "Demons aren't allowed to kill humans without direct approval from the man himself."
    d "Now obviously Lucifer would never give me permission to kill every human on Earth, so I had to get creative."
    d "I started looking around for a human to do my dirty work for me."
    d "At first I looked for serial killers, someone who could kill people in the old-fashioned way."
    d "I quickly realized that I would never get strong enough if I got souls like that one at a time."
    d "I then moved on to find your little friend Yuuki."
    d "I thought that maybe she would be able to do my bidding if I killed her father and tricked her into helping me."
    d "It didn't really work out though so I moved on."
    d "So I went around the world, looking for someone who's willpower was weak enough for me to influence with relative ease."
    d "And that's when I came across you. A kid who hated his life and everything about it."
    d "A kid with barely any friends. A kid who didn't know how to talk to people. A total moron."
    d "But I didn't think you would be ready just yet, so I decided to stage a little murder suicide to really hurt you."
    d "I possessed your dad and used him to kill himself and your sister."
    d "I then influenced you to rush the guy who had a gun to your head."
    d "He killed you and I knew I had everything in place."
    d "I came to you while you were in purgatory and pretended to be an Angel."
    d "I used all of the power I had to give you the power you possess today."
    d "The thing I didn't tell you however, is that you can't go back in time for free."
    d "Every time you die, your body is forced to look for another person's power to steal."
    d "You take their physical power to come back to life, and I take their spiritual energy that's left over."
    d "And now I feel...great!"
    d "But I'm still not nearly powerful enough to do what I need to do."
    d "I still need you to die a few more billion times."
    "I couldn't believe what I was hearing."
    "Dolus is the one who killed my dad and sister?"
    "She knew that I would try and save her!"
    "And in the process she would gain a lot of strength."
    "What should I do? What can I do?"
    menu:
        "Well I just won't use my powers anymore.":
            jump nopower

        "Please just kill me so that I can die with honor...":
            jump honor

    label nopower:
        "I knew how to beat her."
        "I just wouldn't use my powers anymore!"
        "She can't get stronger if I never give her another soul to steal!"
        d "..."
        d "Hahahahahhaha!"
        d "I'm sorry, but that's funny!"
        d "It doesn't matter if you never use your powers again!"
        d "You are human aren't you? And humans die eventually?"
        d "So let's say you never use your powers again."
        d "Eventually you'll just die of old age, and when that happens you will go back in time by a minute and die again."
        d "And that process will repeat until every person on Earth is dead!"
        "..."
        "She's right."
        "I lost."
        jump dolus2

    label honor:
        d "You utter fool."
        d "Honor is just a construct invented by the foolish to give themselves an excuse to throw away their meaningless lives."
        d "Do you ever hear anybody say that someone who was murdered in a back alley or who died in some sort of accident had an honorable death?"
        d "No, they say that they were murdered or killed. That their lives were cut short in a tragedy."
        d "You know who gets an honorable death?"
        d "Soldiers who never go out to war and never come back alive."
        d "People who sacrificed their own lives to save another."
        d "You know what all these people had in common? They had a choice."
        d "They didn't have to die but they did anyways."
        d "I don't call that honor, I call that weakness!"
        d "And I won't let you be weak!"
        d "You have a purpose and I will make sure you serve it!"
        d "And let me guess, right now you're thinking about how you just won't use your powers anymore, aren't you?"
        d "Well let me tell you, It doesn't matter if you never use your powers again!"
        d "You are human aren't you? And humans die eventually?"
        d "So let's say you never use your powers again."
        d "Eventually you'll just die of old age, and when that happens you will go back in time by a minute and die again."
        d "And that process will repeat until every person on Earth is dead!"
        "..."
        "She's right."
        "I lost."
        jump dolus2

label dolus2:
    d "Well I think our time here is done."
    d "Go back to Earth and live your life how you see fit."
    d "Just know that you will die."
    d "Goodbye [name]! Now go do my bidding!"

    scene bedroom night
    with fade
    play music "dead1.mp3"
    "I left the blackness and somehow ended up in my bedroom."
    "It was dark outside, so I must have been with Dolus for a few hours."
    "I didn't know what to do."
    "Life felt meaningless now."
    "Everyone will die because of me."
    "I walked down the stairs while in a haze."
    "I couldn't think if anything clearly."
    "I had no clear direction."
    "I didn't know where my feet were taking me but for some reason I just felt the need to go downstairs."
    scene living room
    with fade
    "I made it down the stairs and into the living room."
    "The light coming from the window beated against my skin."
    "Wait, wasn't it just night?"
    "I couldn't think clearly, I must be imagining things..."
    "I tried to think about what to do, but my brain was totally shot."
    "Nothing made sense."
    "I suddenly felt my stomach growl so I stumbled into the kitchen."
    scene kitchen
    with fade
    "I made it to the kitchen and I saw the one thing that I was hoping that I would never have to see."
    show mom dead
    "..."
    "No..."
    "I threw up onto the kitchen floor."
    "Not another one..."
    "My mom didn't deserve this..."
    "Wait..."
    "Where's Emilia?"
    "I ran to her room to see if she was in there."
    "Nothing."
    "I ran around the whole house, searching in every nook and cranny for the sister that I had just regained."
    "She was nowhere to be found."
    "I then realized that Jerry wasn't here either."
    "Wait, did he ever come to live with us in the timeline?"
    "I tried to remember but nothing came to me."
    scene living room
    with fade
    "I went back downstairs into the living room and let out a scream."
    show yuuki dead
    show winrey dead at left
    show mom dead at right
    "Before me stood three of the people who's deaths were on my hands."
    "GET AWAY FROM ME!"
    "I screamed these words at the top of my lungs."
    "I felt so much guilt and anger at myself."
    "I didn't know if these were just visions or if they were really standing in front of me."
    "All of the jumps and deaths and pain I went through was finally catching up to me."
    "I didn't know what to do or where to run."
    "So I simply ran back into the kitchen."
    scene kitchen
    with fade
    "I ran in there with the sole purpose of getting away from these visions."
    show yuuki dead
    show winrey dead at left
    show mom dead at right
    "They were still there..."
    "I DON'T WANT TO SEE YOU ANYMORE!!!"
    y "You killed us [name]."
    w "We were your frieds, and you killed us."
    m "Why would you do this to your own mother?"
    m "I thought you loved me?"
    "YOU'RE NOT REAL! NONE OF THIS IS REAL!"
    scene bedroom night
    with fade
    "I ran upstairs into my room and closed the door behind me."
    "I collapsed onto the floor and started crying."
    show yuuki dead
    show winrey dead at left
    show mom dead at right
    y "I thought we were friends."
    w "I thought you liked me."
    "I DON'T WANT TO SEE ANY OF YOU ANYMORE!"
    "I don't want to see anything anymore..."
    "I couldn't take this anymore..."
    "This guilt...This pain...This suffering..."
    "Why me? What did I do to deserve it?"
    m "I'm so disappointed in you [name]."
    m "How could you have been so selfish?"
    y "The entire world will die because of you."
    "SHUT UP!"
    "I DON'T WANT TO SEE YOU ANYMORE!"
    "I just wanted these visions to leave me alone."
    scene bathroom home
    with fade
    "I ran into my bathroom and turned the sink water on."
    "I filled the sink up all the way with water and put my entire head into it."
    "The water felt nice and cold."
    "I liked it in here."
    "I couldn't see or hear anything under the water."
    w "Why did you kill me?"
    "AAAAAAGHGGGGGGHHHHH!!!!"
    "I started screaming at the top of my lungs while I was under water."
    "AAAAAAAAAAAHHHHHHHHHH!!!!!"
    "I could scream as loud as I liked and no one would hear me."
    "I ran out of breath so I pulled my head up and looked into the mirror."
    show yuuki dead
    show winrey dead at left
    show mom dead at right
    m "Why did you have to kill us all?"
    w "Why didn't you just kill yourself?"
    y "Why did you have to bring all of us into this."
    "I DIDN'T MEAN TO!"
    "I DIDN'T MEAN FOR ANY OF THIS TO HAPPEN!"
    "I JUST WANTED MY SISTER BACK!"
    y "So selfish..."
    "SHUT UP!"
    "I DON'T TO SEE YOU ANYMORE!"
    "I DON'T WANT TO SEE ANYTHING ANYMORE."
    "I punched the mirror as hard as I could and the whole mirror shattered and pieces of glass spilled everywhere."
    "I looked down at my hand to see that it was covered in blood."
    w "Why don't you just die and join us?"
    "I would if I could..."
    "I knew what would happen if I tried to do that..."
    "I would come back and some poor soul would die and take my place..."
    "What am I supposed to do?"
    "Are these ghosts going to follow me around for the rest of my life?"
    "I don't want to see them anymore."
    "They are just a stark reminder of my past failings..."
    "I wish I never tried to save my sister..."
    "No, I wish I never accepted these powers."
    "I don't want to see my failings anymore..."
    "I wish I couldn't see anymore."
    "Suddenly I looked down in the sink and noticed a particularly sharp piece of glass."
    "I picked it up and held it in my hands."
    m "I wish I never gave birth to you."
    m "Then maybe the world wouldn't have to suffer this fate."
    "I didn't want to see them anymore..."
    "Before I could think of what I was doing, I took the piece of glass and slashed my left eye."
    "AAAAGHHH!"
    "The pain hurt more than I would have ever imagined but it was working."
    "I looked into the mirror and I couldn't see anything out of my left eye anymore."
    "It was completely blind and blood was starting to pour into my right eye."
    "HAHAHAHAHAHA!"
    "I laughed in utter joy when I realized that my pain was about to be over!"
    "I beat Dolus!"
    "I don't have to die to beat her, I just have to blind myself!"
    "If I can't see what's going on, than it's all ok."
    "HAHAHAHA!"
    "I laughed uncontrollably as I took the shard of glass and started to cut open my right eye."
    scene black
    with fade
    "I looked up and realized I won!"
    "I couldn't see them anymore!"
    "I couldn't even hear them anymore!"
    "HAHAHAHAHAHA!"
    "..."
    "Before I knew what was happening, I felt myslef hit the floor."
    scene black
    with fade
    play sound "heart.mp3"
    "{i}BEEP! BEEP! BEEP!{/i}"
    "..."
    "Where am I?"
    "I could hear a beeping sound, but not the one that my alarm made..."
    "Was it a heart monitor? Like the ones in hospitals?"
    "I hear something else as well..."
    "Crying?"
    "But not just anybody..."
    "Emilia!"
    "I could tell that it was her who was crying."
    '"Emilia?" I asked in a low voice.'
    em "..."
    em "[name]! You're awake!"
    "I tried to look over at her but I couldn't see anything."
    "Oh yeah..."
    em "[name]! I'm so happy you're awake!"
    '"Is...Is mom dead?"'
    em "..."
    em "Yes..."
    em "I...I came home from school after something weird happened to a classmate of mine..."
    em "He suddenly froze up and his face was completely empty..."
    em "I was so scared I ran home and I saw mom in the kitchen...And she...she..."
    "Suddenly Emilia burst out into a fit of hysteria."
    em "Why her? Why? Wasn't it enough to lose dad? Why did she have to die as well?"
    em "And then I came upstairs...And I could hear water running from your bathroom..."
    em "I was so relieved that you were home so I walked in your bathroom and I saw..."
    em "There was so much blood..."
    em "It reminded me of dad..."
    em "I thought you had done it too..."
    em "But I could hear you breathing..."
    em "I called 911 but there was no answer."
    em "The thing that happened to my classmate and mom..."
    em "Evidently it's happening all over the world..."
    em "Anyways, I picked you up and drove you to the hospital myself."
    em "[name]...What's going on?"
    em "I saw a news report a few minutes ago saying that around 40 million people were dead just like mom..."
    "I wanted to tell her everything but I couldn't work up the courage to say it."
    "I wanted to tell her about how all of this was my fault. How I did all this to save her. How I cut my own eyes out because I was so ashamed and scared..."
    "But if I did that she wouldn't believe me..."
    "And even if she did, then what?"
    "She would just feel like this whole thing was her fault..."
    "No. I can't have her feel this guilt."
    "I have to carry it myself."
    doc "I see the patient if finally awake."
    "I heard a strange voice enter the room, and I realized it must be a doctor."
    doc "Hello Mr. [name], it is a pleasure to meet you."
    doc "Though I do wish we were meeting on better terms."
    doc "I guess I should cut right to the chase."
    doc "It seems that for whatever reason, you decided to blind yourself."
    doc "After hearing about what happened to your mother, I am sure you did this in a state of hysteria."
    doc "I am truly sorry, but I am afraid this is permanent."
    doc "You will live the rest of your life as a blind man."
    em "No..."
    em "Why God...Why is this happening to everyone I love..."
    "I knew in that instant that I had screwed up."
    "I put even more pain on my poor sister..."
    "I would go back and stop myself but I promised I wouldn't use my power anymore."
    em "It's ok doctor, I will take care of him."
    "And that she did."
    "For the rest of my sad empty life, Emilia took care of me."
    "She gave up her chance at a happy life for me."
    "Every day was sheer misery for me."
    "I knew the day would arrive when I die, and I bring the whole world with me."
    "I just hope that Emilia dies before me. I don't want her soul to be taken."
    "My wish was granted."
    "When I was 63 years old Emilia died of a brain tumor."
    "She never married, never made any friends, and all of our family was dead."
    "I was the only one at her funeral."
    "I was admitted into some elderly place where I was looked after by some nice young man."
    "I never said a word to him."
    "I vowed at Emilia's funeral that I would never say a word to anybody."
    "I didn't deserve to make friends after what I did."
    "17 more years passed, and the faitful day arrived."
    "I had an unpreventable heart attack at the age of 80."
    "The doctors tried everything but they couldn't save me."
    "I slowly drifted away to die..."
    doc "The time of death is 8:09 AM, August the 27th, 2082."
    "And then suddenly I was back on my death bed."
    "I knew that the pain was about to start all over again."
    "I would sit here and die over 8 billion more times."
    doc "The time of death is 8:09 AM, August the 27th, 2082."
    "I died again."
    "I see a young girl in Ireland playing with her dolls."
    "Her mom calls her down for dinner and the girl runs downstairs without a care in the world."
    "She sits down and her mother begins to bring her some food but she lets out a scream."
    "Her daughter sat at the table, frozen in time, with all of her facial features missing."
    doc "The time of death is 8:09 AM, August the 27th, 2082."
    "I see an old man in Nigeria coming home from a hard day of work."
    "He can't wait to sit down and read a book to his young daughter."
    "He never makes it home."
    "He freezes in place at the front door, with a blank look on his face."
    doc "The time of death is 8:09 AM, August the 27th, 2082."
    "I see a man entering his first year of college."
    "He studied hard for all of his high school career because he had a dream."
    "He wanted to become a doctor and find the cure to lung cancer so no one would have to suffer the same fate as his mother."
    "He never came to realize that dream."
    "On the first day of class, he woke up early and rushed to classm excited to start his college career."
    "He walked into class and froze, never to move again."
    doc "The time of death is 8:09 AM, August the 27th, 2082."
    "I see an old woman on her death bed."
    "She lived a long and happy life, but she wanted to tell her family how much she loved them one last time."
    "Right before she could get the words out, she realized that her mouth wouldn't work for some reason."
    "She froze in her death bed, and her family never got to hear how much they meant to her."
    doc "The time of death is 8:09 AM, August the 27th, 2082."
    "I see a police man chasing after a person who had just murdered a boy."
    "The officer chases after him at full speed."
    "Right before he can catch up to him, he freezes in his tracks."
    "The murderer gets away."
    doc "The time of death is 8:09 AM, August the 27th, 2082."
    "I see everything and everybody."
    "The mother who had just watched as her daughter had died at the dinner table meets the same fate."
    "The daughter cannot open up the door to let her father in, as she too is frozen."
    "The college student's professor never gets to teach anybody about medicine again."
    "The family never gets to grieve over the death of their relative."
    "The murderer never gets away with his crime."
    "I see every person on Earth."
    "I see their lives, and I see their deaths."
    "I see everything for the first time in over 60 years."
    "I see all 8 billion deaths."
    "And then I see nothing."
    "It is all over."
    "Dolus won."
    "I feel myself slowly drifting off for the last time."
    "I die, and this time, I don't come back."
    "I have finally found my peace."
    scene black
    with fade
    c "Developed by Chris Ferran"
    c "Story by Chris Ferran"
    c "Characters designed by Chris Ferran"
    c "Characters created in Mannequin, developed by ar14"
    c "Supervised by Michael C. Murphy"
    c "Game Developed in Ren'py"
    c 'Music from https://filmmusic.io
      "Ancient Rite" by Kevin MacLeod (https://incompetech.com)
      License: CC BY (http://creativecommons.org/licenses/by/4.0/)'
    c 'Music from https://filmmusic.io
      "A Very Brady Special" by Kevin MacLeod (https://incompetech.com)
      License: CC BY (http://creativecommons.org/licenses/by/4.0/)'
    c 'Music from https://filmmusic.io
      "Exhilarate" by Kevin MacLeod (https://incompetech.com)
      License: CC BY (http://creativecommons.org/licenses/by/4.0/)'
    c 'Music from https://filmmusic.io
      "Wholesome" by Kevin MacLeod (https://incompetech.com)
      License: CC BY (http://creativecommons.org/licenses/by/4.0/)'
    c 'Music from https://filmmusic.io
      "Easy Lemon" by Kevin MacLeod (https://incompetech.com)
      License: CC BY (http://creativecommons.org/licenses/by/4.0/)'
    c 'Music from https://filmmusic.io
      "Modern Jazz Samba" by Kevin MacLeod (https://incompetech.com)
      License: CC BY (http://creativecommons.org/licenses/by/4.0/)'
    c 'Music from https://filmmusic.io
      "String Impromptu Number 1" by Kevin MacLeod (https://incompetech.com)
      License: CC BY (http://creativecommons.org/licenses/by/4.0/)'
    c 'Music from https://filmmusic.io
      "Redletter" by Kevin MacLeod (https://incompetech.com)
      License: CC BY (http://creativecommons.org/licenses/by/4.0/)'
    c 'Music from https://filmmusic.io
      "Comfortable Mystery 2" by Kevin MacLeod (https://incompetech.com)
      License: CC BY (http://creativecommons.org/licenses/by/4.0/)'
    c 'Music from https://filmmusic.io
      "Unseen Horrors" by Kevin MacLeod (https://incompetech.com)
      License: CC BY (http://creativecommons.org/licenses/by/4.0/)'
    c 'Music from https://filmmusic.io
      "Ishikari Lore" by Kevin MacLeod (https://incompetech.com)
      License: CC BY (http://creativecommons.org/licenses/by/4.0/)'
    c 'Music from https://filmmusic.io
      "Stay The Course" by Kevin MacLeod (https://incompetech.com)
      License: CC BY (http://creativecommons.org/licenses/by/4.0/)'
    c 'Gun sound effect from https://www.freesoundeffects.com/'
    c 'Explosion sound effect from https://freesound.org/people/tommccann/sounds/235968/'
    c 'Alarm sound effect from https://freesound.org/people/ZyryTSounds/sounds/219244/'
    c 'Doorbell sound effect from https://freesound.org/people/kwahmah_02/sounds/275072/'
    c 'Knock sound effect from https://freesound.org/people/Philip_Daniels/sounds/244325/'
    c 'Dropping luggage sound effect from https://freesound.org/people/stephenbist/sounds/434781/'
    c 'Heart monitor sound effect from https://freesound.org/people/samfk360/sounds/148897/'
    c "Special thanks to Michael C. Murphy and the MTSU Honors College"

    return


label StayPut:
    "No. As tempting as it may be to bring my sister back, I shouldn't."
    "Because I met Dolus, I now know that God is real."
    "This means that she must have died for a reason."
    "Who am I to go against God?"
    "Plus would I even be able to survive all of those time jumps?"
    "If my calculations are correct, I would have to jump back over 16 million times!"
    "I'm sure to lose my sanity if I do that."
    "Plus I used to not even carry a gun around, which means I would have to resort to using my old pocket knife."
    "That would be a much more painful death than a shot to the head."
    "Plus that death would'nt be instant like my gun."
    "It would be long and drawn out. It would probably be absurdly painful as well."
    "And since it would take longer to die, I would have to jump a lot more times as well."
    "I'm sure after all is said and done, I would have to jump well over 1 million times."
    "And if the butterfly effect is real, who knows what consequences would come from saving her?"
    "I could somehow end up killing every person on Earth if I'm not careful!"
    "Sorry Emilia, as much as I want to save you, I can't."
    "..."
    "Oh crap!"
    "How could I have forgotten?"

    "The time changed last night, and we moved foward an hour in time!"
    "Class begins in 15 minutes!"
    "I rushed out of my house and ran to school."
    scene classroom
    with fade
    play music "classroom.mp3"
    "I made it to class with exactly no time to spare."
    "I was the last person there, and Mrs. Striker glared at me and told me to take a seat."
    "I sat down and looked at the clock to see what time it was."
    "I made it to class with no time at all to spare."
    show striker
    s "Hello everyone, I was planning on having us play a little memory game today, but instead I think we wil have a pop quiz."
    "The class groaned in unison."
    show striker angry
    s "Yeah, Yeah I know!"
    s "It's just that everyone did so bad on the last test I feel that we need to take another one to make sure everyone knows the material."
    show darius angry at right
    da "How can you expect us to do better on a test we all failed if you don't tell us about it ahead of time?"
    s "Well if you would just shut up for once in your life and let me finish maybe you would find out!"
    da "..."
    s "That's what I thought!"
    s "Now sit down Darius!"
    da "Sorry..."
    hide darius
    s "Ok, now where was I?"
    s "Ah, yes. We will have a test today over the material you all failed."
    s "The difference is that this time, the test is open book."
    "The class cheered in unison."
    show striker happy
    s "Is that alright with everyone?"
    s "Cool. I'll hand out the test now."
    "Everyone reached into their backpack to get their books out and I did the same."
    "I reached into my backpack but something confused me."
    "I could feel my binder, snacks, and a pencil, but no book."
    "Crap!"
    "In my rush this morning I must have forgotten to grab my book."
    "Mega crap!"
    "My grade is pretty bad right now and the years coming to a close, if I fail this test I might fail this class!"
    "And if I fail, I'll have to repeat the year and I'll lose all my friends!"
    "I can't let that happen!"
    "I need to go back in time!"
    "I looked at the clock."
    "Ok, I think that I'll need to go back exactly 27 times to be at my house."
    "I pulled my gun out and did what was second nature to me at this point."
    play sound "gun.mp3"
    "{i}BANG!!!{/i}"
    scene black
    with fade
    play music "black.mp3"
    "..."
    "You know, if I ever lose my powers somehow I'm really going to be screwed."
    "It's become natural to just shoot myself whenever I screw something up."
    "If I do that without my powers, well that's just suicide with extra steps."
    scene classroom
    with fade
    play music "classroom.mp3"
    s "Ok, now where was I?"
    s "Ah, yes. We will have a test today over the material you all failed."
    s "The difference is that this time, the test is open book."
    "One down, 26 to go."
    play sound "gun.mp3"
    "{i}BANG!!!{/i}"
    scene black
    with fade
    play music "black.mp3"
    "I continued to shoot myself again and again."
    "Every time I did I went back by a minute."
    "No surprise there."
    "Eventually I made it back to the exact second that I was aiming for."
    scene bedroom
    with fade
    play music "classroom.mp3"
    "I grabbed my book, put it in my backpack, and left for school."
    scene classroom
    with fade
    show striker angry
    show darius angry at right
    da "How can you expect us to do better on a test we all failed if you don't tell us about it ahead of time?"
    s "Well if you would just shut up for once in your life and let me finish maybe you would find out!"
    da "..."
    s "That's what I thought!"
    s "Now sit down Darius!"
    da "Sorry..."
    hide darius
    s "Ok, now where was I?"
    s "Ah, yes. We will have a test today over the material you all failed."
    s "The difference is that this time, the test is open book."
    "The class cheered in unison."
    show striker happy
    s "Is that alright with everyone?"
    s "Cool. I'll hand out the test now."
    "And just like that, I made it back to right where I was."
    "This time however, I pulled my book out of my backpack just like everyone else."
    "Striker walked around the room and handed everyone the test, one by one."
    "I was the last person she gave the test to."
    s "Alright class, you will have all period to work on this, so there isn't any rush."
    s "Please take as much time as you need."
    hide striker
    "Striker sat down at her desk and the class began to take the test."
    "I went down the list, question by question, and used my book to answer every single question."
    "It was way easier than I thought it would be!"
    "I was able to find every single question in the book without fail."
    "For once, I think I might have actually aced a test!"
    "After about an hour, I finished up and handed the test to Mrs. Striker."
    "I was one of the last people done, but that was fine with me."
    "I would rather take my time and do a good job than rush it and fail."
    "Class ended and everyone went home."
    scene bedroom night
    with fade
    play music "bedroom-night.mp3"
    "It was later that night when I was in my room."
    "I decided that I would watch some tv, as I had a couple hours before I needed to go to sleep."
    "What should I watch?"
    "BroBro?"
    "Nah. After the play, I was all BroBro'd out for a while."
    "Maybe I'll just watch the news for a little while."
    "It's important to know what's going on in the world after all."
    "I turned on the news to see what was going on."
    tv "Breaking News!"
    "Aw geez, what's this gonna be about?"
    tv "27 more victims were found today, dead to the mysterious illness that's taken the world by storm."
    tv "Just like all of the others, these victims were found frozen, with their eyes and other facial features missing."
    tv "Experts still can't find a correlation between these mysterious deaths!"
    "..."
    "Wait..."
    "27?"
    "That number..."
    "Why does it seem so familiar?"
    "I suddenly remembered why."
    "That was the amount of jumps I made today!"
    play music "dead1.mp3"
    "What a coincidence!"
    "I said the words but even I didn't believe them."
    "It couldn't be a coincidence, there has to be a connection."
    "These deaths only started to happen after I got my powers."
    "No..."
    "Please don't tell me that I caused these deaths..."
    "Did I kill Jerry's father?"
    "I shouldn't jump to conclusions just yet."
    "Ok, I'll go back in time right now."
    "I'll jump exactly 17 times, and if the news reporter announces 17 additional deaths, than I know it's me."
    play sound "gun.mp3"
    "{i}BANG!!!{/i}"
    scene black
    with fade
    "It couldn't be me, could it?"
    "Dolus told me that there were no catches to my power."
    "Someone dying every time I go back would definitely be a catch."
    "Why would God give me a power if it would cause so much chaos and carnage?"
    scene bedroom night
    with fade
    play sound "gun.mp3"
    "{i}BANG!!!{/i}"
    "I jumped back an additioanl 16 times."
    "Every time I did, I got more and more nervous for the outcome."
    "After my jumps had completed, I waited in front of my t.v. with bated breath."
    "After 17 of the longest minutes of my life, the news came back on."
    tv "Breaking News!"
    tv "27 more victims were found today, dead to the mysterious illness that's taken the world by storm."
    tv "Just like all of the others, these victims were found frozen, with their eyes and other facial features missing."
    tv "Experts still can't find a correlation between these mysterious deaths!"
    "Yes!"
    "There are no correlations, it was just a strange..."
    "At that second, something terrible started to happen on the news station."
    "As the reporter was finishing up the story, he suddenly stopped talking and froze in his tracks."
    "That wasn't all."
    "The reporters facial features..."
    "Were missing."
    "That wasn't like that before I jumped..."
    "He was just fine earlier!"
    "The news station suddenly stopped broadcasting, and the t.v. went dark."
    "Oh my God!"
    "It's true!"
    "I caused it!"
    "I caused all of the deaths!"
    "It's all my fault!"
    "That means that Jerry's father died because of me..."
    "What do I do?"
    "I suddenly realized something."
    "Since my powers cause this, that means the person who gave me these powers are at fault."
    "Dolus."
    "She did this."
    "She knew what would happen when I got my powers, and she didn't say a word."
    "I was about to call out her name in anger, but I decided against it."
    "What am I supposed to do to stop her?"
    "She's an angel, she is way more powerful than I am!"
    "I have to figure out a way to beat her."
    "But how?"
    "I don't know anything about this sort of stuff, what can I possibly do to stop her?"
    "Maybe I could tell someone and ask for their help?"
    "But who could I possibly tell?"
    "Darius?"
    "He is my best friend but I doubt he would no what to do."
    "My mom?"
    "She wouldn't be any help either."
    "Winrey?"
    "Nope."
    "Jerry?"
    "If I told him that I caused his father's death he would probably just murder me."
    "Not that that would matter, I would just go back in time, but still..."
    "I don't have the courage to tell him the truth..."
    "Mrs. Striker?"
    "She is my teacher, but I doubt she could do anything..."
    "Wait."
    "Suddenly a person popped into my head."
    "Someone who I had just met recently."
    "Someone who annoyed me, but who I had come to admire."
    "Someone who is always talking about this sort of stuff."
    "Yuuki!"
    "She might be insane, but she is always talking about all sorts of crazy stories."
    "If anybody would believe me, it would be her."
    "Ok, that's the plan."
    "Tomorrow at school, I'm gonna tell her everything."
    scene stairs
    with fade
    play music "classroom.mp3"
    "It was the following day and I had gotten to school way earlier than I usually do."
    "I didn't get there early by choice, I couldn't sleep last night at all."
    "I was up all night thinking of my possible options to defeat Dolus and get rid of this curse."
    "I thought about confronting her directly, but that would probably be a death sentence."
    "No, I just need to let Yuuki in on everything."
    "Her brain works differently than anybody I know."
    "If anybody can figure out how to beat an angel, or whatever Dolus really is, it's her."
    "I was waiting on the stairwell because I know Yuuki passes by here every morning."
    "I stood there for about an hour before I spotted her bubblegum hair from a mile away."
    '"Yuuki!" I yelled at her.'
    "Yuuki turned around, noticed me, and ran to me with her arms behind her back."
    show yuuki
    y "Hello mortal."
    y "You're here much earlier than normal, aren't you?"
    y "Not doing anything illegal, right?"
    y "Because if you are, I want in"
    "Why would she think I was doing something illegal?"
    "Well, I guess accidently killion hundreds of people is illegal..."
    "And why would she want to help me if I was doing something illegal?"
    "Is Yuuki even wilder than I previously thought?"
    "Whatever, I got bigger things to worry about."
    menu:
        "Meet me on the roof after school.":
            jump roof

        "I need to tell you something.":
            jump tellyou

    label roof:
        "I decided to tell her to meet me after school on the rooftop."
        "Our school doesn't technically allow anybody to be on the rooftop without direct permission, but I happen to have a key to get up there."
        "It's a long story of how I happened to obtain this key."
        "But the short version is I was good friends with one of the teachers here and he let me have the key."
        "I told him I would only use it when I wanted to be alone, and that was true."
        "After my sister and father died, I would randomly have panic attacks."
        "Luckily I didn't ever have one in the middle of class, but I did have one at school."
        "I was in the aforementioned teacher's office, when it began to happen."
        "The teacher was obviously scared, but my attack went away quickly and I told him the details."
        "I told him that I can feel it coming sometimes, and when I do I need to be alone and get some fresh air."
        "He gave me the key to the roof and I've used it whenever I felt an attack coming ever since."
        "Luckily I stopped having these attacks a year ago so I don't go to the roof that often anymore."
        "It's still pretty nice to have though."
        y "Why would I meet you on the roof, mortal?"
        y "Don't you know that I, Yuuki Juposerotop, an a very busy person?"
        y "I have to go home and find a way to defeat a ghoul thats been giving me trouble."
        y "Wait, it's a love confession, isn't it?"
        y "That's why you want to get me on the roof, right?"
        y "You want to confess your undying love to me in a isolated place where no one would hear."
        show yuuki happy
        y "I gotta admit, that is a pretty smart plan!"
        y "That way when I reject you nobody will hear and you can save face!"
        y "You are far more wise than I give you credit for!"

        "That was definitely not the reson for my meeting, and I assured her it was something else."
        show yuuki angry
        y "Ugghhh, I was just kidding ya'know?"
        y "Ok, I'll meet you on the roof after school."
        y "But this better be good, I have a meeting with an ogre at 5!"
        "I thought she had to defeat a ghoul?"
        "Oh well, I got the answer I needed."
        jump rooftop

    label tellyou:
        "I decided to go ahead and tell her what I needed to say."
        "I was about to begin confessing, when a lot of people started to walk by."
        "Crap, class is about to start, there is no way I can tell her now."
        "I decided to tell her to meet me after school on the rooftop."
        "Our school doesn't technically allow anybody to be on the rooftop without direct permission, but I happen to have a key to get up there."
        "It's a long story of how I happened to obtain this key."
        "But the short version is I was good friends with one of the teachers here and he let me have the key."
        "I told him I would only use it when I wanted to be alone, and that was true."
        "After my sister and father died, I would randomly have panic attacks."
        "Luckily I didn't ever have one in the middle of class, but I did have one at school."
        "I was in the aforementioned teacher's office, when it began to happen."
        "The teacher was obviously scared, but my attack went away quickly and I told him the details."
        "I told him that I can feel it coming sometimes, and when I do I need to be alone and get some fresh air."
        "He gave me the key to the roof and I've used it whenever I felt an attack coming ever since."
        "Luckily I stopped having these attacks a year ago so I don't go to the roof that often anymore."
        "It's still pretty nice to have though."
        y "Why would I meet you on the roof, mortal?"
        y "Don't you know that I, Yuuki Juposerotop, an a very busy person?"
        y "I have to go home and find a way to defeat a ghoul thats been giving me trouble."
        y "Wait, it's a love confession, isn't it?"
        y "That's why you want to get me on the roof, right?"
        y "You want to confess your undying love to me in a isolated place where no one would hear."
        show yuuki happy
        y "I gotta admit, that is a pretty smart plan!"
        y "That way when I reject you nobody will hear and you can save face!"
        y "You are far more wise than I give you credit for!"

        "That was definitely not the reson for my meeting, and I assured her it was something else."
        show yuuki angry
        y "Ugghhh, I was just kidding ya'know?"
        y "Ok, I'll meet you on the roof after school."
        y "But this better be good, I have a meeting with an ogre at 5!"
        "I thought she had to defeat a ghoul?"
        "Oh well, I got the answer I needed."
        jump rooftop

label rooftop:
    scene school rooftop
    with fade
    "Class went by as usual, and afterwards I headed directly to the roof."
    "I would have just gone with Yuuki, but she needed to use the bathroom."
    "I got to the stairs and put the key into the door that lead to the roof."
    "At that moment I realized that it's possible that they might have changed the locks."
    "I haven't been up here in so long, what if it doesn't work now."
    "My worries faded immedietly when the lock made a clicking sound and the door opened at once."
    "Thank God."
    "I waited up there for a couple minutes, and eventually Yuuki strolled up the stairs and greeted me."
    show yuuki
    y "Hello again mortal!"
    y "Please make this quick."
    y "I, Yuuki Frentop, have to go to the dentist at 6!"
    "Out of all the stories she had ever made up, that was the only one that didn't involve any fantasy elements."
    "My heart started to beat faster as I realized that I was about to tell someone my biggest secret."
    menu:
        "I accidently killed a lot of people.":
            jump killed

        "I have the power to go back in time.":
            jump backintime

        "I need your help to defeat an evil being.":
            jump evilbeing

    label killed:
        y "..."
        y "BHAHAHAHAHAHAHAHA!"
        y "That's a good one mortal!"
        y "I know that you don't have it in you to kill someone!"
        y "Plus, even if you did, why would you tell me?"
        show yuuki angry
        y "Unless you're planning to kill me as well..."
        "I realized this probably wasn't the best way to start out my confession."
        "I went ahead and told her the rest of my story."
        "How I died and met Dolus and she gave me these powers."
        "How I used them to make my life better."
        "How I considered using them to save my sister but decided against it."
        "How I found out that my power was killing people against my knowledge."
        "And how I needed her help to defeat Dolus."
        y "..."
        y "You're serious, aren't you?"
        menu:
            "Yes":
                jump yes1

            "Do you need me to prove it?":
                jump needme

        label yes1:
            y "Ok, I believe you."
            show yuuki happy
            y "And I, Yuuki Sequopo, will help you defeat this Dolus creature!"
            "I couldn't believe my ears."
            "She was actually gonna help me!"
            y "We should work on a solution immediately!"
            y "..."
            y "Or almost immediately."
            y "I actually do have a dentist appointment..."
            y "Meet me at the beach tonight at 7:30."
            "The beach?"
            "Why would she want to meet there?"
            "There is so many goodp places to meet, but the beach?"
            "I hate sand."
            "It's coarse and rough and irritating...And it gets everywhere!"
            "Oh well, if she is willing to help me, the least I can do is meet where she wants to meet."
            "I agreed and we went our seperate ways."
            jump beach

        label needme:
            "I knew she wouldn't believe me without any proof, so I decided to prove it to her."
            y "No, I believe you."
            y "I know you wouldn't lie to me about something so serious."
            "To my utmost surprise she actually believed me without any proof."
            "Yuuki really is a good friend..."
            "I never believe her when she talks about any of her stories..."
            "What if some of them are true?"
            show yuuki happy
            y "And I, Yuuki Sequopo, will help you defeat this Dolus creature!"
            "I couldn't believe my ears."
            "She was actually gonna help me!"
            y "We should work on a solution immediately!"
            y "..."
            y "Or almost immediately."
            y "I actually do have a dentist appointment..."
            y "Meet me at the beach tonight at 7:30."
            "The beach?"
            "Why would she want to meet there?"
            "There is so many goodp places to meet, but the beach?"
            "I hate sand."
            "It's coarse and rough and irritating...And it gets everywhere!"
            "Oh well, if she is willing to help me, the least I can do is meet where she wants to meet."
            "I agreed and we went our seperate ways."
            jump beach

    label backintime:
        "I decided to jump right into it and tell her everything."
        "How I died and met Dolus and she gave me these powers."
        "How I used them to make my life better."
        "How I considered using them to save my sister but decided against it."
        "How I found out that my power was killing people against my knowledge."
        "And how I needed her help to defeat Dolus."
        y "..."
        y "You're serious, aren't you?"
        menu:
            "Yes":
                jump yes2

            "Do you need me to prove it?":
                jump needme2

        label yes2:
            y "Ok, I believe you."
            show yuuki happy
            y "And I, Yuuki Sequopo, will help you defeat this Dolus creature!"
            "I couldn't believe my ears."
            "She was actually gonna help me!"
            y "We should work on a solution immediately!"
            y "..."
            y "Or almost immediately."
            y "I actually do have a dentist appointment..."
            y "Meet me at the beach tonight at 7:30."
            "The beach?"
            "Why would she want to meet there?"
            "There is so many goodp places to meet, but the beach?"
            "I hate sand."
            "It's coarse and rough and irritating...And it gets everywhere!"
            "Oh well, if she is willing to help me, the least I can do is meet where she wants to meet."
            "I agreed and we went our seperate ways."
            jump beach

        label needme2:
            "I knew she wouldn't believe me without any proof, so I decided to prove it to her."
            y "No, I believe you."
            y "I know you wouldn't lie to me about something so serious."
            "To my utmost surprise she actually believed me without any proof."
            "Yuuki really is a good friend..."
            "I never believe her when she talks about any of her stories..."
            "What if some of them are true?"
            show yuuki happy
            y "And I, Yuuki Sequopo, will help you defeat this Dolus creature!"
            "I couldn't believe my ears."
            "She was actually gonna help me!"
            y "We should work on a solution immediately!"
            y "..."
            y "Or almost immediately."
            y "I actually do have a dentist appointment..."
            y "Meet me at the beach tonight at 7:30."
            "The beach?"
            "Why would she want to meet there?"
            "There is so many goodp places to meet, but the beach?"
            "I hate sand."
            "It's coarse and rough and irritating...And it gets everywhere!"
            "Oh well, if she is willing to help me, the least I can do is meet where she wants to meet."
            "I agreed and we went our seperate ways."
            jump beach

    label evilbeing:
        "I decided it might be best to start with telling her how much I needed help."
        "I have always heard in writing classes how you should start a story with a hook to draw in your readers."
        "I thought it might be best to do this with Yuuki."
        y "What kind of evil being?"
        "She took that very seriously."
        "I told her that I wasn't sure, but she told me she was an angel of God."
        y "Well she was definitely lying, no angel would be evil."
        "I agreed, and told her the rest of the story."
        "How I died and met Dolus and she gave me these powers."
        "How I used them to make my life better."
        "How I considered using them to save my sister but decided against it."
        "How I found out that my power was killing people against my knowledge."
        "And how I needed her help to defeat Dolus."
        y "..."
        y "You're serious, aren't you?"
        menu:
            "Yes":
                jump yes3

            "Do you need me to prove it?":
                jump needme3

        label yes3:
            y "Ok, I believe you."
            show yuuki happy
            y "And I, Yuuki Sequopo, will help you defeat this Dolus creature!"
            "I couldn't believe my ears."
            "She was actually gonna help me!"
            y "We should work on a solution immediately!"
            y "..."
            y "Or almost immediately."
            y "I actually do have a dentist appointment..."
            y "Meet me at the beach tonight at 7:30."
            "The beach?"
            "Why would she want to meet there?"
            "There is so many goodp places to meet, but the beach?"
            "I hate sand."
            "It's coarse and rough and irritating...And it gets everywhere!"
            "Oh well, if she is willing to help me, the least I can do is meet where she wants to meet."
            "I agreed and we went our seperate ways."
            jump beach

        label needme3:
            "I knew she wouldn't believe me without any proof, so I decided to prove it to her."
            y "No, I believe you."
            y "I know you wouldn't lie to me about something so serious."
            "To my utmost surprise she actually believed me without any proof."
            "Yuuki really is a good friend..."
            "I never believe her when she talks about any of her stories..."
            "What if some of them are true?"
            show yuuki happy
            y "And I, Yuuki Sequopo, will help you defeat this Dolus creature!"
            "I couldn't believe my ears."
            "She was actually gonna help me!"
            y "We should work on a solution immediately!"
            y "..."
            y "Or almost immediately."
            y "I actually do have a dentist appointment..."
            y "Meet me at the beach tonight at 7:30."
            "The beach?"
            "Why would she want to meet there?"
            "There is so many goodp places to meet, but the beach?"
            "I hate sand."
            "It's coarse and rough and irritating...And it gets everywhere!"
            "Oh well, if she is willing to help me, the least I can do is meet where she wants to meet."
            "I agreed and we went our seperate ways."
            jump beach

label beach:
    scene beach sunset simple
    with fade
    play music "beach.mp3"

    "I did as Yuuki said and met her at the beach at 7:30."
    "This place brings back so many memories..."
    "I used to go here all the time with my family."

    "I have so many fond memories of swimming in the ocean with my sister..."
    "One time we swore we sall a shark."

    "Turns out it was just an inflatable toy, but that didn't stop us from telling eveyone about it..."

    "While me and my sister were playing, my dad would always use a public grill to cook some hamburgers."
    "And right around this time, right at sunset, the four of us would come together and eat."
    "Those days are over now."
    "As much as I hate to say it, I'm glad I didn't save my sister."
    "Who knows how many people would have died if I did?"

    "Before I could think about these painful memories for any longer, Yuuki appeared out of nowhere."
    show yuuki
    y "Hello [name]!"
    y "You ready to beat this Dolus lady?"
    "I was happy to see that Yuuki was excited to help me."
    y "Sorry I'm a little late, but I stopped by at my house to pick something up."
    "Suddenly, Yuuki pulled a gigantic hardcover book seemingly out of nowhere."
    y "I've never actually read this book, but I remember that my dad used to read it all the time."
    y "Evidently it was a gift from my mom."
    y "I thought it might come in handy, as it has information on all types of mythological creatures."
    "Yuuki opened the book and a loose slip of paper fell out."
    y "What's this?"
    "Yuuki picked the note up and started to read it."
    show yuuki angry
    y "It's from my dad..."
    y "It's addressed...to me..."
    "I asked Yuuki if she wanted to read it out loud, or if she would rather keep it to herself."
    y "No, it's fine. I can read it out loud."
    y "Who knows, maybe it will contain some valuable information."
    "Yuuki began to read from the note."
    no "To my beloved Yuuki."
    no "Hey Yuuki, I'm sure by the time your reading this letter, I am already dead."
    no "I'm so sorry to leave you all by yourself in such an early stage of your life, but I'm afraid I had no choice."
    no "A demon who disguised herself as an angel has been trying to possess me for a few months now."
    no "I haven't been giving in to her pressure though."
    no "I have been doing everything in my power to stop her advances, but I'm afraid I'm at my last rope."
    no "Your mother taught me some of her powers, and I have been using these to fight her off, but I'm becoming increasingly weaker."
    no "Once again I just want to reiterate how sorry I am for leaving you in a state like this."
    no "But listen to me Yuuki, for what I'm about to tell you is of the utmost importance."
    no "I have reason to believe that this demon will eventually come after you once I am gone."
    no "It seems that she is looking for a susceptible human to do her dirty work."
    no "I don't have the details, but I know that she is trying to become stronger for some reason."
    no "When she comes, I need you to remember that both me and your mother are with you."
    no "Also, you are not as weak as I am."
    no "Your mother taught me a few tricks, but without the proper bloodline there was only so much she could do for me."
    no "You don't have that problem Yuuki."
    no "You have inherited your mother's powers, whether you know it or not!"
    no "I think you do know it though."
    no "You are always going around acting like you have powers..."
    no "You must know that you possess these gifts from your mother, and when that demon comes after you or someone close to you, it will be important for you to use these powers to stop her!"
    no "Now to access these powers you must do a very simple task."
    no "You must believe in yourself."
    no "I know that sounds cheesy, but it's true."
    no "I love you Yuuki, and I know that when the time comes, you will be more powerful than that demon."
    no "Goodbye."
    y "..."
    y "This...This can't be..."
    y "I actually have powers?"
    "I was a little confused as to why this surprised her so much."
    "Yuuki was always going on about her powers."
    "Of course I never believed her, but now that it turns out she was right, why is she so surprised?"
    y "I know I always act like I have powers, but I'm just playing around..."
    y "I do it for attention."
    y "I don't know how to talk to people or make friends, so I just put myself in my own little bubble..."
    y "But now it turns out I actually have powers, and all I need to do is believe in myself?"
    y "Now that's just bad writing..."
    y "But how am I supposed to believe in myself?"
    y "I couldn't save my dad, I couldn't make friends, I couldn't do anything..."
    "How could she say such nonsense?"
    "She couldn't make any friends? What does she think I am?"
    menu:
        "But I'm your friend.":
            jump yourfriend

        "I believe in you.":
            jump believein

    label yourfriend:
        y "..."
        show yuuki
        y "Well of course you are mortal!"
        y "I was only teasing, I know that we are friends!"
        show yuuki angry
        y "I guess I just wanted you to say it..."
        jump close

    label believein:
        y "You...you do?"
        y "But why?"
        "I told her that I believed in her because I've seen how strong and courageous she can be."
        "She's always the life of the party, and she never shows any signs of weakness."
        "If anybody can do it, I knew Yuuki could."
        y "Really?"
        y "Thank you..."
        y "Thank you so much..."
        jump close

label close:
    y "I have to admit mortal, I'm scared."
    y "This thing we have to beat, it seems like she's the one who killed my father."
    y "I don't want her to kill me..."
    "I told Yuuki that wasn't going to happen. We will beat her. We have to beat her."
    "For the sake of every person on Earth we must win."
    show yuuki happy
    y "You're right!"
    y "We will win!"
    y "Or my name isn't Yuuki Fawklberry!"
    y "But just in case, I want to tell you something."
    show yuuki angry
    y "Before I came here... I had no friends, for reasons that I'm sure you can imagine."
    y "Everyone thought I was a freak, a loser, a nobody."
    y "They made fun of me, called me names, hurt me..."
    "She pulled her hair back and showed me a scar on the back of her head."
    y "I didn't know how to make friends."
    y "Both of my parents were dead... I was broken."
    y "I made things up...I told people I had powers..."
    y "I transferred here, expecting everything to be the same."
    y "And at first it was."
    y "You were mean to me, called me names, just like everyone else."
    y "But eventually, you started to like me, think of me as a friend..."
    y "Even if you didn't really show it, I could tell just by the way you looked at me."
    show yuuki
    y "I could tell you thought of me as a friend."
    y "Thank you for that."
    y "Thank you for letting me join your group."
    y "Thank you for letting me perform the play with you guys."
    y "Thank you for not hurting me."
    y "Thank you for not talking about me behind my back."
    y "Thank you for listening to me."
    y "Thank you for putting up with my delusions, even though it turns out they weren't delusions at all."
    y "Thank you for coming to me in your time of need."
    y "Thank you for loving me when no one else would."
    "I didn't know what to say."
    "I was about to say something, but before I could, everything went black."
    scene black
    with fade
    play music "black.mp3"
    "..."
    "Why am I here?"
    show dolus
    d "Hello child."
    d "I have brought you here because I head you say my name a few times, so I came as quickly as I could."
    d "Is there something that you need?"
    menu:
        "What did you do to me?":
            jump dotome1

        "I know what you did.":
            jump knowwhat1

    label dotome1:
        d "I have no idea what you are talking about."
        "I could tell she was lying."
        "I knew exactly what she did."
        jump dolus5

    label knowwhat1:
        d "What are you talking about?"
        jump dolus5

label dolus5:
    "I decided to just come out and accuse her of what I think she did."
    '"You made it so that every time I went back in time, someone died." I said.'
    d "..."
    d "Oh"
    d "So..."
    d "It seems you've figured it out then."

    show dolus evil
    "Suddenly Dolus opened her eyes for the first time and I knew I was dead on the money."
    "She had blood-colored eyes and an evil grin that showed she was happy with what she did."
    d "What tipped you off exactly?"
    d "Was it the first time you went back and heard about a mysterious death on the news."
    d "Or was it the second time? Third? No?"
    d "You just figured it out, didn't you?"
    d "Or maybe deep down you already knew, but you just didn't want to believe it."
    d "Maybe you liked your power so much, that you were ok with a few deaths here and there."
    d "As long as you didn't know them, who cares?"
    d "All those people's deaths, including Jerry's father, are on your hands."
    "I couldn't believe what she was saying."
    "How could she possibly blame me for all this?"
    "She's the one who put this curse on me!"
    "I suddenly remembered back to when I first met Dolus."
    "I asked her if there was a catch to my power, and she said that there was no catch!"

    '"You told me there was no catch!" I yelled at her in anger.'
    d "Actually, my exact words were there is no catch for you."
    d "That statement is completely true."
    d "Nothing bad happened to you when you went back in time, only other people."
    d "You got off scot-free."
    d "The people who died were chosen at random."
    d "Honestly I'm surprised that you knew someone who died at all."
    d "I mean what are the chances of Jerry's dad dying out of the 7 billion people on this planet!"
    d "It's pretty funny when you think about it!"
    '"What did you do to me exactly?" I asked her."'
    "I just wanted to know the details of all this."
    d "Well, I suppose there is no harm in telling you everything."
    d "It's not like you can change anything now!"
    d "My name is Dolus, and as you can probably imagine, I am no Angel."
    d "I am in fact a demon."
    d "I have been working under Lucifer for over 10,000 centuries."
    d "And I just have to say, I hate the guy."
    d "The way he runs Hell is so...boring!"
    d "We get new people in all the time, and he just wastes them!"
    d "All Lucifer does is the traditional torture."
    d "Pulling out people's nails, whippings, gouging out eyes, that sort of thing."
    d "And I would consider myself to be a sort of...visionary."
    d "I have so many great ideas for what we could do with Hell."
    d "So one night, I scheduled a meeting with the big man, and I tell him all of my brilliant ideas."
    d "You know what he did? He laughed in my face!"
    d "He told me to know my place and he sent me on my way."
    d "I felt so angry, so betrayed!"
    d "Growing up I was always told how great Lucifer was!"
    d "And when I go in to meet him I find out he's nothing but your average pencil-pusher!"
    d "He had no inspirations! He was content with the boring old Hell."
    d "So that's when I had a brilliant idea."
    d "If I couldn't get Lucifer to listen to my ideas, I would just become the new Lucifer!"
    d "I decided right then and there that I was going to overthrow Lucifer and become the new King of Hell!"
    d "But there was a slight problem with this plan."
    d "I am but a lowly demon, there was no way in Hell that I could possibly beat him."
    d "That's when I remembered an old tale about how demons can get more power by stealing human souls."
    d "See one human soul isn't that much, but every human soul on Earth?"
    d "That would be more than enough to make me the most powerful demon imaginable."
    d "But there was a slight problem."
    d "Demons aren't allowed to kill humans without direct approval from the man himself."
    d "Now obviously Lucifer would never give me permission to kill every human on Earth, so I had to get creative."
    d "I started looking around for a human to do my dirty work for me."
    d "At first I looked for serial killers, someone who could kill people in the old-fashioned way."
    d "I quickly realized that I would never get strong enough if I got souls like that one at a time."
    d "I then moved on to find your little friend Yuuki."
    d "I thought that maybe she would be able to do my bidding if I killed her father and tricked her into helping me."
    d "It didn't really work out though so I moved on."
    d "So I went around the world, looking for someone who's willpower was weak enough for me to influence with relative ease."
    d "And that's when I came across you. A kid who hated his life and everything about it."
    d "A kid with barely any friends. A kid who didn't know how to talk to people. A total moron."
    d "But I didn't think you would be ready just yet, so I decided to stage a little murder suicide to really hurt you."
    d "I possessed your dad and used him to kill himself and your sister."
    d "I then influenced you to rush the guy who had a gun to your head."
    d "He killed you and I knew I had everything in place."
    d "I came to you while you were in purgatory and pretended to be an Angel."
    d "I used all of the power I had to give you the power you possess today."
    d "The thing I didn't tell you however, is that you can't go back in time for free."
    d "Every time you die, your body is forced to look for another person's power to steal."
    d "You take their physical power to come back to life, and I take their spiritual energy that's left over."
    d "And now I feel...great!"
    d "But I'm still not nearly powerful enough to do what I need to do."
    d "I still need you to die a few more billion times."
    "I couldn't believe what I was hearing."
    "Dolus is the one who killed my dad and sister?"
"What should I do? What can I do?"
menu:
    "Well I just won't use my powers anymore.":
        jump nopower1

    "Please just kill me so that I can die with honor...":
        jump honor1

label nopower1:
        "I knew how to beat her."
        "I just wouldn't use my powers anymore!"
        "She can't get stronger if I never give her another soul to steal!"
        d "..."
        d "Hahahahahhaha!"
        d "I'm sorry, but that's funny!"
        d "It doesn't matter if you never use your powers again!"
        d "You are human aren't you? And humans die eventually?"
        d "So let's say you never use your powers again."
        d "Eventually you'll just die of old age, and when that happens you will go back in time by a minute and die again."
        d "And that process will repeat until every person on Earth is dead!"
        "..."
        "She's right."
        "I lost."
        jump dolus6

label honor1:
        d "You utter fool."
        d "Honor is just a construct invented by the foolish to give themselves an excuse to throw away their meaningless lives."
        d "Do you ever hear anybody say that someone who was murdered in a back alley or who died in some sort of accident had an honorable death?"
        d "No, they say that they were murdered or killed. That their lives were cut short in a tragedy."
        d "You know who gets an honorable death?"
        d "Soldiers who never go out to war and never come back alive."
        d "People who sacrificed their own lives to save another."
        d "You know what all these people had in common? They had a choice."
        d "They didn't have to die but they did anyways."
        d "I don't call that honor, I call that weakness!"
        d "And I won't let you be weak!"
        d "You have a purpose and I will make sure you serve it!"
        d "And let me guess, right now you're thinking about how you just won't use your powers anymore, aren't you?"
        d "Well let me tell you, It doesn't matter if you never use your powers again!"
        d "You are human aren't you? And humans die eventually?"
        d "So let's say you never use your powers again."
        d "Eventually you'll just die of old age, and when that happens you will go back in time by a minute and die again."
        d "And that process will repeat until every person on Earth is dead!"
        "..."
        "She's right."
        "I lost."
        jump dolus6

label dolus6:
    d "Well I think our time here is done."
    d "Go back to Earth and live your life how you see fit."
    d "Just know that you will die."
    d "Goodbye [name]! Now go do my biddi..."
    "Before she could finish her sentence, we both heard a loud sound."
    play sound "explosion.wav"
    "{i}BOOM! BOOM! BOOM!{/i}"
    d "What the hell is that?"
    "Suddenly, we heard another loud sound, and then before my eyes, I saw her."
    show yuuki at right
    play music "rock-music.mp3"
    y "Come on [name], why did you have to start the party without me?"
    "Yuuki!"
    d "How did you possibly get here?"
    d "We're in purgatory, no mortal being can possibly get here on their own!"
    y "I'm not normal mortal!"
    y "My mother was an angel!"
    y "And she passed down her heavenly powers to me!"
    d "Liar!"
    y "I'm many things, and a liar is in fact one of them, but I'm not bluffing this time!"
    d "I'll kill you!"
    y "Oh I don't think so!"
    show yuuki happy at right
    y "I haven't had any time to practice these powers, but I don't think I'll need to perform that well to kick your pathetic self!"
    d "You'll pay for those words you brat!"
    y "I guess we'll find out!"
    y "Who's better, a demon or a half-angel?"
    "I couldn't believe what I was seeing."
    "Yuuki's mother was an angel?"
    "And on top of that she figured out how to use her powers?"
    y "Hey [name], it turns out my dad was right! I did only need to believe in myself!"
    y "And I couldn't have done that without you, so thanks!"
    y "Now let's kill this demon once and for all!"
    "And with that, Yuuki started to do all sorts of crazy things."
    "She shot lasers out of her eyes, flew all around the place, and even used some sort of mind power to make Dolus breakdance!"
    y "That one is my mother's specialty!"
    "And as quick as it started, it ended."
    hide dolus
    "Laying before me was Dolus's corpse."
    "We won."
    "Or I guess Yuuki won, I didn't actually do anything."
    show yuuki angry
    y "That's for my parents you monster."
    '"You did it! You beat Dolus!" I cried out to her in awe.'
    show yuuki
    y "Yeah, she wasn't actually that tough once I started throwing my weight around."
    y "Turns out she's more of the behind the scenes type."
    y "She would rather manipulate people from the shadows instead of fighting face to face."
    y "Which works out in my favor."
    y "I always was better at direct confrontations."
    y "Well, I guess we better get out of here!"
    "Yuuki grabbed my hand and before I knew it, we had teleported to the beach."
    scene beach sunset simple
    with fade
    play music "heaven.mp3"
    show yuuki
    y "Well, I guess we're done here."
    '"Not quite yet." I told her'
    y "Why? What else do we have to do?"
    menu:
        "Kiss her.":
            jump kiss

        "Thank her.":
            jump thankher

    label kiss:
        "Before I could think about what I was doing, I reached out and kissed her."
        show yuuki angry
        y "Wha...? What was that for?"
        '"That was my way of thanking you." I told her with a warm smile on my face'
        y "..."
        y "Well...I didn't really get to thank you properly either..."
        "Yuuki then reached foward and kissed me."
        "Both of our faces were hot red and I could tell things were getting awkward."
        show yuuki happy
        y "Well...I guess it's time to go home!"
        "I agreed and together the two of us walked back to our houses."
        scene black
        with fade
        "The rest of my life went by and it was as amazing as I could have hoped for."
        "Me and Yuuki eventually got married, and Darius proposed to Winrey at the wedding."
        "I thought it was a little tacky, but I let it slide."
        "The four of us remained close friends until we were all old and senile."
        "I even made up with Jerry eventually, and the two of us became good friends."
        "When I was the ripe old age of 86 I passed away peacefully, surrounded by my loved ones."
        "I was scared that I still had the curse, but that worry went away quickly when I woke up and saw a familiar face..."
        scene heaven
        with fade
        show emilia
        em "[name]... Is that really you?"
        "I couldn't believe my eyes. Before me stood my sister. Just as she looked before it happened."
        em "It really is you. I...I can't believe it!."
        em "I'm so happy to see you. Come on, let's go see mom and dad!"
        "My sister grabbed my arm and together we ran off into the sunset. A family reunited."
        "A couple of years later Yuuki, Darius, Winrey and Jerry all joined us."
        "After that day I never felt any pain or suffering. I was happy."
        scene black
        with fade
        c "Developed by Chris Ferran"
        c "Story by Chris Ferran"
        c "Characters designed by Chris Ferran"
        c "Characters created in Mannequin, developed by ar14"
        c "Supervised by Michael C. Murphy"
        c "Game Developed in Ren'py"
        c 'Music from https://filmmusic.io
          "Ancient Rite" by Kevin MacLeod (https://incompetech.com)
          License: CC BY (http://creativecommons.org/licenses/by/4.0/)'
        c 'Music from https://filmmusic.io
          "A Very Brady Special" by Kevin MacLeod (https://incompetech.com)
          License: CC BY (http://creativecommons.org/licenses/by/4.0/)'
        c 'Music from https://filmmusic.io
          "Exhilarate" by Kevin MacLeod (https://incompetech.com)
          License: CC BY (http://creativecommons.org/licenses/by/4.0/)'
        c 'Music from https://filmmusic.io
          "Wholesome" by Kevin MacLeod (https://incompetech.com)
          License: CC BY (http://creativecommons.org/licenses/by/4.0/)'
        c 'Music from https://filmmusic.io
          "Easy Lemon" by Kevin MacLeod (https://incompetech.com)
          License: CC BY (http://creativecommons.org/licenses/by/4.0/)'
        c 'Music from https://filmmusic.io
          "Modern Jazz Samba" by Kevin MacLeod (https://incompetech.com)
          License: CC BY (http://creativecommons.org/licenses/by/4.0/)'
        c 'Music from https://filmmusic.io
          "String Impromptu Number 1" by Kevin MacLeod (https://incompetech.com)
          License: CC BY (http://creativecommons.org/licenses/by/4.0/)'
        c 'Music from https://filmmusic.io
          "Redletter" by Kevin MacLeod (https://incompetech.com)
          License: CC BY (http://creativecommons.org/licenses/by/4.0/)'
        c 'Music from https://filmmusic.io
          "Comfortable Mystery 2" by Kevin MacLeod (https://incompetech.com)
          License: CC BY (http://creativecommons.org/licenses/by/4.0/)'
        c 'Music from https://filmmusic.io
          "Unseen Horrors" by Kevin MacLeod (https://incompetech.com)
          License: CC BY (http://creativecommons.org/licenses/by/4.0/)'
        c 'Music from https://filmmusic.io
          "Ishikari Lore" by Kevin MacLeod (https://incompetech.com)
          License: CC BY (http://creativecommons.org/licenses/by/4.0/)'
        c 'Music from https://filmmusic.io
          "Stay The Course" by Kevin MacLeod (https://incompetech.com)
          License: CC BY (http://creativecommons.org/licenses/by/4.0/)'
        c 'Gun sound effect from https://www.freesoundeffects.com/'
        c 'Explosion sound effect from https://freesound.org/people/tommccann/sounds/235968/'
        c 'Alarm sound effect from https://freesound.org/people/ZyryTSounds/sounds/219244/'
        c 'Doorbell sound effect from https://freesound.org/people/kwahmah_02/sounds/275072/'
        c 'Knock sound effect from https://freesound.org/people/Philip_Daniels/sounds/244325/'
        c 'Dropping luggage sound effect from https://freesound.org/people/stephenbist/sounds/434781/'
        c 'Heart monitor sound effect from https://freesound.org/people/samfk360/sounds/148897/'
        c "Special thanks to Michael C. Murphy and the MTSU Honors College"

        return


    label thankher:
        '"Thank you." I told her.'
        y "What?"
        '"Thanks for everything."'
        '"I used to be so sad and lonely."'
        '" I always felt so angry with the world. But then I met you."'
        '"I thought you were annoying and loud, but eventually I realized just how amazing you were."'
        '"And now you have even managed to save me, no, the world!"'
        '"So, from the bottom of my heart, thank you."'
        '"You truly are the best friend I have ever had." I told her with tears running down my face.'
        y "..."
        y "Right back at ya [name]!"
        "The two of said said our goodbyes and went home."
        scene black
        with fade
        "The rest of my life went by and it was as amazing as I could have hoped for."
        "Winrey and Darius got married and I was the best man."

        "Together, Yuuki, Darius, Winrey, and myself all stayed close friends until we were old and senile."
        "Jerry and I eventually saw through our differences and become close."
        "When I was the ripe old age of 86 I passed away peacefully, surrounded by my loved ones."
        "I was scared that I still had the curse, but that worry went away quickly when I woke up and saw a familiar face..."
        scene heaven
        with fade
        show emilia
        em "[name]... Is that really you?"
        "I couldn't believe my eyes. Before me stood my sister. Just as she looked before it happened."
        em "It really is you. I...I can't believe it!."
        em "I'm so happy to see you. Come on, let's go see mom and dad!"
        "My sister grabbed my arm and together we ran off into the sunset. A family reunited."
        "A couple of years later Yuuki, Darius, Winrey and Jerry all joined us."
        "After that day I never felt any pain or suffering. I was happy."
        scene black
        with fade
        c "Developed by Chris Ferran"
        c "Story by Chris Ferran"
        c "Characters designed by Chris Ferran"
        c "Characters created in Mannequin, developed by ar14"
        c "Supervised by Michael C. Murphy"
        c "Game Developed in Ren'py"
        c 'Music from https://filmmusic.io
          "Ancient Rite" by Kevin MacLeod (https://incompetech.com)
          License: CC BY (http://creativecommons.org/licenses/by/4.0/)'
        c 'Music from https://filmmusic.io
          "A Very Brady Special" by Kevin MacLeod (https://incompetech.com)
          License: CC BY (http://creativecommons.org/licenses/by/4.0/)'
        c 'Music from https://filmmusic.io
          "Exhilarate" by Kevin MacLeod (https://incompetech.com)
          License: CC BY (http://creativecommons.org/licenses/by/4.0/)'
        c 'Music from https://filmmusic.io
          "Wholesome" by Kevin MacLeod (https://incompetech.com)
          License: CC BY (http://creativecommons.org/licenses/by/4.0/)'
        c 'Music from https://filmmusic.io
          "Easy Lemon" by Kevin MacLeod (https://incompetech.com)
          License: CC BY (http://creativecommons.org/licenses/by/4.0/)'
        c 'Music from https://filmmusic.io
          "Modern Jazz Samba" by Kevin MacLeod (https://incompetech.com)
          License: CC BY (http://creativecommons.org/licenses/by/4.0/)'
        c 'Music from https://filmmusic.io
          "String Impromptu Number 1" by Kevin MacLeod (https://incompetech.com)
          License: CC BY (http://creativecommons.org/licenses/by/4.0/)'
        c 'Music from https://filmmusic.io
          "Redletter" by Kevin MacLeod (https://incompetech.com)
          License: CC BY (http://creativecommons.org/licenses/by/4.0/)'
        c 'Music from https://filmmusic.io
          "Comfortable Mystery 2" by Kevin MacLeod (https://incompetech.com)
          License: CC BY (http://creativecommons.org/licenses/by/4.0/)'
        c 'Music from https://filmmusic.io
          "Unseen Horrors" by Kevin MacLeod (https://incompetech.com)
          License: CC BY (http://creativecommons.org/licenses/by/4.0/)'
        c 'Music from https://filmmusic.io
          "Ishikari Lore" by Kevin MacLeod (https://incompetech.com)
          License: CC BY (http://creativecommons.org/licenses/by/4.0/)'
        c 'Music from https://filmmusic.io
          "Stay The Course" by Kevin MacLeod (https://incompetech.com)
          License: CC BY (http://creativecommons.org/licenses/by/4.0/)'
        c 'Gun sound effect from https://www.freesoundeffects.com/'
        c 'Explosion sound effect from https://freesound.org/people/tommccann/sounds/235968/'
        c 'Alarm sound effect from https://freesound.org/people/ZyryTSounds/sounds/219244/'
        c 'Doorbell sound effect from https://freesound.org/people/kwahmah_02/sounds/275072/'
        c 'Knock sound effect from https://freesound.org/people/Philip_Daniels/sounds/244325/'
        c 'Dropping luggage sound effect from https://freesound.org/people/stephenbist/sounds/434781/'
        c 'Heart monitor sound effect from https://freesound.org/people/samfk360/sounds/148897/'
        c "Special thanks to Michael C. Murphy and the MTSU Honors College"

        return
