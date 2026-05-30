import torch as tc 

matrix1 = tc.tensor([[10,20,30],[40,50,60]])
matrix2 = tc.tensor([[10,20],[40,50],[60,70]])

result = tc.matmul(matrix1,matrix2)
print(result)