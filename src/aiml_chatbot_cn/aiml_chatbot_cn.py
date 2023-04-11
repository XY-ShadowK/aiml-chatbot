"""
__name__="aiml_chatbot_cn.aiml_chatbot_cn"
__package__="aiml_chatbot_cn"
"""

import os
import sys
sys.path.append("E:\\code\\python\\Lib\\packages")
import aiml_py3_cn

alice_path='../../../Lib/packages/aiml_py3_cn/Example'
os.chdir(alice_path)

alice=aiml_py3_cn.Kernel()
alice.learn("cn-test.aiml")

while True:
    print("机器人回复: "+alice.respond(input("你说: ")))
