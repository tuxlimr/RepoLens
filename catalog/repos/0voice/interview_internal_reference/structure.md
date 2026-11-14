# Project structure: 0voice/interview_internal_reference

**Analysed commit:** `a549376da3ff8430a03e00ad7e1878ca00a063ad`

**Commit reference:** [a549376da3ff8430a03e00ad7e1878ca00a063ad](https://github.com/0voice/interview_internal_reference/commit/a549376da3ff8430a03e00ad7e1878ca00a063ad)

**Tree at this commit:** [0voice/interview_internal_reference@a549376da3ff](https://github.com/0voice/interview_internal_reference/tree/a549376da3ff8430a03e00ad7e1878ca00a063ad)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | 0voice/interview_internal_reference |
| Description | 2025年最新总结，阿里，腾讯，百度，美团，头条等技术面试题目，以及答案，专家出题人分析汇总。 |
| Stars | 37251 |
| Forks | 9286 |
| Licence | Not detected |
| Language | Python |
| Default branch | master |
| Analysed commit | `a549376da3ff8430a03e00ad7e1878ca00a063ad` |
| Retrieved at | 2026-11-14T19:06:49.236658+00:00 |
| Files in this snapshot | 154 |

## Directory tree

```text
01.阿里篇/  (30 files)
  .gitkeep
  1.1.1 如何实现一个高效的单向链表逆序输出？.md
  1.1.2 已知sqrt(2)约等于1.414，要求不用数学库，求sqrt(2)精确到小数点后10位.md
  1.1.3 给定一个二叉搜索树(BST)，找到树中第 K 小的节点.md
  1.1.4 LRU缓存机制.md
  1.1.5 关于epoll和select的区别，以下哪些说法是正确的.md
  1.1.6 从innodb的索引结构分析，为什么索引的 key 长度不能太长.md
  1.1.7 MySQL的数据如何恢复到任意时间点？.md
  1.1.8 NFS与SMB的区别？.md
  1.1.9 输入 ping IP 后敲回车，发包前会发生什么？.md
  1.2.0 请解释下为什么鹿晗发布恋情的时候，微博系统会崩溃，如何解决？.md
  1.2.1 现有一批邮件需要发送给订阅顾客，且有一个集群（集群的节点数不定，会动态扩容缩容）来负责具体的邮件发送任务，如何让系统尽快地完成发送？.md
  1.2.2 有一批气象观测站，现需要获取这些站点的观测数据，并存储到 Hive 中。但是气象局只提供了 api 查询，每次只能查询单个观测点。那么如果能够方便快速地获取到所有的观测点的数据？.md
  1.2.3 如何实现两金额数据相加（最多小数点两位）.md
  1.2.4 关于并行计算的一些基础开放问题.md
  1.2.5 请计算XILINX公司VU9P芯片的算力相当于多少TOPS，给出计算过程与公式.md
  1.2.6 一颗现代处理器，每秒大概可以执行多少条简单的MOV指令，有哪些主要的影响因素.md
  1.2.7 请分析 MaxCompute 产品与分布式技术的关系、当前大数据计算平台类产品的市场现状和发展趋势.md
  1.2.8 对大数据平台中的元数据管理是怎么理解的，元数据收集管理体系是怎么样的，会对大数据应用有什么样的影响.md
  1.2.9 你理解常见如阿里，和友商大数据平台的技术体系差异以及发展趋势和技术瓶颈，在存储和计算两个方面进行概述.md
  1.3.0 在云计算大数据处理场景中，每天运行着成千上万的任务，每个任务都要进行 IO 读写.md
  1.3.1 最大频率栈.md
  1.3.2 给定一个链表，删除链表的倒数第N个节点，并且返回链表的头结点.md
  1.3.3 如果让你设计一个通用的、支持各种数据库秒级备份和恢复的系统，你会如何设计.md
  … 6 more files
02.华为篇/  (13 files)
  .gitkeep
  2.1.1 static有什么用途？（请至少说明两种）.md
  2.1.2 引用与指针有什么区别？.md
  2.1.3 描述实时系统的基本特性.md
  2.1.4 全局变量和局部变量在内存中是否有区别？如果有，是什么区别？.md
  2.1.5 什么是平衡二叉树？.md
  2.1.6 堆栈溢出一般是由什么原因导致的？.md
  2.1.7 什么函数不能声明为虚函数？.md
  2.1.8 冒泡排序算法的时间复杂度是什么？.md
  2.1.9. Internet采用哪种网络协议？该协议的主要层次结构？.md
  2.2.0 IP地址的编码分为哪俩部分？.md
  2.2.1 用户输入M,N值，从1至N开始顺序循环数数，每数到M输出该数值，直至全部输出。写出C程序.md
  2.2.2 某32位系统下, C++程序，请计算sizeof 的值.md
03.百度篇/  (3 files)
  .gitkeep
  3.4.8 找出数组中出现次数超过一半的数，现在有一个数组，已知一个数出现的次数超过了一半，请用O(n)的复杂度的算法找出这个数。.md
  3.4.9 找出被修改过的数字.md
04.腾讯篇/  (1 files)
  .gitkeep
05.美团篇/  (2 files)
  .gitkeep
  5.2.0 浅复制和深复制？怎样实现深复制？.md
06.头条篇/  (2 files)
  .gitkeep
  一棵二叉树，求最大通路长度（即最大左右子树高度之和）.md
07.滴滴篇/  (1 files)
  .gitkeep
08.京东篇/  (2 files)
  .gitkeep
  简单说一下hadoop和spark的shuffle过程.md
09.MySQL篇/  (11 files)
  .gitkeep
  9.1.0 主键 超键 候选键 外键.md
  9.1.1 数据库事务的四个特性及含义.md
  9.1.2 视图的作用，视图可以更改么？.md
  9.1.3 drop,delete与truncate的区别.md
  9.1.4 索引的工作原理及其种类.md
  9.1.5 连接的种类.md
  9.1.6 数据库范式.md
  9.1.7 数据库优化的思路.md
  9.1.8 存储过程与触发器的区别.md
  9.1.9 解释 SQL 的 left join 和 right join.md
10.Redis篇/  (11 files)
  .gitkeep
  10.1.0 使用Redis有哪些好处？.md
  10.1.1 redis相比memcached有哪些优势？.md
  10.1.2 redis常见性能问题和解决方案.md
  10.1.3 MySQL里有2000w数据，redis中只存20w的数据，如何保证redis中的数据都是热点数据.md
  10.1.3 zookeeper的四种类型的znode.md
  10.1.4 Memcache与Redis的区别都有哪些？.md
  10.1.5 Redis 常见的性能问题都有哪些？如何解决？.md
  10.1.6 redis最适合的场景.md
  10.1.7 Redis的同步机制了解么？.md
  10.1.8 是否使用过Redis集群，集群的原理是什么？.md
11.MongoDB篇/  (48 files)
  .gitkeep
  11.1.0 什么是MongoDB？.md
  11.1.1 MongoDB是由哪种语言写的？.md
  11.1.2 MongoDB的优势有哪些？.md
  11.1.3 什么是数据库？.md
  11.1.4 什么是集合？.md
  11.1.5 什么是文档？.md
  11.1.6 MongoDB和关系型数据库术语对比图.md
  11.1.7 什么是“mongod”？.md
  11.1.8 “mongod”参数有什么？.md
  11.1.9 什么是“mongo”？.md
  11.2.0 MongoDB哪个命令可以切换数据库？.md
  11.2.1 什么是非关系型数据库？.md
  11.2.2 非关系型数据库有哪些类型？.md
  11.2.3 为什么用MOngoDB？.md
  11.2.4 在哪些场景使用MongoDB？.md
  11.2.5 MongoDB中的命名空间是什么意思.md
  11.2.6 哪些语言支持MongoDB.md
  11.2.7 在MongoDB中如何创建一个新的数据库？.md
  11.2.8 在MongoDB中如何查看数据库列表？.md
  11.2.9 MongoDB中的分片是什么意思？.md
  11.3.0 如何查看使用MongoDB的连接？.md
  11.3.1 什么是复制？.md
  11.3.2 在MongoDB中如何在集合中插入一个文档？.md
  … 24 more files
12.Zookeeper篇/  (20 files)
  .gitkeep
  12.1.0 zookeeper是什么？.md
  12.1.1 zookeeper提供了什么？.md
  12.1.2 zookeeper文件系统.md
  12.1.3 zookeeper的四种类型的znode.md
  12.1.4 zookeeper通知机制.md
  12.1.5 zookeeper有哪些应用场景？.md
  12.1.6 zk的命名服务.md
  12.1.7 zk的配置管理服务.md
  12.1.8 zk的集群管理.md
  12.1.9 zk的分布式锁.md
  12.2.0 zk队列管理.md
  12.2.1 zk数据复制.md
  12.2.2 zk中zab的工作原理.md
  12.2.3 zk是如何保证事务的顺序一致性.md
  12.2.4 zk集群下server工作状态.md
  12.2.5 zk是如何选举Leader的？.md
  12.2.6 zk同步流程.md
  12.2.7 分布式通知和协调.md
  12.2.8 zk的session机制.md
13.Nginx篇/  (1 files)
  .gitkeep
14.算法篇/  (1 files)
  .gitkeep
15.内存篇/  (1 files)
  .gitkeep
16.CPU篇/  (1 files)
  .gitkeep
17.磁盘篇/  (1 files)
  .gitkeep
18.网络通信篇/  (1 files)
  .gitkeep
19.安全篇/  (1 files)
  .gitkeep
20.并发篇/  (1 files)
  .gitkeep
21.面经/  (1 files)
  2020秋招面经总结.md
sync_link
```

## Entry points

No application entry point was observed at this commit.

## Main components

No components were identified from the analysed files.

## Important files

No manifest, config, CI, or container files were observed in the analysed set.

## Top-level layout

- `11.MongoDB篇` — 48 analysed file(s)
- `01.阿里篇` — 30 analysed file(s)
- `12.Zookeeper篇` — 20 analysed file(s)
- `02.华为篇` — 13 analysed file(s)
- `09.MySQL篇` — 11 analysed file(s)
- `10.Redis篇` — 11 analysed file(s)
- `03.百度篇` — 3 analysed file(s)
- `05.美团篇` — 2 analysed file(s)
- `06.头条篇` — 2 analysed file(s)
- `08.京东篇` — 2 analysed file(s)
- `(root files)` — 1 analysed file(s)
- `04.腾讯篇` — 1 analysed file(s)
- `07.滴滴篇` — 1 analysed file(s)
- `13.Nginx篇` — 1 analysed file(s)
- `14.算法篇` — 1 analysed file(s)
- `15.内存篇` — 1 analysed file(s)
- `16.CPU篇` — 1 analysed file(s)
- `17.磁盘篇` — 1 analysed file(s)
- `18.网络通信篇` — 1 analysed file(s)
- `19.安全篇` — 1 analysed file(s)
- `20.并发篇` — 1 analysed file(s)
- `21.面经` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `a549376da3ff8430a03e00ad7e1878ca00a063ad` is the revision these paths and observations refer to.
