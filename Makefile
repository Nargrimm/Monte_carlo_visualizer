CC = g++
CFLAGS = -pthread -O3 -g0 -march=native
EXEC = hello


all: monteCarlo

monteCarlo: monte_carlo_back_end.cpp
	$(CC) $^ $(CFLAGS) -o monteCarlo

clean:
	rm monteCarlo
