from pyService.FilterService.filter import Filter
import re
import json
class processor:
    def __init__(self,project,path):
        self.path=path+'/'
        self.project=project
    def process_sc(self):
        dataName = ["allWords.json", "attributes.json", "classes.json", "comments.json", "methods.json"]
        for data in dataName:
            with open(self.path + data, 'r', encoding='utf8')as fp:
                java_dic = json.load(fp)
            for key in java_dic:
                tem = []
                tem.append(java_dic[key])
                java_dic[key] = tem
            java_dic = Filter().splitWords(java_dic)
            output = open(self.path + "/processed" + data, 'w', encoding='utf-8')
            json.dump(java_dic, output, ensure_ascii=False)
            output.close()
            print(self.path + data + "  ok")
    def process_report(self):
        dataName=["JSON-SUMMARY-New"+self.project+"BugRepository.json","JSON-DESCRIPTION-New"+self.project+"BugRepository.json","JSON-SUMMARY&DESCRIPTION-New"+self.project+"BugRepository.json"]
        for data in dataName:
            with open(self.path+data,'r',encoding='utf8')as fp:
                java_dic = json.load(fp)
            # 去掉类似于 at org.eclipse.core.launcher.Main.main(Main.java:871)
            for key in java_dic:
                if (len(re.findall(r'at [^()]+\([^()]+.java:[0-9]*[)]',java_dic[key]))==0):
                    pass
                else:
                    temp=re.findall(r'at[\n]* [^()]+\([^()]+.java:[0-9]*[)]',java_dic[key])
                    for ele in temp:
                        java_dic[key]=java_dic[key].replace(ele,"..")
                tem = []
                tem.append(java_dic[key])
                java_dic[key] = tem

            java_dic = Filter().splitWords(java_dic)
            if data=="JSON-SUMMARY-New"+self.project+"BugRepository.json":
                output = open(self.path+self.project+"_Summary.json", 'w', encoding='utf-8')
            elif data=="JSON-DESCRIPTION-New"+self.project+"BugRepository.json":
                output = open(self.path+self.project+"_Description.json", 'w', encoding='utf-8')
            else:
                output = open(self.path+self.project+"_SummaryAndDescription.json", 'w', encoding='utf-8')
            json.dump(java_dic, output, ensure_ascii=False)
            output.close()
            print(self.path+ data + "  ok")

if __name__ == '__main__':
    # processorInstance=processor("SWT","/Users/xuyuxuan/Software_engineering/大三下/软工3/backend-irblapp/JSON-SWT")
    # processorInstance.process_report()

    processorInstance = processor("AspectJ", "/Users/xuyuxuan/Software_engineering/大三下/软工3/backend-irblapp/JSON-AspectJ")
    processorInstance.process_report()

    # java_dic={'1':'at org.eclipse.core.launcher.Main.main(Main.java:871) asdhiaodhio aidhiaohd  at org.eclipse.core.launcher.Main.main(Main.java:871)'}
    # for key in java_dic:
    #     if (len(re.findall(r'at [^()]+\([^()]+.java:[0-9]*[)]', java_dic[key])) == 0):
    #         pass
    #     else:
    #         temp = re.findall(r'at [^()]+\([^()]+.java:[0-9]*[)]', java_dic[key])
    #         for ele in temp:
    #             java_dic[key]=java_dic[key].replace(ele, "..")
    #     tem = []
    #     tem.append(java_dic[key])
    #     java_dic[key] = tem
    # print(java_dic)
    # dataName=["allWords.json","attributes.json","classes.json","comments.json","methods.json"]
    # pathName=["./resultsOfAST/swt-3.1/","./resultsOfAST/aspectj-RB_V152/","./resultsOfAST/eclipse-3.1/"]
    # for path in pathName:
    #     for data in dataName:
    #         with open(path+data,'r',encoding='utf8')as fp:
    #             java_dic = json.load(fp)
    #         for key in java_dic:
    #             tem = []
    #             tem.append(java_dic[key])
    #             java_dic[key] = tem
    #         java_dic = Filter().splitWords(java_dic)
    #         output = open(path+"processed"+data, 'w', encoding='utf-8')
    #         json.dump(java_dic, output, ensure_ascii=False)
    #         output.close()
    #         print(path+data+"  ok")

        # with open("/Users/xuyuxuan/Software_engineering/大三下/软工3/backend-irblapp/JSON-Eclipse/JSON-SUMMARY&DESCRIPTION-NewEclipseBugRepository.json",'r',encoding='utf8')as fp:
        #     java_dic = json.load(fp)
        # for key in java_dic:
        #     tem = []
        #     tem.append(java_dic[key])
        #     java_dic[key] = tem
        # java_dic = Filter().splitWords(java_dic)
        # output = open("Eclipse_SummaryAndDescription.json", 'w', encoding='utf-8')
        # # output = open("Eclipse_Description.json", 'w', encoding='utf-8')
        # # output = open("Eclipse_Summary.json", 'w', encoding='utf-8')
        # json.dump(java_dic, output, ensure_ascii=False)
        # output.close()
        # print("ok")
