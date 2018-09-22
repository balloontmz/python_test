# -*- coding: utf -8 -*-
import hashlib

class YHash(object):
    def __init__(self, nodes = None, n_number = 3):
        """
            一致性hash算法指的是虚拟节点到物理节点的映射是闭合的圆环
           :param nodes:       所有的节点
           ：param n_number:   一个节点对应多少哥虚拟节点
           ：return：
        """
        self._n_number = n_number
        self._node_dict = dict()
        self._sort_list = []
        if nodes:
            for node in nodes:
                self.add_node(node)

    def add_node(self, node):
        """
        添加node,首先根据虚拟节点的数目，创建所有的虚拟节点，并将其与对应的node对应起来
        当然还需要将虚拟节点的hash值放在排序里面
        这里在添加节点之后，需要保持虚拟节点hash值的顺序
        :param node:
        :return:
        """
        for i in range(self._n_number):
            node_str = '%s%s' % (node, i)
            key = self._gen_key(node_str)
            self._node_dict[key] = node
            self._sort_list.append(key)
        self._sort_list.sort()

    def remove_node(self, node):
        """
        这是一个节点的退出，需要将这个节点的所有虚拟节点都删除
        :param node:
        :return:
        """
        for i in range(self._n_number):
            node_str = '%s%s' % (node, i)
            key = self._gen_key(node_str)
            del self._node_dict[key]
            self._sort_list.remove(key)

    def get_node(self, key_str):
        """
        返回这个字符串应该对应的node，这里先求出字符串的hash值，然后找到第一个小于等于的虚拟节点，然后返回node
        如果hash值大于所有节点，那么用第一个虚拟节点
        :param key_str:
        :return:
        """
        if self._sort_list:
            key = self._gen_key(key_str)
            for node_key in self._sort_list:
                if key <= node_key:
                    return self._node_dict[node_key]
                return self._node_dict[self._sort_list[0]]
        else:
            return None

    @staticmethod
    def _gen_key(key_str):
        """
        通过key,返回当前key的hash值，这里采用md5
        :param key_str:
        :return:
        """
        md5_str = hashlib.md5(key_str.encode('utf8')).hexdigest()
        return int(md5_str, 16)


fjs=YHash(['127.0.0.1', '192.168.1.1'])
print(fjs.get_node('fjs32121'))
