#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int contrast(int ans[]);
int main(){
	int ans[4],input[4],count=0,A=0,B=0,i,j;
	srand(time(NULL));
	do{
		for(i=0;i<4;i++)
			ans[i]=rand()%10;
		//printf("%d",contrast(ans));
	}while(contrast(ans)==0);
	printf("Ans:");
	for(i=0;i<4;i++)
		printf("%d",ans[i]);
	printf("\n");
	do{
		A=0;B=0;
		printf("請輸入四個數字:");
		scanf("%1d%1d%1d%1d",&input[0],&input[1],&input[2],&input[3]);
		while(contrast(input)==0){
			printf("輸入錯誤請重新輸入!!!\n請輸入四個數字:");
			scanf("%1d%1d%1d%1d",&input[0],&input[1],&input[2],&input[3]);
		}
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				if(input[i]==ans[i]){
					A++;break;
				}
				if(input[j]==ans[i]) 
					B++;
			}
		}
		count++;
		if(A!=4)
		printf("%dA%dB\n",A,B);
	}while(A!=4);
	printf("恭喜答對! 共答了%d次",count);
	return 0;
}
int contrast(int x[]){
	int i,j;
	for(i=0;i<4;i++){
		for(j=0;j<4;j++){
			if(i!=j){
				if(x[i]==x[j]){
					return 0;
				}
			}	
		}
	}
	return 1;
}

