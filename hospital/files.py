class files():
    def __init__(self, paths=""):
        self.paths = paths
    
    def write_to_file(self,file_name,content):
        f=open(f"{file_name}", "a")
        f.write(f"{content}\n")
        f.close()
    
    def read_dic_location(self):
        input = open(self.paths, "r")
        w = input.read().splitlines()
        return w
    
    def file_to_nested_dictionary(self):
        x = self.read_dic_location()
        for i in range(len(x)):
            x[i]=x[i].replace("{","").replace("}","").replace("'",'')
        main_dic = {}
        dic1={}
        dic2 = {}
        for i in range(len(x)):
            if ':' in x[i]:
                key1 = x[i][0 : x[i].index(":")]
                x[i]=x[i][x[i].index(":")+1:].strip()
                z=x[i].split(",")
                for j in z:
                    key2 = j[0 : j.index(":")].strip()
                    dic2.setdefault(key2,j[j.index(":")+1:].strip())
                main_dic.setdefault(key1,dic2.copy())
                dic2.clear()
        return main_dic
    
# x=files(r"C:\Users\Lenovo\Desktop\shared_github\hospital\patient.txt")
# x.write_to_file("patient.txt",{"zeyad":{"age":"22","phone_Number":"01148656665"},"adel":{"age":"21","phone_Number":"012"}})
# ziad=x.file_to_nested_dictionary()
# for i in ziad.items():
#     print(i[1]['Gender'])
