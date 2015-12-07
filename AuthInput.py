#-*-coding:utf-8-*-
'''判断由'(',')'组成的字符串要有完整的配对
(()())可以，())(这样的不行'''
def AuthIn(string):
        mylist = []
        for i in string:
                if i == '(':
                        .append(i)
                if i == ')' and not mylist:
                        return False    
                if i == ')' and  mylist:                
                        mylist.pop()                                            
        if not mylist:                                                                          
                return True                                                                                             
        else:                                                                                                                                           return False
