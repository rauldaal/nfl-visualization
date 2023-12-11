import pandas as pd


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

    def load_example(self):
        self.data = pd.read_csv('data/exemple1.csv')
