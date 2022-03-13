# Task 2
# Printing number of vowel in a set

# funtion to find the vowels
def Vowels(s):
  count = 0;
  vow = set("aeiouAEIOU")

  for i in s:
        if i in vow:
            count = count + 1
      
  print("Number of vowels: ", count)

string = 'Hammad Rashid'
print("The string is: ", string);

Vowels(string);
