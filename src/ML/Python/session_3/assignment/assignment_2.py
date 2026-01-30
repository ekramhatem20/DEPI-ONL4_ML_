import os
def thanos (folder_path):
     if not os.path.exists(dir):
        os.makedirs(dir)
     else:
        print("The path is exist")
     for i in range (10):
        inner_path = os.path.join(dir,"dir",+str(i))
        if not os.path.exists(inner_path):
            os.makedirs(inner_path)
     