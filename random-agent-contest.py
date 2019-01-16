from retro_contest.local import make


def main():
    env = make(game='SonicTheHedgehog-Genesis', state='LabyrinthZone.Act1')
    _ = env.reset()
    while True:
        _, _, done, _ = env.step(env.action_space.sample())
        env.render()
        if done:
            _ = env.reset()


if __name__ == '__main__':
    main()
