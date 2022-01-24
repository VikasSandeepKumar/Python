# Variable scope in Python - boundary of variable within a program
# Local Scope

# Global keyword

# def var_scope_demo():
#     x=20
#     print(x)
#
# var_scope_demo()
#
# def var_scope_demo1():
#     print( x )
#
# var_scope_demo()
# var_scope_demo1()


# Global Scope
# def var_scope_demo():
#     global x
#     x = 20
#     print( x )
#
# def var_scope_demo1():
#     print( x )
#
# var_scope_demo()
# var_scope_demo1()

# LEGB rule: Local -> Enclosing->Global->Built-in
x = 100
def var_scope_demo():
    x = 20
    print(x)
    def var_scope_demo1():
        x = 50
        print(x)
        def grand_child():
            x = 40
            print(x)
        grand_child()
        var_scope_demo1()

var_scope_demo()