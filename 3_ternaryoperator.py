is_freind=True
#Ternary Operator -->(conditional expression)expresion evaluates to a value(0 or 1).
#condition_if_true if condition else condition_if_false
can_message="message allowed " if is_freind else "not allowed to message"
print(can_message)
is_freind=False
can_message="message allowed " if is_freind else "not allowed to message"
print(can_message)

#SHORT CIRCUITING
is_freind=True
is_user=True
if is_freind and is_user:#and means if both are true then only it will be executed.
    print("freinds forever")
if is_freind or is_user:#or means either one of is true it will be executed.
    print("freinds forever")
#using or is a little bit efficient 
#because interpreter will not go 
#ahead for executing second expression if it finds first expression is True.
#it also works with and as well .but again it depends on what you need.


