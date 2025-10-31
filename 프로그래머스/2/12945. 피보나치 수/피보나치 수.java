class Solution {
    public int solution(int n) {
        int answer = 0;
        int k = 3;
        int fi[] = new int[n+1];
        
        fi[0] = 0;
        fi[1] = 1;
        fi[2] = 1;
        
        while(k<=n){
            fi[k] = (fi[k-1] + fi[k-2] + 1234567) % 1234567;
            if(fi[k] == 1234567){
                fi[k] = 0;
            }
            
            k+=1;
        }
        
        answer = (fi[n]);
        
        return answer;
    }
}