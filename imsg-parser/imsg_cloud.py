import numpy as np
from PIL import Image
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
import os
    
if __name__ == "__main__":
    
    d_str = '../texts/'
    save_path = '../wordclouds/'
    
    nltk.download('stopwords')
    stops = set(stopwords.words('english'))
    sw = ['Replying', 'heic', 'Image', 'PNG', 'jpeg', 'from', 'thaiv', 'esther'
          ,'u', 'ur', 'tmp', 'gif', 'Loved']
    
    for word in sw:
        stops.add(word)
    
    directory = os.fsencode(d_str)
    
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        
        if filename.endswith(".txt"): 
            f = open(d_str + filename, 'r')
            
            text = f.read()
            wc = WordCloud(stopwords=list(stops)).generate(text)
            plt.imshow(wc)
            wc.to_file(save_path + filename[:len(filename) - 4] + '.png')
            # plt.show()
            
            f.close()
            