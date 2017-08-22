### XXNote设计
#### 简易版本
限定死只支持一级目录，目录下只有文件没有文件夹。
- `bj *`或者`bj 两个空格` 查询目录下所有的文件
- `bj xxx` 查询指定文件
- `xjbj xxx` 在指定目录下创建文件xxx,并用sublime打开
    + sublime需要提供命令行支持？ 
- `scbj xxxx` 回车后执行git add . && git commit -m 'xxxx' && git push origin master，并且通知上传情况。
- `gxbj xxxx` 从git服务器更新笔记, git pull
- `bjml` 打开笔记目录


#### 复杂版本


    - bj  打开指定目录下的所有文件，回车进入下一级，如果是文本，则直接sublime打开
        + 查询目录下的所有文件，并将结果返回
    - xjbj  {name} 在指定目录下用sublime创建一个新的笔记并且添加后缀.md
    - scbj 将指定目录下的笔记上传git
    - gxbj 从git服务器更新笔记