import os


from ....Lib.packages import aiml_py3_CN


'''
import sys
sys.path.append("E:\\code\\python\\Lib\\packages")
import aiml_py3_CN
'''

alice_path='../../../Lib/packages/aiml_py3_CN/Example'
os.chdir(alice_path)

alice=aiml_py3_CN.Kernel()
alice.learn("cn-test.aiml")

while True:
    print("机器人回复: "+alice.respond(input("你说: ")))
