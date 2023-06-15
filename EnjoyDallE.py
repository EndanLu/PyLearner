#!/usr/bin/python3

#Note: The openai-python library support for Azure OpenAI is in preview.
import os
import openai
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from skimage import io

def genDallEImage(pmpt):
    openai.api_type = "azure"
    openai.api_base = "https://gpt-cdp-01.openai.azure.com/"
    openai.api_version = "2023-06-01-preview"
    #openai.api_key = os.getenv("OPENAI_API_KEY")
    openai.api_key = "ace2c45f24ae4046a40afa139c6fd1cb"     # Copied from Azure OpenAI Studio

    response = openai.Image.create(
        prompt=pmpt,
        size='512x512',
        n=1
    )

    image_url = response["data"][0]["url"]
    print(image_url)

    #img = mpimg.imread("/Users/DLU/Downloads/MicrosoftTeams-image.png")
    #plt.imshow(img)  ##相当于对图像进行了处理，但不能显示，需要配合plt.show()
    #plt.axis('off')  ##没有这一步最后的图像会有坐标轴
    #plt.show()

    #image = io.imread(image_url)
    #io.imshow(image)
    #io.show()

    image = io.imread(image_url)
    plt.imshow(image)
    plt.axis('off')
    plt.show()