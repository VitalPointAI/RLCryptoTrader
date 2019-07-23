import gym
from gym import spaces

class StockTradingEnv(gym.Env):
    """A stock trading environment for OpenAI Gym"""
    metadata = {'render.modes': ['human']}

    def ___init___(self, df):
        super(StockTradingEnv, self).___init___()
        self.df = df
        self.reward_range = (0, MAX_ACCOUNT_BALANCE)

        #Define action and observation space
        #Actions of the format Buy x%, Sell x%, Hold, etc...
        self.action_space = spaces.Box(low=np.array([0,0]), high=np.array([3,1]), dtype=np.float16)

        #Prices contains the OHCL values for the last five prices
        self.observation_space = spaces.Box(low=0, high=1, shape=(6,6), dtype=np.float16)

    def step(self, action):
        #Execute one step within the environment
        ...

    def reset(self):
        #Reset the state of the environment to an initial state
        self.balance = INITIAL_ACCOUNT_BALANCE
        self.net_worth = INITIAL_ACCOUNT_BALANCE
        self.max_net_worth = INITIAL_ACCOUNT_BALANCE
        self.shares_held = 0
        self.cost_basis = 0
        self.total_shares_sold = 0
        self.total_sales_value = 0

        #Set the current step to a random point within the data frame
        self.current_step = random.randint(0, len(self.df.loc[:,'Open'].values)-6)

        return self._next_observation()

    def _next_observation(self):
        #Get the data points for last 5 days and scale to between 0-1
        frame = np.array([self.df.loc[self.current_step: self.current_step+5, 'Open'].values / MAX_SHARE_PRICE,
        self.df.loc[self.current_step: self.current_step+5, 'High'].values / MAX_SHARE_PRICE,
        self.df.loc[self.current_step: self.current_step+5, 'Low'].values / MAX_SHARE_PRICE,
        self.df.loc[self.current_step: self.current_step+5, 'Close'].values / MAX_SHARE_PRICE,
        self.df.loc[self.current_step: self.current_step+5, 'Volume'].values / MAX_NUM_SHARES,])

        #Append additional data and scale each value to between 0-1
        obs = np.append(frame, [[
            self.balance / MAX_ACCOUNT_BALANCE,
            self.max_net_worth / MAX_ACCOUNT_BALANCE,
            self.shares_held / MAX_NUM_SHARES,
            self.cost_basis / MAX_SHARE_PRICE,
            self.total_shares_sold / MAX_NUM_SHARES,
            self.total_sales_value / (MAX_NUM_SHARES * MAX_SHARE_PRICE),
        ]], axis=0)

        return obs
    
    def render(self, mode='human', close=False):
        #Render the environment to the screen
        ...