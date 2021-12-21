#02. Matplotlib 숫자 입력하기
# import matplotlib.pyplot as plt

# plt.plot([2, 3, 5, 10])
# #plt.plot([1, 2, 3, 4], [2, 3, 5, 10]) 동일한 결과

# plt.show()

import matplotlib.pyplot as plt

data_dict = {'data_x': [1, 2, 3, 4, 5], 'data_y': [2, 3, 5, 10, 8]}

plt.plot('data_x', 'data_y', data=data_dict)
plt.show()