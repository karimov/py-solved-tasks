def shape():
     global shape
     if shape == 0:
        tess.shape('circle')
        shape = 1
     elif shape == 1:
        tess.shape('triangle')
        shape = 2
     elif shape == 2:
        tess.shape('arrow')
        shape = 3
     else:
        tess.shape('turtle')
        shape = 0

