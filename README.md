# AutoScript
一些自动化脚本，让机器代替人做一些"fucking things"。

# 脚本列表：     
## 一、hostloc：自动踢楼脚本 (for www.hostloc.com)    

  介绍：C大经常开金盾, So浏览器渲染; 由于hostloc服务器老是502,或由于"网络的不确定性",So 踢中为止    
        
  使用：  
     
 ```
 【for Centos】
 sudo yum -y install epel-release
 sudo yum -y install python-pip
 sudo yum clean all
 sudo pip install lxml
 sudo pip install selenium
 【for Ubuntu/Debian】
 sudo apt-get -y install python-pip
 sudo apt-get install libfontconfig
 sudo pip install lxml
 sudo pip install selenium
 【run script】
 python hostloc.py 踢楼地址 踢楼楼层 踢楼口号 账户 密码
  ```       
      
## 二、未完待续    
