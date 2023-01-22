"""Creates the proverb from the input list provided"""

def proverb(*ip_list, qualifier):
    """Creates the proverb from the input list provided"""
    ans_list = []
    if len(ip_list) >= 1:
        for item in range(0,len(ip_list) -1 ):
            ans_list.append(f"For want of a {ip_list[item]} the {ip_list[item + 1]} was lost.")
        ans_list.append(f"And all for the want of a {ip_list[0]}.")
    if qualifier:
        ans_list[-1] = f"And all for the want of a {qualifier} {ip_list[0]}."

    return ans_list
