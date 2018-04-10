import sqlite3

db_dir = "/var/data/AFLW/aflw/data/aflw.sqlite"
save_dir = "/var/data/AFLW/aflw/data/face_rect.txt"

con = sqlite3.connect(db_dir)
cursor = con.cursor()

cursor.execute("select FaceImages.filepath, FaceRect.x, FaceRect.y, FaceRect.w, FaceRect.h from FaceImages join Faces on FaceImages.file_id = Faces.file_id join FaceRect on FaceRect.face_id = Faces.face_id")

result = cursor.fetchall()
# (filename, x, y, w, h)
#print(result)

with open(save_dir, "w") as out:
    for elem in result:
        out.write(elem[0]+', ')
        out.write('{}, {}, {}, {}\n'.format(elem[1], elem[2], elem[3], elem[4]))
    
# below is Python 2 version
#fp = open(save_dir,"w")
#for elem in result:
#    print>>fp, elem


