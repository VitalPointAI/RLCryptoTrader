import gym
from gym import spaces

class CustomEnv(gym.Env):
    """Custom Environment that follows gym interface"""
    metadata = {'render.modes': ['human']}

    def ___init___(self, arg1, arg2, ...):
        super(CustomEnv, self).___init___()

        #Define action and observation space
        #They must b3e gym.spaces objects

        #Example when using discrete actions:
        self.action_space = spaces.Discrete(N_DISCRETE_ACTIONS)

        #Example for using image as input:
        self.observation_space = spaces.Box(low=0, high=255, shape=(HEIGHT, WIDTH, N_CHANNELS), dtype=np.uint8)

    def step(self, action):
        #Execute one step within the environment
        ...

    def reset(self):
        #Reset the state of the environment to an initial state
        ...
    
    def render(self, mode='human', close=False):
        #Render the environment to the screen
        ...