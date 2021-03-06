#include <iostream>
#include "TH1D.h"

#include "pkg-aa/h1d.hh" // just to test...
#include "pkg-ab/h1d.hh"

namespace pkg_ab {

void test_h1d()
{
  TH1D *h = new TH1D("h1-ab", "h1-ab", 100, 0., 100.);
  std::cout << "h1-ab: " << h->GetEntries() << "\n";
  delete h; h = NULL;
}

}
