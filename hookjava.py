import sys
import time

import frida
# coding=utf-8


def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)


try:
    device = frida.get_remote_device()
    # pid = device.spawn(['com.bbte.internal'])
    # pid = device.spawn(['com.physics.sim.game.box'])
    #
    # device.resume(pid)
    # time.sleep(1)
    # session = device.attach(pid)
    # session = device.attach("com.bbte.internal")

    session = device.attach("com.gameley.blademaster.spinning.en")
    # 加载s1.js脚本
    with open("./myScript.js") as f:
        script = session.create_script(f.read())
    # script = session.create_script(jsCode)
    script.on('message', on_message)
    # raw_input()
    script.load()
    sys.stdin.read()

# session.detach()
except KeyboardInterrupt:
    print("[!] Killing app...")