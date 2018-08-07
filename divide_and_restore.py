import numpy as np
import cv2
import argparse
import itertools
import glob
import os
def two_dimensional(k):
    try:
        x, y = map(int, k.split(','))
        return x, y
    except:
        raise argparse.ArgumentTypeError("Splitting and upscaling in two dimensions only")
def splitter(x,n):
     em=[]
     if x.shape[0]%n[0] !=0:
          x=x[x.shape[0]%n[0]:,:,:]
     elif x.shape[1]%n[1] != 0:
          x=x[:,x.shape[1]%n[1]:,:]
     r=x.shape[0]/n[0]
     c=x.shape[1]/n[1]
     for i in range(n[0]):
          for j in range(n[1]):
               em.append(x[i*r:(i+1)*r,j*c:(j+1)*c])
     return em
def subtract(a, b):
     return "".join(a.rsplit(b))
def main():
     ap = argparse.ArgumentParser()
     ap.add_argument("-p", "--path", help="enter path")
     ap.add_argument("-n", "--splits", help="enter number of splits",type=two_dimensional)
     ap.add_argument("-t", "--image", help="insert type of image eg. .JPG")
     ap.add_argument("-r", "--upscale", help="insert upscale resolution eg 100 100",type=two_dimensional)
     args=vars(ap.parse_args())
     path=str(args["path"])
     if args.get("splits") is None:
          splits=(3,3)
     else:
          splits=tuple(args["splits"])
     if args.get("image") is None:
          img_type=".JPG"
     else:
          img_type=str(args["image"])
          if img_type[0]!='.':
               img_type='.'+img_type
     if args.get("upscale") is None:
          resol=(3280,2464)
     else:
          resol=tuple(args["upscale"])
     for filepath in glob.glob(os.getcwd()+'/'+path+'*'+img_type):
          img=cv2.imread(filepath)
          buff=splitter(img,splits)
          for i in range(len(buff)):
               buff[i]=cv2.resize(buff[i],resol,interpolation=cv2.INTER_CUBIC)
               cv2.imwrite(subtract(filepath,img_type)+"_"+str(i)+img_type,buff[i])  

if __name__=='__main__':
     main()
