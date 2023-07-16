class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        count = []
        for i in emails:
            a = i.split("@")
            a[0] = a[0].replace(".",'')
            if '+' in a[0]:
                e = a[0].split('+')
                a[0] = e[0]
            m = "@".join(a)
            if m not in count:
                count.append(m)
        return len(count)
                    

