# Shadowrocket-Config-to-QRcode
将shadowsocks小飞机的配置文件gui-config.json转换成二维码，以便手机端快速扫码添加配置
---
https://blog.csdn.net/lecepin/article/details/52063843
---
配置文件包含以下几个信息
```
"server" : "",     // 服务器地址，也就是hostname
"server_port" : ,  // 服务端口
"password" : "",   // 密码
"method" : "",     // 加密方式
"remarks" : ""     // 备注
```
配置文件的二维码信息格式如下
`ss://Base64(method[-auth]:password@hostname:port/#Base64(remark))`
其中*Base64()*表示对字符串进行Base64编码，需要注意的是remark信息先单独进行一次Base64编码后，拼接在前面其他的信息后，整体再编码一次。
