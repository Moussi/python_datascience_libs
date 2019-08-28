import json
class Agent:
    def say_hello(self, first_name):
        return "Hello "+ first_name

    def __init__(self, **agent_attributes):
        for attr_name, attr_value in agent_attributes.items():
            setattr(self, attr_name, attr_value)


class Position:
    def __init__(self, longitude, latitude):
        self.latitude = latitude
        self.longitude = longitude

agent_attributes = json.load(open("agents-100k.json"))

type(agent_attributes)

for ag in agent_attributes:
    agent = Agent(**ag)
    print(agent.agreeableness)

# first_agent = Agent(agent_attributes)
# second_agent = Agent(agent_attributes)
#
# print(first_agent.say_hello("Moussi"), second_agent.say_hello("Malek"))
# print(first_agent.country_name)
# print(second_agent.agreeableness)