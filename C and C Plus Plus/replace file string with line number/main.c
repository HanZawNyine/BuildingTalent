#include <stdio.h>

int main() {
    printf("Exam Question for file handling and pointer\n");
    printf("*********************************************************\n");
    char fileName[50]="hzn.txt",allData[100],replaceValueLine[50]="Hello Baby";
    int lineNUmber=0,
    NofValue[50];
    char SecondHalf[50];
    int ch=0;char cp;
    printf("Input the file name to be opened : ");
    scanf("%s",fileName);

    printf("Input the line no you want to replace : ");
    scanf("%d",&lineNUmber);
    //printf("%s\n",fileName);
    FILE *fptr;FILE *overPtr;


    fptr= fopen(fileName,"r+");
    if(fptr != NULL){
        int i=0,j=0;
        while(cp!=EOF){
            cp = fgetc(fptr);
            //printf("%c",cp);
            allData[i]= cp;

            if(cp=='\n'){
                ch++;
                //printf("%d ",ch);
                NofValue[j]=i;
              //  printf("a ... %d\n",NofValue[j]);
                //printf("n indexes : %d\n",i);
                j++;
            }
            i++;

        }
       printf("line of numbers : %d\n",ch);
           //printf("Data : \nn%s\n",allData);
       printf("replace Line Number : %d\n",lineNUmber);
       printf("Start Number : %d\n",NofValue[lineNUmber-2]);
       printf("End Number : %d\n",NofValue[lineNUmber-1]);
       int iiii=0;
       int startValue=NofValue[lineNUmber-2];
       int endValue = NofValue[lineNUmber-1]+1;
       printf("End Value is : %d\n",endValue);

       startValue+= 1;
       printf("Replace starting : %d\n",startValue);

        int ggh=0;
        while(allData[endValue]!='\0'){

            SecondHalf[ggh] = allData[endValue];\
            ggh++;endValue++;
        }

       int leng = sizeof(replaceValueLine) / sizeof(replaceValueLine[0]);
       for(int zzzz=0;zzzz<=leng;zzzz++ ){
        allData[startValue]=replaceValueLine[iiii];
        startValue++;
        iiii++;
       }
       //printf("Replacing : %s\n",allData);

       printf("All Data : %s",allData);

       printf("\n%s",SecondHalf);

       //fgets(allData, sizeof(allData), stdin);

      // fprintf(fptr, "%s", allData);

     overPtr = fopen(fileName,"w");
    fprintf(overPtr, "%s\n%s", allData,SecondHalf);

    fclose(overPtr);

    }else{
        printf("error");
    }
    fclose(fptr);

    return 0;
}
