import os
import sys


def read_test_input():
    with open("testinput.txt", "r") as f:
        cont = f.read()
        return cont.split("\n")


def read_input():
    with open("input.txt", "r") as f:
        cont = f.read()
        return cont.split("\n")
    

class Forrest:
    def __init__(self, trees):
        self.trees=trees
        self.x_size=max([x.coordinate_x for x in self.trees])+1
        self.y_size=max([x.coordinate_y for x in self.trees])+1

        

    def print_forrest(self,mark_visible=False):
        str_forrest=''
        for tree in self.trees:
            #print(f'Tree (x={tree.coordinate_x}, y={tree.coordinate_y})')
            
            if mark_visible:    
                if tree.visible:
                    str_forrest+='X'
                else:
                    str_forrest+=str(tree.value)
            else:
                str_forrest+=str(tree.value)
            if tree.coordinate_x==self.x_size-1:
                
                str_forrest+='\n'



        print(str_forrest)
    
    def get_max_scenic_score(self):
        return max(x.scenic_score for x in self.trees)



class Tree:
    def __init__(
        self,
        value,
        coordinate_x,
        coordinate_y,
        parent_row,
        parent_column,
        forrest_y_size,
        forrest_x_size,
    ):
        self.value = int(value)
        self.coordinate_x = int(coordinate_x)
        self.coordinate_y = int(coordinate_y)
        self.parent_row = [int(x) for x in parent_row]
        self.parent_column = [int(x) for x in parent_column]
        self.forrest_y_size = forrest_y_size
        self.forrest_x_size = forrest_x_size
        self.visible = False
        self.set_borders_to_visible()
        self.check_if_visible()
        self.scenic_score=0
        self.get_scenic_score()


    def check_if_visible(self):
    
        #merged_row=self.parent_row.insert(self.coordinate_x,self.value,)
        if self.visible == False:
            row_visible=False
            column_visible=False    
            if  ((self.value > max(self.parent_row[0:self.coordinate_x])) or
                (self.value > max(self.parent_row[self.coordinate_x+1:len(self.parent_row)]))):
                row_visible=True
                

            if  ((self.value > max(self.parent_column[0:self.coordinate_y])) or
                (self.value > max(self.parent_column[self.coordinate_y+1:len(self.parent_column)]))):
                column_visible=True
                

            if column_visible or row_visible:
                
                self.visible=True
            
            

    def set_borders_to_visible(self):
        if self.coordinate_x == 0 or self.coordinate_y == 0:
            self.visible = True
        elif (
            self.coordinate_y == self.forrest_y_size-1
            or self.coordinate_x == self.forrest_x_size-1
        ):
            self.visible = True

    def get_scenic_score(self):

        def get_score_for_direction(view:list,value=self.value, reverse=False):
            if reverse:
                view.reverse()
            score=0
            for t in view:
                
                score+=1
                if int(t)>=value:
                    break
                
            return score
        
        self.west_view=get_score_for_direction(self.parent_row[0:self.coordinate_x], reverse=True)
        self.east_view=get_score_for_direction(self.parent_row[self.coordinate_x+1:len(self.parent_row)])
        self.north_view=get_score_for_direction(view=self.parent_column[0:self.coordinate_y],reverse=True)
        self.south_view=get_score_for_direction(view=self.parent_column[self.coordinate_y+1:len(self.parent_column)])

        

                
        self.scenic_score=self.west_view*self.east_view*self.north_view*self.south_view
                



def prepare_data(input):
    forrest = []

    for index_x, tree_row in enumerate(input):
        forrest.append([])
        for index_y, tree in enumerate(tree_row):
            forrest[index_x].append(tree)

    return forrest, index_x + 1, index_y + 1


def create_forrest(data, x_length, y_length):
    trees = []
    for index_y, row in enumerate(data):
        x_parents = [x for x in row]
        for index_x, column in enumerate(row):
            t = Tree(
                value=column,
                coordinate_x=index_x,
                coordinate_y=index_y,
                parent_row=x_parents,
                parent_column=[x[index_x] for x in data],
                forrest_x_size=x_length,
                forrest_y_size=y_length,
            )
            trees.append(t)
    return Forrest(trees=trees)


def solve_question_1(forrest):
    return len([x for x in forrest.trees if x.visible])


def solve_question_2(forrest):
    return forrest.get_max_scenic_score()


def main():
    input = read_input()
    data, x_length, y_length = prepare_data(input=input)

    forrest = create_forrest(data=data, y_length=y_length, x_length=x_length)

    forrest.print_forrest()
    print('')
    forrest.print_forrest(mark_visible=True)

    print(f"Amount of visible Trees: {solve_question_1(forrest=forrest)}")

    print(f"Highest Scenic Score: {solve_question_2(forrest=forrest)}")


if __name__ == "__main__":
    os.system("clear")
    main()
