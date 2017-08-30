import os

class CVHelper(object):

    """Utilities for image processing and computer vision apps"""

    def __init__(self, verbose=False):
        """Constructor. Set verbose, if verbose = True print image paths"""
        self.verbose = verbose

    def read_images_filename(self,  folder_path, recursive=False):
        """Reads images filename in a folder

        :folder_path: Folder path that contains the images 
        :recursive: Look inside subfolders
        :returns: List of image paths, e.g.,
        ['/path/to/im1.jpg', '/path/to/im2.png', '/path/to/img3.tiff']
        """
        #
        # Add code Here
        #
        #List in charge of storing the images
        image_list=[]
        extensiones=[".jpg",".png",".tiff",".bpm"]
        #Prints the different outputs that can occur
        if(recursive):
            print("Recursive search: ")
            if(self.verbose):
                print("Start of printing...")
            else:
                print("Verbose False")
        else:
            print("Non-recursive search")
            if(self.verbose):
                print("Start of printing..")
            else:
                print("Verbose False")
        #Loop running all directories delivered with folder_path
        for root,dirs,files in os.walk(folder_path):
            #Conditionals which will filter the recursive income or not
             if recursive:
                # Loop which will store the name of the files
                for name in files:
                    # Divides the route and shows the name and extension considering the extension
                    (namef,extend)=os.path.splitext(name)
                    # Condition that allows only to consider images with specific extensions
                    if (extend == ".jpg" or extend == ".png" or extend == ".bmp" or extend == ".tiff"):
                        if(extend!=".DS_Store"):
                            # Add the image to the list, with all its features
                            image_list.append(root +namef + extend)
                            # Condition for printing address, file and extension
                            if self.verbose:
                                print (root+ namef + extend)

             else :
                # Loop which will take all directions as long as they exist
                while len(dirs) > 0:
                    # Delete the last address
                    dirs.pop()
                    # Loop which will store the name of the files
                    for name in files:
                        # Divides the route and shows the name and extension considering the extension point
                        (namef, extend) = os.path.splitext(name)
                        # Condition that allows only to consider images with specific extensions
                        if (extend == ".jpg" or extend == ".png" or extend == ".bmp" or extend == ".tiff"):
                            if (extend != ".DS_Store"):
                                # Add the image to the list, with all its features
                                image_list.append(root + namef + extend)
                                # Condition for printing address, file and extension
                                if self.verbose:
                                    print(root + namef + extend)

        return image_list

#Address that will be entered to a parameter (folder_path)
path="../../Desktop/imagenes/zero/test_images/test_images"
#Assignment of variable to constructor class, which will return a Boolean
cvhelper = CVHelper(True)
image_list = cvhelper.read_images_filename(path, True)



        # End code
        #
