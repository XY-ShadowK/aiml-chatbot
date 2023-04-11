"""
__name__="aiml_chatbot_cn.aiml_chatbot_cn"
__package__="aiml_chatbot_cn"
"""

import aiml
import os

'''
def get_module_dir(name):
    path=getattr(sys.modules[name],'__file__',None)
    if not path:
        raise AttributeError('module %s has not attribute __file__' %name)
    return os.path.dirname(os.path.abspath(path))

alice_path=get_module_dir('aiml')+'/alice'
os.chdir(alice_path)

alice=aiml.Kernel()
alice.learn(startup.xml)
alice.respond('LOAD ALICE')

while True:
    print alice.respond(raw_input("Enter your message >> "))
'''

chatbot_path = '../../chatbot/corpus'
os.chdir(chatbot_path)

chatbot = aiml.Kernel()
chatbot.learn("std-startup.xml")

print("choosing the aiml chatbot!")
print("1. basic chatbot")
if input() == "1":
    chatbot.respond("load aiml basic")

while True:
    print(chatbot.respond(input("Enter your message >> ")))
