#!/usr/bin/python

class EditDistance():
  
  def __init__(self):
    print("\nStarting...")
	
  def calculateLevenshteinDistance(self, str1, str2):
    #create table
    dis_table = [0] * (len(str1) + 1)
    for i in range(len(str1) + 1):
      dis_table[i] = [0] * (len(str2) + 1)
    for i in range(len(str1) + 1):
      dis_table[i][0] = i
    for j in range(len(str2) + 1):
      dis_table[0][j] = j
    #calculate each distance value for each cell
    for i in range(0, len(str1) + 1):
      for j in range(0, len(str2) + 1):
        #0th row
        if i == 0:
          dis_table[i][j] = j
        #0th col
        elif j == 0:
          dis_table[i][j] = i
        else:
          #characters are same
          if str1[i-1] == str2[j-1]:
            value = min(dis_table[i-1][j] + 1, dis_table[i][j-1] + 1, dis_table[i-1][j-1])
            dis_table[i][j] = value
          else:
            value = min(dis_table[i-1][j] + 1, dis_table[i][j-1] + 1, dis_table[i-1][j-1] + 1)
            dis_table[i][j] = value

    return dis_table[len(str1)][len(str2)]
    
  def calculateOSADistance(self, str1, str2):
    #create table
    dis_table = [0] * (len(str1) + 1)
    for i in range(len(str1) + 1):
      dis_table[i] = [0] * (len(str2) + 1)
    for i in range(len(str1) + 1):
      dis_table[i][0] = i
    for j in range(len(str2) + 1):
      dis_table[0][j] = j
    #calculate each distance value for each cell
    for i in range(0, len(str1) + 1):
      for j in range(0, len(str2) + 1):
        #0th row
        if i == 0:
          dis_table[i][j] = j
        #0th col
        elif j == 0:
          dis_table[i][j] = i
        else:
          #characters are same
          if str1[i-1] == str2[j-1]:
            value = min(dis_table[i-1][j] + 1, dis_table[i][j-1] + 1, dis_table[i-1][j-1])
            dis_table[i][j] = value
          elif str1[i-1] == str2[j-2] and str1[i-2] == str2[j-1]:
            value = min(dis_table[i-1][j] + 1, dis_table[i][j-1] + 1, dis_table[i-1][j-1] + 1, dis_table[i-2][j-2] + 1)
            dis_table[i][j] = value
          else:
            value = min(dis_table[i-1][j] + 1, dis_table[i][j-1] + 1, dis_table[i-1][j-1] + 1)
            dis_table[i][j] = value

    return dis_table[len(str1)][len(str2)]
  
  def calculateDLDistance(self, str1, str2):
    #create table
    dis_table = [0] * (len(str1) + 1)
    for i in range(len(str1) + 1):
      dis_table[i] = [0] * (len(str2) + 1)
    for i in range(len(str1) + 1):
      dis_table[i][0] = i
    for j in range(len(str2) + 1):
      dis_table[0][j] = j
    #combines "abc" and "man" to "abcman" and returns list of each char
    combined_str_list = list(str1+str2)
    #returns list of unique chars so [a, b, c, m, a, n] -> [a, b, c, m, n]
    unique_str_list = list(dict.fromkeys(combined_str_list))
    #take in unique_str_list and make our alphabet_map
    alphabet_map = {k: v for v, k in enumerate(unique_str_list)}
    #initiate distance1
    distance1 = [0] * len(alphabet_map)

    for i in range(len(str1) + 1):
      dis_table[i][0] = i
    for j in range(len(str2) + 1):
      dis_table[0][j] = j

    #calculate each distance value for each cell
    for i in range(1, len(str1) + 1):
      distance2 = 0
      for j in range(1, len(str2) + 1):
          k = distance1[alphabet_map[str2[j-1]]]
          l = distance2

          #if substitution is possible
          if str1[i-1] == str2[j-1]:
            distance2 = j
            value = min(dis_table[i-1][j] + 1, 
              dis_table[i][j-1] + 1, 
              dis_table[i-1][j-1], 
              dis_table[k-1][l-1] + (i-k-1) + (j - l - 1) + 1)
            dis_table[i][j] = value
          else:
            value = min(dis_table[i-1][j] + 1, 
              dis_table[i][j-1] + 1, 
              dis_table[i-1][j-1] + 1, 
              dis_table[k-1][l-1] + (i-k-1) + (j - l - 1) + 1)
            dis_table[i][j] = value

      distance1[alphabet_map[str1[i-1]]] = i

    return dis_table[len(str1)][len(str2)]

if __name__ == '__main__':
  ed = EditDistance()
  #task 1
  print("\nTask 1 tests:")
  print(ed.calculateLevenshteinDistance("colleg", "college")) #1
  print(ed.calculateLevenshteinDistance("colleg", "collegee")) #2
  print(ed.calculateLevenshteinDistance("college", "dollege")) #1
  print(ed.calculateLevenshteinDistance("dllge", "colleg")) #4
  #task 2
  print("\nTask 2 tests:")
  print(ed.calculateOSADistance("CA", "ABC")) #3
  print(ed.calculateOSADistance("CA", "AC")) #1
  print(ed.calculateOSADistance("CAXY", "ACYX")) #2
  print(ed.calculateOSADistance("ACD", "BDC")) #2
  print(ed.calculateOSADistance("ADCZ", "ACEDZ")) #3, should be 2 for DL
  #task 3
  print("\nTask 3 tests:")
  print(ed.calculateDLDistance("CA", "ABC"))
  print(ed.calculateDLDistance("ADCZ", "ACEDZ"))
  print(ed.calculateDLDistance("saturday", "sunday"))
  print(ed.calculateDLDistance("kitten", "sitting"))
  print(ed.calculateDLDistance("ICNORRREBT", "INCORRECT"))
