The dataset in stored in such format
/train
        /class_1
        /class_2
        .
        .
/valid
        /class_1
        /class_2
        .
        .
/test
        /class_1
        /class_2
        .
        .

The structure must be maintained, otherwise the dataloader won't work.

The main model file is the VGG16_TRansfer_Learning.ipynb which is a jupyter notebook, 
all the requirements and depedencies are in the file requirements.txt
If a new model needs to be trained, the file can be run from the beginning. 

The model is too large so I cannot also submit to myuni.
The trained model is saved at vgg16-transfer-4.pth (Please do not change this name)

At the end of the notebook, there is a section titled as "Testings to display the resutls".
The following blocks loads the model and shows the results.