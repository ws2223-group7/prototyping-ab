from badagent import Bad_Agent


if __name__ == '__main__':
    agent1 = Bad_Agent("agent1")
    agent2 = Bad_Agent("agent2")

    agenten = [agent1, agent2]

    for agent in agenten:
        agent.SayHello();