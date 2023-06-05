type F = (x: number) => number;

function compose(functions: F[]): F {
    const rec = (i:number,x:number) => {
        const fn = functions[i];
        if (i+1 == functions.length){
            return fn(x);
        }
        else{
            return fn(rec(i+1,x));
        }
    }
	return function(x) {
        if (functions.length){
            return rec(0,x);
        }
        else{
            return x;
        }
    }
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */