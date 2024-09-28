class Solution(object):
    def countAndSay(self, n: int) -> str:
        """
        :type n: int
        :rtype: str
        4 -> 1211
        """

        result = "1"
        for i in range(n-1):
            result = self.get_rle(result)
        return result
    
    def get_rle(self, text: str) -> str:
        last_ch = text[0]
        count = 0
        result = ""
        for ch in text:
            if ch == last_ch:
                count += 1
            else:
                result += f"{count}{last_ch}"
                count = 1
                last_ch = ch
        return result + f"{count}{last_ch}"

if __name__ == "__main__":
    print(Solution().countAndSay(4))

    