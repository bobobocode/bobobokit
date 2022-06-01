function print(delay, message){
    return new Promise(function(resolve, reject){
        setTimeout(function(){
            console.log(message);
        }, delay);
        resolve();
    });
}

async function asyncFunc(){
    await print(1000, 'first');
    await print(2000, 'second');
    await print(3000, 'third');
}

asyncFunc();
console.log('here');
