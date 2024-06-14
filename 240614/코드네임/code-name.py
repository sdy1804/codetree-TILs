class Agent:
    def __init__(self, name, score):
        self.name = name
        self.score = score

agents = []
for _ in range(5):
    code_name, scores = input().split()
    scores = int(scores)
    agents.append(Agent(code_name, scores))

minimum = 100
for i in range(len(agents)):
    if agents[i].score < minimum:
        minimum = agents[i].score
        min_agent = agents[i].name

print(min_agent, minimum)