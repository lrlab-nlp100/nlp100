cols = list(zip(*[line.split("\t") for line in open("hightemp.txt", "r")]))
open("outputfiles/col1.txt", "w").write("\n".join(cols[0]))
open("outputfiles/col2.txt", "w").write("\n".join(cols[1]))