from string import Template

def xyz(x, y, z):
    t = Template("${a}時の${b}は${c}")
    return t.substitute(a = x, b = y, c = z)

if __name__ == "__main__":
    x,y,z = 12,"気温", 22.4
    print(xyz(x,y,z))
