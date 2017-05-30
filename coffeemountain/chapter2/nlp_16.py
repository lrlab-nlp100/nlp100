import sys,math

N = sys.argv[1]
lines = [line for line in open("hightemp.txt","r")]
unit = math.ceil(len(lines)/int(N))

for i in range((int(N))):
    with open("outputfiles/file_16_"+str(i+1)+".txt","w") as f:
        f.write("".join(lines[i*unit:(i+1)*unit]))
