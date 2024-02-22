# Compute the psnr,ssim,mse,rmse of images
### Denpendency
* python 3
* opencv 3
* skimage
* numpy

### Getting started
* pip install -U scikit-image
* mkdir "HR" and "SR"
* put ground true and super-resolved images in both dir
* python psnr
### Notice
* The name of images in both type should be same
* we used 'from skimage.metrics import structural_similarity as compare_ssim' in line4 instead 'from skimage.measure import compare_ssim' in line3 in lateset version of skimage
