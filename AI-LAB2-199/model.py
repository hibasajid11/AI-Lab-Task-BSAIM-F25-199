class StatefulClassroomAgent:
    def __init__(self):
        self.previous_mode = None

    def act(self, temp, occupied):
        if not occupied:
            target = "ECO"
        elif temp > 26:
            target = "COOL"
        elif temp < 20:
            target = "WARM"
        else:
            target = "IDLE"
            
        if target == self.previous_mode:
            command_sent = False
        else:
            command_sent = True
            self.previous_mode = target
            
        return target, command_sent

agent = StatefulClassroomAgent()
percepts = [(29, True), (29, True), (20, True), (26, True), (19, True), (29, False)]
for step, percept in enumerate(percepts, 1):
    mode, sent = agent.act(*percept)
    print(f"Step {step} | Percept: {percept} | Target: {mode} | Command Sent: {sent}")