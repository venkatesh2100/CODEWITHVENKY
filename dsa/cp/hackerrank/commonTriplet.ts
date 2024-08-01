function compareTriplets(a: number[], b: number[]): number[] {
  const newArr: number[] = [0,0];
  for (let i = 0; i <3; i++) {
      if (a[i] > b[i]) {
          newArr[0] +=1;
      }else if(a[i]<b[i]){
          newArr[1]+=1;
      }
  }

  return newArr;
}