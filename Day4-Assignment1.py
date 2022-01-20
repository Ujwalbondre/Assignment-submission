def func_1(a,b,c,d,e,f,g):
    print(f"Yours LIST is:- \n{a}")
    print("------------------")
    print(f"Yours INT is:- \n{b}")
    print("------------------")
    print(f"Yours FLOAT is:- \n{c}")
    print("------------------")
    print(f"Yours TUPLE is:- \n{d}")
    print("------------------")
    print(f"Yours SET is:- \n{e}")
    print("------------------")
    print(f"Yours DICT is:- \n{f}")
    print("------------------")
    print(f"Yours BOOL is:- \n{g}")
    print("------------------")

a= [12,445.20,'xx','w',[1,4,3],{"name":"vikas","age":'12'}]
d=(22,11,222,321)
e={'e','x','a','m','x',1,2,3,3}
f={"country":"IND","Dist":'Thane'}
b=input("Enter you INT  :-")
c=input("Enter you FLOAT :-")
g=bool(input("Enter you BOOL :-"))

func_1(a,b,c,d,e,f,g)