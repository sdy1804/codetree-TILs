class Secret:
    def __init__(self, secret_code, meeting_point, time):
        self.secret_code =secret_code
        self.meeting_point = meeting_point
        self.time = time

secret_code, meeting_point, time = input().split()
Agent = Secret(secret_code, meeting_point, time)

print(f'secret code : {Agent.secret_code}')
print(f'meeting point : {Agent.meeting_point}')
print(f'time : {Agent.time}')