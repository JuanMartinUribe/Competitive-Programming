type ReturnObj = {
    increment: () => number,
    decrement: () => number,
    reset: () => number,
}
class Obj {
    num: number;
    initialNum : number;
    
    constructor(num) {
        this.num = num;
        this.initialNum = num;
    }
    increment(): number {
        return ++this.num;
    }
    decrement(): number {
        return --this.num;
    }
    reset(): number {
        this.num = this.initialNum;
        return this.num;
    }
}
function createCounter(init: number): ReturnObj {
    return new Obj(init);
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */ 