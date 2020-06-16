class Solution:
    def validIPAddress(self, IP: str) -> str:
        import re
        if "." in IP:
            return self.ipv4(IP)
        elif ":" in IP:
            return self.ipv6(IP)
        else:
            return "Neither"
        
    def ipv4(self, IP):
        
        pattern = re.compile("^([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$")
        if len(IP.split(".")) == 4:
            for i in IP.split("."):
                if not pattern.match(i):
                    return "Neither"
        else:
            return "Neither"
        return "IPv4"
    
    
    def ipv6(self, IP):
        
        pattern = re.compile("^([0-9a-fA-F]{1,4})$")
        if len(IP.split(":")) == 8:
            for i in IP.split(":"):
                if not pattern.match(i):
                    return "Neither"
        else:
            return "Neither"
        return "IPv6"