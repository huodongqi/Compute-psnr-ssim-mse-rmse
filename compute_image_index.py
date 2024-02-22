import cv2
import os
import numpy as np
#from skimage.measure import compare_ssim
from skimage.metrics import structural_similarity as compare_ssim

sr_dir = os.listdir('./SR')
hr_dir = os.listdir('./HR')

psnr = 0.0
ssim = 0.0
mse = 0.0
rmse = 0.0
n = 0


def to_grey(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def function_compute_mse(imageA, imageB):
    err = np.sum((imageA.astype('float') - imageB.astype('float')) ** 2)
    err /= float(imageA.shape[0] * imageB.shape[1])
    return err

for hr_image in hr_dir:
    for sr_image in sr_dir:
        if sr_image == hr_image:
            if (sr_image[-3:]) != 'png':
                continue
            compute_psnr = cv2.PSNR(cv2.imread('./SR/' + sr_image), cv2.imread('./HR/' + hr_image))
            compute_ssim = compare_ssim(to_grey(cv2.imread('./SR/' + sr_image)),
                                        to_grey(cv2.imread('./HR/' + hr_image)))
            compute_mse = function_compute_mse(to_grey(cv2.imread('./SR/' + sr_image)), 
                                               to_grey(cv2.imread('./HR/' + hr_image)))
            compute_rmse = np.sqrt(compute_mse)
            
            print(sr_image + ' PSNR = ', compute_psnr)
            print(sr_image + ' SSIM = ', compute_ssim)
            print(sr_image + ' MSE = ', compute_mse)
            print(sr_image + ' RMSE = ',compute_rmse)
            print("++++++++++++++++++++++++++++")

            psnr += compute_psnr
            ssim += compute_ssim
            mse += compute_mse
            rmse += compute_rmse
            n += 1
            print("finish compute [%d/%d]" % (n, len(hr_dir)-1))

psnr = psnr / float(n)
ssim = ssim / float(n)
mse = mse / float(n)
rmse = rmse / float(n)

print('----------------------------')
print("average PSNR = ", psnr)
print("average SSIM = ", ssim)
print("average MSE = ", mse)
print("average RMSE = ", rmse)
print("count = ", n)

