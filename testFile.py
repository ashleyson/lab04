from lab04 import solveMaze
def test_solveMaze():
    maze = [
    ['+','+','+','+','+','+'],
    ['+',' ','+',' ',' ','+'],
    ['+',' ',' ',' ','G','+'],
    ['+',' ','+','+','+','+'],
    ['+',' ',' ',' ',' ','+'],
    ['+','+','+','+','+','+']]

    maze1 = [
    ['+','+','+','+','+','+'], 
    ['+',' ','+',' ','+','G'],
    ['+',' ',' ',' ','+','+'],
    ['+',' ','+','+',' ','+'],
    ['+',' ',' ',' ',' ','+'],
    ['+','+','+','+','+','+']]

    assert solveMaze(maze,4,4) == True
    assert maze == [
    ['+','+','+','+','+','+'], 
    ['+',7,'+',10,11,'+'],
    ['+',6,8,9,'G','+'],
    ['+',5,'+','+','+','+'],
    ['+',4,3,2,1,'+'],
    ['+','+','+','+','+','+']]

    assert solveMaze(maze1,4,4) == False
    assert maze1 == [
    ['+','+','+','+','+','+'], 
    ['+',8,'+',11,'+','G'],
    ['+',7,9,10,'+','+'],
    ['+',6,'+','+',2,'+'],
    ['+',5,4,3,1,'+'],
    ['+','+','+','+','+','+']]
    
