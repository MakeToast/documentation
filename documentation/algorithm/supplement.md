### 보충 : 데이터파일 읽어서 저장하기

- 구조체 정의
```
    typedef struct place{
        int index;
        char * state;
        char * name;
        double lon, lat;
        double distFromCapital;
    } Place;
```
- 포인터 배열
```
    #define MAX 40000
    Place * places[MAX];
```

- 전체 코드
```
#include <stdio.h>
#include "place.h"

#define MAX 40000
#define BUFFER_SIZE 1000

Place * places[MAX];
int n = 0;
char * fileName = "Alabama AL Distances.TXT";

void readData(char * name);
void rename(Place * p);

int main(){
    readData(fileName);
    return 0;
}

void readData(char * name){
    char buffer[BUFFER_SIZE];
    FILE * fp = fopen(fileName, "r");
    while(fgets(buffer, BUFFER_SIZE, fp) != NULL){

        Place * place = (Place *)malloc(sizeof(Place));
        char * p = strtok(buffer, "\t");
        place->state = strdup(p);
        p = strtok(NULL, "\t");
        place->name = strdup(p);
        p = strtok(NULL, "\t");
        place->lon = (double)atof(p);
        p = strtok(NULL, "\t");
        place->lat = (double)atof(p);
        p = strtok(NULL, "\t");
        place->disFromCapital = (double)atof(p);

        rename(place);

        places[n++] = place;
    }

    fclose(fp);
}

void rename(Place * p){
    int count = 0;
    for(int i = 0; i < n; i++){
        if (strncmp(p->name, places[i]->name, strlen(p->name)) == 0){
            count++;
        }
    }
    if(count > 0)
    {
        char namebuffer[BUFFER_SIZE];
        sprintf(namebuffer, "%s%d", p->name, (count+1));
        free(p->name);
        p->name = strdup(namebuffer);
    }
}
```