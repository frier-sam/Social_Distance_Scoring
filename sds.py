import face_recognition
import pandas as pd


# iw = len(image)
# ih = len(image[0])


####define vertical scoring rules (if there is a distance depth wise , this is the approximation)
def vertical_score(a1,a2):
#     print('ver')
    #caluculate ration
    if a1>=a2:
        r = (a2/a1)*100
    else:
        r = (a1/a2)*100
    if r>=85:
        score= 10
    elif r>75 and r<=85:
        score = 9
    elif r>65 and r<=75:
        score = 8
    elif r>55 and r<=65:
        score = 7
    elif r>45 and r<=55:
        score = 6
    elif r>35 and r<=45:
        score = 5
    elif r>25 and r<=35:
        score = 4
    elif r>15 and r<=25:
        score = 3
    elif r>5 and r<=15:
        score = 2
    else:
        score = 0
    return score

####define horizontal scoring rules
####distance between them should be around 9 times more than their face width based in global averages to have around 6ft distance in real life
def horizontal_score(l1,l2,right,left):
#     print('hori')
    w = (l1+l2)/2 #average pixel face width
    dis = abs(left - right) #distance between left of next face to right of current face in pixels
    r = dis/w #ration
#     print(w,dis)
    if r<2:
        score =10
    elif r<3 and r>2:
        score = 9
    elif r<4 and r>3:
        score = 8
    elif r<5 and r>4:
        score = 7
    elif r<6 and r>5:
        score = 6
    elif r<7 and r>6:
        score = 5
    elif r<8 and r>7:
        score = 4
    elif r<9 and r>8:
        score = 3
    elif r<10 and r>9:
        score = 2
    elif r<11 and r>10:
        score = 1
    else:
        score = 9    
    return score

def score(img):
    image = face_recognition.load_image_file(img)

    face_locations = face_recognition.face_locations(image)
    score = []
    ######limit for people in picture that will auto result a score 10
    if len(face_locations)>50:
        score = 10
    else:
    #     totalfacewidth = 0
    #     for face in face_locations:
    #         totalfacewidth = (face[1]-face[2]) + totalfacewidth
    #     avgwi = totalfacewidth/len(face_locations)
        faces = pd.DataFrame(face_locations,columns=['top', 'right', 'bottom', 'left']).sort_values(by=['left'])
        faces = faces.reset_index(drop=True)
        for face in faces[:-1].index:
    #         print(face)
            ####caluculate pixel length and are of individual face and next face
            ifw = abs(faces.iloc[face].right - faces.iloc[face].left)
            nfw = abs(faces.iloc[face+1].right - faces.iloc[face+1].left)
            ifa = ifw *(faces.iloc[face].bottom - faces.iloc[face].top)
            nfa = nfw*(faces.iloc[face+1].bottom - faces.iloc[face+1].top)

    #         print('face1')
            #####check for overlapping horizontally
            if faces.iloc[face+1].left < faces.iloc[face].right:
                ####if horizaontal horizontal overlapping is present then add  the vertical scoring
                score.append(vertical_score(ifa,nfa))   

            else:
                if ifa>=nfa:
                    r = (nfa/ifa)*100
                else:
                    r = (ifa/nfa)*100
                ###check if the depth distance is significant
                if r>60:
                    ###if defpth distance is not that high, then add the horizontal score
                    score.append(horizontal_score(ifw,nfw,faces.iloc[face].right,faces.iloc[face+1].left))
                else:
                    ####else add vertical score
                    score.append(vertical_score(ifa,nfa))
                    
    #### checking if there are more than 3 score greater than 8 if so it will automatically provide a score of 10
    scount = len([i for i in score if i > 8])
    ####average the score
    asc = 0
    if scount>=3:
        asc=10
    else:
        for i in score:
            asc = i + asc
        asc = asc/len(score)
    
    return asc

            
    
# print(score)