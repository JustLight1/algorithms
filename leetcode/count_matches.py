"""
Easy
Topics
Companies
Hint
You are given an array items, where each items[i] = [typei, colori, namei] 
describes the type, color, and name of the ith item. You are also given a rule 
represented by two strings, ruleKey and ruleValue.

The ith item is said to match the rule if one of the following is true:

ruleKey == "type" and ruleValue == typei.
ruleKey == "color" and ruleValue == colori.
ruleKey == "name" and ruleValue == namei.
Return the number of items that match the given rule.
"""


def countMatches(items, rulekey, rulevalue):
        rule_mapping = {
            "type": 0,
            "color": 1,
            "name": 2,
        }
        ret = 0
        for item in items:
            print(item)
            idx = rule_mapping[rulekey]
            if item[idx] == rulevalue:
                ret += 1
        
        return ret
