# 미로찾기(Decision Problem)
- 답이 yes or no 인 문제
```
boolean findPath(x, y)
    if(x, y) is either on the wall or a visited cell
        return false;
    else if(x, y) is the exit
        return true;
    else
        mark (x, y) as a visited cell ;
        for each neighbouring cell(x`, y`) of (x, y) do
            if (x`, y`) is on the pathway and not visited
                return true;
        return false;
```
- C++
```
int n = 8;
int maze[8][8] = {
	{0,0,0,0,0,0,0,1},
    {0,1,1,0,1,1,0,1},
    {0,0,0,1,0,0,0,1},
    {0,1,0,0,1,1,0,0},
    {0,1,1,1,0,0,1,1},
    {0,1,0,0,0,1,0,1},
    {0,0,0,1,0,0,0,1},
    {0,1,1,1,0,1,0,0}	};
int track[8][8] = {
	{0,0,0,0,0,0,0,1},
    {0,1,1,0,1,1,0,1},
    {0,0,0,1,0,0,0,1},
    {0,1,0,0,1,1,0,0},
    {0,1,1,1,0,0,1,1},
    {0,1,0,0,0,1,0,1},
    {0,0,0,1,0,0,0,1},
    {0,1,1,1,0,1,0,0}	};


void printmaze()
{
	for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
        	printf("%d ",maze[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}
void findPath(int x, int y){
    if(x == n-1 && y == n-1)
    {
    	printmaze();
    	exit(0);
    }
    else{
        track[x][y] = 1;
        
        if(x-1 >= 0 && track[x-1][y] == 0 && maze[x-1][y] == 0)
        {
        	maze[x-1][y] = 2;
            track[x-1][y] = 1;
            findPath(x-1, y);
            maze[x-1][y] = 0;
        }
        if(x+1 < n && track[x+1][y] == 0 && maze[x+1][y] == 0)
        {
        	maze[x+1][y] = 2;
            track[x+1][y] = 1;
            findPath(x+1, y);
            maze[x+1][y] = 0;
        }
        if(y-1 >= 0 && track[x][y-1] == 0 && maze[x][y-1] == 0)
        {
            track[x][y-1] = 1;
            maze[x][y-1] = 2;
            findPath(x, y-1);
            maze[x][y-1] = 0;
        }
        if(y+1 < n && track[x][y+1] == 0 && maze[x][y+1] == 0)
        {
            track[x][y+1] = 1;
            maze[x][y+1] = 2;
            findPath(x, y+1);
            maze[x][y+1] = 0;
        }
    }
}
int main(void){
    printmaze();
    maze[0][0] = 2;
    findPath(0, 0);
}
```
- Java
```
public class Maze {
    private static int N=8;
    private static int [][] maze = {
        {0,0,0,0,0,0,0,1},
        {0,1,1,0,1,1,0,1},
        {0,0,0,1,0,0,0,1},
        {0,1,0,0,1,1,0,0},
        {0,1,1,1,0,0,1,1},
        {0,1,0,0,0,1,0,1},
        {0,0,0,1,0,0,0,1},
        {0,1,1,1,0,1,0,0}
    };

    private static final int PATHWAY_COLOUR = 0;
    // unvisited이며 아직 출구로 가는 경로가 될 가능성이 있는 cell
    private static final int WALL_COLOUR = 1;
    private static final int BLOCKED_COLOUR = 2;
    // visited이며 출구까지의 경로상에 있지 않음이 밝혀진 cell
    private static final int PTH_COLOUR = 3;

    public static boolean findMazePath(int x, int y){
        if(x < 0 || y < 0 || x >= N || y >= N)
            return false;
        else if(maze[x][y] != PATHWAY_COLOUR)
            return false;
        else if(x == N-1 && y == N-1){
            maze[x][y] = PATHWAY_COLOUR;
            return true;
        }
        else{
            maze[x][y] = PATHWAY_COLOUR;
            if(findMazePath(x-1, y) || findMazePath(x, y+1) || findMazePath(x+1, y) || findMazePath(x, y-1)){
                return true;
            }
            maze[x][y] = BLOCKED_COLOUR;
            return false;
        }
    }
    public static void printMaze()
    {
        for(int i = 0; i < 8; i++)
        {
            for(int j = 0; j < 8; j++)
            {
                System.out.print(maze[i][j]);
            }
            System.out.println();
        }
    }
    public static void main(String [] args){
        printMaze();
        findMazePath(0,0);
        printMaze();
    }
}
```