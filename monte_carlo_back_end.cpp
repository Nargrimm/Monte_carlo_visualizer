#include <iostream>
#include <random>
#include <thread>
#include <future>

double monte_carlo(double iteration)
{
  size_t inside = 0;
  double x = 0;
  double y = 0;

  std::random_device dev;
  std::mt19937 rng(dev());
  std::uniform_real_distribution<> dist(0.0, 1.0);
  for (double i = 0; i < iteration; i++)
  {
    x = dist(rng);
    y = dist(rng);
    if (x * x + y * y <= 1)
    {
      inside += 1;
    }
  }
  return (4 * ((double)inside / iteration));
}

int main(int argc, char *argv[])
{
  if (argc < 3)
  {
    std::cout << "Please provide 2 arguments:" << std::endl;
    std::cout << "- The number of iteration desired, higher number means slower but more precise results" << std::endl;
    std::cout << "- The number of threads you want to use. We will average the results of each threads for a better precision" << std::endl;
    return -1;
  }

  double numberOfIterations = std::stod(std::string(argv[1]));
  int numberOfThreads = std::stod(std::string(argv[2]));

  std::vector<std::future<double>> vect;
  double res = 0;
  for (int i = 0; i < numberOfThreads; i++)
  {
    vect.push_back(std::async(std::launch::async, monte_carlo, numberOfIterations));
  }
  for (int i = 0; i < numberOfThreads; i++)
  {
    res += vect[i].get();
  }
  std::cout.precision(17);
  std::cout << res / numberOfThreads << std::endl;
  return 0;
}
