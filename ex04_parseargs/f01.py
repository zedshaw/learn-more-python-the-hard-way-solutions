import sys
args = sys.argv

bar = ''
baz = ''
foo = ''
exld = False
lst_int = []
start_bool = False
tn_bool = False

#template1 = "Namespace(bar={bar}, baz={baz}, exclude={exld}, foo={foo}, integers={lst_int}, start={start_bool}, turn_on={tn_bool})"
template2 = f"usage: {args[0]} [-h] [-f FOO] [-b BAR] [-z BAZ] [-t] [-x] [-s] N [N ...]"



lst_arguments = [
    ('-h','--help','   show this help message and exit'),
    ('-f','--foo','FOO','foo help'),
    ('-b','--bar','BAR','bar help'),
    ('-z','--baz','BAZ','baz help'),
    ('-t','--turn-on'),
    ('-x','--exclude'),
    ('-s','--start')
]

arg_str = list()
for tup in lst_arguments:
    arg_str.append("".join(tup))
arg_str = "".join(arg_str)

def check_appnd(arg):
    if str.isdigit(arg):
        for tup in lst_arguments:
            if arg in tup:
                return False
        return True


for arg in args:

    if check_appnd(arg):
        lst_int.append(int(arg))

    if arg in lst_arguments[0]:
        print(template2+"\n\n")
        print("positional arguments")
        print("    N\n\n")
        print("optional arguments")
        for larg in lst_arguments:
            for l in larg:
                print(l,end=" ")
            print()
        sys.exit()
    if arg in lst_arguments[1]:
        idx = args.index(arg)
        foo = args[idx+1]
    if arg in lst_arguments[2]:
        idx = args.index(arg)
        bar = args[idx+1]
    if arg in lst_arguments[3]:
        idx = args.index(arg)
        baz = args[idx+1]
    if arg in lst_arguments[4]:
        tn_bool = True
    if arg in lst_arguments[5]:
        exld = True
    if arg in lst_arguments[6]:
        start_bool = True

arg_str = arg_str + foo + bar + baz + args[0] + "".join([str(num) for num in lst_int])
for arg in args:
    if not arg in arg_str:
        print(f"{args[0]}: error: unrecognized arguments: {arg}")
        sys.exit()

print(f"Namespace(bar={bar}, baz={baz}, exclude={exld}, foo={foo}, integers={lst_int}, start={start_bool}, turn_on={tn_bool})")
