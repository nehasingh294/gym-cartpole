from gym.envs.registration import register

register(
    id='cartpole-v2',
    entry_point='gym_foo.envs:CartpoleEnv',
)

