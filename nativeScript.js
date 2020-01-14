setImmediate(function () {
    //传入绝对地址
    var baseAddr = 0x9EE53000;
    var releAddr = 0x00008E64;
    var absoluteAddr = baseAddr + releAddr;
    console.log('函数绝对地址：'+ absoluteAddr.toString(16));
    var nativePointer = new NativePointer(absoluteAddr);

    Interceptor.attach(nativePointer, {
        onEnter: function(args){
            send("入参:" + args[0] + ", " + args[1]);
        },

        onLeave: function(retval){
            send("ret" + retval)
        }
    });
});