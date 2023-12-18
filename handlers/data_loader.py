import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class DataLoader():

    def __init__(self, players_df=None, plays_df=None, week_df=None):
        # self.players = pd.read_csv(players_df)
        # self.plays = pd.read_csv(plays_df)
        # self.weeks = pd.read_csv(week_df)
        self.data = None
        self.num_frames = 0

    def get_game(self, game_id):
        self.play = self.weeks[self.weeks['gameId'] == game_id]

    def get_play(self, play_id):
        self.data = self.play[self.play['playId'] == play_id]
        self.num_frames = len(self.data['frameId'].unique().tolist())

    def get_num_frames(self):
        self.num_frames = len(self.data['frameId'].unique().tolist())

    def get_frame_information(self, frames_id):
        return self.data[self.data['frameId'] == frames_id]

    def get_prev_frame_information(self, frames_id):
        return self.data[(self.data['frameId'] <= frames_id) & (self.data['frameId'] > frames_id-10)]

    def load_example(self, id=None):
        self.data = pd.read_csv(f'data/{id}_playid.csv')

    def _generate_stats(self):
        # stat1 - tracking
        plt.figure(figsize=(10, 6))
        data = self.data
        team_a, team_b = data['team'].unique()[:2]
        # Plot TB team in blue
        sns.scatterplot(x='x', y='y', data=data[data['team'] == team_b], color='blue', label='TB')
        # Plot DAL team in red
        sns.scatterplot(x='x', y='y', data=data[data['team'] == team_a], color='red', label='DAL')
        plt.title('Player Positions - TB (Blue) and DAL (Red)')
        plt.legend()
        plt.savefig('textures/stat1.jpg', bbox_inches='tight', pad_inches=0)
        # stat2 - barras
        