#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import cv2


# In[ ]:


import numpy as np
import cv2


cap=cv2.VideoCapture('C:/Users/AK/Downloads/test2.mp4')
feature_params = dict( maxCorners = 100,
                       qualityLevel = 0.3,
                       minDistance = 7,
                       blockSize = 7 )

lk_param=dict(winSize=(10,10),
             maxLevel=2,
             criteria=(cv2.TermCriteria_COUNT|cv2.TermCriteria_EPS,10,0.3))

clr=np.random.randint(0,255,(100,3))

ret,old_frame=cap.read()
old_gray=cv2.cvtColor(old_frame,cv2.COLOR_BGR2GRAY )
p0=cv2.goodFeaturesToTrack(old_gray,mask=None,**feature_params)


mask = np.zeros_like(old_frame)


while(1):
    rat,frame=cap.read()
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY )
    
    p1,st,err=cv2.calcOpticalFlowPyrLK(old_gray,gray_frame,p0,None,**lk_param )
    
    good_new = p1[st==1]
    good_old = p0[st==1]
    
    
    for i,(new,old) in enumerate(zip(good_new,good_old)):
        a,b=new.ravel()
        c,d=old.ravel()
        
        mask = cv2.line(mask, (a,b),(c,d), clr[i].tolist(), 2)
        frame=cv2.circle(frame,(a,b),5,clr[i].tolist(),-1)
        
        
        img=cv2.add(frame,mask)
        img=cv2.resize(img,(700,650))
        cv2.imshow('img',img)
        
        k=cv2.waitKey(0)
        if k==ord('u'):
            break
            
            
        old_gray = frame_gray.copy()
        p0 = good_new.reshape(-1,1,2)
        
cv2.destroyAllWindows()
cap.release()


# In[ ]:




