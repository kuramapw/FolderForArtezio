class Student:
    name="name"
    conf={'exam_max': 30 ,'lab_max':7,'lab_num':10, 'k':0.61}
    def __init__(self,name,conf):
        self.name=name
        self.conf=conf

    res=[0 for res in range(conf['lab_num'])]
    res_exam=0
    def make_lab(self,m,n):
        if(m>self.conf['lab_max']):
            m=self.conf['lab_max']
        if not n.exist():
            for i in self.res:
                if(i==0):
                    self.res=m
                    break
        else:
            if(n<self.conf['lab_num']):
                self.res.insert(n,m)
        return self

    def make_exam(self,m):
        if(m>self.conf['exam_max']):
            m=self.conf['exam_max']
        self.res_exam=m
        return self

    def if_certified(self):
        return (sum(self.res)+self.res_exam,(sum(self.res)+self.res_exam)>(self.k*(self.conf['exam_max']+self.conf['lab_max']+self.conf['lab_num'])))
    pass