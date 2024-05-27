
import math
multiples: list = []
for threeD in range(1,3):
 multiples.append([])
 for twoD in range(1,3):
  multiples[threeD-1].append([])
  for oneD in range(1,3):
   multiples[threeD-1][twoD-1].append(oneD)
print(multiples)


# my_first_list = ['a', 'b', 'c']
# my_second_list = ['d', 'e', 'f', 'g']
# my_third_list = my_second_list[0:1] + my_first_list[1:2]
# my_third_list.append('h')
# print (my_third_list[1:])



# my_list = [[9, 8], [7, 6], [5, 4], [3, 2]]
# my_list.sort()
# print(my_list)
