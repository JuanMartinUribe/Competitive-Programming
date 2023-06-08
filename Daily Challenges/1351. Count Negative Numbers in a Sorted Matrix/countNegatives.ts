function countNegatives(grid: number[][]): number {
    const R = grid.length;
    const C = grid[0].length;
    let currCol = 0;
    let negatives = 0;

    for (let currRow=R-1;currRow>=0;currRow--){
        while(currCol<C && grid[currRow][currCol]>=0){
            currCol+=1
        }
        negatives += grid[currRow][currCol]<0 ? C-currCol : 0; 
        console.log(negatives);
    }
    return negatives;

    
};