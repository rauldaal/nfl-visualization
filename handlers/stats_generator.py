from scipy.spatial import Voronoi, voronoi_plot_2d
import numpy as np
import matplotlib.pyplot as plt

class Voronoi_Generator:
    def __init__(self) -> None:
        self.saved_file_path = "tmp/voronoi.jpg"
        self.last_computed_frame = None

    def compute_voronoi(self, data, frame):
        if self.last_computed_frame != frame:
            data = data.dropna(subset=['nflId'])
            teams = data['team'].unique()
            data['team_color'] = data['team'].apply(lambda x: 'blue' if x == teams[0] else 'red')
            data['y'] = -data['y']
            points = data[['x', 'y']].to_numpy()
            colours = data['team_color'].to_list()
            coords = np.append(points, [[999,999], [-999,999], [999,-999], [-999,-999]], axis = 0)
            vor = Voronoi(coords[:,:2])
            fig = voronoi_plot_2d(vor, show_vertices=False)
            for j in range(len(coords)):
                region = vor.regions[vor.point_region[j]]
                if not -1 in region:
                    polygon = [vor.vertices[i] for i in region]
                    plt.fill(*zip(*polygon), colours[j], alpha=0.4)
            plt.xlim(0, 122)
            plt.ylim(-55, 0)

            plt.axis('off')
            plt.legend().set_visible(False)

            # Guardar la imagen
            plt.savefig(self.saved_file_path, bbox_inches='tight', pad_inches=0)
            self.last_computed_frame = frame

        return self.saved_file_path
    


    
    