#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MakeIndex.py - 自动生成学习资源索引

该脚本用于遍历docs/Study/assert目录下的所有文件夹，
并自动生成对应的索引到docs/Study/index.md文件中，
同时在每个学习资料文件夹下也自动创建对应的index.md文件。
索引包含文件夹卡片和详细的PDF文件列表。

使用方法：
    python MakeIndex.py

作者：AI助手
日期：2024
"""
import os

# 确保中文显示正常
import sys
if sys.version_info[0] < 3:
    reload(sys)
    sys.setdefaultencoding('utf-8')

# 定义项目根目录
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
# 定义assert文件夹路径
ASSERT_DIR = os.path.join(ROOT_DIR, 'assert')
# 定义index.md文件路径
INDEX_FILE = os.path.join(ROOT_DIR, 'index.md')


def get_folder_icon(folder_name):
    """根据文件夹名称返回对应的FontAwesome图标"""
    icon_map = {
        'cs': 'code',              # 计算机科学使用代码图标
        'math': 'calculator',      # 数学使用计算器图标
        'physics': 'atom',         # 物理使用原子图标
        'english': 'language'      # 英语使用语言图标
    }
    return icon_map.get(folder_name.lower(), 'folder')  # 默认使用文件夹图标


def generate_index():
    """生成索引内容，包括文件夹卡片和详细的文件列表"""
    # 初始化索引内容，包含YAML前端元数据和页面标题
    index_content = [
        '---',
        'title: 学习经验分享',
        'comments: true',
        'template: main.html',
        '---',
        '',
        '这里是中国科学技术大学计算机科学与技术学院辩论队的学习经验分享页面！',
        '',
        '## 学习资源索引',
        '<div class="grid cards" markdown>',
    ]
    
    # 获取assert目录下的所有文件夹并按名称排序
    folders = [f for f in os.listdir(ASSERT_DIR) if os.path.isdir(os.path.join(ASSERT_DIR, f))]
    
    # 为每个文件夹生成卡片链接
    for folder in sorted(folders):
        folder_path = os.path.join(ASSERT_DIR, folder)
        icon = get_folder_icon(folder)
        index_content.append(f'* [:fontawesome-solid-{icon}:  {folder}学习资料](assert/{folder}/)')
    
    index_content.append('</div>')
    index_content.append('')
    
    # 为每个文件夹生成详细内容部分
    for folder in sorted(folders):
        folder_path = os.path.join(ASSERT_DIR, folder)
        files = [f for f in os.listdir(folder_path) if f.endswith('.pdf')]
        
        index_content.append(f'## {folder}学习资料详情')
        index_content.append('')
        
        if files:
            # 如果文件夹中有PDF文件，列出所有文件
            for file in sorted(files):
                # 移除文件扩展名作为链接文本
                file_name = os.path.splitext(file)[0]
                # Markdown中不需要转义括号，保留原始文件名即可
                index_content.append(f'* [{file_name}](assert/{folder}/{file})')
        else:
            # 如果文件夹为空，显示提示信息
            index_content.append('* 暂无学习资料，敬请期待...')
            
        index_content.append('')
        
    return '\n'.join(index_content)


def write_index(content):
    """将索引内容写入index.md文件"""
    with open(INDEX_FILE, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'已成功更新索引文件: {INDEX_FILE}')


def generate_folder_index(folder_path, folder_name):
    """为每个学习资料文件夹生成对应的index.md文件"""
    # 构建文件夹下的index.md路径
    folder_index_file = os.path.join(folder_path, 'index.md')
    
    # 获取文件夹下的所有PDF文件
    files = [f for f in os.listdir(folder_path) if f.endswith('.pdf')]
    
    # 初始化文件夹索引内容
    folder_index_content = [
        '---',
        f'title: {folder_name}学习资料',
        'comments: true',
        'template: main.html',
        '---',
        '',
        f'# {folder_name}学习资料',
        '',
    ]
    
    # 如果文件夹中有PDF文件，列出所有文件
    if files:
        folder_index_content.append('## 资料列表')
        folder_index_content.append('')
        for file in sorted(files):
            # 移除文件扩展名作为链接文本
            file_name = os.path.splitext(file)[0]
            folder_index_content.append(f'* [{file_name}]({file})')
    else:
        # 如果文件夹为空，显示提示信息
        folder_index_content.append('## 资料列表')
        folder_index_content.append('')
        folder_index_content.append('* 尚在完善中...')
    
    # 写入文件夹下的index.md文件
    with open(folder_index_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(folder_index_content))
    print(f'已成功创建文件夹索引: {folder_index_file}')


if __name__ == '__main__':
    print('开始生成学习资源索引...')
    
    # 生成主索引文件
    index_content = generate_index()
    write_index(index_content)
    
    # 获取assert目录下的所有文件夹并按名称排序
    folders = [f for f in os.listdir(ASSERT_DIR) if os.path.isdir(os.path.join(ASSERT_DIR, f))]
    
    # 为每个文件夹生成index.md文件
    for folder in sorted(folders):
        folder_path = os.path.join(ASSERT_DIR, folder)
        generate_folder_index(folder_path, folder)
    
    print('所有索引生成完成！')