# workflows
Alfred 的workflows 备份，可以在[AlfredWorkflow](http://alfredworkflow.com/)上找到很多好玩的workflow，知乎上有篇[文章](https://www.zhihu.com/question/20656680)对这部分做了很好的说明。

### 使用的workflow说明
#### UTF8Codec
- ec 对字符进行url encode
- dc 对字符进行url decode

#### 有道翻译加强版
- 有道翻译API: 
    + [申请地址](http://fanyi.youdao.com/openapi?path=data-mode)
    + API key：1070404396
    + keyfrom：DevlxFY
    
- `yd boost` ，对xxx进行翻译，可以智能识别中英文
- `yd boost say`，输入say指令，即可朗读单词或句子（中文不可朗读）。
- `yd boost add` ，将单词添加到自己的单词本，需要先设置网易账号：
    + 在Run Script下的php脚本中进行设置，内部有中文提示。
- 查不到翻译结果回车会到网站查询

### wrokflow制作说明
- 使用script filter出现无法回车添加到粘贴板的问题。

#### pac-helper
先在里面将对应的pac地址配上，然后执行如下命令：
- pac 1
- pac 2

#### QuickDNS
快速的切换DNS
- `dns 114` 等等

#### Domain Searcher
查询域名有没有被人申请。 此workflow反应比较慢，应该改为在输入时取消掉之前的请求，只执行最新的请求。
- `dm devlxx.com` 查询devlxx.com是否被占用
- `dmx devlxx.com` 查询所有后缀的域名是否被占用
