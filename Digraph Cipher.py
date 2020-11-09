# A simple program that encrypts your text using Digrapgh Cipher method #

import cv2


def diciph(word):

 # c=cv2.imread('dgcph.jpg')
 # cv2.imshow('a',c)
 # cv2.waitKey(0)

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
 
 # c=cv2.imread('dgcph.jpg')
 # cv2.imshow('a',c)
 # cv2.waitKey(0)


## DRIVER FUNCTION ##

if __name__ == "__main__":
  a=str(input("Enter the word to be encrypted: "))
  diciph("shail")


