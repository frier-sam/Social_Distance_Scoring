## Social DIstance Scoring

This package helps in scoring a picture to quantify the social distancing factor
Score ranges for 0-10 where 
0 - well maintained social distancing(people are far)
10 - social distancing rules are ignored(people are very near to each other)


### Theory

    human faces are 7.4 inch width on average world wide, to maintain social distancing one needs to be 6ft(72inch) apart form each other, considerinf shoulder width and posture approximation following is determined
    
    If 2 faces are found in a picture and seperated by pixel length  more than 9 times the pixel width of their faces, then we can say social distancing rules are followed .
    
    There are cases for ditance being maintaned in therms of depth, from camera which is hard to caluculate so i chose ration of faces as a metric to calculate the score
    
    

#### installation
    
    git clone this 
    
    
    
#### Known issues
    faces shoulc be visible in image for detection