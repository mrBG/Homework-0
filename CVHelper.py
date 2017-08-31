
import os
import fire

class CVHelper(object):

    """Utilities for image processing and computer vision apps"""

    def __init__(self, verbose=False):
        """Constructor. Set verbose, if verbose = True print image paths"""
        self.verbose = verbose

    def read(self,  folder_path, recursive=False):
        """Reads images filename in a folderf

        :folder_path: Folder path that contains the images
        :recursive: Look inside subfolders
        :returns: List of image paths, e.g.,
        ['/path/to/im1.jpg', '/path/to/im2.png', '/path/to/img3.tiff']
        """
        #
        # Add code Here
        #

        image_list=[]

        image=[".jpg",".png" , ".bmp", ".tiff"]
        if(recursive):
            print("Recursive search: ")
        else:
            print("Non-recursive search")

        for root,dirs,files in os.walk(folder_path):
             if recursive:
                for name in files:
                    (namef,extend)=os.path.splitext(name)
                    if (extend in image):
                        if(extend!=".DS_Store"):
                            image_list.append(root +namef + extend)
             else :
                while len(dirs) > 0:
                    dirs.pop()
                    for name in files:
                        (namef, extend) = os.path.splitext(name)
                        if (extend in image):
                            if (extend != ".DS_Store"):
                                image_list.append(root + namef + extend)
        if self.verbose:
            print(image_list)




if __name__ =='__main__':
    fire.Fire(CVHelper)
""""
path="../../Desktop/imagenes/zero/test_images/test_images"
cvhelper = CVHelper(False)
image_list = cvhelper.read_images_filename(path, False)
"""


        # End code
        #
