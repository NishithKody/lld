"""
class HtmlHelper:
    # @param (string)
    # @return (list)
    @classmethod
    def parseUrls(url):
        # Get all urls from a webpage of given url. 
"""

from collections import deque
class Solution:
    """
    @param url(string): a url of root page
    @return (list): all urls
    """      

    def get_host(self, url):
        rem_https = url[7:]
        return rem_https.split('/')[0]

    def crawler(self, url):
        visit = set()
        url_q = deque()
        url_q.append(url)
        host_url = self.get_host(url)

        while(len(url_q)>0):
            cur_url = url_q.popleft()
            if(cur_url in visit):
                continue
            
            visit.add(cur_url)
            urls_in_cur_page = HtmlHelper.parseUrls(cur_url)

            for url in urls_in_cur_page:
                if(self.get_host(url) == host_url):
                    url_q.append(url)
        
        return list(visit)
    