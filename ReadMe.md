---
title: USTC-CS-DEBATE仓库说明
---
## 说明
这是中国科学技术大学计算机科学与技术学院辩论队github仓库。

## 配置环境
在windows下下载mkdocs库，
```shell
pip install mkdocs
pip install mkdocs-material
pip install mkdocs-material-extensions
```
## mkdocs使用入门：
```shell
mkdocs serve #实时预览
mkdocs build #生成静态文件
mkdocs gh-deploy #将静态文件作为gh-pages分支推送到远程
```
## git命令-推送和同步
```shell
git fetch origin main #拉取远程main分支
git merge #合并
```
```shell
git add . #在本地提交所有更改
git commit -m "变更的注释信息" #commit
git push origin main 