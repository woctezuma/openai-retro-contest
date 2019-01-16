import retro


def run(display_on_screen=True, num_steps=400):
    env = retro.make(game='Airstriker-Genesis', state='Level1')
    _ = env.reset()
    for _ in range(num_steps):
        _, _, done, _ = env.step(env.action_space.sample())
        if display_on_screen:
            env.render()
        if done:
            _ = env.reset()

    return True


def main():
    env = retro.make(game='Airstriker-Genesis', state='Level1')
    _ = env.reset()
    while True:
        _, _, done, _ = env.step(env.action_space.sample())
        env.render()
        if done:
            _ = env.reset()


if __name__ == '__main__':
    main()
