setImmediate(function () {
//    Java.perform(function () {
//        // const connection = Java.use("b.c.d.b.a");
//        const AppActivity = Java.use("org.cocos2dx.javascript.AppActivity");
//        AppActivity.MainPurchasesUpdated.implementation = function (v) {
//
//            send("arg1 ====" arg1)
//            // send("onClick");
//            send("MainPurchasesUpdated");
//
//
//            return this.MainPurchasesUpdated(arg1);
//        }
//
//
//    })

    Java.perform(function () {
        // const connection = Java.use("b.c.d.b.a");
        const Activity = Java.use("c.a.a.a.b.b");
        Activity.a.overload("java.lang.String","java.util.List","com.android.billingclient.api.n").implementation = function (arg1,arg2,arg3) {
            // send("onClick");



            send("arg1 ----" + arguments[0] + "  arg2 -----" + arguments[1] + "  arg3 -----"+ arguments[2] + "  arg4 -----"+ arguments[3])
            console.log("onclick");
            return this.a(arg1,arg2,arg3);
        }
    })
});