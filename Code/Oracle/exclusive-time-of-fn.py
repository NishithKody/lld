class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        
        res = [0] * n
        call_stack = []
        cur_time = 0

        for log in logs:
            [fn, status, time] = log.split(':')

            fn = int(fn)
            time = int(time)

            if(status == 'start'):
                if(call_stack):
                    prev_fn = call_stack[-1]
                    res[prev_fn] += time - cur_time
                
                call_stack.append(fn)
                cur_time = time
            else:
                prev_fn = call_stack.pop()
                res[prev_fn] += time - cur_time + 1
            
                cur_time = time + 1
        
        return res           
