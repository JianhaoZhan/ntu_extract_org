# example: python generate.py /New-8T/mars/ntu60/ /New-8T/mars/NTU_Skeleton/ /New-8T/mars/NTU_RGB/
import sys, os, cv2
org_dir = sys.argv[1]
target_dir = sys.argv[2]
skeleton_list = os.listdir(org_dir)
skeleton_list.sort()
length_skeleton = 1
rgb_dirs = sys.argv[3]

for ii in skeleton_list:
    tmp_dir = os.path.join(target_dir,  'nturgbd_rgb_s'+ii[1:4], ii.split('.')[0])
    rgb_dir = os.path.join(rgb_dirs,  'nturgbd_rgb_s'+ii[1:4], ii.split('.')[0])
    from_dir = org_dir
    if not os.path.exists(tmp_dir):
        os.makedirs(tmp_dir)
    try:
        if len(os.listdir(tmp_dir)) == len(os.listdir('/New-8T/mars/NTU_RGB/nturgbd_rgb_s'+ii[1:4]+'/'+ii.split('.')[0])):
            continue
    except:
        print('no compare!!!')
    
    with open(os.path.join(from_dir,ii), 'r+') as f:
        num_frame = int(f.readline())
        for i in range(num_frame):
            people = int(f.readline())
            image = cv2.imread(os.path.join(rgb_dir, '{:0>5d}.jpg'.format(i+1)))
            #if people == 2:
            #    print(tmp_dir+' people is 2!!!')
            for j in range(people):
                f.readline()
                tmp = f.readline()
                if int(tmp) != 25:
                    print('num of skeleton is not 25 !==>{}'.format(tmp_dir)) 
                lt = [(False, False)]     
                for _ in range(int(tmp)):
                    zjh = f.readline().split(' ')
                    try:# To Avoid NaN
                        x, y = int(float(zjh[5])/1920*455), int(float(zjh[6])/1080*256)
                        lt.append((x, y))
                    except:
                        lt.append((float('inf'), float('inf')))
                vs = [(24, 12), (12, 25), (12, 11), (11, 10), (10, 9), (9, 21), (21, 3), (3, 4), (21, 5), (5, 6), (6, 7), (7, 8), (8, 22), (8, 23), (21, 2), (2, 1), (1, 17), (17, 18), (18, 19), (19, 20), (1, 13), (13, 14), (14, 15), (15, 16)]
                for k in vs:
                    x1, y1, x2, y2 = lt[k[0]][0], lt[k[0]][1], lt[k[1]][0], lt[k[1]][1]
                    if x1 < 1e5 and x2 < 1e5 and y1 < 1e5 and y2 < 1e5:
                        cv2.line(image,(int(x1),int(y1)),(int(x2),int(y2)),(0,0,255),length_skeleton)
                for tt in range(1, 26):
                    if lt[tt][0] < 1e5 and lt[tt][1] < 1e5:
                        cv2.circle(image, (lt[tt][0], lt[tt][1]), 1, (0, 255, 0), thickness=-1)
            cv2.imwrite(os.path.join(tmp_dir, '{:0>5d}.jpg'.format(i+1)), image)
