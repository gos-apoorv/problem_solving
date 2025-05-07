class Solution {
    public int minimumTime(int[] jobs, int[] workers) {

        // Sorth both the array in ascending order
        Arrays.sort(jobs);
        Arrays.sort(workers);

        int maxJobDays = 0;
        int currentJobDays = 0;

        // Iterate through both the arrays
        for(int i =0 ; i<jobs.length; i++){
            // This helps to get the days required for workers even in workers are greater than jobs
            // Or even if its a multiplication factor of jobs
            currentJobDays = (jobs[i]+workers[i]-1)/workers[i];
            maxJobDays = Math.max(maxJobDays, currentJobDays);
        }

        return maxJobDays;
        
    }
}