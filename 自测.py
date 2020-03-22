# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 17:04:31 2020

@author: hzc
"""


#ip,l=int(input()),int(input())
ip,l=5050,3
arr=[i for i in range(ip,0,-1)]
arr_max=arr[0]
arr_tmp=[]
k=[j for j in range(l,101)]
def a():
    for l in k:
        for idx in range(0,len(arr)):
            arr_tmp.append(arr[idx])
#            print(arr_tmp)

            if len(arr_tmp)>=l and 0<l<=100:
    #                print('开始计算')
                if sum(arr_tmp)==arr_max:
                    return arr_tmp
                del arr_tmp[0]
res=a()
if res==None:
    print('No')
else:
    print(res)

#for cnt in range(ip,0,-1):
#    print(cnt)
