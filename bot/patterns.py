patterns = [
{
  "pattern": r"\b(?P<greeting>Hi|Hello|Hey|hello|hi)\b",
  "intent": 'Hello'
}, 
{
  "pattern": r'\b(bye|exit|quit|leave|stop)\b',
  "intent": 'Exit'
},
{
  "pattern" :r"(tell me about|who made|when was|released)",
  "intent":"Videogame"
},
  {
  "pattern" :r"(recommend me)",
  "intent":"Recommendation"
},
{
  "pattern": r'\b(help)\b',
  "intent": "Help"
}];