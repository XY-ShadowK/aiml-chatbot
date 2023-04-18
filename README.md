# 部署帮助
# python要求
python版本为3.7，安装了aiml包，即可使用aiml_chatbot和aiml_question  
python版本为3.7，下载https://github.com/yaleimeng/py3Aiml_Chinese ，并自行修改\src\aiml_chatbot_cn内容中路径，即可使用aiml_chatbot_cn  
需要修改的代码块如下  

    sys.path.append("E:\\code\\python\\Lib\\packages")
    import aiml_py3_cn
    
    alice_path='../../../Lib/packages/aiml_py3_cn/Example'
    os.chdir(alice_path)
