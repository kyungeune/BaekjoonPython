class Solution {
    public int solution(int n) { 
        int answer = 0;
        if(n==2){
            return 1;
        }
        // for문 
        int sum=0;  // sum값
        int k=n;  // k는 n부터 하나씩 작아지는 고정값
        int m = k;  // m은 더해야하는 값(유동)
        
        while(k>=1){
                sum+=m;
            
                if(sum==n){  // sum이 n과 같으면
                    answer+=1;
                    if(m==1){ // 근데 m의 값이 1이라 앞으로 더할 수 있는 숫자중에 제일 큰 숫자니까
                        return answer;
                    }
                    k-=1;  // 다음 k 순회
                    m = k; // m은 다시 하나씩 작아질것
                    sum=0; // sum 초기화
                }else if(sum>n){
                    k-=1;
                    m = k;
                    sum=0;
                }else{
                    if(m==1){ // 근데 m의 값이 1이라 앞으로 더할 수 있는 숫자중에 제일 큰 숫자인데도, sum보다 작단 얘기니까, 더이상 돌릴 가치가 없음
                    return answer;
                }
                    m-=1; // 계속 이어서 진행
                }
            
                
            }
            
        
        return answer;
    }
}