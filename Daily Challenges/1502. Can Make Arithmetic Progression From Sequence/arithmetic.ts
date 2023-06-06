function canMakeArithmeticProgression(arr: number[]): boolean {
    arr.sort((a,b) => {return a-b});
    const delta = arr[1]-arr[0];
    let ans = true;
    arr.forEach((value,index)=>{
        if (index<arr.length-1 && (arr[index+1]-value)!=delta){
            ans = false;
            return;
        }
    });
    return ans;
};