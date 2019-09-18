import os
from sure import expect
from pytlas.testing import create_skill_agent

# Testing a pytlas skill is easy.
# Start by instantiating an agent trained only for this skill.

agent = create_skill_agent(os.path.dirname(__file__), lang='en')

class TestTemplateSkill:

  def setup(self):
    #TODO
    pass
    
