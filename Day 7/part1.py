class Dir:
    def __init__(self,name,parent=None):
        self.name=name
        self.parent=parent
        self.children=[]
        self.type='directory'

    def add_child(self,child):
        self.children.append(child)
    
    def get_parent(self):
        return self.parent
    

    
    



class file:
    def __init__(self,name,size,filetype,parent):
        self.name=name
        self.size=size
        self.filetype=filetype
        self.parent=parent
        self.type='file'

    
def read_input():
    with open('input.txt','r') as f:
        cont=f.read()
        return cont
    
    
def read_test_input():
    with open('test_input.txt','r') as f:
        cont=f.read()
        return cont
    
def print_directory(directoy:Dir,hierarchy=0):
    

    if directoy.type=='directory':
        for content in directoy.children:
            s=''
            for i in range(0,hierarchy):
                s+='\t'
            s+=f'{content.name} ({content.type})'
            print(s)
            
            if content.type=='directory':
                print('Hallo')
                for subcontent in content.children:
                    print_directory(directoy=subcontent,hierarchy=hierarchy+1)

            #print(content.name+' '+content.type)

    

def main():
    cont=read_test_input().split('\n')

    command_mode=False
    list_mode=True

    dir=Dir(name='root')
    hierarchy=0

    for index,command in enumerate(cont):
        s=str(index)
        for i in range(0,hierarchy):
            s+='\t'
        s+=f'-{dir.name} ({dir.type})'
        #print(s)

        

        if list_mode and '$' in command:
            list_mode=False
            command_mode=True

        if command=='$ ls':
            list_mode=True
            command_mode=False
            continue

        if command_mode and '$ cd ' in command:
            if '..' in command:
                dir=dir.get_parent()
                hierarchy-=1
                continue
            dest_dir_name=command.split(' ')[2]
            dest_dir=Dir(name=dest_dir_name,parent=dir)
            dir.add_child(child=dest_dir)
            dir=dest_dir
            hierarchy+=1
            continue


        if list_mode:
            if 'dir ' in command:
                name=command.split(' ')[1]
                dir.add_child(child=Dir(name=name,parent=dir))
                continue

            else:
                name=command.split(' ')[1]
                size=command.split(' ')[0]
                try:
                    filetype=name.split('.')[1]
                except IndexError:
                    filetype=None
                dir.add_child(child=file(name=name,size=size,filetype=filetype,parent=dir))
                continue

    while dir.parent != None:
        dir=dir.parent
    print_directory(directoy=dir)
    #print(dir.children[0].children)



if __name__=='__main__':
    main()