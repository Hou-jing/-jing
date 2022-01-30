import torchvision.transforms as transforms
import cv2 as cv
img = cv.imread('mlp_img/image_0.png')
print(img.shape)  # numpy数组格式为（H,W,C）
transf = transforms.ToTensor()
img_tensor = transf(img) # tensor数据格式是torch(C,H,W)
print(img_tensor.size())

transf2 = transforms.Compose(
  [
    transforms.ToTensor(),
    transforms.Normalize(mean=(0.5, 0.5, 0.5), std=(0.5, 0.5, 0.5))
  ]
)
img_tensor2 = transf2(img)
print(img_tensor2.shape)
from torchvision.utils import save_image
save_image(img_tensor2, 'ceshi2_分布未处理.jpg')


# import matplotlib.pyplot as plt
# plt.imshow(img_numpy)