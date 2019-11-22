import discord
from discord.ext import commands
from imageai.Prediction import ImagePrediction
import os
from PIL import Image
import requests
from io import BytesIO
import numpy as np
class ImageDingen(commands.Cog):
    model = None

    def __init__(self, client):
        self.client = client
        
        # Load model
        path = os.path.abspath(os.path.join(__file__ ,"../../..")) + "\\resnet50_weights_tf_dim_ordering_tf_kernels.h5"
        print(path)
        prediction = ImagePrediction()
        prediction.setModelTypeAsResNet()
        prediction.setModelPath( path ) 
        prediction.loadModel()

        self.model = prediction

    @commands.command()
    async def whatisthis(self, ctx, arg):
        response = requests.get(arg)
        img = Image.open(BytesIO(response.content))
   
        np_img = np.array(img)
        predictions, percentage_probabilities = self.model.predictImage(np_img, input_type='array', result_count=5)
        message = ""
        for index in range(len(predictions)):
            message += (f"{predictions[index]}  :  {percentage_probabilities[index]} % \n")
        
        await ctx.send(message)


# Called to setup the extension
def setup(client):
    client.add_cog(ImageDingen(client))