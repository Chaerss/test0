import numpy as np
from PIL import Image
import cv2
def wiener_filtering(input_signal, h, K):
    '''
    维纳滤波
    :param input_signal: 输入信号
    :param h: 退化函数（时域）
    :param K: 参数K
    :return: 维纳滤波后的信号（幅值）
    '''
    output_signal = []  # 输出信号

    output_signal_fft = [] # 输出信号的傅里叶变换

    input_signal_cp = np.copy(input_signal) # 输入信号的副本

    input_signal_cp_fft = np.fft.fft2(input_signal_cp)  # 输入信号的傅里叶变换

    h_fft = np.fft.fft2(h) # 退化函数的傅里叶变换

    h_abs_square = np.abs(h_fft)**2 # 退化函数模值的平方

    # 维纳滤波
    output_signal_fft = np.conj(h_fft) / (h_abs_square + K)

    output_signal = np.abs(np.fft.ifft2(output_signal_fft * input_signal_cp_fft)) # 输出信号傅里叶反变换

    return output_signal

img = Image.open('D:\关军楠文档\Python\python\wera.png')
image = np.array(img)
image = cv2.resize(image,(250,250))
fx = Image.open('D:\关军楠文档\Python\python\weina.png')
fxx = np.array(fx)
fxx = cv2.resize(fxx,(250,250))

im = wiener_filtering(image,fxx,100)
cv2.imshow("2",image)
cv2.imshow("3",fxx)
cv2.imshow("1",im)
key = cv2.waitKey(0)