try:
    f = open("arquivo2.txt","w")
    f.write("eu 1\n")
    f.write("eu 2\n")
finally:
    f.close()
