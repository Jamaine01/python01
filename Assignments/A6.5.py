text = 'X-DSPAM-Confidence:    0.8475'
num = text.find('0')
whole_num = text.find('5' , num)
real_num = float(text[num:whole_num+1])
print real_num


