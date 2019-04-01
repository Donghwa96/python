# print("hello world")
#
# a= [1, 2, 3, 4, 5]
#
# for i in range(1, 10):
#     print("%" * 10, "{}".format(i), "단")
#     for j in range(1, 10):
#         print(i * j)
#
#
# for i in range(1, 10):
#     for j in range(1,10) :
#         for k in range(1, 10):
#             print(i*j*k)

height= input("피라미드의 높이 : ")
hei = int(height)
for k in range(1, hei+1):
    print("{}".format((hei-k)*" "), "{}".format((2*k-1)*"*"), "{}".format((hei-k)*" "))




