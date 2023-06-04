function map(arr: number[], fn: (n: number, i: number) => number): number[] {
    let newArr:number[] = [];
    arr.forEach((element:number,i:number)=>{
        newArr.push(fn(element,i));
    });
    return newArr;
};