class Solution:
    def minimumTime(self, jobs: List[int], workers: List[int]) -> int:
        # Sort both the arrays
        jobs.sort()
        workers.sort()
        ans = 0

        # Find the length to iterate through both
        job_lenth = len(jobs)

        for i in range(job_lenth):
            days = jobs[i]
            capacity = workers[i]

            # If workers are more or equal to jobs
            if capacity >= days:
                ans = max(ans, 1)
            else:
                # If workers are less than jobs so get multiplier
                total_days = (days // capacity) if (days % capacity) == 0 else (days // capacity) + 1
                ans = max(ans, total_days)
        return ans

