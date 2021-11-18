OBJS1 =demo1.o 

all: demo1

demo1: $(OBJS1)
	$(CC) -o demo1 $(CFLAGS) $(LDFLAGS) $(OBJS1) -pthread

$(OBJS1) : %.o : %.c
	$(CC) -c $(CFLAGS) $< -o $@

clean:
	rm -f demo1 *.o

