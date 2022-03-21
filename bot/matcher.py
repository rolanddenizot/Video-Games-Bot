from .patterns import patterns
import re


def matchPattern(str):
    matched = [
        item for item in patterns
        if re.search(item["pattern"],str,re.IGNORECASE)
    ]
    
    if (matched):
        return {
            'intent': matched[0]['intent'],
            'entities': createEntities(str, matched[0]['pattern'])
        }

        return ''


def createEntities(str, pattern):
    aa=re.compile("(?i)"+pattern)
    return aa.search(str).groupdict()