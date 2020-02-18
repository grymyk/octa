import turtle

step = 20

def tree(branchLen, cursor, twig):
    global step
    
    if branchLen > twig:
        next_branch = branchLen - step
        double_level = step * 2
        
        width_twig = next_branch / step
        
        cursor.pensize(width_twig)
        
        # trunk
        cursor.forward(branchLen)
        
        # right twig
        cursor.right(step)
        tree(next_branch, cursor, twig)
        
        # left twig
        cursor.left(double_level)
        tree(next_branch, cursor, twig)
        
        cursor.right(step)
        cursor.backward(branchLen)

def main():
    cursor = turtle.Turtle()
    screen = turtle.Screen()
    
    # 10 is max to screen
    level = 7
    
    twig = 5
    branch_len = level * step
    
    cursor.left(90)
    cursor.up()
    cursor.backward(350)
    cursor.down()
    
    # ~ cursor.pensize(5)
    # ~ cursor.pencolor("green")
    
    tree(branch_len, cursor, twig)
    
    screen.exitonclick()

if __name__ == "__main__":
    main()
