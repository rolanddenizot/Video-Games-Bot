# Video Game Bot - DIA2

## Members
- Roland DENIZOT
- Antoine COHEN

## Description
We offer you a chatbot that gives some informations about video games and that can recommend video games in function of your own tastes.

Please write "Help" in the discord channel to have some hints about how to use the bot

You can also say hi to him or say bye

Please don't ask the bot to save to the favorites a video game released after April 2019. But you can still ask for some informations about a video game of any year. The dataset we are using for recommendation system knows only video games before April 2019.

## Bot Info  (faire video)
- Chatbot platform: Discord
- Link to the discord server: https://discord.gg/2p2kTNEExp
- To chat with the bot, just *run the Repl program* and *write "Help"* in the channel "Welcome" in the discord server to have some hints about how to use the bot
- [Chat with bot](https://discord.gg/2p2kTNEExp) (redirect to the discord server)
- [Working video of this bot](https://www.youtube.com/watch?v=YOUTUBE_VIDEO_ID_HERE)

## Recommender System (a faire)
Please describe the recommender system in your chatbot. How it works and the details about it.

## Language Processing (faire video wit.ai)
Please describe the language processing step. Using external services, AI, regular expression, etc. or mix of them.
If you have reg ex, please write them with an example:

The first step is to know if the bot has to respond to a video game info, a recommendation or semething else. For that, we use a regex:

| Regex    | Intent | Example    |
|----------|--------|------------|
| ```\b(?P<greeting>Hi|Hello|Hey|hello|hi)\b``` | Hello | Hi |
| ```\b(bye|exit|quit|leave|stop)\b``` | Exit | bye |
| ```(tell me about|who made|when was|released)``` | Videogame | Tell me about Skyrim<br>Who made Black Ops II?<br>When was Grand Theft Auto V released? |
| ```(recommend me)``` | Recommendation | Recomend me some games |
| ```\b(help)\b``` | Help | Help |


After that, if the intent "Videogame" is triggered, we use Wit.ai to return an intent and entities and to learn

If you use other services like wit.ai, please include a video from the trained texts. [Video](https://www.youtube.com/watch?v=YOUTUBE_VIDEO_ID_HERE)



### Intents and Entities (a faire)
Please describe your chatbot intents and entities.
Each intent should be in the new line:
e.g.:

| Intent         | Entities               |
|----------------|------------------------|
| get movie info | title, year (optional) |
| get weather    | city, date (optional)  |

## Scenarios

### Scenario 1:
| User | Bot                                                     |
|------|---------------------------------------------------------|
| Hi   | Hello to you to @Roland DENIZOT!                        |

### Scenario 2:
| User | Bot                                                     |
|------|---------------------------------------------------------|
| Bye   | Goodbye !                        |

### Scenario 3:
| User | Bot                                                     |
|------|---------------------------------------------------------|
| Help   | To use the bot, ask a question about plot, release date or creators of video games<br>Here are some examples of questions you can ask:<br>- *Tell me about Skyrim*<br>- *Who made Black Ops II?*<br>- *When was Grand Theft Auto V released?*<br>Once you've searched for some games, you can ask the question:<br>-*Recommend me some games*<br>in order to have some personalized recommendations for you                        |

### Scenario 4:
| User     | Bot                                              |
|----------|--------------------------------------------------|
| Tell me about Skyrim    | Game information about **The Elder Scrolls V: Skyrim**:<br>**Game summary:** <br>Skyrim reimagines and revolutionizes the open-world fantasy epic, bringing to life a complete virtual world open for you to explore any way you choose. Play any type of character you can imagine, and do whatever you want; the legendary freedom of choice, storytelling, and adventure of The Elder Scrolls is realized like never before.<br>**Game storyline:** <br>The Empire of Tamriel is on the edge. The High King of Skyrim has been murdered. Alliances form as claims to the throne are made. In the midst of this conflict, a far more dangerous, ancient evil is awakened. Dragons, long lost to the passages of the Elder Scrolls, have returned to Tamriel. The future of Skyrim, even the Empire itself, hangs in the balance as they wait for the prophesized Dragonborn to come; a hero born with the power of The Voice, and the only one who can stand amongst the dragons.<br>=====================================<br>You seem to be interested about the game **The Elder Scrolls V: Skyrim**, would you like to save it to your favorites ?<br>✅ ❌                        |
| clicked on ❌   | Ok, I don't add **The Elder Scrolls V: Skyrim** to your favorites games.                        |

### Scenario 5:
| User | Bot                                                     |
|------|---------------------------------------------------------|
| When was counter strike released?   | The release date of **Counter-Strike** was **2000/11/14**<br>=====================================<br>You seem to be interested about the game **Counter-Strike**, would you like to save it to your favorites ?<br>✅ ❌                        |
| clicked on ✅   | Ok, I add **Counter-Strike** to your favorites games.<br>Which rate would you like to give to **Counter-Strike** ?<br>1️⃣ 2️⃣ 3️⃣ 4️⃣ 5️⃣                       |
| clicked on 3️⃣   | Ok, I add the rate **3.0** to **Counter-Strike**.                      |

### Scenario 6:
| User              | Bot                                                      |
|-------------------|----------------------------------------------------------|
| Who made Black Ops II?   | The involved companies for **Call of Duty: Black Ops II** are: <br>Treyarch, Activision, Square Enix<br>=====================================<br>You seem to be interested about the game ** Call of Duty: Black Ops II**, would you like to save it to your favorites ?<br>✅ ❌ |
|  | You took too much time to respond in message 1, we didn't add **Call of Duty: Black Ops II** to your favorite games.       |

### Scenario 7:
| User | Bot                                                     |
|------|---------------------------------------------------------|
| Recommend me some games    | I'm looking for some recommendations for you, please wait a little bit<br>Mario Kart DS,Wii Fit,Wii Fit Plus|

### Scenario 8:
| User | Bot                                                     |
|------|---------------------------------------------------------|
| hfbtyfuy    | Sorry😢! I didn't understand what ou mean, I know you said: hfbtyfuy|