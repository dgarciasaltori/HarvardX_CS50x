#include <stdio.h>
#include <cs50.h>

void print_space(int n);
void print_hashtag(int n);


int main(void)
{
    int height, space, hashtag;
    do
    {
        height = get_int("What's the height of pyramid from 1 to 8?\n");
    }
    while(height < 1 || height > 8);

    space = height-1;
    hashtag=1;

    for(int i=0;i<height;i++)
    {
        print_space(space);
        print_hashtag(hashtag);
        printf("  ");
        print_hashtag(hashtag);
        printf("\n");
        space--;
        hashtag++;
    }
}




void print_space(int n)
{
    for(int i=0;i<n;i++)
    {
        printf(" ");
    }
}

void print_hashtag(int n)
{
    for(int i=0;i<n;i++)
    {
        printf("#");
    }
}