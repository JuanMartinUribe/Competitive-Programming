class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        bit = 0
        bitmap = collections.defaultdict(bool)
        dev_skills = collections.defaultdict(set)
        for skill in req_skills:
            bitmap[skill] = 2**bit
            bit+=1
        
        for dev,skills in enumerate(people):
            for skill in skills:
                dev_skills[dev].add(skill)
        cache = {}
        def backtrack(i,skillmask):
            if (i,skillmask) in cache:
                return cache[(i,skillmask)]
            if skillmask == 2**len(req_skills)-1:
                return []
            if i == len(people):
                return [0]*61
            incl_skillmask = skillmask
            for skill in dev_skills[i]:
                if skill in bitmap:
                    incl_skillmask |= bitmap[skill]
            included = backtrack(i+1,incl_skillmask)+[i] if incl_skillmask!=skillmask and incl_skillmask!=0 else [0]*61
            not_included = backtrack(i+1,skillmask)
            cache[(i,skillmask)] = min(included,not_included,key = lambda f:len(f))
            return cache[(i,skillmask)]
        return backtrack(0,0) 
