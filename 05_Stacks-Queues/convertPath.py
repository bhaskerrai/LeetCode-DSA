'''
Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system, convert it to the simplified canonical path.

In a Unix-style file system, a period '.' refers to the current directory, a double period '..' refers to the directory up a level, and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'. For this problem, any other format of periods such as '...' are treated as file/directory names.

The canonical path should have the following format:

The path starts with a single slash '/'.
Any two directories are separated by a single slash '/'.
The path does not end with a trailing '/'.
The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')
Return the simplified canonical path.

 

Example 1:

Input: path = "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.

'''

# def simplifyPath(path: str) -> str:
#     stack = []

#     for s in path:
#         print("\nabhi esko dekheinge:", s)

#         if s == ".":
#             # print("if chala")
#             if stack and stack[-1] == ".":
#                 while len(stack) != 1:
#                     # print("while chala")
#                     stack.pop()
#                     # print(stack)
            
#             else:
#                 stack.append(s)
#                 # continue


#         elif stack and s == "/":
#             # print("elif chala")
#             if stack[-1] == "/":
#                 # stack.append(s)
#                 continue
#             elif stack[-1] == ".":
#                 while stack[-1] != "/":
#                     print("hahk")
#                     stack.pop()
#             else:
#                 stack.append(s)
            
    
#         else:
#             # print("else chala")
#             stack.append(s)

#         print(stack)


#     if len(stack) > 1 and ( stack[-1] == "/" or stack[-1] == "." ):
#         stack.pop()

#     return "".join(stack)




def simplifyPath(path: str) -> str:
    stack = []
    path = path.split("/")

    # for s in path:
    #     if s != "":
    #         if s == ".":
    #             continue

    #         elif s == "..":
    #             if stack:
    #                 stack.pop()
    #             else:
    #                 continue

    #         else:
    #             stack.append(s)

    for s in path:
        if s == "..":
            if stack:
                stack.pop()
        
        elif s == "." or not s:  # if "." or an empty string
            continue

        else:
            stack.append(s)
    
    return "/" + "/".join(stack)


print(simplifyPath("/home/"))
print(simplifyPath("/../"))
print(simplifyPath("/home//foo/"))
print(simplifyPath("/a/../../b/../c//.//"))
print(simplifyPath("/a//b////c/d//././/.."))

