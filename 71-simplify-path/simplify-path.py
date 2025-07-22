class Solution:
    def simplifyPath(self, path: str) -> str:
        folder_list = path.split("/")

        prefix  = "/"
        ans = []

        for folder in folder_list:
            # print("pre", folder, "-->", ans)
            if ".." == folder and len(ans) >= 1:
                ans.pop()
            elif ".." == folder and len(ans) < 1:
                continue
            elif "." == folder or folder == '':
                continue
            else:
                ans.append(folder)
            # print("post", folder, "-->", ans)

        return "/" + "/".join(ans)