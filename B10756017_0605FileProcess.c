#include <stdio.h>
#include <stdlib.h>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */
struct node{
	int id;
	int data;
	struct node *next;
};
typedef struct node NODE;
NODE *first,*before,*now;
int num;
void b_sort(){
	NODE *temp;
	int i,j;
	for(i=num;i>=1;i--){
		now=first;
		for(j=1;j<i;j++){
			temp=now->next;
			if(now->data<temp->data){
				int a = now->data;
				now->data=temp->data;
				temp->data=a;
				int b = now->id;
				now->id=temp->id;
				temp->id=b;
			}
			now=now->next;
		}
	}
}
int main(int argc, char *argv[]) {
	FILE *fin,*fout;
	char ch;
	int i;
	fin = fopen("text.txt","r");
	fout = fopen("out.txt","w+t");
	printf("輸入資料筆數");
	scanf("%d",&num);
	/*if(fin!=NULL && fout!=NULL){
		while((ch=getc(fin))!=EOF) OR while(!feof(fin)){
			putc(ch,fout);//將字串ch寫入檔案fout 
		}
	}
	else{
		printf("檔案讀取失敗");
		return 0;
	}*/	
	for(i=1;i<=num;i++){
		fscanf(fin,"%d\n",&ch);
		now=(NODE*)malloc(sizeof(NODE));
		now->id=i;
		now->data=ch;
		if(i==1){
			first=now;
		}
		else{
			before->next=now;
		}
		before=now;now->next=NULL;
	}
	b_sort();
	now=first;
	while(now!=NULL){
		printf("%d,%2d\n",now->id,now->data);
		int a=now->id,b=now->data;
		fprintf(fout,"%d,%2d\n",a,b);
		now=now->next;
	}
	fclose(fin);
	fclose(fout);
	system("pause");
	return 0;
}

