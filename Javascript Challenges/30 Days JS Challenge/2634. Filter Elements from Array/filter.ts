function filter(arr: number[], fn: (n: number, i: number) => any): number[] {
    let new_arr:number[] = [];
    arr.forEach((element,i) => {
        if (fn(element,i)){
            new_arr.push(element);
        }
    })
    return new_arr;
};