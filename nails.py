import utils_nails
import numpy as np
import os

# 주소 바꾸기 ! 
datasetpath='./nail.tar.tar'



# 학습된 모델불러오는건데 조금 오래걸림 
seg = utils_nails.fingernailseg(datasetpath)
seg.create_unet()
seg.model.load_weights('./unet.h5')


from matplotlib.image import imread
from PIL import Image
import matplotlib.pyplot as plt
# get_ipython().run_line_magic('matplotlib', 'inline')

def makeNail(raw, color):

    # base 주소 바꾸기 
    test = []
    raw = Image.open(raw)
    raw = np.array(raw.resize((192, 160)))

    test.append(raw)
    test = np.array(test).astype('float32')
    test /= 255
    ans = seg.model.predict(test, batch_size=8, verbose=0)
    plt.imshow(raw)
    plt.imshow(ans[0,:,:,-1], alpha=0.3, cmap=color)
    plt.axis('off')
    plt.savefig(f'./results/sample_result.jpg', dpi=300)
    return os.listdir('results')
    
    
