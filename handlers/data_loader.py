import numpy as np
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
        dist = self.distancia_recorrida_por_jugador(data)
        team1name, team2name = dist.keys()
        team1, team2 = dist.values()
        dist_team_1 = pd.DataFrame(list(team1.items()), columns=['Jugador', 'Distancia1'])
        dist_team_2 = pd.DataFrame(list(team2.items()), columns=['Jugador', 'Distancia2'])
        dist_team_2['Distancia2'] = dist_team_2['Distancia2']*-1
        dist_team_1['playerNum'] = list(range(11))
        dist_team_2['playerNum'] = list(range(11))
        df = pd.merge(dist_team_1, dist_team_2, on='playerNum', how='inner')
        plt.figure(figsize=(10, 6))
        # Barplot horizontal comparando Distancia1 y Distancia2 para cada playerNum
        bars1 = plt.barh(df['playerNum'], df['Distancia1'], color='blue', label='Distancia1')
        bars2 = plt.barh(df['playerNum'], df['Distancia2'], color='orange', label='Distancia2')

        for bar1, bar2, player_num, id1, id2 in zip(bars1, bars2, df['playerNum'], df['Jugador_x'], df['Jugador_y']):
            plt.text(bar1.get_width(), bar1.get_y() + bar1.get_height()/2, f'{int(id1)}', ha='left', va='center', color='black')
            plt.text(bar2.get_width(), bar2.get_y() + bar2.get_height()/2, f'{int(id2)}', ha='left', va='center', color='black')
        plt.title('Comparación de distancia recorrida')

        legend_text = [
            f'Blue: {team1name}',
            f'Orange: {team2name}',
        ]

        plt.text(1.05, 0.5, '\n'.join(legend_text), transform=plt.gca().transAxes, fontsize=10, va='center')
        plt.savefig('textures/stat2.jpg', bbox_inches='tight', pad_inches=0)

        

    def calcular_distancia(self, x1, y1, x2, y2):
        return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    def distancia_recorrida_por_jugador(self, dataframe):
        teams = dataframe[dataframe['team'] != 'football']['team'].unique()
        distancias_Team = {}
        for t in teams:
            jugadores = dataframe[dataframe['team'] == t]['nflId'].unique()
            distancias_por_jugador = {}

            for jugador in jugadores:
                jugador_data = dataframe[dataframe['nflId'] == jugador]
                distancia_total = 0.0

                for i in range(1, len(jugador_data)):
                    x1, y1 = jugador_data.iloc[i - 1]['x'], jugador_data.iloc[i - 1]['y']
                    x2, y2 = jugador_data.iloc[i]['x'], jugador_data.iloc[i]['y']
                    distancia_total += self.calcular_distancia(x1, y1, x2, y2)

                distancias_por_jugador[jugador] = distancia_total

            distancias_Team[t] = distancias_por_jugador
        return distancias_Team
    
    
        