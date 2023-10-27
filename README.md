#Program to print star pyramids
outer_loop=6
inner_loop=1
for x in range(4):
    for y in range(outer_loop):
        print (" ", end='')
    for z in range(inner_loop):
        print("*",end=' ')  
    print(" ")  
    outer_loop -=2
    inner_loop +=2
print("program done")

'''Output
      *  
    * * *  
  * * * * *  
* * * * * * *  
program done'''
