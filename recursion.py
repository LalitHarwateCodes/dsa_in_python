def walk(steps):
    if steps == 0:
        return
    walk(steps -1)
    print(steps)


walk(100)
   
    



