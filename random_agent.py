import retro


def run(display_on_screen=True, num_steps=400):
    env = retro.make(game='Airstriker-Genesis', state='Level1')
    obs = env.reset()
    for step_no in range(num_steps):
        obs, rew, done, info = env.step(env.action_space.sample())
        if display_on_screen:
            env.render()
        if done:
            obs = env.reset()

    return True


def main():
    env = retro.make(game='Airstriker-Genesis', state='Level1')
    obs = env.reset()
    while True:
        obs, rew, done, info = env.step(env.action_space.sample())
        env.render()
        if done:
            obs = env.reset()


if __name__ == '__main__':
    main()
