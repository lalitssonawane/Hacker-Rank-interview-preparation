#A string is said to be a child of a another string if it can be formed by deleting 0 or more characters from the other string. Letters cannot be rearranged. Given two strings of equal length, what's the longest string that can be constructed such that it is a child of both?



import os

# Complete the commonChild function below.
def commonChild(s1, s2):
  maxAt = {}

  for i1 in range(len(s1)):
    maxForI1 = 0
    for i2 in range(len(s2)):
      potentialSum = maxForI1 + 1

      # You might be tempted to use the max() function to simplify the next three lines,
      # but that makes the solution so much slower that several of the test cases fail.
      other = maxAt.get(i2, 0)
      if other > maxForI1:
        maxForI1 = other

      if s1[i1] == s2[i2]:
        maxAt[i2] = potentialSum

  return max(maxAt.values(), default=0)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()