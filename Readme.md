## Social Distance Scoring

This package helps in scoring a picture to quantify the social distancing factor
Score ranges for 0-10 where 

0 - well maintained social distancing(people are far)

10 - social distancing rules are ignored(people are very near to each other)


### Theory

human faces are 7.4 inch width on average world wide, to maintain social distancing one needs to be 6ft(72inch) apart form each other, considering shoulder width and posture approximation following is determined
    
If 2 faces are found in a picture and seperated by pixel length  more than 9 times the pixel width of their faces, then we can say social distancing rules are followed .
    
There are cases for distance being maintaned in terms of depth, from camera which is hard to calculate so i chose ration of faces as a metric to calculate the score in that case
    
    
### Usage
  #### installation
    
        git clone https://github.com/frier-sam/Social_Distance_Scoring.git
        cd Social_Distance_Scoring/
        pip install -r requirements.txt
        python app.py
        
 Then go to http://localhost:4444
 
 images are saved in image folder(that will be created automatically)
 if you don't want to save the images that you scored, uncommet the line 30 in app.py    
    
    
#### Known problem that can be improved upon
faces should be visible in image for detection
