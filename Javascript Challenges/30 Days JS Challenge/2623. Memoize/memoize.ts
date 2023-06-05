type Fn = (...params: any) => any

function memoize(fn: Fn): Fn {
    const cache = new Map();
    return function(...args) {
        const new_args:string = args.join(',');
        if (!(cache.has(new_args))){
            let res = fn(args[0],args[1]);
            cache.set(new_args,res);
        }
        return cache.get(new_args);
    }
}



/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */