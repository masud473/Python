import multiprocessing
from time import perf_counter as perf
from requests import get
path='F:/Images/'
def downloader(url,index):
    response=get(url)
    print('Download started',index)
    open(path+f'Image-{str(index)}.jpg','wb').write(response.content)
    print('Download complete',index)
url='https://picsum.photos/1920/1080'
list=[]
for i in range(1,101):
    if __name__=='__main__':
        t=multiprocessing.Process(target=downloader, args=[url,i])
        x=t.start()
        list.append(x)
for i in list:
    i.join()