import random
import copy

def print_matrix(mat):
  for i in range(len(mat)):
    print(mat[i])
  print(" ")

def generate_random_matrix_with_wildcards(rows, cols):
  """Generates a random Boolean matrix with wildcards of size row*col. """
  mat=[]
  for i in range(rows):
    col = []
    for j in range(cols):
      x=random.randint(0,2)
      if x == 2:
        col.append('*')
      else:
        col.append(x)
    mat.append(col)
  return mat

def get_hamming_distance(row_a, row_b):
  """ Returns hamming distance of two rows. """
  count=0
  for i in range(len(row_a)):
    if row_a[i] != row_b[i] :
      count+=1
  return count

def get_diameter_of_matrix(mat):
  """ Returns Diameter of matrix and rows for which it was max. """
  diameter=0
  diameter_and_rows = [] # [diameter i j] 
  for i in range(len(mat)):
    for j in range(len(mat[0])):
      if get_hamming_distance(mat[i],mat[j]) > diameter :
        diameter = get_hamming_distance(mat[i],mat[j])
        row_a = i
        row_b = j
  diameter_and_rows.append(diameter)
  diameter_and_rows.append(row_a)
  diameter_and_rows.append(row_b)
  return diameter_and_rows

def get_diameter_with_wildcards(mat):
  """ Go through all possibilities to return the exact diameter. """
  rows,cols=(len(mat),len(mat[0]))
  for i in range(rows):
    for j in range(cols):
      if mat[i][j]=='*':
        mat[i][j]=0
        diameter_a=get_diameter_with_wildcards(copy.deepcopy(mat))
        mat[i][j]=1
        diameter_b=get_diameter_with_wildcards(copy.deepcopy(mat))
        return min(diameter_a,diameter_b)
  return get_diameter_of_matrix(mat)[0]

def exact_diameter_brute_force(mat):
  print("OPT Diameter is {}".format(get_diameter_with_wildcards(mat)))

#@title Algorithm
def min_diameter_completion(mat):
  """ Iterative Algo for min diameter. """
  row = len(mat)
  col = len(mat[0])
  # Create a copy of the matrix
  copy_mat = copy.deepcopy(mat)
  # 1. Replace wildcards randomly
  for i in range(row):
    for j in range(col):
      if copy_mat[i][j]=="*":
        mat[i][j]=random.randint(0,1)
  # 2. Iterate and Improve Diameter
  for t in range(len(mat)*len(mat)):
    diameter_and_rows = get_diameter_of_matrix(copy_mat)  # Get Diameter of matrix and rows
    row_a = diameter_and_rows[1]
    row_b = diameter_and_rows[2]
    for i in range(col):
      if mat[row_a][i]== '*' and mat[row_b][i] == '*' :
        copy_mat[row_a][i]=copy_mat[row_b][i] 
      elif copy_mat[row_a][i]== '*' and copy_mat[row_b][i] != '*':
        copy_mat[row_a][i]=copy_mat[row_b][i] 
      elif mat[row_a][i] != '*' and mat[row_b][i] == '*':
        copy_mat[row_b][i]=copy_mat[row_a][i] 
  # 3. Report the final diameter of the matrix
  diameter_and_rows = get_diameter_of_matrix(copy_mat)
  print('Approx Diameter of M is {}'.format(diameter_and_rows[0]))

#@title Main

if __name__=='__main__':
  for i in range(20):
    rows,cols=(7,7)
    mat=generate_random_matrix_with_wildcards(rows, cols)
    #print("Randomly generated matrix")
    #print_matrix(mat)
    print(" ")
    print("Iteration {}".format(i+1))
    min_diameter_completion(copy.deepcopy(mat))
    #print("Matrix After approximation.")
    #print_matrix(mat)
    exact_diameter_brute_force(copy.deepcopy(mat))
