#include <iostream>
#include "TH1D.h"

#include "pkg-ab/h1d.hh"

using namespace pkg_ab;

void test_th1d()
{
  TH1D *h = new TH1D("h1-ab", "h1-ab", 100, 0., 100.);
  std::cout << "h1-ab: " << h->GetEntries() << "\n";
  delete h; h = NULL;
}
