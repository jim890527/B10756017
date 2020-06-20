# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""
import numpy as np
import cv2
import matplotlib.pyplot as plt

# 椒鹽雜訊
def addsalt(img, SNR):#funtion
    img_ = img.copy()
    c, h, w = img_.shape
    mask = np.random.choice((0, 1, 2), size=(1, h, w), p=[SNR, (1 - SNR) / 2., (1 - SNR) / 2.])
    mask = np.repeat(mask, c, axis=0)# 按channel 複製到 與img具有相同的shape
    img_[mask == 1] = 255    # 鹽噪
    img_[mask == 2] = 0      # 椒噪
    return img_

#高斯雜訊
def add_gasuss(image, mean=0, sigma=0.001):
    image = np.array(image/255, dtype=float) # 將像素點/255建立陣列
    noise = np.random.normal(mean, sigma ** 0.5, image.shape) # 建立一個與image一樣大的陣列，內容為(mean~sigma^0.5)隨機產生
    out = image + noise # 陣列內容相+
    if out.min() < 0:   # 若out中有小於0的值則執行
        low_clip = -1.
    else:
        low_clip = 0.
    out = np.clip(out, low_clip, 1.0)   # 強制out內容介於low_clip~1.0之間
    out = np.uint8(out*255)
    #cv.imshow("gasuss", out)
    return out

#一維影象的直方圖
def whole_hist(image):
	plt.hist(image.ravel(), 256, [0, 256]) #numpy的ravel函式功能是將多維陣列降為一維陣列
	plt.show()

#RGB影象的直方圖
def channel_hist(image):
	color = ('b', 'g', 'r')   #這裡畫筆顏色的值可以為大寫或小寫或只寫首字母或大小寫混合
	for i , color in enumerate(color):
		hist = cv2.calcHist([image], [i], None, [256], [0, 256])  #計算直方圖
		plt.plot(hist, color)
		plt.xlim([0, 256])
	plt.show()
    
# Main
img1 = cv2.imread(r'cry.jpg') 
img2 = cv2.imread(r'001.jpg') 
img2 = cv2.resize(img2,(1024,768), cv2.INTER_AREA)# 更改尺寸
img512 = cv2.resize(img1,(512,512), cv2.INTER_AREA)# 更改尺寸
img3 = cv2.imread(r'skyblue.jpg') 
img3 = cv2.resize(img3,(1040,780), cv2.INTER_AREA)# 更改尺寸
hsv = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)# hsv圖，比RGB更直觀的表達色彩的陰暗、色調及鮮豔度
yuv = cv2.cvtColor(img2, cv2.COLOR_BGR2YUV)# yuv圖，壓縮每幀圖片的數據量，對影片幫助較大
cv2.namedWindow("LA",cv2.WINDOW_NORMAL)# 標題為LA的視窗可調整 
cv2.imshow("LA",img2)
cv2.waitKey(0)
cv2.imshow("HSV",hsv)
cv2.imshow("YUV",yuv)
cv2.waitKey(0)
cv2.destroyAllWindows()# 關閉所有視窗
size1 = img1.shape# 抓取圖片大小(高、寬、維度)
#print ("\n讚讚\n")
print (size1)
gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)# 轉為灰階圖
ret,thresh1 = cv2.threshold(gray,127,255,0)# 二值化(127 以上改成255  以下改0)
ret,thresh2 = cv2.threshold(gray,127,255,1)
cv2.imshow("TheCry",img1)# 原圖
#cv2.imshow("GrayTheCry",gray)# 灰階圖
#cv2.imshow("Binarization",thresh1)# 二值圖
cv2.waitKey(0)
htitch= np.hstack((gray,thresh1,thresh2))# 合併
cv2.imshow("Hstack",htitch)
cv2.waitKey(0)
cv2.destroyAllWindows()
gray1 = cv2.cvtColor(img512, cv2.COLOR_BGR2GRAY)# 轉為灰階圖
#cv2.imwrite('output.jpg',gray1, [cv2.IMWRITE_JPEG_QUALITY, 90])# 輸出htitch為output.jpg，品質為90(0-100)
cv2.imwrite('skyblue.png', img3, [cv2.IMWRITE_PNG_COMPRESSION, 5])

# 椒鹽雜訊
SNR_list = [0.9, 0.7, 0.5, 0.3]# 四種SNR的雜訊效果
for i in range(len(SNR_list)):
    img_s = addsalt(img1.transpose(2, 1, 0), SNR_list[i])     # c,
    img_s = img_s.transpose(2, 1, 0)
    cv2.imshow("PepperandSalt", img_s)
    cv2.waitKey(0)
    #plt.imshow(img_s[:,:,::-1])     # bgr --> rgb
cv2.destroyAllWindows()

# 中值濾波
img_m = addsalt(img1.transpose(2, 1, 0), SNR_list[0])#0.9
img_m = img_m.transpose(2, 1, 0)#圖像旋轉
#cv2.imshow("SNR=0.9", img_m)
cv2.waitKey(0)
#cv2.destroyAllWindows()
img_m3 = cv2.medianBlur(img_m,3)# 執行中值濾波
img_m5 = cv2.medianBlur(img_m,5)# 執行中值濾波
img_m7 = cv2.medianBlur(img_m,7)# 執行中值濾波
median_s = np.hstack((img_m,img_m3,img_m5,img_m7))# 重複顯示
cv2.namedWindow("medianBlur",cv2.WINDOW_NORMAL)# 標題為medianBlur的視窗可調整 
cv2.imshow("medianBlur",median_s)# 顯示不同遮罩大小的效果
cv2.imwrite('salt.jpg',median_s, [cv2.IMWRITE_JPEG_QUALITY, 90])# 輸出median_s為jpg，品質為90(0-100)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('salt.jpg',img_m,[cv2.IMWRITE_JPEG_QUALITY, 90])

# 高斯雜訊
img_g = add_gasuss(img1,0,0.001)

# 中值濾波
img_g5 = cv2.medianBlur(img_g,5)# 執行中值濾波
median_g = np.hstack((img1,img_g,img_g5))
cv2.imshow("gasuss",median_g)
cv2.imwrite('gasuss.jpg',median_g, [cv2.IMWRITE_JPEG_QUALITY, 90])
cv2.waitKey(0)
cv2.destroyAllWindows()

# 直方圖繪製
whole_hist(img1)
channel_hist(img1)

# 均衡化
(b, g, r) = cv2.split(img1)
bH = cv2.equalizeHist(b)
gH = cv2.equalizeHist(g)
rH = cv2.equalizeHist(r)
frameH = cv2.merge((bH, gH, rH))
cv2.imshow("image",frameH)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Sobel
x = cv2.Sobel(gray,cv2.CV_16S,1,0)# Sobel函数求完导数后会有负值，还有会大于255的值，因此要轉為16位元
y = cv2.Sobel(gray,cv2.CV_16S,0,1)
absX = cv2.convertScaleAbs(x)   # 转回uint8
absY = cv2.convertScaleAbs(y)
dst = cv2.addWeighted(absX,0.5,absY,0.5,0)# 由于Sobel是在两个方向计算的，最后还需将其组合起来
cv2.imshow("Result", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()