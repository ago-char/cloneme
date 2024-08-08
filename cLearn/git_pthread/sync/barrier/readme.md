/*
if you use pthread_barrier_t in your c file without :
#define _POSIX_C_SOURCE 200112L
before first include then vs code will show problem with your file and it will underline pthread_barrier_t with red.. looks code untidy. It will still compile to make exe but beffer use "#define _POSIX_C_SOURCE 200112L" and before first "#include<....>" statement in you c code .Thanks
*/
