class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        events = [[start,True] for start,end in flowers] + [[end,False] for start,end in flowers]
        def tiebreak(x):
            return [x[0],0] if x[1] else [x[0],1]
        events.sort(key=tiebreak)
        people = sorted([[person,i] for i,person in enumerate(people)])
        cur_event = 0
        flowers = 0
        ans = [0]*len(people)
        for person,index in people:
            while cur_event<len(events) and (events[cur_event][0]<person or (events[cur_event][0]==person and events[cur_event][1])):
                flowers = flowers+1 if events[cur_event][1] else flowers-1
                cur_event+=1
            ans[index]=(flowers)
        return ans