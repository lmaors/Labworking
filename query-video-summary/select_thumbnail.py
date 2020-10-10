from os.path import dirname, abspath
import os
import matplotlib .pyplot as plt
import matplotlib.image as mpimg
import qvsumm
from qvsumm.utils_func import preprocess_video

direc = dirname(dirname(abspath(__file__))) + '/experiment/chapter_0'


if not os.path.exists('data/vgg19.pkl'):
    print('Need vgg19 model!')

score_function = qvsumm.get_QAR_function()

### Load the word2vec model ###
w2vmodel = qvsumm.get_word2vec_function()

# Inputs : Text query and YouTube URL of the video
videoURL="https://www.youtube.com/watch?v=-nGbufx6Ecc&ab_channel=NBCNews"
video_name = '-nGbufx6Ecc.mp4'
query="joe biden"
# print('_'.join(query.split(' ')))

# 数据预处理
imagenames= preprocess_video(query,videoURL,video_name)


scores,_=qvsumm.get_rel_Q_scores(score_function, w2vmodel, query, imagenames)

K=5

indices=sorted(range(len(scores)), key=lambda k: scores[k],reverse=True)
# print ([scores[indices[i]]  for i in range(K)])

if not os.path.exists(direc + "/thumbnails/"):
    os.mkdir(direc + "/thumbnails/")

for i in range(K):
    print(scores[indices[i]])
    img = mpimg.imread(direc + "/frames/"+str(indices[i])+".png")
    mpimg.imsave(direc + "/thumbnails/"+ '_'.join(query.split(' '))+ '_' + str('%.6f' % scores[indices[i]])+".png",img)

plt.figure(figsize=(60, 10))
for enum,i in enumerate(indices[0:K]):
    if enum==3:
        plt.title("Query: "+str(query),fontsize=70)
    plt.subplot(1,K, enum+1);plt.imshow(mpimg.imread(direc + "/frames/"+str(i)+".png"));plt.axis('off')
    plt.annotate(str(scores[i]), xy=(1, 0), xycoords='axes fraction', fontsize=60,
                 horizontalalignment='right', verticalalignment='bottom',color='green')
plt.show()

# 负面结果
# plt.figure(figsize=(60, 10))
# for enum,i in enumerate(indices[len(indices)-K:len(indices)]):
#     if enum==3:
#         plt.title("Query: "+str(query),fontsize=70)
#     plt.subplot(1,K, enum+1);plt.imshow(mpimg.imread(direc + "/frames/"+str(i)+".png"));plt.axis('off')
#     plt.annotate(str(scores[i]), xy=(1, 0), xycoords='axes fraction', fontsize=60,
#                  horizontalalignment='right', verticalalignment='bottom',color='green')
# plt.show()