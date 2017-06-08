# You can place the script of your game in this file.

# Characters
define e = Character('Man', color="#c8ffc8")
define s = Character('Spirit', color="#c8ffc8")

# Scenes
image blank = "#ffffff"
image intro1 = im.Scale("intro1.png", 800, 360)
image intro2 = im.Scale("intro2.png", 800, 360)
image wow1 = im.Scale("wow1.jpg", 800, 360)
image wow2 = im.Scale("wow2.jpg", 800, 360)
image wow3 = im.Scale("wow3.jpg", 800, 360)

# The game starts here.
label start:

    play music "orb1.mp3"

    scene intro1
    with dissolve

    scene intro2
    with dissolve

    scene blank
    with dissolve

    e "I'm sorry."
    e "I'm so sorry, I..."
    e "I couldn't grant you your wish."
    e "So... I'm sorry."

    scene wow1
    with dissolve

    "Why is this voice apologizing to me?"
    "I lay there, wondering..."
    "It seems as if I couldn't move."
    "It seems as if I couldn't open my eyes."
    "It seems as if I couldn't even open my mouth to speak."
    "I... can't remember anything..."
    "What even... happened to me?"

    e "There is a painful feeling in my chest."
    e "I've always been watching you."
    e "But I never would of known..."
    e "That it would actually happen."

    "I could feel the shakiness in his voice."
    "About 3 minutes passed before he finally spoke again."
    "But it felt like time was much slower."

    e "I couldn't protect you in the end."

    scene wow2
    with dissolve

    "I wanted to speak."
    "But it felt like my grip on this world is getting weaker and weaker."
    "I guess..."
    "I guess I'm actually dying."

    scene blank
    with dissolve

    "Suddenly, I started hearing a voice."
    "It was not the voice of that man."

    s "Your time is not up yet."
    s "You still have a job to do, right?"
    s "The only job you can do in this world."

    "'Huh?', I replied back."

    s "You...will know eventually."

    "The next moment, memories suddenly started flooding in."

    scene wow3
    with dissolve

    "I trembled and said: "
    "'It's not manly to cry, Tachibana.''"

    scene blank
    "The End"

    return
