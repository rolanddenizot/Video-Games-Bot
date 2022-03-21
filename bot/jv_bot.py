from .matcher import matchPattern
from .wit_wrapper import wit_nlp
from .api import getGameInfo,getInvolvedCompanies,getReleaseDate,getGameName
import pandas as pd


async def process_text_message(message,client):
  # read more on https://github.com/davidchua/pymessenger
  try:
    regex=matchPattern(message.content)
    print(f'regex: {regex}')
   
    #await message.channel.send(f'You said: {message.content}')
    
    if(regex == None):
      await message.channel.send(f"*Sorry😢! I didn't understand what ou mean, I know you said: {message.content}*")
    elif(regex['intent'] == 'Hello'):
      await message.channel.send(f"Hello to you to {message.author.mention}!")
    elif(regex['intent'] == 'Help'):
      await message.channel.send(f"To use the bot, ask a question about plot, release date or creators of video games\nHere are some examples of questions you can ask:\n- *Tell me about Skyrim*\n- *Who made Black Ops II?*\n- *When was Grand Theft Auto V released?*\nOnce you've searched for some games, you can ask the question:\n-*Recommend me some games*\n in order to have some personalized recommendations for you")
    elif(regex['intent'] == 'Exit'):
      await message.channel.send(f"Goodbye !")
    elif(regex['intent'] == 'Recommendation'):
      await message.channel.send("I'm looking for some recommendations for you, please wait a little bit")
      from .recommender import getRecommendation
      await message.channel.send(getRecommendation(message))
    elif(regex['intent'] == 'Videogame'):
      await process_game_message(message,client)
  except:
      await message.channel.send(f'*Sorry, an error occured, I know you said: {message.content}*')
    
  
async def process_game_message(message,client):
  nlp=wit_nlp(message.content)
  print(f"nlp: {nlp}")
  print(f'entities: {nlp["entities"].keys()}')
  intent_name = nlp["intents"][0]["name"]
  print(f'intent name: {intent_name}')
  confidence = nlp["intents"][0]["confidence"]

  if confidence >= 0.9:
    entities = nlp["entities"].keys()
    entity_name = nlp["entities"]["game_title:game_title"][0]["name"]
    print(f'entity name: {entity_name}')

    if intent_name == 'game_info':
      if True in ['release_date' in e for e in entities]:
        game_name = nlp["entities"]["game_title:game_title"][0]["body"]
        release_date = getReleaseDate(game_name)
        api_game_name = getGameName(game_name)
        
        await message.channel.send(f'The release date of **{api_game_name}** was **{release_date}**')
      else:
        game_name = nlp["entities"]["game_title:game_title"][0]["value"]
        print(f'game name: {game_name}')
        game_info = getGameInfo(game_name)
        print(f'game info: {game_info}')
        api_game_name = getGameName(game_name)
        
        await message.channel.send(f'Game information about **{api_game_name}**:\n{game_info}')
        
    elif intent_name == 'studio_info':
      if entity_name == 'game_title':
        game_name = nlp["entities"]["game_title:game_title"][0]["value"]
        print(f'game name: {game_name}')
        api_game_name = getGameName(game_name)
        companies = getInvolvedCompanies(api_game_name)
        await message.channel.send(companies)

    await save_game_favorite(message,api_game_name,client)

  else:
    await message.channel.send(f"Sorry😢! I'm not enough confident about what you mean, I know you said: {message.content}")
    await message.channel.send(f"We are sorry about that, we will try to fix it as soon as possible")

async def save_game_favorite(message,api_game_name,client):
  try:
    message1 = await message.channel.send(f'=====================================\nYou seem to be interested about the game **{api_game_name}**, would you like to save it to your favorites ?')
    await message1.add_reaction("✅")
    await message1.add_reaction("❌")
  except:
    await message.channel.send(f'*We are sorry, an error occured, please try again later*')

  try:
    def check_y_or_n(reaction, user):
      return user == message.author and (str(reaction.emoji) == '✅' or str(reaction.emoji) == '❌')
      
    reaction, user = await client.wait_for("reaction_add", timeout=20.0, check=check_y_or_n)
    print(reaction)
    if reaction.emoji == "✅":
      await message.channel.send(f"Ok, I add **{api_game_name}** to your favorites games.")
      message2 = await message.channel.send(f'Which rate would you like to give to **{api_game_name}** ?')
      await message2.add_reaction("1️⃣")
      await message2.add_reaction("2️⃣")
      await message2.add_reaction("3️⃣")
      await message2.add_reaction("4️⃣")
      await message2.add_reaction("5️⃣")
      
      try:
        def check_rating(reaction, user):
          return user == message.author and (str(reaction.emoji) == '1️⃣' or str(reaction.emoji) == '2️⃣' or str(reaction.emoji) == '3️⃣' or str(reaction.emoji) == '4️⃣' or str(reaction.emoji) == '5️⃣')
          
        reaction, user = await client.wait_for("reaction_add", timeout=20.0, check=check_rating)
        print(reaction)
        if reaction.emoji == "1️⃣":
          rate = 1.0
          await message.channel.send(f"Ok, I add the rate **{rate}** to **{api_game_name}**.")
        elif reaction.emoji == "2️⃣":
          rate = 2.0
          await message.channel.send(f"Ok, I add the rate **{rate}** to **{api_game_name}**.")
        elif reaction.emoji == "3️⃣":
          rate = 3.0
          await message.channel.send(f"Ok, I add the rate **{rate}** to **{api_game_name}**.")
        elif reaction.emoji == "4️⃣":
          rate = 4.0
          await message.channel.send(f"Ok, I add the rate **{rate}** to **{api_game_name}**.")
        elif reaction.emoji == "5️⃣":
          rate = 5.0
          await message.channel.send(f"Ok, I add the rate **{rate}** to **{api_game_name}**.")
        else:
          rate = 0.0
          await message.channel.send(f"Ok, I add the rate **{rate}** to **{api_game_name}**.")
        jv = pd.read_csv("videogames.csv")
        print('loaded jv !')
        id = jv.loc[jv['Name']==api_game_name].iloc[0]['Rank']
        print(f'Game id in the jv df: {id}')
        print(f'Message author: {message.author}')
        print(f'Rate: {rate}')
        ratings = pd.read_csv("ratings.csv", index_col=0)
        print('loaded ratings !')
        ratings = ratings.append({"userId":message.author,"jvId":id,"rating":rate},ignore_index=True)
        ratings.to_csv('ratings.csv')
        print('wrote ratings !')
      except:
        await message.channel.send(f"*You took too much time to respond in message 2, we didn't add **{api_game_name}** to your favorite games.*")
        
    else:
      await message.channel.send(f"Ok, I don't add **{api_game_name}** to your favorites games.")
  except:
    await message.channel.send(f"*You took too much time to respond in message 1, we didn't add **{api_game_name}** to your favorite games.*")

def process_other_message(bot,sender,message):
  bot.channel.send(sender,f'*Sorry😢! I can understand only the text messages*')

def process_exception(bot,sender,message,exception):
  #process exception, send sorry to user log the exception
  import traceback
  traceback.print_exc()