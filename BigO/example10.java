void nFacRuntimeFunc(int n) {
    for(int i=0; i<n; i++) {
      nFacRuntimeFunc(n-1);
    }
  }