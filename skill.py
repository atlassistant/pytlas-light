from pytlas import training, translations, intent, meta


@training('en')
def en_training(): return """
%[turn_the_light_on]
  ligth the @[room] light
  turn on the @[room] light
  illuminate the @[room]

%[turn_the_light_off]
  shut the @[room] light off
  turn off the @[room] light

@[room]
  kitchen
  living
  living room
  bathroom
  bedroom
  mike's bedroom
  bathroom on the first floor
  room 6
  cellar  
  attic
  corridor 3  
"""


@training('fr')
def fr_training(): return """
%[turn_the_light_on]
  allume la lumière ~[article] @[room]
  illumine ~[article] @[room]

%[turn_the_light_off]
  éteint la lumière ~[article] @[room]
  obscurcie ~[article] @[room]

~[article]
  de la
  du
  la
  le
  l'

@[room]
  cuisine
  salle de bain du premier
  couloir du bas
  chambre de julien
  cave
  pièce 4
  grenier
"""

# Let's define some metadata for this skill. This step is optional but enables
# pytlas to list loaded skills with more informations:

@meta()
def template_skill_meta(_): return {
  'name': _('Light skill'),
  'description': _('Let there be the light'),
  'author': 'atlassistant',
  'version': '1.0.0',
  'homepage': 'https://github.com/atlassistant/pytlas-light',
}

# Now, adds some translations for supported languages:

@translations('fr')
def fr_translations(): return {
  'Light skill': 'Compétence Lumière',
  'Let there be the light': 'Que la lumière soit',
  'That the light no longer': 'Que la lumière ne soit plus',
  'Fiat lux' : 'Fiat lux'
}  

class ActionHandler:
  def handle_turn_the_light_on(self, room):
    pass
  def handle_turn_the_light_off(self, room):
    pass

handler = None

@intent('turn_the_light_on')
def on_turn_the_light_on(req):
  global handler
  # Using the pytlas API to communicate with the user: https://pytlas.readthedocs.io/en/latest/writing_skills/handler.html
  room = req.intent.slot('room').first().value
  if not room:
    return req.agent.ask('room',req._('Where do you want the light to be lit?'))
  if handler != None:
    handler.handle_turn_the_light_on(room)
  req.agent.answer(req._('Let there be the light'), action='on', room = room)
  return req.agent.done()

@intent('turn_the_light_off')
def on_turn_the_light_off(req):
  global handler
  # Using the pytlas API to communicate with the user: https://pytlas.readthedocs.io/en/latest/writing_skills/handler.html
  room = req.intent.slot('room').first().value
  if not room:
    return req.agent.ask('room',req._('Where do you want to turn off the light?'))
  if handler != None:
    handler.handle_turn_the_light_off(room)
  req.agent.answer(req._('That the light no longer'), action='off', room = room)
  return req.agent.done()