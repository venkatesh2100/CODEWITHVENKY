function hourglassSum(arr: number[][]): number {
    // Write your code here
    let sum=0;
    for(let i=0;i<4;i++){
        for(let j=0;j<4;j++){
            const temp=arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2];
    if(i==0 && j==0){
   sum=temp; 
    }  else if(temp>sum){
    sum=temp;
   
    } 
    }
    }
    return sum;

}
