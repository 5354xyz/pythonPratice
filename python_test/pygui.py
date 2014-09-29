from Tkinter import *
from tkMessageBox import *
import sys,json
import urllib,urllib2
from os import path
from urllib import quote
from urllib import unquote
import re
import sys
class EntryDemo( Frame):

    """ Demonstrate Entrys and Envent Building"""

    def __init__( self ):

        Frame.__init__(self)

        self.pack(expand=YES,fill = BOTH)

        self.master.title("please input keywords and url here")

        self.master.geometry("800x600") #width X length

        #Entry Demo

        self.frame1 = Frame(self)

        self.frame1.pack( pady = 5 ) #垂直间距

        

        self.text1 = Entry(self.frame1, name="text1") #放置在frame1上

        self.text1.bind("<Return>",self.showContents )
        self.text1.insert(INSERT, "Enter keywords here")
        self.text1.bind("<Enter>", self.textEnter) #鼠标事件:进入

        self.text1.pack(side=LEFT, padx=5)

        self.text2 = Entry(self.frame1, name="text2")

        self.text2.insert(INSERT, "Enter url here")

        self.text2.bind("<Return>",self.showContents )
        self.text2.bind("<Enter>", self.textEnter) #鼠标事件:进入

        self.text2.pack(side=LEFT,padx=5)

        self.frame2=Frame(self)

        self.frame2.pack(pady=5)

        

        self.text3=Entry(self.frame2, name="text3")

        self.text3.insert(INSERT,"Uneditable text field")


        #button Demo

        self.frame3= Frame(self)

        self.frame3.pack(pady = 5)

        self.plainButton=Button(self.frame3, text="submit",\

            command= self.pressedPlain)

        self.plainButton.bind("<Enter>", self.rolloverEnter) #鼠标事件:进入

        self.plainButton.bind("<Leave>", self.rolloverLeave) #鼠标事件：离开

        self.plainButton.pack(side=LEFT,padx=5, pady=5)


        #showlebal
        self.frame4= Frame(self)

        self.frame4.pack(pady = 5)
        self.conclusion=Text(self.frame4)
        #self.conclusion.wrap(WORD)
        self.conclusion.pack()
        

    def pressedPlain(self):
        message = "keywords=",self.text1.get(),"url=",self.text2.get()
        self.conclusion.delete(0.0, END)
        #showinfo("Message",message)
        dic = self.getret(self.text1.get(),self.text2.get())
        #conclusion
        conclusion = u'trace conclusion:'
        
        if dic['conclusion'] is not None:
            for i,val in enumerate(dic['conclusion']):
                print conclusion,'-',val
                conclusion="".join([conclusion,val])
        else :
            conclusion="".join([conclusion,'debug does not return the conclusion','\t'])
        line = '\n model\t\tCheck-list\t\tresult\t\t\tdetail'
        conclusion="".join([conclusion,line])
        #record
        ac_tag=''
        bc_tag=''
        bs_tag=''
        buildMissModule_tag=''
        spiderMissModule_tag=''
        if dic['record'] is not None:
            res = self.recordClassify(dic['record'])
            if res[0]is not None:
                for i,val in enumerate(res[0]):
                    
                    ac_tag="".join([val,'\n'])
            if res[1]is not None:
                for i,val in enumerate(res[1]):
                    
                    bc_tag="".join([val,'\n'])
            if res[2]is not None:
                for i,val in enumerate(res[2]):
                    
                    bs_tag="".join([val,'\n'])
            if res[3]is not None:
                for i,val in enumerate(res[3]):
                    
                    buildMissModule_tag="".join([val,'\n'])
                    #print '+++'*5,buildMissModule_tag
            if res[4]is not None:
                for i,val in enumerate(res[4]):
                    
                    spiderMissModule_tag="".join([val,'\n'])
            
            #print buildMissModule_tag 
            record="".join([spiderMissModule_tag,buildMissModule_tag,bs_tag,bc_tag,ac_tag,'\n'])
            conclusion="".join([conclusion,record.decode('utf8')])
        else:
            conclusion="".join([conclusion,'\nno detail'])
        self.conclusion.insert(INSERT,conclusion)
        conclusion=''
    def rolloverEnter(self,event):

        event.widget.config(relief=GROOVE)

    def rolloverLeave(self,event):

        event.widget.config(relief=RAISED)
    def textEnter(self,event):
        #print event.widget.get()
        if (event.widget.get() == 'Enter keywords here') or (event.widget.get() == 'Enter url here' ) :
            event.widget.delete(0,20)
            

    def showContents(self, event):

        theName=event.widget.winfo_name()

        theContents=event.widget.get()

        showinfo("Message", theName +":"+ theContents)
    def getret(self,keywords,url_test):
        url_0='''
            http://debug0.baidu.com:8088/frame/frame.php?input=%7B%22url%22%3A%22'''
        url_test=quote(url_test)
        url_1 = '''%22%2C%22link%22%3A%22http%3A%2F%2Fdebug0.baidu.com%3A9000%2Fmsg%2Fhome%2Fservice%3Fwd%3D'''
        url_2 = '''%26lm%3D0%26cl%3D3%26ct%3D0%26info%3D2%26lang%3Dcn%26ie%3Dutf-8%26env%3Ddebug0.baidu.com%253A9100%26ac_cl%3D3%26rn%3D10%26level%3D4128799%26rebuildu%3D%255B%255D%26tn%3Dbaidudata%22%2C%22name%22%3A%22urlmiss%22%7D&cb=caseflow.urlmiss_finish
                '''
        keywords=quote(keywords.encode('utf8'))
        url = "".join([url_0,url_test,url_1,keywords, url_2])
        #print url
        ret = urllib.urlopen(url)
        
        ret_data = ret.read()
        #print ret_data
        ret_data = ret_data[24:-1]
        #print ret_data 

        json.dumps(ret_data)
        dic = json.loads(ret_data,encoding='utf8')
        #print dic,'\n'
        return dic
        
    def recordClassify(self,listrecord):
        rePath = './/reDataPath.txt'
        with open(rePath) as re_data:  
                reStr = re_data.readlines()
        ac=[]
        bc=[]
        bs=[]
        buildMissModule=[]
        spiderMissModule=[]
        for v in range(0,len(listrecord)):
            #print listrecord[v]  listrecord[v]
            listrecord_i = listrecord[v].replace(" ","").replace(" ","").strip()
            for i,val in enumerate(reStr):
                val = val.split('|')
                rt = val[0].replace(" ","").replace(" ","").strip()
                rt=unicode(rt,'utf8')
                pattern = re.compile(rt)
                
                match = pattern.match(listrecord_i)
                if match:
                    if val[3] == 'ac\n' :
                        str_ac = "".join(['\nac\t\t',val[1],'\t\t',val[2],'\t\t\t',val[0]])
                        ac.append(str_ac)
                    elif val[3] == 'bc\n' :
                        str_bc = "".join(['\nbc\t\t',val[1],'\t\t',val[2],'\t\t\t',val[0]])
                        bc.append(str_bc)
                    elif val[3] == 'bs\n' :
                        str_bs = "".join(['\nbs\t\t',val[1],'\t\t',val[2],'\t\t\t',val[0]])
                        bs.append(str_bs)
                    elif val[3] == 'buildMissModule\n' :
                        str_buildMissModule = "".join(['\nbuildMissModule\t\t',val[1],'\t\t',val[2],'\t\t\t',val[0]])
                        buildMissModule.append(str_buildMissModule)
                    elif val[3] == 'spiderMissModule\n' :
                        str_spiderMissModule = "".join(['\nspiderMissModule\t\t',val[1],'\t\t',val[2],'\t\t\t',val[0]])
                        spiderMissModule.append(str_spiderMissModule)
                    else :
                        pass
                   
        ret_list=[ac,bc,bs,buildMissModule,spiderMissModule]
        
        return ret_list

def main():
    EntryDemo().mainloop()

if __name__=="__main__":
    
    print 'start'
    main()
