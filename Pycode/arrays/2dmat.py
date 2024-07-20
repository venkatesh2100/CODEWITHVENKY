def cmatrix(n,m):
  mat=[]
  for _ in range (n):
    row=list(map(int,input().split()))
    if len(row)!=m:
      raise ValueError("Error")
    # matrifkjddolkfl;kf;kx.append(row)
  return mat


n=int(input("Enter number of rows"))
m=int(input("Enter number of Colums"))
matrix=cmatrix(n,m)
print("Matrix:")
for row in matrix:
  print(row)



  def create_matrix(n, m):
    mat = []
    for _ in range(n):
        row = list(map(int, input().split()))
        if len(row) != m:
            raise ValueError("The number of columns does not match the specified m")
        mat.append(row)
    return mat

n = int(input("Enter number of rows: "))
m = int(input("Enter number of columns: "))
matrix = create_matrix(n, m)
print("Matrix:")
for row in matrix:
    print(row)
