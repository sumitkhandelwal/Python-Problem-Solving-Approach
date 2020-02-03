class A:  
    def Sum(self,a,b):  
        return a+b;  
class B:  
    def Mul(self,a,b):  
        return a*b;  
class C(A,B):  
    def Div(self,a,b):  
        return a/b;  
data = C()  
print(issubclass(C,B))  
print(issubclass(A,B))  
