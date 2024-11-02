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
    
    def file_to_dictionary(self):
        x = self.read_dic_location()
        for i in x:
            i.replace("{","").replace("}","")
        dic = {}
        for i in x:
            if ':' in i:
                key1 = i[0 : i.index(":")]
                dic[key1] = (
                    i[i.index(":")+1:]
                )
        return dic
    
x=files(r"C:\D\Amit\Duo\hospital\patient.txt")
# x.write_to_file("patient.txt",{"zeyad":{"age":"22","phone_Number":"01148656665"},"adel":{"age":"21","phone_Number":"012"}})
ziad=x.file_to_dictionary()
print(ziad)
print(type(ziad))