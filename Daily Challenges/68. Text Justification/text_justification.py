class Solution:
    def fullJustify(self, words: List[str], max_width: int) -> List[str]:
        def justify(line,width):
            if len(line)==1:
                return line[0]+(" "*(width-len(line[0])))
            spaces_amt = width-sum([len(w) for w in line])
            space_len,extra_space = divmod(spaces_amt,len(line)-1)
            ans = []
            for i,w in enumerate(line[:-1]):
                ans.append(w+(" "*space_len))
                if i+1<=extra_space:
                    ans[-1]+=" "
            return "".join(ans)+line[-1]
        ans = []
        cur_line = []
        cur_len = 0
        for word in words:
            if cur_len+len(word)+len(cur_line)<=max_width:
                cur_line.append(word)
                cur_len+=len(word)
            else:
                ans.append(justify(cur_line,max_width))
                cur_line = [word]
                cur_len = len(word)
        if cur_line:
            ans.append(justify(cur_line,max_width))
        last_line = []
        for w in ans[-1].split(" "):
            if w!="":
                last_line.append(w.replace(" ",""))
        ans[-1] = " ".join(last_line)
        ans[-1] += " "*(max_width-len(ans[-1]))
        return ans