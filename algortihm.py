class Node():
    def __init__(self) -> None:
        self.variable = None
        self.left = None
        self.right = None

    def setvar(self, var):
        self.variable = var

    def setleft(self, left):
        self.left = left
    
    def setright(self,right):
        self.right = right

variableorder = ["a", "b", "c", "d"]


phi = Node()

#d
phi.setvar("d")
phi.setleft(Node())
phi.setright(Node())

#a
phi.left.setvar("a")
phi.left.setleft(1)
phi.left.setright(0)

#c
phi.right.setvar("c")
phi.right.setleft(1)
phi.right.setright(Node())

#b
phi.right.right.setvar("b")
phi.right.right.setleft(1)
phi.right.right.setright(Node())

#a
phi.right.right.right.setvar("a")
phi.right.right.right.setleft(0)
phi.right.right.right.setright(1)


beta = Node()
#c
beta.setvar("c")
beta.setleft(1)
beta.setright(Node())

#b
beta.right.setvar("b")
beta.right.setleft(0)
beta.right.setright(Node())

#a
beta.right.right.setvar("a")
beta.right.right.setleft(0)
beta.right.right.setright(1)


def constrain(beta, phi):
    if beta == 0:
        return 0
    elif beta == 1:
        return f"{phi}"
    elif type(beta) is Node and phi in [0,1]:
        return f"{phi}"
    else:
        if variableorder.index(phi.variable) > variableorder.index(beta.variable):
            
            print(f"{phi.variable}?{constrain(beta, phi.left)}:{constrain(beta, phi.right)}")

        elif variableorder.index(phi.variable) == variableorder.index(beta.variable):

            if beta.left != 0 != beta.right:
                print(f"{phi.variable}?{constrain(beta, phi.left)}:{constrain(beta, phi.right)}")
            elif beta.left == 0:
                return f"{constrain(beta.right,phi.right)}"
            elif beta.right == 0:
                return f"{constrain(beta.left,phi.left)}"

        elif variableorder.index(phi.variable) < variableorder.index(beta.variable):
            
            if beta.left != 0 != beta.right:
                print(f"{beta.variable}?{constrain(beta.left, phi)}:{constrain(beta.right, phi)}")
            elif beta.left == 0:
                return f"{constrain(beta.right,phi.right)}"
            elif beta.right == 0:
                return f"{constrain(beta.left,phi.left)}"

constrain(beta, phi)