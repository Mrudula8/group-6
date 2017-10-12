import random
import re
def filename(fp,fp1,e,a,fp3):
        #print("yuio")
        c=0
        l=[]
        fp3=open(username,"w")
        fp3.write("Level-{}\n".format(a))
        while(c<5):
                if(a<=2):
                        line_number =random.randrange(1,20)
                elif(a>2):
                        line_number=random.randint(1,10)
                if(line_number not in l):
                        l.append(line_number)
                        fp3.write("Question no:{}\n".format(line_number))
                        with open(fp) as f:
                            i = 1
                            for line in f:
                                if i == line_number:
                                    break
                                i += 1
                        print(line,end="")
                        fp3.write("{}\n".format(line))
                        y=input()
                        x=y.lower()
                        count=0
                        with open(fp1) as f1:
                            i = 1
                            for line1 in f1:
                                if i == line_number:
                                    break
                                i += 1
                        line2=line1[:len(line1)-1]
                        if(x==line2):
                                fp3.write("answered correctly\n")
                                if(c<4):
                                        print("Congratulations! Go for next one")
                                c+=1
                        else:
                                while(x!=line2 and count<2):
                                        count=count+1
                                        print("Try Again!!")
                                        y=input()
                                        x=y.lower()
                                        if(x==line2):
                                           fp3.write("answered correctly\n")
                                           if(c<4):
                                                  print("Congratulations! Go for next one")
                                           c+=1
                                           continue
                        if(x!=line2 and count==2):
                                fp3.write("answered incorrectly\n")
                                break
                else:
                        
                        continue
        
        if(c==0):
                e+=0
                if(e==0):
                        print("Better Luck Next Time!!")
                else:
                        print("U Got {} coins!!".format(e))
        elif(c==1):
                e+=10
                print("U Got {}k  Coins!!".format(e))
        elif(c==2):
                e+=20
                print("U Got {}k Coins!!".format(e))
        elif(c==3):
                e+=30
                print("U Got {}k Coins!!".format(e))
        elif(c==4):
                e+=40
                print("U Got {}k Coins!!".format(e))
        elif(c>=5):
                e+=50
                if(a<=2):
                        print("Completed Level-{0}.You can enter into Level-{1}!!".format(a,a+1),end="")
                else:
                        print("U Got 150k Coins!!")
                        print("************************ U Won!! **********************")
        return e
username=input("Please Enter Your Name:\n")
s=0
i=0
count=0
fp2=open("usernames","a+")
fp2.write("{}\n".format(username))
fp2=open("usernames","r")
prev_line=None
for line in fp2.readlines():
    count+=1    
if(count==1):
 s+=1
 fp3=open(username,"w")
 print("Sign Up!")
 name=input("Enter Your Full name:")
 password=input("Enter atleast 6-characters Password:")
 while(len(password)<6):
  password=input("Please enter a valid password:")
 fp3.write("Password:{}\n".format(password))
 fp3.write("Name:{}\n".format(name))
 email=input("Enter Your Email-Id:")
 match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
 while(match == None):
  email=input("Please Enter a valid Email-Id:")
  match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
 fp3.write("Email:{}\n".format(email))
 mobile=input("Enter Your mobile number:")
 while(len(mobile)!=10):
  mobile=input("Please enter a valid 10-digit mobile number:")
 fp3.write("Mobile no:{}\n".format(mobile))
else:
 fp2=open("usernames","r")
 for line1 in fp2.readlines():
   if(prev_line is not None):
    x=prev_line[:len(prev_line)-1]
    if(username==x):
     fp3=open(username,"r")
     j=input("Please Enter the Password:")
     a=fp3.readline()
     for i in range(0,len(a)):
      if(a[i]==':'):
       index=i
       break
     w=a[index+1:len(a)-1]
     if(j==w):
      fp3=open(username,"a+")
      i+=1
      s+=1
      break
     else:
      #print("qwert")
      while(j!=w):
       j=input("Please the correct Password:")
      #print("@@s")
      print(s)
      s+=1
      i+=1
      break
      print(s)
   prev_line=line1
 if(i==0):
  #print("oiuyt")              
  s+=1
  fp3=open(username,"w")
  print("Sign Up!")
  name=input("Enter Your Full name:")
  password=input("Enter atleast 6-characters Password:")
  while(len(password)<6):
   password=input("Please enter a valid password:")
  fp3.write("Password:{}\n".format(password))
  fp3.write("Name:{}\n".format(name))
  email=input("Enter Your Email-Id:")
  match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
  #print(match)
  while(match == None):
   email=input("Please Enter a valid Email-Id:")
   match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
  fp3.write("Email:{}\n".format(email))
  mobile=input("Enter Your mobile number:")
  while(len(mobile)!=10):
   mobile=input("Please enter a valid 10-digit mobile number:")
  fp3.write("Mobile No:{}\n".format(mobile))
  fp3.write("\n")
if(s>=1):
 #print(s)
 #print("**s")
 k=filename('question','answer',0,1,fp3)
 #print("^^")
 if(k==50):
  print("\n")
  k=filename('general','ganswer',50,2,fp3)
 if(k==100):
  print("\n")
  k=filename('sequences','sanwer',100,3,fp3)
fp3.write("Your Reward:{}k Coins\n".format(k))
fp3.write("------------End of Game---------------------\n")
fp3.close()       
