# A simple program that encrypts your text using Digrapgh Cipher method #

# You can find the table that I used to encrypt the text using below given link. Save it as 'dgcph.jpg' #
# https://www.google.com/url?sa=i&url=https%3A%2F%2Fcrypto.interactive-maths.com%2Fdigraph-substitution-ciphers.html&psig=AOvVaw27PUfxyisv5U6olwTKQKLU&ust=1604991496396000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCNiitrPx9OwCFQAAAAAdAAAAABAJ#

import cv2

def diciph(word):

 word=word.upper()

 if word.isalpha():
   s=(list(word))
   l=len(s)
   if (l%2)!=0:
       s.append("X")
       l=len(s)
   c=[]
   for i in range(l):

       if(i%2 is 0):
         asc=ord(s[i])+9
         if asc>90:
            asc=64+asc-90
         char=chr(asc)
         c.append(char)


       if(i%2!=0):
         asc=ord(s[i])+17
         if asc>90:
            asc=64+asc-90
         char=chr(asc)
         c.append(char)


   for i in range(len(c)):
    print(c[i],end=' ')

   s=input("\n\nDo you want to verify you answer? [Yes/No]: ")
   if (str(s)=="yes" or str(s)=="Yes" or str(s)=="Y" or str(s)=="y"):
      print("Check out the popped up image on your Taskbar!:)")
      c=cv2.imread('dgcph.jpg')
      cv2.imshow('a',c)
      cv2.waitKey(0)

  

  
 else:
    print("enter valid word with letters only")
 

## DRIVER FUNCTION ##

if __name__ == "__main__":
  a=str(input("Enter the word to be encrypted: "))
  diciph(a)


