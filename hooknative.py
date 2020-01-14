import frida
import sys

# 查看进程命令  adb shell -> su -> ps -ef | grep "com.xxx"   ->  获得进程id
# 查看so文件函数起始地址  adb shell -> su ->  cat /proc/进程id/maps | grep "lib.so"

# nativePointer构造函数中传入函数的绝对地址。


jscode = """
setImmediate(function () {
    Java.perform(function () {
        const Activity = Java.use("com.example.testandroid.MyActivity");
        Activity.onClick.implementation  = function (v) {
            console.log('abc');
            return this.onClick(v);
        }
        
    })
});
"""


def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)


device = frida.get_remote_device()

# 如果存在两个一样的进程可以采用 device.attach(pid)的方式
session = device.attach("com.example.testandroid")

script = session.create_script(jscode)
script.on("message", on_message)
script.load
print("daadf")
sys.stdin.read()
