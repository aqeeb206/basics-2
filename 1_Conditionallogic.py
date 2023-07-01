is_old = True
is_license = True
if is_old:
    print('you are old enough to drive!')
elif is_license:#you can have multiple elif statements.
    print("you can drive now!")
else:  # else block only runs if the  if block of code  evaluates to false.
    print('you are not eligible to drive!')
print('checkcheck')
# another better way to check
if is_old and is_license:
    print('you are old enough to drive and you have license to drive')
# keyword-->(and) means if  both expressions are true then only it will be executed.
# INDENTATION IN PYHTON
# Be mindful of indentation.
# In python the interpreter actually find meaning in the spaces.
#little spaces can change the outcome of the program.
