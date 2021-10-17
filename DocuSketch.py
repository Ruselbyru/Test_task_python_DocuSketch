import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os



class DrawingPlots:

    # Instance Constructor
    def __init__(self, link):
        self.link=link

    # Charting function
    def draw_plots (self, columns: list[str], start=0, stop=-1) -> list:
        self.columns=columns
        self.start = start
        self.stop = stop

        # read DF from json
        data= pd.read_json(self.link)
        numeric = np.array(data.index[self.start:self.stop])

        # create dir
        if not os.path.isdir('plots'):
            os.mkdir('plots')

        # create plot
        plt.style.use('classic')
        fig, ax = plt.subplots()
        plt.ylabel('value', fontsize= 20)
        plt.xlabel('index', fontsize= 20)


        try:
            for col in self.columns:
                y = data[col][self.start:self.stop]
                ax.plot (numeric, y, label=col)
        except KeyError:
            print (f'Bad name column: {col}')
        else:
            plt.legend()
            # saving file
            file_name = ",".join(self.columns)
            fig.savefig(f'plots/{file_name}.png')

            # read and save path
            list_path=[]
            for root, dirs, files in os.walk('plots'):
                for file in files:
                    list_path.append(os.path.join(root,file))
            return list_path






if __name__ == '__main__':
    link = 'https://ai-process-sandy.s3.eu-west-1.amazonaws.com/purge/deviation.json'
    x= DrawingPlots(link)
    x.draw_plots(columns=['max','min','mean'], start=20, stop=45)
    # x.draw_plots(columns=['gt_corners', 'rb_corners'], start=0, stop=30)






